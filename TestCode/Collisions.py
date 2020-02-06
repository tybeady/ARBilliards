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

	def __init__(self, active, type, diameter, coordinates, vector = vector()):
		self._active = active #if on table then TRUE else FALSE
		self._type = type #0 if cue ball 1 if object ball
		self._diameter = diameter #scaling for vector math purposes
		self._coordinates = coordinates #(x,y)
		self._vector = vector #see vector class
        
    def getVector(self):
        return self._vector
	
	def ballCollision(self, collideeBall):
    
        # Run calculations for active ball collision
        if collideeBall._active = TRUE:
            pass
        
        # Run calculations for inactive ball collision
        else:
            # Create a triangle to model resultant vectors
            deltx = self._coordinates[1] - collideeBall._coordinates[1]
            delty = self._coordinates[2] - collideeBall._coordinates[2]
            hypot = math.sqrt( (math.pow(deltx,2) - math.pow(delty,2) ) ) # Can be thought of as the distance between balls
            # Referring to model triangle jpg, draw resulting collision angles
            theta1 = math.atan(deltx/delty)-self._direction
            theta2 = math.asin((hypot*math.sin(theta1))/(self._diameter))
            theta2min = (math.pi-theta1)/2
            theta3 = math.pi - theta1 - theta2
            thetaDelta = math.pi/2 - self._direction
            thetaH = theta3 - thetaDelta
            # Calculate new starting coordinates and vectors
            if  theta2min >= theta2:
                newColliderThetaf = (math.pi-theta2)+self.direction
            else:
                newColliderThetaf = self.direction
            if (theta2 > 0): #Aimed to the right of the object ball
                newCollideeThetaf = newColliderThetaf - math.pi/2
            elif (theta2 < 0): #Aimed to the left of the object ball
                newCollideeThetaf = newColliderThetaf + math.pi/2
            else: #Aimed directly at the center of the object ball
                newCollideeThetaf = newColliderThetaf
            newColliderCoord[1] = self._coordinates[1] + self._diameter*cos(thetaH)
            newColliderCoord[2] = self._coordinates[2] + self._diameter*sin(thetaH)
        return newCollideeCoordThetaf, newColliderThetaf, newColliderCoord

		    # def CueObjCollision(i, deltx, delty, thetaf): #Use this when an object ball is identified along the cue trajectory
    # #Uses radians, can be switched to degrees if needed
        # deltx = obc[0]-cbc[0] #Triangle height
        # delty = obc[1]-cbc[1] #Triangle base length	
        # hypotenuse = math.sqrt( (math.pow(deltx,2) - math.pow(delty,2) ) ) #Distance formula measuring hypotenuse
        # theta1 = math.atan(deltx/delty)-thetaf[i] #Draw interior angle of projected ob placement
        # theta2 = math.asin((hypotenuse*math.sin(theta1))/(D)) #Draw interior angle of projected ob placement
        # theta2min = (math.pi-theta1)/2 #This is the minimum value theta3 can be
        # theta3 = 180 - theta1 - theta2
        # thetaDelta = 90 - thetaf[i]
        # thetaH = theta3 - thetaDelta
        
        # endcuexarray[i] = D*cos(thetaH) = startcuexarray[i+1]
        # endcueyarray[i] = D*sin(thetaH) = startcueyarray[i+1]
        # if  theta2min >= theta2:
            # thetaf = (math.pi-theta2)+thetaf[i+1]
        # else:
            # thetaf[i+1] = thetaf[i]
        # if (theta2 > 0) #Aimed to the right of the object ball
            # thetaTangent[i+1] = thetaf[i+1] - math.pi/2
        # elif (theta2 < 0) #Aimed to the left of the object ball
            # thetaTangent[i+1] = thetaf[i+1] + math.pi/2
        # else: #Aimed directly at the center of the object ball
            # thetaTangent[i+1] = thetaf[i+1]
        # CueEndType[i] = 0
        
        # return endcuexarray[i], endcueyarray[i], thetaf[i+1], CueEndType[i]
        
    # sys.exit(CueObjCollision())
		
		#TODO: add update to self._vector
	
	def wallCollision(self, wallResistance):
    
        

    # def CueWallCollision(): #Use this when no object ball is identified along the cue trajectory
    # #This whole portion is assuming the grid is layed out correctly on the table. The limits are, for the sake of this code: [0,511] (width) and [0,255] (height)
    # #REMEMBER TO INCLUDE the walla being treated as D/2 closer to the center to account for the ball's radius
        # if (0 < theta0 < (math.pi/2)) #Aimed at top right corner of the table
            # deltxtr = 511-cbc[0] #Triangle height to top right pocket
            # deltytr = 255-cbc[1] #Triangle base length to top right pocket
            # hypotenusetr = math.sqrt( (math.pow(deltxtr,2) - math.pow(deltytr,2) ) ) #Distance formula measuring hypotenuse to top right pocket
            # theta1 = math.atan(deltxtr/deltytr) #angle from cue ball to tr pocket
            # if (theta0 < theta1) #Hitting the right wall
                # thetaf = (math.pi/2)+theta0
            # elif (theta0 > theta1) #Hitting the top wall
                # thetaf = (math.pi/2)-theta0
            # else #Gonna scratch it, THROW IN WARNING?
                # pass
        # elif ((math.pi/2) < theta0 < math.pi) #Aimed at top left corner of table
            # deltxtl = cbc[0] #Triangle height to top left pocket
            # deltytl = 255-cbc[1] #Triangle base length to top left pocket
            # hypotenusetl = math.sqrt( (math.pow(deltxtl,2) - math.pow(deltytl,2) ) ) #Distance formula measuring hypotenuse to top left pocket
            # theta1 = math.atan(deltxtl/deltytl) #angle from cue ball to tl pocket
            # if (theta0 > theta1) #Hitting the top wall
                # thetaf = (math.pi/2)+theta0
            # elif (theta0 < theta1) #Hitting the left wall
                # thetaf = theta0(math.pi/2)
            # else #Gonna scratch it, THROW IN WARNING?
                # pass
        # elif (math.pi < theta0 < (3*math.pi/4)) #Aimed at bottom left corner of table
            # deltxbl = cbc[0] #Triangle height to bottom left pocket
            # deltybl = cbc[1] #Triangle base length to bottom left pocket
            # hypotenusebl = math.sqrt( (math.pow(deltxbl,2) - math.pow(deltybl,2) ) ) #Distance formula measuring hypotenuse to bottom left pocket
            # theta1 = math.atan(deltxbl/deltybl) #angle from cue ball to bl pocket
            # if (theta0 < theta1) #Hitting the left wall
                # thetaf = (math.pi/2)+theta0
            # elif (theta0 > theta1) #Hitting the bottom wall
                # thetaf = theta0-(math.pi/2)
            # else #Gonna scratch it, THROW IN WARNING?
                # pass
        # elif ((3*math.pi/4) < theta0 < 0) #Aimed at bottom right corner of table
            # deltxbr = 511-cbc[0] #Triangle height to bottom right pocket
            # deltybr = cbc[1] #Triangle base length to bottom right pocket
            # hypotenusebr = math.sqrt( (math.pow(deltxbr,2) - math.pow(deltybr,2) ) ) #Distance formula measuring hypotenuse to bottom right pocket
            # theta1 = math.atan(deltxbr/deltybr) #angle from cue ball to br pocket
            # if (theta0 < theta1) #Hitting the bottom wall
                # thetaf = (math.pi/2)+theta0
            # elif (theta0 > theta1) #Hitting right top wall
                # thetaf = theta0-(math.pi/2)
            # else #Gonna scratch it, THROW IN WARNING?
                # pass
        # else 
            # thetaf = theta0+math.pi #They're just gonna nail the wall head on
            # CueEndType[i] = 1
            # #I'm worried about what'll happen if we hit the ball straight to a pocket when shot right next to the wall
    # sys.exit(CueWallCollision())
		pass

		
class events():
	def __init__(self, time, startCoordinate, stopCoordinate, ballIndex, secondaryBallIdex = None):
	
        self._startCoordinate = startCoordinate #(x,y)
        self._stopCoordinate = stopCoordinate #(x,y)
		self._ballIndex = ballIndex #points to collider
		self._secondaryBallIndex = secondaryBallIdex #None if wall
		self._time = time #points to when collision happens
		
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
	
	def addEvent(self,events):
		if self._events:
			for i,e in enumerate(self._events):
				if e.time > events.time:
					self._events.insert(i-1,event.time)
					return
		self._events.append(event.time)
		return
