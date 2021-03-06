from random import randrange
import helpers

def sign(n): # A simple linear classifier for the line y=x
	# modify this to create new classifiers
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
			- bias: Bias of the perceptron
			- weightsLearningRate: rate at which weights are updated
			- biasLearningRate: rate at which bias is updated
			- momentum: Controls the momentum of perceptron learning
		'''
		self.weights = []
		self.bias = 10*abs(randnorm())
		self.weightsLearningRate = 0.0001
		self.biasLearningRate = 0.001
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
			
			# Experiment 1: Update weights according to how much the outputs differ (error), in what direction the input is (inputs[i])
			# and a learning rate
			self.weights[i] += error * inputs[i] * self.weightsLearningRate

			# Experiment 2: Update Update weights according to how much the outputs differ (error), distance of input from line and a learning rate
			# distFromLine = helpers.mod(helpers.dot(self.weights, inputs))
			# self.weights[i] += error * distFromLine * self.weightsLearningRate

			# Update bias
			self.bias += error * self.biasLearningRate
			# self.weights[i] += error * self.weightsLearningRate
		
		