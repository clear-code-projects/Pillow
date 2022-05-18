from PIL import Image, ImageChops

panda = Image.open('picture.jpg').convert('RGBA')
owl = Image.open('owl.jpg') # same size as panda image
python = Image.open('python.png') # smaller than the panda image + has transparency

# merging images with image.methods()
image_blend = Image.blend(panda,owl,10) # both images need same size and mode
# image_composite = Image.composite(panda,owl,Image.new('L',panda.size,50))

# image paste
panda.paste(python,(100,300), mask = python)

# channel operations 
# image_overlay = ImageChops.overlay(panda,owl)
# image_darker = ImageChops.darker(panda,owl) 
# image_lighter = ImageChops.lighter(panda,owl) 
# image_soft_light = ImageChops.soft_light(panda,owl) 
# image_hard_light = ImageChops.hard_light(panda,owl) 
# image_difference = ImageChops.difference(panda,owl)
# image_modulo = ImageChops.add_modulo(panda,owl) 
# image_screen = ImageChops.screen(panda,owl) 

# more complex channel operations 
# image_add = ImageChops.add(panda,owl,scale = 2.0,offset = 100)
# image_subtract = ImageChops.subtract(panda,owl,scale = 2.0,offset = 100)
# image_logical_and = ImageChops.logical_and(panda.convert('1'),owl.convert('1'))
# image_logical_or = ImageChops.logical_or(panda.convert('1'),owl.convert('1'))

# super easy 
# image_invert = ImageChops.invert(panda)

# masking
# mask must have a specfic mode: RGBA, 1 or L
# mask = Image.open('mask.png')
# image_masked_alpha = Image.alpha_composite(panda.convert('RGBA'),mask)
# image_masked = Image.composite(owl,panda,mask.convert('L'))

panda.show()