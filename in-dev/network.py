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

	def __init__(self, sizes):
		self.n_layers = len(sizes)
		self.sizes = sizes
		self.biases = [algebra.np.random.randn(y,1) for y in sizes[1:]]
		self.weights = [algebra.np.random.randn(x,y) for (x,y) in zip(sizes[:-1], sizes[1:])]

	
	def feedforward(self, inp):

		out = inp

		for b, w in zip(self.biases, self.weights):
			out = activation.logistic(np.dot(w, out) + b)

		return out


	def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):

		if test_data is not None:
			n_test = len(test_data)

		n = len(training_data)

		for j in xrange(epochs):
			algebra.shuffle(training_data)
			mini_batches = [
							training_data[k:k+mini_batch_size]
							for k in xrange(0,n,mini_batch_size)
							]
			for mini_batch in mini_batches:
				self.update_mini_batch(mini_batch, eta)

			if test_data:
				print "Epoch", j, ":", self.evaluate(test_data), n_test
			else:
				print "Epoch", j, "complete"


	def update_mini_batch(self, mini_batch, eta):

		# Temporary biases and weights
		temp_b = [np.zeros(b.shape) for b in self.biases]
		temp_w = [np.zeros(w.shape) for w in self.weights]

		for x,y in mini_batch:
			d_temp_b, d_temp_w = self.backprop(x,y)
			temp_b = [tb + dtb for (tb,dtb) in zip(temp_b, d_temp_b)]
			temp_w = [tw + dtw for (tw,dtw) in zip(temp_w, d_temp_w)]

		self.weights = [w - (eta / len(mini_batch))*tw
						for w,tw in zip(self.weights, temp_w)]

		self.biases = [b - (eta / len(mini_batch))*tb
						for b,tb in zip(self.biases, temp_b)]