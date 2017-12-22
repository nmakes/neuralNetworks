from math import sqrt, pow, exp, arctan, abs, log, sin, cos
from random import random, shuffle
import numpy as np

def mult(vec1, vec2):
	
	if len(vec1) != len(vec2):
		print "mult(): ERROR!! VECTORS ARE OF DIFFERENT LENGTH. vec1 =", vec1, ", vec2 =", vec2
		return None
	else:
		vec = []
		for i in range(len(vec1)):
			print i
			vec.append(vec1[i] * vec2[i])

		return vec


def dot(vec1, vec2):
	
	Sum = 0.0

	if len(vec1) != len(vec2):
		print "dot(): ERROR!! VECTORS ARE OF DIFFERENT LENGTH. vec1 =", vec1, ", vec2 =", vec2
		return None
	else:
		for i in range(len(vec1)):
			Sum += vec1[i] * vec2[i]

		return Sum


def mod(vec, l_measure=2):

	Sum = 0

	if type(l_measure)==int:
		
		for i in vec:
			Sum += pow(i,l_measure)

		Sum = pow(i, 1/float(l_measure))

		return Sum

	else:

		print "mod(): ERROR!! l_measure not identified. l_measure =", measure
		return None
