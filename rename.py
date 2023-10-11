import os
import re

list = os.listdir("to rename")
for folder_name in list:
    if x := re.search(r"^CS50P_W(.)$", folder_name):
        new_name = f"Week {x.group(1)}"
        os.rename(f"to rename/{folder_name}", f"to rename/{new_name}")
            
    elif y := re.search(r"^CS50P_W(.)P$", folder_name):
        new_name = f"Week {y.group(1)} problem"
        os.rename(f"to rename/{folder_name}", f"to rename/{new_name}")
