from PIL import Image, ImageFilter
# https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html

# image import
image = Image.open('picture.jpg')

# basic filters
image_blur = image.filter(ImageFilter.BLUR)
image_contour = image.filter(ImageFilter.CONTOUR)
image_detail = image.filter(ImageFilter.DETAIL)
image_edge = image.filter(ImageFilter.EDGE_ENHANCE)
image_edge_more = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
image_find_edges = image.filter(ImageFilter.FIND_EDGES)
image_emboss = image.filter(ImageFilter.EMBOSS)
image_sharp = image.filter(ImageFilter.SHARPEN)
image_smooth = image.filter(ImageFilter.SMOOTH)
image_smooth_more = image.filter(ImageFilter.SMOOTH_MORE)

# # rank filters
# image_filtered_min = image.filter(ImageFilter.MinFilter(size = 5))
# image_filtered_median = image.filter(ImageFilter.MedianFilter(size = 5))
# image_filtered_max = image.filter(ImageFilter.MaxFilter(size = 5))

# multiband 
image_boxblur = image.filter(ImageFilter.BoxBlur(radius = 4))
image_gaussblur = image.filter(ImageFilter.GaussianBlur(radius = 10))
image_unsharp = image.filter(ImageFilter.UnsharpMask(radius = 4))

# combine filters: blur + emboss 
image_emboss = image.filter(ImageFilter.EMBOSS)
image_emboss_blur = image_emboss.filter(ImageFilter.GaussianBlur(radius = 2))

image_gaussblur.save('7.png')