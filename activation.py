import algebra

# Standard activation functions

# Identity
def identity(x):
	return x

def d_identity(x):
	return 1

# Step
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

# Logistic
# AKA Sigmoid
def logistic(x):
	return 1/(1+algebra.exp(-x))

def d_logistic(x):
	f= logistic(x)
	return f * (1 - f)

# Tan Hyperbolic
def tanh(x):
	return (2.0/(1+exp(-2*x))) - 1.0

def d_tanh(x):
	f= tanh(x)
	return 1-f*f

# Inverse Tan
def arctan(x):
	return algebra.arctan(x)

def d_arctan(x):
	return 1.0/(1+x*x)

# Softsign
def softsign(x):
	return x / (1 + algebra.abs(x))

def d_softsign(x):
	return 1 / ((1 + algebra.abs(x)) ** 2)

# Inverse Square root Unit
def isru(x,a):
	return x / algebra.sqrt(1 + a*x*x)

def d_isru(x,a):
	return (1 / algebra.sqrt(1 + a*x*x))**3

# Rectified Linear Unit
def relu(x):
	if x<0:
		return 0
	else:
		return x

def d_relu(x):
	if x<0:
		return 0
	else:
		return 1

# Leaky ReLU
def leakyRelu(x):
	if x<0:
		return 0.01*x
	else:
		return x

def d_leakyRelu(x):
	if x<0:
		return 0.01
	else:
		return 1

# Parametric ReLU
def paramRelu(x,a):
	if x<0:
		return a*x
	else:
		return x

def d_paramRelu(x,a):
	if x<0:
		return a
	else:
		return 1

# Randomized ReLU
def randomRelu(x):
	if x<0:
		a = algebra.random()
		return (a*x, a)
	else:
		return x

def d_randomRelu(x,a):
	if x<0:
		return a
	else:
		return 1

# Exponential Linear Unit
def elu(x,a):
	if x<0:
		return a * (algebra.exp(x)-1)
	else:
		return x

def d_elu(x,a):
	if x<0:
		return elu(x,a) + a
	else:
		return 1

# S-shaped ReLU
def srelu(x,al,tl,ar,tr):
	if tl>tr:
		print "ERROR [srelu()]: tl > tr"
		return None
	else:
		if x<=tl:
			return tl + al*(x-tl)
		elif tl<x<tr:
			return x
		else:
			return tr + ar*(x-tr)

def d_srelu(x,al,tl,ar,tr):
	if tl>tr:
		print "ERROR [srelu()]: tl > tr"
		return None
	else:
		if x<=tl:
			return al
		elif tl<x<tr:
			return 1
		else:
			return ar

# Inverse Square Root Linear Unit
def isrlu(x,a):
	if x<0:
		return x / algebra.sqrt(1 + a*x*x)
	else:
		return x

def d_isrlu(x,a):
	if x<0:
		return (1 / algebra.sqrt(1 + a*x*x))**3
	else:
		return 1

# Adaptive Piecewise Linear Unit
def apl():
	pass
	# TODO: Implement adaptive piecewise linear 

def d_apl():
	pass
	# TODO: Implement derivative of adaptive piecewise linear

# Softplus
def softplus(x):
	return algebra.log(1+algebra.exp(x))

def d_softplus(x):
	return 1 / (1 + algebra.exp(-x))

# Bent Identity function
def bentIdentity(x):
	return ((algebra.sqrt(x**2 + 1) - 1)/2 + x)

def d_bentIdentity(x):
	return (x / (2 * (algebra.sqrt(x**2 + 1))) + 1)

# SoftExponential
def softExp(x,a):
	if a==0:
		return x
	elif a > 0:
		return (algebra.exp(a*x)-1)/a + a
	else:
		return -(algebra.log(1-a*(x+a)))/a

def d_softExp(x,a):
	if a<0:
		return 1/(1-a*(a+x))
	else:
		return algebra.exp(a*x)

# Sinusoidal
def sin(x,a=1,b=1):
	return a*algebra.sin(b*x)

def d_sin(x,a=1,b=1):
	return a*b*algebra.cos(b*x)

# Cardinal Sin
def sinc(x):
	if x==0:
		return 1
	else:
		return algebra.sin(x)/x

def d_sinc(x):
	if x==0:
		return 0
	else:
		return algebra.cos(x)/x - algebra.sin(x)/x

# Gaussian
def gaussian(x):
	return algebra.exp(-x**2)

def d_gaussian(x):
	return -2*x*algebra.exp(-x**2)
