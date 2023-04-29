from pathlib import Path
import glob
import os
import numpy as np
import sys
path = Path.cwd()

files = [file.stem for file in path.rglob('*')]
current_dir = "Images_Labels2021/SmallGateLabels"

#"Images_Labels2021/SmallGateLabels/IMG_3123.txt" Relative File Path
# for i in files:
    

for fullpath in glob.iglob(os.path.join(current_dir, "*.txt")):  
  title, ext = os.path.splitext(os.path.basename(fullpath))
  currFile = current_dir + "/" + title + '.txt'
  file = open(currFile, encoding="utf8")
#   with open(currFile, "r") as f:
#         lines = f.readlines()
#   with open(currFile, "w") as f: 
#     print(lines)
#     lines = lines[0]
#     f.write(lines)

#   print(title)
#   print(currFile)
#   #file_val.write(current_dir + "/" + title + '.JPG' + "\n")