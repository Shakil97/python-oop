class Book():
	"""docstring for Book"""
	def __init__(self, title, author, pages):
		
		self.title = title
		self.author = author
		self.pages = pages


		def __str__(self):
			return "title : {}, author : {}, pages : {}".format(self.title,self.author,self.pages)


			def __len__ (self):
				return self.pages

				def __del__(self):
					print("A BOOK IS DESTROYED")


		b = Book("PYTHON", "JOSE", 200)
		del b
		print(b)
		print(len(b))
		