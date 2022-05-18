from PIL import Image

# create new image by import 
image = Image.open('picture.jpg')

# alternative way to import an image 
# with Image.open('picture.jpg') as image:
# 	image.show()

# create a new image from scratch
image_blank = Image.new('RGBA',(1000,600))

# show the picture
# image_blank.show()

# saving the picture
#image.save('test_save.png')

# image information
print(image.size)
print(image.filename)
print(image.format)
print(image.format_description)