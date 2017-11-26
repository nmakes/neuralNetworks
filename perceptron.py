from random import randrange

def sign(n): # Classifier
	if n>=0:
		return 1
	else:
		return -1

def randnorm(): # Gives a floating value between -1 and 1
	return randrange(-1, 1)

class Perceptron: # Perceptron class

	# Constructor
	def __init__(self):

		'''
			- weights: Weights corresponding to each input to the perceptron
			- learningRate: rate at which weights are updated
			- momentum: Controls the momentum of perceptron learning
		'''
		self.weights = []
		self.bias = 10*abs(randnorm())
		self.learningRate = 0.001
		self.momentum = 0.1;

		'''
			Initializing weights with random weights
		'''
		for i in range(2):
			self.weights.append(randnorm())

		'''
		The following weights make a y=x line classifier. Thus, 100% accuracy is achieved with the given sign function.
		'''
		# self.weights.append(1)
		# self.weights.append(-1)


	def guess(self, inputs):
		sum = 0

		for i in range(len(self.weights)):
			sum += inputs[i] * self.weights[i]

		output = sign(sum-self.bias)

		return output


	def train(self, inputs, target):
		guess = self.guess(inputs)
		error = target - guess

		for i in range(len(self.weights)):
			self.weights[i] += error * inputs[i] * self.learningRate
			self.bias += error * self.learningRate
			# self.weights[i] += error * self.learningRate
		
		