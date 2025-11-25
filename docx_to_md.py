from docx import Document
from markdownify import markdownify as md
from datetime import datetime
import os
import re

# Folder containing DOCX files
docx_folder = "."
output_folder = "_posts"

for file in os.listdir(docx_folder):
    if file.endswith(".docx") and not file.startswith("~$"):
        docx_path = os.path.join(docx_folder, file)

        # Read the DOCX
        doc = Document(docx_path)

        # Extract text
        full_text = ""
        for para in doc.paragraphs:
            full_text += para.text + "\n\n"

        # Convert to Markdown
        markdown_text = md(full_text)

        # Generate a clean title from the filename
        title = os.path.splitext(file)[0]
        slug = re.sub(r'\s+', '-', title.lower())

        # Get today’s date
        date_str = datetime.today().strftime('%Y-%m-%d')
        filename = f"{date_str}-{slug}.md"
        output_path = os.path.join(output_folder, filename)

        # YAML front matter
        front_matter = f"""---
layout: post
title: "{title}"
date: {date_str}
categories: blog
tags: []
---

"""

        # Combine front matter + markdown
        full_md = front_matter + markdown_text

        # Save Markdown
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_md)

        print(f"✅ Converted {file} → {output_path}")