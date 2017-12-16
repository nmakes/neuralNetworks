from math import sqrt

def dot(vec1, vec2):
	
	prod = 0

	print vec1, vec2

	if len(vec1) != len(vec2):
		print "dot(): ERROR!! VECTORS ARE OF DIFFERENT LENGTH. vec1 =", vec1, ", vec2 =", vec2
		return None
	else:
		vec = []
		for i in range(len(vec1)):
			print i
			vec[i] = vec1[i] * vec2[i]

		return vec

def mod(vec, measure='euclidean'):

	sum = 0

	if measure=='euclidean':
		for i in vec:
			sum += i*i
		sum = sqrt(sum)
		return sum
	else:
		print "mod(): ERROR!! measure not identified. measure =", measure
		return None