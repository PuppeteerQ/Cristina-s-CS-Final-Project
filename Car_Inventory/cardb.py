"""
The goal of Car_inventory project is to write a program that can manipulate a car inventory database and accessories database with functions of:
1.find car
2.add car
3.remove car
4.show database
5. find accessories by car
6.export inventory
7. quit program

The cardb.py file is to create a program that can initialize, read in and manipulate databases.

Overall, the program is divided into 3 parts. 
Part 1: Class for database of car
Part 2: Class for database of accessories
Part 3: Search engine(or a program created to manipulate carDB and accDB)

"""

import json
#import json module
from tabulate import tabulate
#import tabulate module to format output

#create a Car class
class Car(object):
	#initialization
	def __init__(self,model_num,year,color,maker,model,body_type,quantity):
		
		self.model_num = model_num
		self.year = year
		self.color = color
		self.maker = maker
		self.model = model
		self.body_type = body_type
		self.quantity = quantity
	
	#convert to a json file
	def tojson(self):

		return self.__dict__

	#return a static method
	@staticmethod
	#create a function that demonstrate db info on car with formatted output 
	def list_cars_info(cars):
		
		print(tabulate([car.values() for car in cars], 
		headers= list(cars[0].keys())))

	@staticmethod
	#create a function to add cars in inventory
	def add_car():
		#takes input from users 
		model_num = str(input("Please input car model number: "))
		year = int(input("Please input car year: "))
		color = str(input("Please input car color: "))
		maker = str(input("Please input car maker: "))
		model = str(input("Please input car model: "))
		body_type = str(input("Please input car body type: "))
		quantity = int(input("Please input car quantity: "))
		#append the init method
		c = Car(model_num,year,color,maker,model,body_type,quantity)
		#return the inventory
		return c

#Create a class for the 2th part - accessory db
class Accessory(object):
	#initialization
	def __init__(self,seq_id,name,model_number,year,color,maker,model,body_type,quantity):
		self.seq_id = seq_id
		self.name = name
		self.model_number = model_number
		self.year = year
		self.color = color
		self.maker = maker
		self.model = model
		self.body_type = body_type
		self.quantity = quantity
	
	#convert to a json file
	def tojson(self):

		return self.__dict__

	#create a function that demonstrate db info on accessories with formatted output 
	@staticmethod
	def list_accessories_info(accessories):
		
		print(tabulate([acc.values() for acc in accessories], 
		headers= list(accessories[0].keys())))

	
#Part 3: Create a search engine(program) class to manipulate DBs
class CarDBEngine(object):
	#initialization
	def __init__(self):
		self.car_db = {}
		self.accessory = {}
	
	#Create a function to load database
	#since we already have info of databases in JSON file, to load databases, simply read the JSON file
	def load_db(self,json_file):
		#
		with open(json_file,'r') as fp:

			db = json.load(fp)
			self.car_db = db['cars']
			self.accessory = db['accessories']

	# Find Car by Model Number 
	def find_car_by_model_number(self,model_number):

		if model_number in self.car_db.keys():
			
			Car.list_cars_info([self.car_db[model_number]]);
			
	#function to add car
	def add_car(self):
		c = Car.add_car().tojson()
		self.car_db[c['model_num']] = c
		
	#function to remove car
	#delete car by given model number
	def remove_car_by_model_number(self,model_num):
		if model_num in self.car_db.keys():
			del self.car_db[model_num]
			
	#display car inventory
	def show_inventory(self):

		Car.list_cars_info(list(self.car_db.values()));

	def export_inventory(self):
	#create a function to export inventory
	#convert dict into string that can be write in JSON file
		db = {}
		db['cars'] = {}
		db['accessories'] = {}
		for key,value in self.car_db.items():
			db['cars'][key] = value
		for key,value in self.accessory.items():
			db['accessories'][key] = value
		with open('cardb.json','w') as fp:
			json.dump(db,fp)

	#create a function to find a match
	def find_matched_cars(self,seq):
		if seq in self.accessory.keys():
			model_number = self.accessory[str(seq)]['model_number']
			if model_number in self.car_db.keys():
				Car.list_cars_info([self.car_db[model_number]])
			else:
				print('No Match')
		else:
			print('No Match')
		

	#create a function show acc database
	def show_accessories(self):
		#output accesspry info
		Accessory.list_accessories_info(list(self.accessory.values()));
	
	#if user inputs quit, exit program
	def quit(self):
		print('See you next time')
		self.export_inventory()
		exit(0)
		
#main function, operation meun

if __name__ == '__main__':

	engine = CarDBEngine()
	print('Welcome to the mini Car database engine (enter quit to exit)')
	print("Instructions:")
	print("<find car> find the car given model number")
	print("<add car> add a new type of car")
	print("<remove car> remove car given model number")
	print("<show cars> show all cars")
	print("<show acc> show all accessories")
	print("<export> export the db to json file")
	print("<find match> find match by giving accessory seq id")
	#open the json file that contains database we have set up in advance
	engine.load_db('cardb.json')
	#if everything okay
	while True:
		#Tell user to input a command 
		cmd = input("please input your command: ")
		#if user inputs find car
		#request input of model number
		#call engine to find car by model number given
		if "find car" == cmd:
			model_number = (input("please input model number: "))
			engine.find_car_by_model_number(model_number)
		#if user inputs add car
		#call engine to add car 
		elif "add car" == cmd:
			engine.add_car()
		#if user inputs remove car
		#request for a model number
		#then removed 
		elif "remove car" == cmd:
			model_number = (input("please input model number: "))
			engine.remove_car_by_model_number(model_number)
		#if user inputs show cars
		#call engine to show inventory
		elif "show cars" == cmd:
			engine.show_inventory()
		#if user inputs show acc
		#call engine to show acc inventory
		elif "show acc" == cmd:
			engine.show_accessories()
		#if user inputs export
		#call engine's export object
		elif "export" == cmd:
			engine.export_inventory()
		#if user inputs find match
		#call engine to find match by seq id
		elif "find match" ==  cmd:
			seq_id = (input("please input accessory seq id: "))
			engine.find_matched_cars(seq_id)
		#if user inputs quit, stop the program
		elif "quit" == cmd:
			engine.quit()
		#if input is not valid
		#reshow the meun
		else:
			print("your command is wrong")
			print("Instructions:")
			print("<find car> find the car given model number")
			print("<add car> add a new type of car")
			print("<remove car> remove car given model number")
			print("<show cars> show all cars")
			print("<show acc> show all accessories")
			print("<export> export the db to json file")
			print("<find match> find match by giving accessory seq id")
			


	#engine.load_db('cardb.json')
	#engine.show_accessories()
	#engine.find_car_by_model_number('c3')
	#engine.add_car()
	#engine.remove_car_by_model_number('c5')
	#engine.export_inventory()
	#engine.find_matched_cars(1)