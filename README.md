# Spec Master

This guide provides technical instructions for configuring source documents, adjusting code-level text formatting, and navigating the HTML Spec Section Manager.

## Document Setup and Formatting

To utilize the database-driven spec system, individual specification files must be configured correctly before compiling the layout.

* Save each individual spec section as a separate Word doc file.
* Ensure all source text strictly follows the required CSI Masterspec formatting. 
* If the spec sections contain critical notes that require user editing, format this text in red. 
* The system will flag this red text to ensure it is addressed by the user before final compilation.

> `[Placeholder: Screenshot of Word doc file showing CSI formatting and red critical notes]`

---

## Adjusting Text Formatting in Code

Visual formatting preferences are controlled via the tool's underlying code. To adjust text formatting as desired, you must edit the code directly.

1. **Locate the CSS File:** Open the CSS stylesheet associated with the web dashboard's frontend interface.
2. **Target the Classes:** Locate the corresponding CSS classes mapped to the spec section hierarchy.
3. **Modify Properties:** Edit standard CSS properties (e.g., `font-weight`, `margin-left`, `text-decoration`) to reflect your desired visual output.
4. **Save and Refresh:** Save the file and refresh the browser dashboard to review the updated formatting.

> `[Placeholder: Screenshot of CSS Code Snippet Highlighting Formatting Classes]`

---

## PDF Export Rendering Discrepancies

**Disclaimer:** The preview may not reflect the final PDF export. 

This discrepancy occurs due to the fundamental differences between HTML/CSS and PDF rendering engines. Because web browsers and PDF generators calculate elements like font spacing, margins, and word-wrapping differently, always review the exported PDF to verify precise layout alignment.

> `[Placeholder: Screenshot of side-by-side comparison showing HTML preview vs. PDF export]`

---

## Navigation Tips and Tricks

To maximize the efficiency of the modular system, observe the following operational guidelines:

* **Project Toggling:** The tool provides the ability to add or remove spec sections on a per-project basis. Use the interface checkboxes to easily "turn on/off" sections.
* **Dynamic Table of Contents:** The Table of Contents is designed to update automatically as sections are added or removed.
* **Network Storage:** Store the specs database on a shared project folder on your server to ensure the entire team is pulling from the most current file versions.
* **Layout Estimation (Width):** Calculate the exact overall width the layout will take up using the formula: W_total = (W_col * N_cols) + (S_gap * (N_cols - 1)).
* **Layout Estimation (Height):** Calculate the exact overall height using the formula: H_total = N_lines * H_line.

> `[Placeholder: Screenshot of Web Dashboard UI showing Section Toggles, Dynamic TOC, and Layout Previews]`
