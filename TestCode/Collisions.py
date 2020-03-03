import sys
import numpy
import math

class CollisionMath():
    def __init__(self, state, force):
        _state = state
        _force = force

    def updateStateSpace(self,Time):
        pass

class vector():

    def __init__(self, magnitude = None, direction = None, startCoords, stopCoords):
        self._magnitude = magnitude #speed of the ball
        self._direction = direction #radians
        self._startCoords = startCoords #(x,y)
        self._stopCoords = stopCoords #(x,y)

    def decay(self, resistance, distanceTraveled):
        #INSERT MATH
        pass


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
        if collideeBall._active == TRUE:
            pass
        
        # Run calculations for inactive ball collision
        else:
            # Create a triangle to model resultant vectors
            deltx = self._coordinates[0] - collideeBall._coordinates[0]
            delty = self._coordinates[1] - collideeBall._coordinates[1]
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
            newColliderCoord[0] = self._coordinates[0] + self._diameter*cos(thetaH)
            newColliderCoord[1] = self._coordinates[1] + self._diameter*sin(thetaH)
            #TODO: Add vector magnitude degeneration
            #TODO: Add in time implementation
            #TODO: add update to self._vector
            
        return newCollideeCoordThetaf, newColliderThetaf, newColliderCoord

    def wallCollision(self, wallResistance, cornerCoords):

        # #This whole portion is assuming the grid is layed out correctly on the table.
        # #REMEMBER TO INCLUDE the walls being treated as D/2 closer to the center to account for the ball's radius
        if (0 < self.direction and self.direction < (math.pi/2)): #Aimed at top right corner of the table
            deltxtr = cornerCoords[1][0] - self.coordinates[0] #Triangle height to top right pocket
            deltytr = cornerCoords[1][1] - self.coordinates[1] #Triangle base length to top right pocket
            hypot = math.sqrt( (math.pow(deltxtr,2) - math.pow(deltytr,2) ) ) #Distance formula measuring hypotenuse to top right pocket
            theta1 = math.atan(deltxtr/deltytr) #angle from cue ball to tr pocket
            if (self.direction < theta1): #Hitting the right wall
                newColliderThetaf = math.pi - self.direction
            elif (self.direction > theta1): #Hitting the top wall
                newColliderThetaf = (-1) * self.direction
            else: #Gonna scratch it, THROW IN WARNING?
                pass
                
        elif ((math.pi/2) < self.direction and self.direction < math.pi): #Aimed at top left corner of table
            deltxtl = cornerCoords[0][0] - self.coordinates[0] #Triangle height to top left pocket
            deltytl = cornerCoords[1][1] - self.coordinates[1] #Triangle base length to top left pocket
            hypot = math.sqrt( (math.pow(deltxtl,2) - math.pow(deltytl,2) ) ) #Distance formula measuring hypotenuse to top left pocket
            theta1 = math.atan(deltxtl/deltytl) #angle from cue ball to tl pocket
            if (self.direction > theta1): #Hitting the top wall
                newColliderThetaf = (-1) * self.direction
            elif (self.direction < theta1): #Hitting the left wall
                newColliderThetaf = math.pi - self.direction
            else: #Gonna scratch it, THROW IN WARNING?
                pass
                
        elif (math.pi < self.direction and self.direction < (3*math.pi/4)): #Aimed at bottom left corner of table
            deltxbl = cornerCoords[0][0] - self.coordinates[0] #Triangle height to bottom left pocket
            deltybl = cornerCoords[0][1] - self.coordinates[1] #Triangle base length to bottom left pocket
            hypot = math.sqrt( (math.pow(deltxbl,2) - math.pow(deltybl,2) ) ) #Distance formula measuring hypotenuse to bottom left pocket
            theta1 = math.atan(deltxbl/deltybl) #angle from cue ball to bl pocket
            if (self.direction < theta1): #Hitting the left wall
                newColliderThetaf = math.pi - self.direction
            elif (self.direction > theta1): #Hitting the bottom wall
                newColliderThetaf = (-1) * self.direction
            else: #Gonna scratch it, THROW IN WARNING?
                pass
                
        elif ((3*math.pi/4) < self.direction and self.direction < 0): #Aimed at bottom right corner of table
            deltxbr = cornerCoords[1][0] - self.coordinates[0] #Triangle height to bottom right pocket
            deltybr = cornerCoords[0][1] - self.coordinates[1] #Triangle base length to bottom right pocket
            hypot = math.sqrt( (math.pow(deltxbr,2) - math.pow(deltybr,2) ) ) #Distance formula measuring hypotenuse to bottom right pocket
            theta1 = math.atan(deltxbr/deltybr) #angle from cue ball to br pocket
            if (self.direction < theta1): #Hitting the bottom wall
                newColliderThetaf = (-1) * self.direction
            elif (self.direction > theta1): #Hitting right wall
                newColliderThetaf = math.pi - self.direction
            else: #Gonna scratch it, THROW IN WARNING?
                pass
                
        else:
            newColliderThetaf = self.direction+math.pi #They're just gonna nail the wall head on
            #I'm worried about what'll happen if we hit the ball straight to a pocket when shot right next to the wall
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

    # Code ripped to help collisionCheck    
    def ccw(A,B,C):
        return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

    # Return true if line segments AB and CD intersect
    def intersect(A,B,C,D):
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

    def collisionCheck(self, colliderBall):
        eventColls = []
        ballColls = []
        #while(TRUE):
        for e in self._events:
            if(self.intersect(colliderBall[6][4], colliderBall[6][5], e.startCoordinate, e.endCoordinate)):
                eventColls.append(e)
        for b in self._ballArr:
            if(self.intersect(colliderBall[6][4], colliderBall[6][5], b.coordinates, b.coordinates)):
                ballColls.append(b)
        return eventColls, ballColls
        
    def timeCheck(self, colliderBallID, eventColls, ballColls):
        # soonestCollision = #Define crazy too long time
        # for e in eventColls:
            # if: #Identify colliderBallID how?
                # soonestCollision = e
        # for b in ballColls:
            # if:
                # soonestCollision = e
        # return soonestCollision
        pass
        
    def exactCollision(self, colliderBall, soonestCollision):
            
        pass
    
def main():
    addBall(TRUE, 0, 59)
    pass