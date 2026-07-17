# HTML Spec Section Manager

This guide provides technical instructions for configuring source documents, adjusting code-level text formatting, and navigating the HTML Spec Section Manager web dashboard.

## Document Setup and Formatting

To utilize the database-driven spec system, individual specification files must be configured correctly before compiling the layout.

* [cite_start]**File Modularity:** Break the master document down so that every 3-part spec section is saved as its own individual file[cite: 333].
* [cite_start]**CSI Formatting:** Ensure all source text strictly follows the standard 3-part CSI Masterspec formatting list conventions[cite: 315].
* [cite_start]**Critical Notes (Red Text):** If a specification section contains critical notes that require user editing or review, format this text in red within the source document[cite: 4]. [cite_start]The system will flag this red text to ensure it is modified before final compilation[cite: 4].

![Placeholder: Example of Word Document Setup with Red Text and CSI Formatting](#)

---

## Adjusting Text Formatting in Code

[cite_start]To alter the visual output of the text, adjustments must be made directly to the underlying code[cite: 5].

1.  **Locate the CSS File:** Open the CSS stylesheet associated with the web dashboard's frontend interface.
2.  **Target the Classes:** Locate the specific CSS classes mapped to the CSI hierarchy.
3.  [cite_start]**Modify Properties:** Adjust the relevant CSS properties to reflect your desired margins, font weights, or indentations[cite: 25].
    * [cite_start]Use bold and underline formatting for primary section titles[cite: 87, 334].
4.  **Save and Refresh:** Save the file and hard-refresh the browser dashboard to review the updated formatting.

![Placeholder: CSS Code Snippet Highlighting CSI Formatting Classes](#)

---

## PDF Export Rendering Discrepancies

> [cite_start]**Disclaimer:** The visual preview rendered in the HTML/CSS web dashboard may not perfectly match the final output of the exported PDF[cite: 6].

[cite_start]Web browsers and PDF generators utilize entirely different rendering engines[cite: 6]. This can cause variations in how the engines calculate margins and word-wrapping. Always review the exported PDF to verify precise layout alignment.

![Placeholder: Side-by-side comparison of HTML preview vs. PDF export](#)

---

## Navigation Tips and Tricks

To maximize the efficiency of the modular system, observe the following operational guidelines:

* [cite_start]**Project Toggling:** Use the web interface checkboxes to easily add or remove ("turn on/off") specific spec sections on a per-project basis[cite: 318, 338].
* [cite_start]**Automated Table of Contents:** The Table of Contents automatically generates and updates dynamically based on the specific file sections you have toggled on[cite: 317, 339].
* [cite_start]**Shared Network Environment:** Store the database of individual text files on a shared network server folder so the entire design team is pulling from the most current file versions[cite: 382].

### Layout Estimations
[cite_start]If you need to calculate the exact physical boundaries the layout will take up, use the following formulas[cite: 325, 350, 351]:
* [cite_start]**Total Width:** $W_{total}=(W_{col}\times N_{cols})+(S_{gap}\times(N_{cols}-1))$ [cite: 352]
* [cite_start]**Total Height:** $H_{total}=N_{lines}\times H_{line}$ [cite: 352]

![Placeholder: Web Dashboard UI showing Section Toggles, TOC, and Layout Previews](#)
