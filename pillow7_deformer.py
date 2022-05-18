from PIL import Image, ImageOps

class Deformer():
	def getmesh(self,img):
		w,h = img.size
		# # define a shape in the original image 
		# source_shape = (0,0,0,h,w - 1000,h,w,0)
		# # define a rectangle in the new image
		# target_rect = (0,0,w,h) # left,top,right,bottom
		
		left = ((0,0,w // 2, h),(0, 0, 0, h, w // 2, h, w // 2 , 0))
		right = ((w // 2,0,w,h),(w // 2, 0, w // 2, h, 0, h, 0 , 0))
		flip = ((w // 2, 0, w, h ),(w // 2, h, w // 2, 0, w, 0, w - 1000 , h))

		# return all the shapes
		return [left,right]

# image import
image = Image.open('picture.jpg')
deform = ImageOps.deform(image,Deformer())
deform.save('17.png')

# more advanced example: https://www.pythoninformer.com/python-libraries/pillow/imageops-deforming/