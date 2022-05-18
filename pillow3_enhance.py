from PIL import Image, ImageEnhance
# https://pillow.readthedocs.io/en/stable/reference/ImageEnhance.html

# image import
image = Image.open('picture.jpg')

# create an enhancer
color_enhancer = ImageEnhance.Color(image) # vibrance
contrast_enhancer = ImageEnhance.Contrast(image) # contrast
brightness_enhancer = ImageEnhance.Brightness(image) # contrast
sharpness_enhancer = ImageEnhance.Sharpness(image) # contrast

# applying the enhancer
enhanced_image = brightness_enhancer.enhance(5)
enhanced_image.show()