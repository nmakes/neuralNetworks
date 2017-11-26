import turtle as t
from random import randrange
from math import sqrt

class Point:

	def __init__(self):
		self.x = randrange(200)
		#print self.x,
		self.y = randrange(200)
		#print self.y

		t.tracer(1,0)
		t.speed(0)

		t.setup(1000,1000)
		t.setworldcoordinates(0,0,1000,1000)

		t.hideturtle()

		self.label = None

		if self.x>=self.y:
			self.label = 1
			t.color("blue")
		else:
			self.label = -1
			t.color("red")

	def show(self, drawColor=None):
		t.penup()
		t.setposition(self.x * 4, self.y * 4)

		if(drawColor==None):

			if self.label == 1:
				t.color(1.0,0.0,0.0)
			elif self.label == -1:
				t.color(0.0,0.0,1.0)
		else:
			t.color(drawColor)

		t.pendown()
		t.pensize(4)
		t.fd(2)
		t.penup()

def draw_YeqX():
	t.penup()
	t.setposition(0,0)
	t.pensize(1)
	t.seth(45)
	t.color("black")
	t.pendown()
	t.fd(1700)

def draw_aYeqbX(a,b):
	if a==0:
		tanTheta = 1000 # Very high value
	else:
		tanTheta = float(b/a)
	t.penup()
	t.setposition(0,0)
	t.color("pink")
	t.pensize(1)
	t.pendown()
	t.setposition(1700*(1/sqrt(1+(tanTheta**2))), 1700*(tanTheta/sqrt(1+(tanTheta**2))))
	t.penup()

def draw_aYeqbXplusc(a,b,c):
	if a==0:
		tanTheta = 1000.0 # Very high value
	else:
		tanTheta = float(b)/a
	t.penup()
	t.setposition(0,float(c)/a)
	t.color("pink")
	t.pensize(1)
	t.pendown()
	t.setposition(1700*(1/sqrt(1+(tanTheta**2))), c + 1700*(tanTheta/sqrt(1+(tanTheta**2))))
	t.penup()