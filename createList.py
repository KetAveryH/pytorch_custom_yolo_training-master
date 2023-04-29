import glob
import os
import numpy as np
import sys
current_dir = "Images_Labels2021/SmallGateImages"
split_pct = 10  # 10% validation set
file_train = open("Images_Labels2021/train.txt", "w")  
file_val = open("Images_Labels2021/val.txt", "w")  
counter = 1  
index_test = round(100 / split_pct)  
for fullpath in glob.iglob(os.path.join(current_dir, "*.JPG")):  
  title, ext = os.path.splitext(os.path.basename(fullpath))
  if counter == index_test:
    counter = 1
    file_val.write(current_dir + "/" + title + '.JPG' + "\n")
  else:
    file_train.write(current_dir + "/" + title + '.JPG' + "\n")
    counter = counter + 1
file_train.close()
file_val.close()