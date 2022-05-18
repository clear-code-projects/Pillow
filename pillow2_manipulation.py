from PIL import Image, ImageColor

# image import
image = Image.open('picture.jpg')

# documentation
# https://pillow.readthedocs.io/en/stable/reference/Image.html?
print(ImageColor.colormap)
# rotate 
# image_rotate = image.rotate(60,expand = True, fillcolor = ImageColor.getcolor('red','RGB'))

# # crop 
# image_crop = image.crop((550,400,1500,1150))

# # flipping the image / transpose the image
# image_flip_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# image_flip_vertical = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# image_transpose = image.transpose(Image.Transpose.TRANSPOSE)
# # options: FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM, ROTATE_90, ROTATE_180, ROTATE_270, TRANSPOSE, TRANSVERSE.

# # resize 
# image_resize = image.resize((600,1000)) # bad example

# # better example
# scale_factor = 2
# new_image_size = (image.size[0] * scale_factor,image.size[1] * scale_factor)
# image_resize_better = image.resize(new_image_size)

# display
#image_resize_better.show()