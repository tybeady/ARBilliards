from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import requests
import base64
import json
import cv2
import numpy as np
from .Smoother import Smooth
from .Smoother import Edges
from .HoughCircles import getCircles
from .CalculateVectors import VectorManager



datapath = 'C:/Users/Sarah Medved/Desktop/Tests/points.txt'
imgpath = 'C:/Users/Sarah Medved/Desktop/Tests/Images/testimage.jpg'
VM = VectorManager(60,50, 200, 300)


param1 = 40
param2 = 25
minSize = 20
maxSize = 60

@csrf_exempt 
def calibrationValues(request):
    global param1,param2,minSize,maxSize

    if request.method == 'GET':
        param1 = float(request.GET.get('param1'))
        param2 = float(request.GET.get('param2'))
        minSize = int(request.GET.get('minSize'))
        maxSize = int(request.GET.get('maxSize'))
        return HttpResponse([param1,param2,minSize,maxSize])
    else:
        return HttpResponseBadRequest("Request Must Be GET")

@csrf_exempt 
def tableInit(request):

    if request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest("Request Must Be Post")

@csrf_exempt 
def index(request):
    
    #return HttpResponse("Working")

    if request.method == 'POST':
        #HandleText(request)
        print("Post")
        
        HandleImage(request)
        return HttpResponse("POST")
    else:
        return HttpResponse("GET")


#####################################################
def HandleImage(request):
    imgpost = request.FILES["file"]
    imgdata = imgpost.read()
    #jpg_original = base64.b64decode(imgdata)
    jpg_as_np = np.frombuffer(imgdata, dtype=np.uint8)
    img = cv2.imdecode(jpg_as_np, flags=1)
    #frame = Smooth(img)
    frame,c = getCircles(img,param1,param2,minSize,maxSize)
    cv2.imwrite('./0.jpg', frame)
    print("Here")
            
def HandleText(request):
    datapost = str(request.POST);
    #datapost = datapost[19:25]; 
    with open(datapath, 'a') as f:
        f.write(datapost);
        f.write("\n")
    f.close()
        
