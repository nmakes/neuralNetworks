# Assuming sigmoid neuron

'''
		[ ]
		[ ]		[ ]
		[ ]		[q]
		[ ]   /	[ ]
		[ ]  /  [ ]
		[ ] /	[ ]
		[p]		[ ]
		[ ]		[ ]
		[ ]

Layer:	N-1 	 N

Wpq = weight between q'th neuron of layer N and p'th neuron of layer N-1
lr = learning rate
Onq = output of qth neuron in nth layer
On_1p = output of pth neuron in (n-1)th layer

'''


Wpq = Wpq - lr * Onq * (1-Onq) * (On_1p)