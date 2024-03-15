import os
import shutil

def copy_dir(source: str, destination: str) -> None:
    if not os.path.exists(path=source):
        raise Exception("directory to be copied doesn't exist")
        return

    if os.path.exists(path=destination):
        shutil.rmtree(destination)

    os.mkdir(path=destination)

    for child_path in os.listdir(source):
        full_path = os.path.join(source, child_path)
        if os.path.isfile(full_path):
            shutil.copy(full_path, destination)
        else:
            copy_dir(
                source=full_path, 
                destination=os.path.join(destination, child_path)
            )
