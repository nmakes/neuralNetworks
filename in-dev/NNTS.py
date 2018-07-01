class ActivationFunction(object):

	def __init__(self):

		out = None
		der = None


class RegularizationFunction:

	def __init__(self):

		out = None
		der = None
		

class Errors:

	@staticmethod
	

class ErrorFunction:

	def __init__(self):

		self.error = {"output":None, "target":None}
		self.der = {"output":None, "target":None}


class Node:

	def __init__(self, ID = "Uninitialized ID", activation = ActivationFunction(), initZero = bool()):

		self.id = ID

		#List of input links.
		self.inputLinks = []

		if initZero:
			self.bias = 0
		else:
			self.bias = 0.1
		
		# List of output links.
		self.outputs = []
		self.totalInput = None
		self.output = None

		# Error derivative with respect to this node's output.
		self.outputDer = 0
		
		# Error derivative with respect to this node's total input.
		self.inputDer = 0

		# Accumulated error derivative with respect to this node's total input since
		# the last update. This derivative equals dE/db where b is the node's
		# bias term.
		self.accInputDer = 0

		# Number of accumulated err. derivatives with respect to the total input
		# since the last update.
		self.numAccumulatedDers = 0
		
		# Activation function that takes total input and returns node's output
		self.activation = ActivationFunction()


	# Recomputes the node's output and returns it. */
	def updateOutput():
		
		# Stores total input into the node.
		self.totalInput = self.bias
		
		for j in len(self.inputLinks):
			link = self.inputLinks[j]
			self.totalInput += link.weight * link.source.output

		self.output = self.activation.output(self.totalInput)
		return self.output