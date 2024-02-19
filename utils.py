import scipy as sc
import numpy as np
from numpy import cos,sin,exp,log,tan 
import math

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if n < 0 :
		res = False
	else :
		if n == 0 :
			res = 1
		else :
			x = 1
			for i in range(1, n+1) :
				x *= i
			res = x

	return res

def roots(a, b, c):
	delta = b**2-4*a*c
	if delta > 0 :
		res = (round((-b + math.sqrt(delta))/2*a, 3), round((-b - math.sqrt(delta))/2*a, 3))
	elif delta == 0 :
		res=(round(-b/2*a, 3))
	else :
		res =()
	return res

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	def func(x):
		return eval(function)
	resutl, error = sc.integrate.quad(func, lower, upper) 
	return resutl

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
