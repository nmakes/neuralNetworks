from random import random, randrange
import turtle as t
from math import sqrt
import config

def random_choose(L):

	# Choose an element from the list randomly

	i = randrange(len(L))

	return L[i]


class Point:

	def __init__(self, x = None, y = None):

		if y==None:
			self.y = randrange(config.default_scale)
		if x==None:
			self.x = randrange(config.default_scale)

		self.x = x
		self.y = y

class Line:

	def __init__(self, m=1, c=0, scale=config.default_scale):

		self.m = m
		self.c = c
		self.scale = scale

	def f(self, x, shift=0):

		deviation = random_choose([-1,1]) * shift * self.scale
		return self.m * x + self.c + deviation


class PointGenerator:

	def __init__(self, line=Line(1,0), shift=0.02, scale=config.default_scale):

		# scale (S) : number of pixels covered as S*S
		# line : y = mx + c line about which points will be generated
		# shift (d) : maximum variation in y (fraction of total pixels given in scale) from the generator line for a given x

		self.scale = scale
		self.line = line
		self.shift = shift

	def generate(self, N):

		# Generate N points

		points = []

		for i in range(N):

			x = random() * self.scale
			x = int(x)
			y = self.line.f(x, self.shift * random())
			
			points.append(Point(x,y))

		return points


class GUI:

	def __init__(self, center_screen=config.default_center_screen, scale = config.default_scale, padding = config.default_padding): # Constructor

		self.scale = scale
		self.padding = padding

		# Set up turtle cursor
		t.tracer(1,0)
		t.speed(0)
		t.screensize(scale + 2*padding, scale + 2*padding, 'white')

		# t.setup(scale + 2*padding, scale + 2*padding)
		if center_screen:
			t.setworldcoordinates(0,0,scale, scale)
			pass
		else:
			t.setworldcoordinates(-padding,-padding,scale+padding,scale+padding)

		t.hideturtle()


	def plotPoint(self, point, drawColor="Blue", thickness=3): # plot a point
		
		# Go to the position of the point
		t.penup()
		t.setposition(point.x, point.y)

		# Set the color
		t.color(drawColor)

		# Put the point
		t.pendown()
		t.pensize(thickness)
		t.fd(2)
		t.penup()

	
	
	def plotLine(self, line, drawColor="red", thickness=1, vertical=False):
		
		# Draw line
		t.penup()
		
		# Line Color
		t.color(drawColor)

		# Line Thickness
		t.pensize(thickness)

		# Set the line's Y-intercept
		t.setposition(0, line.c)

		# Set the second point (last point according to the scale)
		t.pendown()

		if vertical:
			t.setposition(0, self.scale)
		else:
			t.setposition(self.scale, line.f(self.scale))
		
		t.penup()


	def plotAxes(self, drawColor="black"):

		# X Axis
		self.plotLine(Line(0, 0), drawColor, 2)

		# Y Axis
		self.plotLine(Line(0, 0), drawColor, 2, vertical=True)


class VanillaGradientDescent:

	def __init__(self, name="Unnamed Learning Algorithm"):

		self.name = name


	def costFunction(self, predictedList, targetList):

		m = len(predictedList)

		C = 1.0/(2*m)
		S = 0

		for i in range(m):
			pass



	# def train(self, line, inputs)



centerScreen=True

gui = GUI(center_screen=centerScreen)
gui.plotAxes()

p = Point(0, 0)
p2 = Point(config.default_scale, config.default_scale)
l = Line(0.5,20)

gui.plotPoint(p)
gui.plotPoint(p2)
gui.plotLine(l)

generator = PointGenerator(l, 0.09)
points = generator.generate(100)

for P in points:
	gui.plotPoint(P, 'darkgreen')

input('press enter to quit..')