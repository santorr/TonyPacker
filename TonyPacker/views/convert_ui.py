"""
Convert all .ui file to .py with command line :
pyuic4 input.ui -o output.py
"""
import os
from pathlib import Path

path = os.path.dirname(os.path.abspath(__file__))

for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    if extension == ".ui":
        cmd = f"pyuic5 {Path(path, file)} -o {Path(path, name + '_convert.py')}"
        os.system(cmd)
        print(f"[DEBUG] File converted with success : {file} to {name + '_convert.py'}")
