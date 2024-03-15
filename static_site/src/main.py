from utils import copy_dir
from generate_page import generate_pages_recursive
import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    static_source = os.path.join(dir_path,"../static")
    public_dest = os.path.join(dir_path, "../public") 

    copy_dir(source=static_source, destination=public_dest)
    source_index = os.path.join(dir_path, "../content")
    destination_index = os.path.join(public_dest)
    template_source = os.path.join(dir_path, "../template.html")
    generate_pages_recursive(
        dir_path=source_index, 
        dest_dir_path=destination_index, 
        template_path=template_source
    )

if __name__ == "__main__":
    main()