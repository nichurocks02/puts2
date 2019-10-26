#!/usr/bin/python3
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

mul=[]
e=[]

for i in range(len(num1)):
	
	parameters = {
	"A":Fraction(num1[i]),
	"B":Fraction(num2[i])
	}


	result_mul = float(parameters["A"] * parameters["B"])
	mul.append(result_mul)


	url3 = 'http://127.0.0.1:5000/mul'
	response3 = requests.get(url3, params=parameters)
	data3=response3.text
	e.append(float(data3))


	class test(unittest.TestCase):
		def test_mul(self):
			print('performing test on multiplication')
			print('**********************************')
			for i in range(len(num1)):
				self.assertAlmostEqual(mul[i],e[i])
				
				if (str(mul[i])[:11]) == (str(e[i])[:11]):
					print((str(mul[i])[:11])+' '+((str(e[i]))[:11])+ ' ' + 'success')
				else:
					print((str(mul[i])[:11])+' '+((str(e[i]))[:11])+ ' ' + 'fail')


			print('**********************************')

if __name__ == '__main__':	
	unittest.main()


