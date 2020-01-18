# image converter
import os
import sys
from PIL import Image
from PIL import ImageFilter

# the funtion is called with sys.arg[1] = ./raw_images and sys.arg[2]= ./newfilespng
# grab 1st and second argument

#raw_images_file = argv[1]
#new_images_file = argv[2]

# 1s get the current Tab
path = os.getcwd()
#print ("The current working directory is %s" % path)

# grab the new folder name
converted_images_file = 'test'
raw_images_file = 'Images'

converted_images_file_PATH = path + '/' + converted_images_file
raw_images_file_PATH = path + '/' + raw_images_file


#print("absname with path= %s" % os.path.abspath(path))

print("exists? = %s" % os.path.exists(converted_images_file_PATH))

#print("list = %s" % os.listdir(path))

# check if is new/exists, if not create a new

if os.path.exists(converted_images_file_PATH):
    print(f'file already exist see the list below :\n {os.listdir(path)} ')
else:
    os.mkdir(converted_images_file)
    print(f'file {converted_images_file} created ! see the list below : \n {os.listdir(path)}')



#loop through /raw_images images by images
for i in os.listdir(raw_images_file_PATH):
    filename, extension = os.path.splitext(i)
    im = Image.open(raw_images_file_PATH + '/' + filename + extension)
    im.thumbnail((400,400)) # change the format to thumbnails
    converted_image = im.convert('L') # applicate Grey Filter
    target = '.png'
    converted_image.save(converted_images_file_PATH + '/' + filename + target, 'png') # convert the file to png in the new_file