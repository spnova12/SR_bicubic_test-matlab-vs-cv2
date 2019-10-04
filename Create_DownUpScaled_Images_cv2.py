from os import listdir
from os.path import join
import cv2
import os
import numpy as np

input_folder_dir = 'SR_testing_datasets/Set5'
output_folder_dir = 'SR_testing_datasets_cv2/Set5'

if not os.path.exists(output_folder_dir):
    os.makedirs(output_folder_dir)

input_dirs = [join(input_folder_dir, x) for x in sorted(listdir(input_folder_dir))]
print(input_dirs)
scale = 4.0
for input_dir in input_dirs:
    img = cv2.imread(input_dir)
    img = img.astype(np.float)

    img = cv2.resize(img, None, fx=1/scale, fy=1/scale, interpolation=cv2.INTER_CUBIC)
    img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

    img = np.around(img)
    img = img.clip(0, 255)
    img = img.astype(np.uint8)

    cv2.imwrite(os.path.splitext(output_folder_dir + '/' + os.path.basename(input_dir))[0] + '.png', img)