import sys
import subprocess
import importlib.util
import ctypes

def ensure_packages():
    required = {
        "fastapi": "fastapi", 
        "uvicorn": "uvicorn", 
        "docx": "python-docx", 
        "pydantic": "pydantic"
    }
    
    missing = []
    for import_name, install_name in required.items():
        if importlib.util.find_spec(import_name) is None:
            missing.append(install_name)
            
    if missing:
        msg = "First-time setup detected. Please wait while the required libraries install.\n\nThis may take a minute or two."
        ctypes.windll.user32.MessageBoxW(0, msg, "Spec Manager Setup", 0 | 0x40)
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])

ensure_packages()

import os
import json
import re
import uvicorn
import tkinter as tk
from tkinter import filedialog
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from docx import Document

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CONFIG_FILE = "config.json"
LATEST_COMPILED_DATA = {} 

DIVISIONS = {
    "01": "DIVISION 01 - GENERAL REQUIREMENTS",
    "02": "DIVISION 02 - EXISTING CONDITIONS",
    "03": "DIVISION 03 - CONCRETE",
    "04": "DIVISION 04 - MASONRY",
    "05": "DIVISION 05 - METALS",
    "06": "DIVISION 06 - WOOD, PLASTICS, AND COMPOSITES",
    "07": "DIVISION 07 - THERMAL AND MOISTURE PROTECTION",
    "08": "DIVISION 08 - OPENINGS",
    "09": "DIVISION 09 - FINISHES",
    "10": "DIVISION 10 - SPECIALTIES",
    "11": "DIVISION 11 - EQUIPMENT",
    "12": "DIVISION 12 - FURNISHINGS"
}

def load_config():
    default_config = {
        "master_library": r"ENTER_DEFAULT_MASTER_LIBRARY_DIR_HERE",
        "project_output": r"ENTER_DEFAULT_PROJECT_OUTPUT_DIR_HERE"
    }
    
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)
            return {
                "master_library": data.get("master_library") or default_config["master_library"],
                "project_output": data.get("project_output") or default_config["project_output"]
            }
    return default_config

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

class CompileRequest(BaseModel):
    project_folder: str 
    selected_files: List[str]

def parse_docx_to_masterspec(filepath, csi_num=""):
    doc = Document(filepath)
    parsed_lines = []
    is_first_line = True
    csi_digits = re.sub(r'\D', '', csi_num)
    
    for para in doc.paragraphs:
        raw_text = para.text.strip()
        if not raw_text:
            continue
            
        if is_first_line:
            is_first_line = False
            text_upper = raw_text.upper()
            if "SECTION" in text_upper or (csi_digits and csi_digits in re.sub(r'\D', '', text_upper)):
                continue
                
        # Build an HTML-safe string that highlights red text for the web preview
        html_text = ""
        for run in para.runs:
            if not run.text: continue
            
            # Simple escape to prevent HTML injection errors
            escaped_text = run.text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            
            has_alert = False
            # Check for pure red (FF0000) or standard Word red (C00000)
            if run.font.color and run.font.color.rgb:
                if str(run.font.color.rgb).upper() in ["FF0000", "C00000", "FF0004"]:
                    has_alert = True
            # Check if text is highlighted
            if run.font.highlight_color:
                has_alert = True
                
            if has_alert:
                # Updated to pure RGB red (#FF0000) and added text-transform: uppercase
                html_text += f'<span style="color: #FF0000; font-weight: bold; text-transform: uppercase; background-color: #fadbd8; padding: 0 3px; border-radius: 2px;">{escaped_text}</span>'
            else:
                html_text += escaped_text
                
        # Determine MasterSpec hierarchy level
        level = "Body"
        if re.match(r"^PART\b", raw_text): level = "Heading 1"
        elif re.match(r"^\d+\.\d+", raw_text): level = "Heading 2"
        elif re.match(r"^[A-Z](?:\.|\s)", raw_text): level = "List 1"
        elif re.match(r"^\d+\.", raw_text): level = "List 2"
        elif re.match(r"^[a-z]\.", raw_text): level = "List 3"
        elif re.match(r"^\d+\)", raw_text): level = "List 4"
        elif re.match(r"^[a-z]\)", raw_text): level = "List 5"
        
        # Save BOTH raw text (for Revit) and html_text (for the browser preview)
        parsed_lines.append({"level": level, "text": raw_text, "html": html_text.strip()})
            
    return parsed_lines

