from cardb import Car
from cardb import Accessory
import json


#main function
if __name__ == '__main__':

	c1 = Car('c1',2011,'blue','China','c1-A','sedan',4).tojson()
	c2 = Car('c2',2008,'yellow','US','c2-A','sedan',1).tojson()
	c3 = Car('c3',2001,'blue','England','c3-F','SUV',5).tojson()
	c4 = Car('c4',2019,'blue','Netherland','c4-K','SUV',2).tojson()
	c5 = Car('c5',1911,'blue','England','c5-past','SUV',5).tojson()

	a1 = Accessory(1,'seat','c1',2019,'black','Japan','c1-A','sedan',2).tojson()
	a2 = Accessory(2,'wheel','c4',2019,'black','UK','c4-K','SUV',10).tojson()
	a3 = Accessory(3,'window','c3',2009,'white','Taiwan','c1-F','Jeep',12).tojson()
	a4 = Accessory(4,'wheel','c1',2009,'white','Taiwan','c1-F','SUV',1).tojson()


	db = {}
	db['cars'] = {}

	db['cars']['c1'] = c1
	db['cars']['c2'] = c2
	db['cars']['c3'] = c3
	db['cars']['c4'] = c4
	db['cars']['c5'] = c5

	db['accessories'] = {}
	db['accessories'][1] = a1
	db['accessories'][2] = a2
	db['accessories'][3] = a3
	db['accessories'][4] = a4

#write all the data to the JSON file
#export to fp
	with open('cardb.json','w') as fp:
		json.dump(db,fp)
