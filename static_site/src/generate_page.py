import os
from block_markdown import markdown_to_html_node

def extract_title(markdown: str):
    blocks = markdown.split("\n")

    title = ""
    for block in blocks:
        if block.startswith("# "):
            title = block[2:]
            break
    
    if not title:
        raise Exception(f"Title couldn't be extracted from {markdown}!")

    return title

def generate_page(from_path: str, dest_path: str, template_path: str):
    print(f"Generate page from {from_path} to {dest_path} with {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    
    with open(template_path, "r") as f:
        template = f.read()

    markdown_to_html = markdown_to_html_node(markdown=markdown).to_html()

    title = extract_title(markdown=markdown)

    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", markdown_to_html)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with open(dest_path, "w") as f:
        f.write(page)