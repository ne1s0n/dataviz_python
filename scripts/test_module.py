#This file is used to show how module import works

def greet(name : str):
	"""
	A function to greet somebody
	
	Use this function when you want to greet somebody, specifying
	their name
	
	Parameter:
		name (int) : the name of the person to be greeted
	
	Returns: nothing
	"""
	
	print('Hello my dear ' + str(name))

def insult(name : str):
	"""
	A function to insult somebody
	
	Use this function when you want to insult somebody, specifying
	their name
	
	Parameter:
		name (int) : the name of the person to be insulted
	
	Returns: nothing
	"""
	
	print(str(name) + ', you absolute fool!')
