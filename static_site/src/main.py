from utils import copy_dir
from generate_page import generate_page
import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    static_source = os.path.join(dir_path,"../static")
    public_dest = os.path.join(dir_path, "../public") 

    copy_dir(source=static_source, destination=public_dest)
    source_index = os.path.join(dir_path, "../content/index.md")
    destination_index = os.path.join(public_dest, "index.html")
    template_source = os.path.join(dir_path, "../template.html")
    generate_page(
        from_path=source_index, 
        dest_path=destination_index, 
        template_path=template_source
    )

if __name__ == "__main__":
    main()