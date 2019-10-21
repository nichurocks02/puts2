#!usr/bin/python
from flask import Flask,request 
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


sub=[]
d=[]

for i in range(len(num1)):
	
	parameters = {
	"A":Fraction(num1[i]),
	"B":Fraction(num2[i])
	}


	result_sub = float(parameters["A"] - parameters["B"])
	sub.append(result_sub)

	url2 = 'http://127.0.0.1:5000/sub'
	response2 = requests.get(url2, params=parameters)
	data2=response2.text
	d.append(float(data2))

	class test(unittest.TestCase):	

		def test_Sub(self):
			for i in range(len(num1)):
				self.assertAlmostEqual(sub[i],d[i])

			
if __name__ == '__main__':	
	unittest.main()