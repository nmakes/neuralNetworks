from random import random, randrange


def random_choose(L):

	# Choose an element from the list randomly

	i = randrange(len(L))

	return L[i]


class PointGenerator:

	def __init__(self, scale=800, generator={'m':1, 'c':0}, shift=0.02):

		# scale (S) : number of pixels covered as S*S
		# generator : y = mx + c line about which points will be generated
		# shift (d) : maximum variation in y (fraction of total pixels given in scale) from the generator line for a given x

		self.scale = scale
		self.generator = generator
		self.shift = shift


	def generate(N):

		# Generate N points

		points = []

		m = self.generator['m']
		c = self.generator['c']

		for i in range(N):

			x = random() * self.scale
			x = int(x)
			y = m*x + c
			deviation = random_choose([-1,1]) * self.shift * self.scale
			points.append()