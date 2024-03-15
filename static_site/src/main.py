from utils import copy_dir
import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    copy_dir(
        source=os.path.join(dir_path,"../static"), 
        destination=os.path.join(dir_path, "../public")
    )

if __name__ == "__main__":
    main()