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

div=[]
f=[]

for i in range(len(num1)):
	
	parameters = {
	"A":Fraction(num1[i]),
	"B":Fraction(num2[i])
	}


	result_div = float(parameters["A"] / parameters["B"])
	div.append(result_div)


	url4 = 'http://127.0.0.1:5000/div'
	response4 = requests.get(url4, params=parameters)
	data4=response4.text
	f.append(float(data4))


	class test(unittest.TestCase):
		def test_div(self):
			for i in range(len(num1)):

				self.assertAlmostEqual(div[i],f[i])
				if (str(div[i])[:11])==(str(f[i]))[:11]:
					print(str(div[i])[:11] + ' ' + (str(f[i]))[:11] + ' ' + 'success')
				else:
					print(str(div[i])[:11] + ' ' + (str(f[i]))[:11] + ' ' + 'fail')

if __name__ == '__main__':	
	unittest.main()


