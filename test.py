#!/usr/bin/python
#from flask import Flask,request 
import unittest
import requests
import json 
from fractions import Fraction
import random

num1=[]
num2=[]
print('please wait for some time as your test is being performed')
for i in range(100):
	a=random.uniform(0,1)
	if a < 0.5:
		num1.append(random.randint(1,100))
		num2.append(random.randint(100,200))

	else:
		num1.append(random.uniform(1,100))
		num2.append(random.uniform(100,200))


add=[]
c=[]
for i in range(len(num1)):
	
	parameters = {
	"A":Fraction(num1[i]),
	"B":Fraction(num2[i])
	}

	result_add = float(parameters["A"] + parameters["B"])
	add.append(result_add)

	url1 = 'http://127.0.0.1:5000/add'
	response1 = requests.get(url1, params=parameters)
	data=response1.text
	c.append(float(data))


	class test(unittest.TestCase):	


		def test_Add(self):
			print('performing test on addition')
			print('****************************************')
			for i in range(len(num1)):
				self.assertAlmostEqual(add[i],c[i])
				if (str(add[i])[:11]) == (str(c[i])[:11]):
					print( (str(add[i])[:11])+' '+((str(c[i]))[:11])+ ' ' + 'success' )
				else:
					print( (str(add[i])[:11])+' '+((str(c[i]))[:11])+ ' ' + 'fail' )
			print('****************************************')	

if __name__ == '__main__':	
	unittest.main()


