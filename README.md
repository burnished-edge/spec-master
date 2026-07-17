# Spec Master

This guide provides technical instructions for configuring source documents, adjusting code-level text formatting, and navigating the HTML Spec Section Manager web dashboard.

## Document Setup and Formatting

To utilize the database-driven spec system, individual specification files must be configured correctly before compiling the layout.

* [cite_start]**File Modularity:** Break the monolithic master document down so that every 3-part spec section is saved as its own individual file[cite: 21].
* [cite_start]**CSI Formatting:** Ensure all source text strictly follows the standard 3-part CSI Masterspec formatting list conventions[cite: 22].
* [cite_start]**Critical Notes (Red Text):** If a specification section contains critical notes that require user editing or review, format this text in red within the source Word document[cite: 23]. [cite_start]The system will flag this red text to ensure it is modified before final compilation[cite: 24].

![Placeholder: Example of Word Document Setup with Red Text and CSI Formatting](path/to/word_setup_image.png)

---

## Adjusting Text Formatting in Code

[cite_start]To alter the visual output of the text (e.g., margins, font weights, indentations), adjustments must be made directly to the underlying code[cite: 25].

1.  [cite_start]**Locate the CSS File:** Open the CSS stylesheet associated with the web dashboard's frontend interface[cite: 26].
2.  [cite_start]**Target the Classes:** Locate the specific CSS classes mapped to the CSI hierarchy (e.g., `section-header`, `part-title`, `list-level-1`)[cite: 27].
3.  [cite_start]**Modify Properties:** Adjust the relevant CSS properties[cite: 28].
    * [cite_start]Use `font-weight: bold;` and `text-decoration: underline;` for primary section titles[cite: 28, 29].
    * [cite_start]Adjust `margin-left` or `padding-left` values to strictly control hanging indent depths for nested lists[cite: 30].
4.  [cite_start]**Save and Refresh:** Save the file and hard-refresh the browser dashboard to review the updated formatting[cite: 31].

![Placeholder: CSS Code Snippet Highlighting CSI Formatting Classes](path/to/css_code_image.png)

---

## PDF Export Rendering Discrepancies

> [cite_start]**Disclaimer:** The visual preview rendered in the HTML/CSS web dashboard may not perfectly match the final output of the exported PDF[cite: 32].

[cite_start]Web browsers and PDF generators utilize entirely different rendering engines to calculate font kerning, margins, and word-wrapping[cite: 33]. [cite_start]Subtle variations in character spacing may cause lines to wrap at different points in the final PDF than they appear on the screen[cite: 34]. [cite_start]Always review the exported PDF to verify precise layout alignment[cite: 35].

![Placeholder: Side-by-side comparison of HTML preview vs. PDF export](path/to/pdf_rendering_comparison.png)

---

## Navigation Tips and Tricks

[cite_start]To maximize the efficiency of the modular system, observe the following operational guidelines[cite: 36]:

* [cite_start]**Project Toggling:** Use the web interface checkboxes to easily add or remove specific spec sections on a per-project basis[cite: 36].
* [cite_start]**Automated Table of Contents:** The Table of Contents automatically generates and updates dynamically based on the specific file sections you have toggled on[cite: 37].
* [cite_start]**Shared Network Environment:** Store the database of individual text files on a shared network server folder so the entire design team is pulling from the most current file versions[cite: 38].

### Layout Estimations
[cite_start]If you need to calculate the exact physical boundaries the layout will take up, use the following formulas[cite: 39]:
* [cite_start]**Total Width:** $W_{total}=(W_{col}\times N_{cols})+(S_{gap}\times(N_{cols}-1))$ [cite: 39]
* [cite_start]**Total Height:** $H_{total}=N_{lines}\times H_{line}$ [cite: 39]

![Placeholder: Web Dashboard UI showing Section Toggles, TOC, and Layout Previews](path/to/dashboard_ui_image.png)
