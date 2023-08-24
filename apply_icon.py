import os
import shutil

output_base_dir = "output"

def create_icon_copies(directory):
    for subdir, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename == "armor.png":
                source = os.path.join(subdir, filename)
                dest = os.path.join(subdir, "icon.png")
                shutil.copy2(source, dest)

create_icon_copies(output_base_dir)
