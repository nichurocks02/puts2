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

#print(num1)
#print(num2)

#fn=['2','11.2','21/7','2','3','21.7','11.7']
#sn=['7','21.7','11/21','21.7','7/11','7/21','21.7']
'''above lists are defined in such a manner such that all the data types 
for calculation - integer, fraction and decimal values compute among each
other to check the solution written in main.py'''
#count=0
add=[]
sub=[]
mul=[]
div=[]
c=[]
d=[]
e=[]
f=[]
r=[]
for i in range(len(num1)):
	
	parameters = {
	"A":Fraction(num1[i]),
	"B":Fraction(num2[i])
	}
	#print(count)
	#r.append(parameters["A"])
	result_add = float(parameters["A"] + parameters["B"])
	add.append(result_add)
	result_sub = float(parameters["A"] - parameters["B"])
	sub.append(result_sub)
	result_mul = float(parameters["A"] * parameters["B"])
	mul.append(result_mul)
	result_div = float(parameters["A"] / parameters["B"])
	div.append(result_div)

	url1 = 'http://127.0.0.1:5000/add'
	response1 = requests.get(url1, params=parameters)
	data=response1.text
	c.append(float(data))


	url2 = 'http://127.0.0.1:5000/sub'
	response2 = requests.get(url2, params=parameters)
	data2=response2.text
	d.append(float(data2))


	url3 = 'http://127.0.0.1:5000/mul'
	response3 = requests.get(url3, params=parameters)
	data3=response3.text
	e.append(float(data3))
		

	url4 = 'http://127.0.0.1:5000/div'
	response4 = requests.get(url4, params=parameters)
	data4=response4.text
	f.append(float(data4))

	class test(unittest.TestCase):	


		def test_Add(self):
			for i in range(len(num1)):
				self.assertAlmostEqual(add[i],c[i])
				

		def test_Sub(self):
			for i in range(len(num1)):
				self.assertAlmostEqual(sub[i],d[i])

			
		def test_mul(self):
			count=0
			for i in range(len(num1)):
				#count=count+1
				#print(count)
				self.assertAlmostEqual(mul[i],e[i])
			
		def test_div(self):
			for i in range(len(num1)):
				self.assertAlmostEqual(div[i],f[i])

'''print(len(c))
print(len(d))
print(len(e))
print(len(f))
print(len(add))
print(len(sub))
print(len(div))
print(len(mul))
'''
if __name__ == '__main__':	
	unittest.main()
