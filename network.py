import algebra
import activation

class Neuron: # Describes the neuron

	'''
		Written by Naveen Venkat
		nav.naveenvenkat@gmail.com
		https://github.com/nmakes
	'''

	def __init__(self, weights=None, bias=None, activation=None):
		self.weights = weights
		self.bias = bias
		self.activation = activation


	# Update weights & bias
	def update(self, dws, db):
		self.weights -= dws
		self.bias -= db


	# Modify the neuron, if required in future
	def modify(self, weights, bias, activation):
		self.weights = weights
		self.bias = bias
		self.activation = activation		


	def predict(self, inputs):



class layer: # Describes a layer in the network

	def __init__(self, neurons=None):
		self.neurons = neurons


class network:

	def __init__(self, n_layers, )