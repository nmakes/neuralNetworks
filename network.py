import algebra

# Standard activation functions

def identity(x):
	return x

def d_identity(x):
	return 1

def step(x):
	if x<0:
		return 0
	else:
		return 1

def d_step(x):
	if x!=0:
		return 0
	else:
		return None

def logistic(x):
	return 1/(1+algebra.exp(-x))

def d_logistic(x):
	f= logistic(x)
	return f * (1 - f)

def tanh(x):
	return (2.0/(1+exp(-2*x))) - 1.0

def d_tanh(x):
	f= tanh(x)
	return 1-f*f

def arctan(x):
	return algebra.arctan(x)

def d_arctan(x):
	return 1.0/(1+x*x)

def softsign(x):
	return x / (1 + algebra.abs(x))

def d_softsign(x):
	return 1 / ((1 + algebra.abs(x)) ** 2)

def isru(x,a=1):
	return x / algebra.sqrt()

standard_activation_functions = {
	'identity': (lambda x: x, lambda x: 1),
	'step': (lambda x: 0 if x<0 else 1, lambda x: 0 if x!=0 else None),
	'logistic': (lambda x: 1/(1+algebra.exp(-x)), lambda x: (1/(1+algebra.exp(-x)))*(1- (1/(1+algebra.exp(-x))))),
	'tanh': (lambda x: (1+algebra.exp(-2*x)))/(1+algebra.exp(-2*x)), 
}

class ActivationFunction:

	def __init__(self, name=None, F=None, dF=None):
		
		if name == 'identity':

		self.name = name
		self.F = F
		self.dF : dF,


	def 

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