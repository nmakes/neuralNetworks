import algebra
import activation

class Neuron: # Describes the neuron

	'''
		Written by Naveen Venkat
		nav.naveenvenkat@gmail.com
		https://github.com/nmakes
	'''

	def __init__(self, weights=None, bias=None, activation=None, d_activation=None):
		self.weights = weights
		self.bias = bias
		self.activation = activation
		self.d_activation = d_activation


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
		pass


class Layer: # Describes a layer in the network

	def __init__(self, n_neurons=None, weightsList=None, biasList=None, activation=None, d_activation=None, neurons=None):
		self.n_neurons = n_neurons
		self.activation = activation
		self.d_activation = d_activation

		if neurons == None:
			neurons = [Neuron(activation, d_activation)]


class network:

	def __init__(self, n_layers, )