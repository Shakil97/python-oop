class Circle():
	"""docstring for Circle"""

	pi = 3.14
	def __init__(self, radius=1):
	
		self.radius = radius

		def Area(self):
			
			return self.radius* self.radius*Circle.pi

			def set_radious(self,new_r):
				self.radius= new_r


myc = Circle(3)
print(myc.Area())

		