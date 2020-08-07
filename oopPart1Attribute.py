class Dog():

	#class object attribute

	species = "mamman"

	 
	 def __init__(self,breed,name):
         self.breed = breed
         self.name = name

	 MyDog= Dog(breed="lab", name="sammy")

	 print(MyDog.breed)
	 print(MyDog.name)
	 print(MyDog.species)
		