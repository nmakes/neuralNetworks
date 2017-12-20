import turtle as t
from random import randrange
from math import sqrt

class Point:

	def __init__(self, scale = 800): # Constructor

		# Initialize a random point
		self.x = randrange(200)
		self.y = randrange(200)

		# Set up turtle cursor
		t.tracer(1,0)
		t.speed(0)
		t.setup(1000,1000)
		t.setworldcoordinates(0,0,1000,1000)
		t.hideturtle()
		
		# Set label for the point (known from )
		self.label = sign(self.x-self.y)


	def show(self, drawColor=None): # show a point
		
		# Go to the position of the point
		t.penup()
		t.setposition(self.x * 4, self.y * 4)

		# Set the color
		if(drawColor==None):

			if self.label == 1:
				t.color(1.0,0.0,0.0)
			elif self.label == -1:
				t.color(0.0,0.0,1.0)
		else:
			t.color(drawColor)

		# Put the point
		t.pendown()
		t.pensize(4)
		t.fd(2)
		t.penup()


# Draw y=x line
def draw_YeqX():
	t.penup()
	t.setposition(0,0)
	t.pensize(1)
	t.seth(45)
	t.color("black")
	t.pendown()
	t.fd(1700)


# Draw aY = bX line
def draw_aYeqbX(a,b):
	
	# Calculate slope
	if a==0:
		tanTheta = 1000 # Very high value
	else:
		tanTheta = float(b/a)
	
	# Draw line
	t.penup()
	t.setposition(0,0)
	t.color("pink")
	t.pensize(1)
	t.pendown()
	t.setposition(1700*(1/sqrt(1+(tanTheta**2))), 1700*(tanTheta/sqrt(1+(tanTheta**2))))
	t.penup()


# Draw aY = bX + c line
def draw_aYeqbXplusc(a,b,c):
	
	# Calculate slope
	if a==0:
		tanTheta = 1000.0 # Very high value
	else:
		tanTheta = float(b)/a
	
	# Draw line
	t.penup()
	if a==0:
		t.setposition(0,0)
	else:
		t.setposition(0,float(c)/a)
	t.color("pink")
	t.pensize(1)
	t.pendown()
	t.setposition(1700*(1/sqrt(1+(tanTheta**2))), c + 1700*(tanTheta/sqrt(1+(tanTheta**2))))
	t.penup()