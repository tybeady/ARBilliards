
import sys
import numpy
import math

exampleCueBall = (1, 0, 59.5, [15,15], math.pi/4)
exampleObjBall = (1, 1, 59.5, [29,30])
newColliderCoord = []
cornerCoords = [100, 100]

# Create a triangle to model resultant vectors
deltx = exampleCueBall[3][0] - exampleObjBall[3][0]
delty = exampleCueBall[3][1] - exampleObjBall[3][1]
hypot = math.sqrt(math.pow(deltx,2)+math.pow(delty,2)) # Can be thought of as the distance between balls
# Referring to model triangle jpg, draw resulting collision angles
theta1 = math.atan(deltx/delty)-exampleCueBall[4]
theta2 = math.asin((hypot*math.sin(theta1))/(exampleCueBall[2]))
theta2min = (math.pi-theta1)/2
theta3 = math.pi - theta1 - theta2
thetaDelta = math.pi/2 - exampleCueBall[4]
thetaH = theta3 - thetaDelta
# Calculate new starting coordinates and vectors
if  theta2min >= theta2:
    newColliderThetaf = (theta2)+exampleCueBall[4]
elif theta2min <= theta2:
    newColliderThetaf = (math.pi-theta2)+exampleCueBall[4]
else: # head-on collision
    newColliderThetaf = exampleCueBall[4]
if (theta2 > 0): #Aimed to the right of the object ball
    newCollideeThetaf = newColliderThetaf - math.pi/2
elif (theta2 < 0): #Aimed to the left of the object ball
    newCollideeThetaf = newColliderThetaf + math.pi/2
else: #Aimed directly at the center of the object ball
    newCollideeThetaf = newColliderThetaf
#newColliderCoord[1] = exampleCueBall[3][0] + exampleCueBall[2]*math.cos(thetaH)
#newColliderCoord[2] = exampleCueBall[3][1] + exampleCueBall[2]*math.sin(thetaH)

print(newColliderThetaf, newCollideeThetaf)

if (0 < newColliderThetaf and newColliderThetaf < (math.pi/2)): #Aimed at top right corner of the table
    deltxtr = cornerCoords[1] - exampleCueBall[3][0] #Triangle height to top right pocket
    deltytr = cornerCoords[0] - exampleCueBall[3][1] #Triangle base length to top right pocket
    hypot = math.sqrt( (math.pow(deltxtr,2) - math.pow(deltytr,2) ) ) #Distance formula measuring hypotenuse to top right pocket
    theta1 = math.atan(deltxtr/deltytr) #angle from cue ball to tr pocket
    if (newColliderThetaf < theta1): #Hitting the right wall
        newColliderThetaf = math.pi - newColliderThetaf
    elif (newColliderThetaf > theta1): #Hitting the top wall
        newColliderThetaf = (-1) * newColliderThetaf
    else: #Gonna scratch it, THROW IN WARNING?
        pass
print(newColliderThetaf)