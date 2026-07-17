# HTML Spec Section Manager

This guide provides technical instructions for configuring source documents, adjusting code-level text formatting, navigating the HTML Spec Section Manager web dashboard, and executing the end-user workflow.

> **PREREQUISITE:** You must have Python installed for this tool to work. Python is available for install from Software Center.

## Table of Contents
  * [Document Setup and Formatting](#document-setup-and-formatting)
  * [End-User Workflow](#end-user-workflow)
  * [Adjusting Text Formatting in Code](#adjusting-text-formatting-in-code)
  * [PDF Export](#pdf-export)
  * [Tips and Tricks](#tips-and-tricks)
  * [Layout Estimations](#layout-estimations)

---

### Document Setup and Formatting

To utilize the database-driven spec system, individual specification files must be configured correctly before compiling the layout.

* **File Modularity:** Each 3-part specification section must be saved as an individual Word document.
* **CSI Formatting:** All text within these Word documents must adhere strictly to CSI Masterspec formatting conventions. The tool assumes your text is formatted per Masterspec list hierarchy.
* **Critical Notes (Red Text):** Any critical notes still requiring user review or modification at the time of export should be formatted in red text within the source Word document. 
* **Red Text Flagging:** The HTML tool preserves this red text in its PDF export.

![Word doc file showing CSI formatting and red critical notes](docs/images/spaces.png)

---

### End-User Workflow

1. **Copying spec files** Copy the folder of Individual Specs from the server to your project folder. If making or copying your own spec files, see previous section for requirements.

![Folder of individual Word doc specs files](docs/images/docx.png)

2. **Launching the Dashboard:** To start the tool, simply double-click the designated Windows shortcut (which points to the `manager.pyw` file). The script will silently spin up a local Python server in the background and automatically open the dashboard in your default web browser (typically to the `index.html` file stored in the same folder as `manager.pyw`).

3. **Setting a project specs folder:** Once the web page loads, you will see the interface shown below. You will need to set two folder paths, one containing all the individual spec section files

4. **Selecting Spec Sections:** Once the web page loads, you will see a clean interface displaying the available spec sections. Simply check or uncheck the boxes to turn specific sections "on" or "off" for your current project. As you toggle these sections, the Table of Contents will automatically generate and update to match your selections.

5. **Compiling the Data:** When you are satisfied with your selected sections, initiate the compilation (e.g., by clicking "Compile"). The backend engine will grab the text from your selected files, build the Table of Contents, and stitch everything together into a single, continuous package (like a JSON or text file) that is ready for Revit.
6. **Closing the Tool:** When you are finished managing the specs, just close the web browser tab. The local Python server running in the background will automatically detect this and shut itself down.
7. **Placing/Updating in Revit:** Finally, switch over to your Revit project and click the "Update Specs" button on your pyRevit ribbon. The script will locate any existing spec text notes tied to that package, delete them entirely, and automatically regenerate fresh, fully formatted text columns on your sheet using the newly compiled data.

---

### Adjusting Text Formatting in Code

Visual formatting preferences are controlled via the tool's underlying code. To adjust text formatting, you must edit the code directly.

1. **Locate the CSS File:** Open the CSS stylesheet associated with the web dashboard's frontend interface.
2. **Target the Classes:** Locate the specific CSS classes mapped to the CSI hierarchy (e.g., `section-header`, `part-title`, `list-level-1`).
3. **Modify Properties:** Edit standard CSS properties (e.g., `font-weight`, `margin-left`, `text-decoration`) to reflect your desired visual output. 
4. **Save and Refresh:** Save the file and hard-refresh the browser dashboard to review the updated formatting.

![Placeholder: Screenshot of CSS Code Snippet Highlighting Formatting Classes]

---

### PDF Export

> **Disclaimer:** The visual preview rendered in the HTML/CSS web dashboard may not perfectly match the final output of the exported PDF.

HTML web browsers and PDF generators utilize entirely different rendering engines. These differences affect how the engines calculate font spacing, margins, and word-wrapping. Always review the final PDF export to verify precise line breaks and layout alignments.

![Placeholder: Screenshot of side-by-side comparison showing HTML preview vs. PDF export]

---

### Tips and Tricks

Observe the following operational guidelines to maximize the efficiency of the modular system:

* **Project Toggling:** Use the web dashboard checkboxes to easily add or remove ("turn on/off") individual specification sections for your specific project.
* **Automated Table of Contents:** The Table of Contents automatically generates and updates dynamically to reflect the active sections you have toggled on.
* **Network Storage:** Store the database of individual spec section files on a shared network project folder to ensure the entire team is pulling from the most current versions.

---

### Layout Estimations
If you need to calculate the exact physical boundaries the layout will take up, use the following formulas:
* **Total Width:** $W_{total} = (W_{col} \times N_{cols}) + (S_{gap} \times (N_{cols} - 1))$
* **Total Height:** $H_{total} = N_{lines} \times H_{line}$

![Placeholder: Screenshot of Web Dashboard UI showing Section Toggles, Dynamic TOC, and Layout Previews]


