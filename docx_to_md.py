from docx import Document
from markdownify import markdownify as md
from datetime import datetime
import os
import re

# Path to your DOCX file
docx_path = "example.docx"

# Read the DOCX
doc = Document(docx_path)

# Extract text
full_text = ""
for para in doc.paragraphs:
    full_text += para.text + "\n\n"

# Convert to Markdown
markdown_text = md(full_text)

# Generate a clean title from the filename
title = os.path.splitext(os.path.basename(docx_path))[0]
slug = re.sub(r'\s+', '-', title.lower())  # spaces → dashes

# Get today’s date for the post filename
date_str = datetime.today().strftime('%Y-%m-%d')
filename = f"{date_str}-{slug}.md"

# Path to _posts folder
output_path = os.path.join("_posts", filename)

# YAML front matter for Jekyll
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

# Save the Markdown file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_md)

print("✅ Conversion complete! Markdown saved to", output_path)