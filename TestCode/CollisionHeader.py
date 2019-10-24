import sys
import numpy
import math

def CollisionMath():

    D = 57.15 #Cue and object ball radii
    theta0 = 45 #Essentially the trajectory of the cue ball with our assumptions, technically cue trajectory
    cbc = [100,100] #Cue ball coordinates. The first array value will be the x coordinate, the second y
    obc = [200,200] #Object ball coordinates. The first array value will be the x coordinate, the second y
    ballCoords = [cbc,obc]
    BeginnerError = math.pi/180 #0.2 degree offset
    IntermediateError = math.pi/360 #0.1 degree offset
    ExpertError = math.pi/3600 #0.01 degree offset
        
    def CueWallCollision(): #Use this when no object ball is identified along the cue trajectory
    #This whole portion is assuming the grid is layed out correctly on the table. The limits are, for the sake of this code: [0,511] (width) and [0,255] (height)
        if (0 < theta0 < (math.pi/2)) #Aimed at top right corner of the table
            deltxtr = 511-cbc[0] #Triangle height to top right pocket
            deltytr = 255-cbc[1] #Triangle base length to top right pocket
            hypotenusetr = math.sqrt( (math.pow(deltxtr,2) - math.pow(deltytr,2) ) ) #Distance formula measuring hypotenuse to top right pocket
            theta1 = math.atan(deltxtr/deltytr) #angle from cue ball to tr pocket
            if (theta0 < theta1) #Hitting the right wall
                thetaf = (math.pi/2)+theta0
            elif (theta0 > theta1) #Hitting the top wall
                thetaf = (math.pi/2)-theta0
            else #Gonna scratch it, THROW IN WARNING?
                pass
        elif ((math.pi/2) < theta0 < math.pi) #Aimed at top left corner of table
            deltxtl = cbc[0] #Triangle height to top left pocket
            deltytl = 255-cbc[1] #Triangle base length to top left pocket
            hypotenusetl = math.sqrt( (math.pow(deltxtl,2) - math.pow(deltytl,2) ) ) #Distance formula measuring hypotenuse to top left pocket
            theta1 = math.atan(deltxtl/deltytl) #angle from cue ball to tl pocket
            if (theta0 > theta1) #Hitting the top wall
                thetaf = (math.pi/2)+theta0
            elif (theta0 < theta1) #Hitting the left wall
                thetaf = theta0(math.pi/2)
            else #Gonna scratch it, THROW IN WARNING?
                pass
        elif (math.pi < theta0 < (3*math.pi/4)) #Aimed at bottom left corner of table
            deltxbl = cbc[0] #Triangle height to bottom left pocket
            deltybl = cbc[1] #Triangle base length to bottom left pocket
            hypotenusebl = math.sqrt( (math.pow(deltxbl,2) - math.pow(deltybl,2) ) ) #Distance formula measuring hypotenuse to bottom left pocket
            theta1 = math.atan(deltxbl/deltybl) #angle from cue ball to bl pocket
            if (theta0 < theta1) #Hitting the left wall
                thetaf = (math.pi/2)+theta0
            elif (theta0 > theta1) #Hitting the bottom wall
                thetaf = theta0-(math.pi/2)
            else #Gonna scratch it, THROW IN WARNING?
                pass
        elif ((3*math.pi/4) < theta0 < 0) #Aimed at bottom right corner of table
            deltxbr = 511-cbc[0] #Triangle height to bottom right pocket
            deltybr = cbc[1] #Triangle base length to bottom right pocket
            hypotenusebr = math.sqrt( (math.pow(deltxbr,2) - math.pow(deltybr,2) ) ) #Distance formula measuring hypotenuse to bottom right pocket
            theta1 = math.atan(deltxbr/deltybr) #angle from cue ball to br pocket
            if (theta0 < theta1) #Hitting the bottom wall
                thetaf = (math.pi/2)+theta0
            elif (theta0 > theta1) #Hitting right top wall
                thetaf = theta0-(math.pi/2)
            else #Gonna scratch it, THROW IN WARNING?
                pass
        else 
            thetaf = theta0+math.pi #They're just gonna nail the wall head on
            #I'm worried about what'll happen if we hit the ball straight to a pocket when shot right next to the wall
    
    sys.exit(CueWallCollision())

    def CueObjCollision(): #Use this when an object ball is identified along the cue trajectory
    #Uses radians, can be switched to degrees if needed
        deltx = obc[0]-cbc[0] #Triangle height
        delty = obc[1]-cbc[1] #Triangle base length	
        hypotenuse = math.sqrt( (math.pow(deltx,2) - math.pow(delty,2) ) ) #Distance formula measuring hypotenuse
	
        theta1 = math.atan(deltx/delty)-theta0 #Draw interior angle of projected ob placement
        theta2 = math.asin((hypotenuse*math.sin(theta1))/(D)) #Draw interior angle of projected ob placement
        theta2min = (math.pi-theta1)/2 #This is the minimum value theta3 can be
        if  theta2min >= theta2:
            thetaf = (math.pi-theta2)+theta0
        else:
            thetaf = theta0
        return Cuex
        return Objectx
            
    sys.exit(CueObjCollision())

    def UserErrorFactor():
    
        if (SL == 0)
            UEExtremeLeft = thetaf + BeginnerError #User Extreme Error to the left of the trajectory in reference to the user
            UEExtremeRight = thetaf - BeginnerError #User Extreme Error to the right of the trajectory in reference to the user
        elif (SL == 1)
            UEExtremeLeft = thetaf + IntermediateError #User Extreme Error to the left of the trajectory in reference to the user
            UEExtremeRight = thetaf - IntermediateError #User Extreme Error to the right of the trajectory in reference to the user
        elif (SL == 2)
            UEExtremeLeft = thetaf + ExpertError #User Extreme Error to the left of the trajectory in reference to the user
            UEExtremeRight = thetaf - ExpertError #User Extreme Error to the right of the trajectory in reference to the user
        
    sys.exit(UserErrorFactor())

    def CreateHoloLensShipPackage():
    
        Cue = {"start" : (x1,y1), "end" : (x2,y2), "endType" : EndType}
        Object = {"start" : (x1,y1), "end" : (x2,y2), "endType" : EndType}
    
    sys.exit(CreateCuePackage())
    
sys.exit(CollisionMath())
