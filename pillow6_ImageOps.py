from PIL import Image, ImageOps

# image import
image = Image.open('picture.jpg')

# color changes
image_contrast = ImageOps.autocontrast(image = image, cutoff = 5)
image_inverted = ImageOps.invert(image)
image_solarize = ImageOps.solarize(image = image, threshold = 100) 
image_posterize = ImageOps.posterize(image = image, bits = 1) 
image_grayscale = ImageOps.grayscale(image = image) 
image_equalized = ImageOps.equalize(image = image)
image_colorize = ImageOps.colorize(image = image.convert('L'), black = 'blue', white = 'red')

# dimension changes 
image_mirror = ImageOps.mirror(image)
image_flip = ImageOps.flip(image)
image_scale = ImageOps.scale(image = image, factor = 0.4)
image_contain = ImageOps.contain(image = image, size = (500,200))

# Adding and removing
image_border = ImageOps.expand(image = image, border = 100, fill = (255,255,0))
image_padded = ImageOps.pad(image = image, size = (2500,1600))
image_fit = ImageOps.fit(image = image, size = (500,300))
image_crop = ImageOps.crop(image = image, border = 400)

image_flip.show()