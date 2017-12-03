from perceptron import *
from gui import *

# Global Variables
no_examples = 2000

while(True):
	
	# Variables used
	points = [] 			# List of training points
	acc = 0 				# Accuracy
	prevWeightRatio = 1		# Ratio of weights (useful for analysis)

	# Reset canvas
	t.reset()

	# Create a perceptron
	brain = Perceptron()

	# Generate Random Points
	for i in range(no_examples):
		points.append(Point())

	# Execute for each point
	for point in points:

		# Inputs of the perceptron
		inputs = [point.x, point.y]

		# Target label (class)
		target = point.label
		
		# Predicted label
		guess = brain.guess(inputs)

		'''
			If the predicted label is correct, show the point in green, otherwise, show it in red.
		'''
		if guess==target:
			point.show("green")
			acc += 1
		else:
			point.show("red")

		'''
			Train the perceptron based on this input. If the guess is wrong, change the weights and biases
			to adjust according to this input.
		'''
		brain.train(inputs, target)
		
		# Display the weights and biases
		if brain.weights[1]!=0:
			print brain.weights[0] / brain.weights[1], brain.bias
		else:
			print "+inf", brain.bias

		# draw_aYeqbX(brain.weights[1], -brain.weights[0])
		draw_aYeqbXplusc(brain.weights[1], -brain.weights[0], -brain.bias)

	# Draw the 	
	draw_YeqX()

	inputs = [-9, 0.5]
	guess = brain.guess(inputs)

	print "ACCURACY: ", 100*acc/float(no_examples), "%"

	# Exit Condition
	console_inp = raw_input("continue? (y/n): ")
	if console_inp=='n' or console_inp=='N':
		break