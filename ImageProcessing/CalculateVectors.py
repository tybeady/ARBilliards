##VectorManager
##
##PURPOSE:
##Create a way to quickly and easily calculate the 3D location of a pixel on an image given the (X,Y,Z) camera position and
##the (X,Y,Z) position of the center pixel
##
##EXAMPLE USE:
##VM = VectorManager(60,50, 200, 300)
##VM.SetCameraAngle((0,5,0),(3,0,2))
##v1 = VM.CalculateVector(150,200)
##v2 = VM.CalculateVector(75,80)


import math



class VectorManager():

    ######## INIT #########
    ##VARIABLE ||||||||| DESCRIPTION
    ##==============================
    ##_HRZ_FOV         | Horizontal Field of View defined by the cameras focal length and sensor size input in degrees
    ##_VRT_FOV         | Vertical Field of View defined by the cameras focal length and sensor size input in degrees
    ##_pixelH          | The size in pixels of the height of the image
    ##_pixelW          | The size in pixels of the width of the image
    def __init__(self,Hrz_FOV,Vrt_FOV,PixelW,PixelH):
        _HRZ_FOV = math.radians(Hrz_FOV)
        _VRT_FOV = math.radians(Vrt_FOV)
        _pixelH = PixelH
        _pixelW = PixelW
        _radPerPixH = _VRT_FOV/_pixelH
        _radPerPixW = _HRZ_FOV/_pixelW
        _alphaBase = _HRZ_FOV/2
        _betaBase = _VRT_FOV/2
        _CameraAlphaBase = 0
        _CameraBetaBase = 0

    ##Given alpha and beta where alpha is the rotations from the X axis in respect to the Z (ignoring the Y) and beta is the rotations from the
    ##Z axis in respect to Y (ignoring X) returns a vector that is in the direction of the combined angles.
    def CalculateDirectionVector(self,alpha,beta):
        alpha = math.radians(alpha)
        beta = math.radians(beta)
        x = math.sin(alpha)*math.cos(beta)
        y = math.cos(beta)
        z = math.sin(alpha)*math.sin(beta)
        return (x,y,z)


    ##Scales the vector by a scalor. Used to take the direction vector produced above and extend it so the Y value is the same as the difference
    ##between the camera height and the gaze height
    def ScaleVector(self,v,s,i=1):
        scalor = s/v[i]
        _v = (v[0]*scalor,v[1]*scalor,v[2]*scalor)
        return _v


    ##Ran once per image to set the base alpha and beta to the top right of the image
    def SetCameraAngle(self,CameraPos,GazePos):
        CameraAngleV = math.atan((CameraPos[2] - GazePos[2])/(CameraPos[1] - GazePos[1]))
        CameraAngleH = math.atan((CameraPos[2] - GazePos[2])/(CameraPos[0] - GazePos[0]))
        _CameraAlphaBase = CameraAngleH + _alphaBase
        _CameraBetaBase = CameraAngleV + _betaBase

    ##Ran multiple times per image to return the vector from the camera to any pixel in the image on a XZ plane at Y height of the gaze position
    def CalculateVector(self,PixelX,PixelY):
        PixelAlpha = _CameraAlphaBase + PixelX*_radPerPixH
        PixelBeta = _CameraBetaBase + PixelY*_radPerPixV
        v = CalculateDirectionVector(PixelAlpha,PixelBeta)
        return ScaleVector(v,abs(CameraPos[1] - GazePos[1]))
