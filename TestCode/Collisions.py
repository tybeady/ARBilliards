class CollisionMath():
	def __init__(self, state, force):
		_state = state
		_force = force
		
	def updateStateSpace(self,Time):
		pass


class vector():

	def __init__(self, magnitude = None, direction = None):
		self._magnitude = magnitude #speed of the ball
		self._direction = direction #radians
	
	def decay(self, resistance, distanceTraveled):
		#INSERT MATH


class ball():

	def __init__(self, active, type, diameter, cooridnates, vector = vector()):
		self._active = active #if on table then TRUE else FALSE
		self._type = type #0 if cue ball 1 if object ball
		self._diameter = diameter #scaling for vector math purposes
		self._cooridnates = cooridnates #(x,y)
		self._vector = vector #see vector class
	
	def ballCollision(self, collideeBall):
		#INSERT MATH
		
		#TODO: add update to self._vector
		pass
	
	def wallCollision(self, wallResistance):
		#INSERT MATH
		pass

		
class event():
	def __init__(self, time, ballIndex, secondaryBallIdex = None):
	
		self._ballIndex = ballIndex #points to collider
		self._secondaryBallIndex = secondaryBallIdex #None if wall
		self.time = time #points to when collision happens
		
class table():

	def __init__(self, cornerCoords, ballArr = [], wallResistance, feltResistance):
		self._cornerCoords = cornerCoords #pass two tuples in array forming diagonal of table [(x1,y1),(x2,y2)]
		self._ballArr = ballArr
		self._wallResistance = wallResistance
		self._feltResistance = feltResistance
		self._events = []
		self._pocketLocations = [
				(cornerCoords[0][0],cornerCoords[0][1]),
				(cornerCoords[0][0],cornerCoords[1][1]),
				(cornerCoords[1][0],cornerCoords[0][1]),
				(cornerCoords[1][0],cornerCoords[1][1])
			]
		if (abs(cornerCoords[0][0] - cornerCoords[1][0]) > abs(cornerCoords[0][1] - cornerCoords[1][1])):
			self._pocketLocations.extend([
				(((cornerCoords[0][0]+cornerCoords[1][0])/2),cornerCoords[0][1]),
				(((cornerCoords[1][0]+cornerCoords[1][0])/2),cornerCoords[1][1])])
		else:
			self._pocketLocations.extend([
				(cornerCoords[0][0],((cornerCoords[0][1]+cornerCoords[1][1])/2)),
				(cornerCoords[1][0],((cornerCoords[0][1]+cornerCoords[1][1])/2))])

	def addBall(self, ball):
		self._ballArr.append(ball)
		return
		
	def takeStep(self):
		nextEvent = self._events.pop(0)
	
	def addEvent(self,event):
		if self._events:
			for i,e in enumerate(self._events):
				if e.time > event.time:
					self._events.insert(i-1,event.time)
					return
		self._events.append(event.time)
		return
