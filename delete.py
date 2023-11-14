import os
import numpy as np
from PIL import Image

# Define the path to the masks folder
mask_folder = "C:/Users/subham.jalan/Desktop/opt/pothole-segmentation/dataset/train/masks"

# Get a list of all the files in the masks folder
mask_files = os.listdir(mask_folder)
count = 0
for i in range(len(mask_files)):
    mask_path = os.path.join(mask_folder, mask_files[i])
    mask = np.array(Image.open(mask_path))
    if np.count_nonzero(mask < 0.01) == 1024 * 640 * 3:
        os.remove(mask_path)
        os.remove(os.path.join("C:/Users/subham.jalan/Desktop/opt/pothole-segmentation/dataset/train/images", mask_files[i].replace("POTHOLE.png", "RAW.jpg")))
        count += 1
print("removed: ", count, "files")
