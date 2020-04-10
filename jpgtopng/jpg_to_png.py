import sys
import os
from PIL import Image


imagefolder = sys.argv[1]
output_folder = sys.argv[2]



if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for filename in os.listdir(imagefolder):
    img = Image.open(f'{imagefolder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    print('all done')
