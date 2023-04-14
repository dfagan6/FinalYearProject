from PIL import Image
import os

# set the path to the directory containing the images
path = r"C:\Users\dfaga\Documents\FYP2\images_forProjects\examples"

# set the new dimensions for the images
new_width = 500
new_height = 500

# loop through each file in the directory
for file_name in os.listdir(path):
    # check if the file is an image
    if file_name.endswith('.jpg') or file_name.endswith('.png') or file_name.endswith('.jpeg'):

        # open the image file
        image = Image.open(os.path.join(path, file_name))

        # resize the image
        resized_image = image.resize((new_width, new_height))

        # save the resized image with the original file name
        resized_image.save(os.path.join(path, file_name))
