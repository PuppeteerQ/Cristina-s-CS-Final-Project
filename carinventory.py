#!/usr/bin/python

import sqlite3

connect = sqlite3.connect('car.db')
c = connect.cursor()
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS CarInventory (Model_Number Integer, Year Integer, Make TEXT, Color TEXT, Model TEXT, Body_Type TEXT, Quantity Integer, PRIMARY KEY(Model_Number))')

def data_insert():
	c.execute("INSERT INTO CarInventory VALUES(123,'2000','BEH','RED','0X110','S',1)")
	connect.commit()
	c.close()
	connect.close()
	
create_table()
data_insert()