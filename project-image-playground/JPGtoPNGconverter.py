import sys
import os
from PIL import Image

# grob the first and second module
image_folder = './pokemons/'
output_folder = sys.argv[0]

print(image_folder)

# check is new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
#loop through pokemons,
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    img.save(f'{output_folder}{filename}', 'png')  #save them to new folder
    print('all done!')