@app.get("/browse")
def browse_folder():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder_path = filedialog.askdirectory(title="Select Directory")
    root.destroy()
    return {"path": folder_path}

@app.get("/config")
def get_config():
    return load_config()

@app.post("/config")
def update_config(config_data: dict):
    save_config(config_data)
    return {"status": "success"}

@app.get("/available-specs")
def get_available_specs():
    config = load_config()
    library_path = config.get("master_library")
    
    if not library_path or not os.path.exists(library_path):
        return {"error": "Master library path not set or invalid."}
        
    files = [f for f in os.listdir(library_path) if f.endswith(".docx") and not f.startswith("~")]
    return {"files": files}

@app.post("/compile")
def compile_specs(request: CompileRequest):
    global LATEST_COMPILED_DATA
    config = load_config()
    library_path = config.get("master_library")
    output_dir = request.project_folder or config.get("project_output")
    
    if not library_path or not os.path.exists(library_path):
        raise HTTPException(status_code=400, detail="Library path invalid.")
        
    toc_data = {}
    
    for file in request.selected_files:
        clean_name = file.replace(".docx", "")
        clean_name = re.sub(r'(?i)^SECTION\s*-?\s*', '', clean_name).strip()
        
        match = re.match(r'^([\d\s]{6,8})\s*-?\s*(.*)', clean_name)
        if match:
            raw_csi = match.group(1).strip()
            csi_num = re.sub(r'\s+', '', raw_csi)
            title = match.group(2).strip()
        else:
            csi_num = "000000"
            raw_csi = ""
            title = clean_name
            
        prefix = csi_num[:2]
        if prefix not in toc_data:
            toc_data[prefix] = []
            
        toc_data[prefix].append({"csi": raw_csi, "title": title, "file": file})

    compiled_package = []
    
    compiled_package.append({"level": "Title", "text": "TABLE OF CONTENTS"})
    
    for div in sorted(toc_data.keys()):
        div_name = DIVISIONS.get(div, f"DIVISION {div}")
        compiled_package.append({"level": "TOC Division", "text": div_name})
        
        for item in sorted(toc_data[div], key=lambda x: x["csi"]):
            compiled_package.append({
                "level": "TOC Item", 
                "csi": item["csi"], 
                "title": item["title"]
            })

    for div in sorted(toc_data.keys()):
        for item in sorted(toc_data[div], key=lambda x: x["csi"]):
            section_heading = f"SECTION {item['csi']} - {item['title']}".upper()
            compiled_package.append({"level": "Title", "text": section_heading})
            
            filepath = os.path.join(library_path, item["file"])
            if os.path.exists(filepath):
                parsed_data = parse_docx_to_masterspec(filepath, item['csi'])
                compiled_package.extend(parsed_data)
            
    if output_dir and os.path.exists(output_dir):
        output_path = os.path.join(output_dir, "compiled_specs.json")
        with open(output_path, "w") as f:
            json.dump(compiled_package, f, indent=4)
            
    LATEST_COMPILED_DATA = compiled_package
    
    return {"status": "success", "message": "Specs compiled successfully."}

@app.get("/latest")
def get_latest():
    if not LATEST_COMPILED_DATA:
        raise HTTPException(status_code=404, detail="No active compilation found in memory.")
    return LATEST_COMPILED_DATA

if __name__ == "__main__":
    import sys
    import os
    
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')
    
    uvicorn.run(app, host="127.0.0.1", port=8000)