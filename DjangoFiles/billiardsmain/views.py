from django.http import HttpResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

datapath = 'C:/Users/Sarah Medved/Desktop/Tests/points.txt'
imgpath = 'C:/Users/Sarah Medved/Desktop/Tests/Images/testimage.jpg'

@csrf_exempt 
def index(request):
    
    return HttpResponse("Working")

    if request.method == 'POST':
        HandleText(request)
        HandleImage(request)
        return HttpResponse("POST")
    else:
        return HttpResponse("GET")

#####################################################
def HandleImage(request):
    imgpost = request.FILES["file"]
    imgdata = imgpost.read()
    with open(imgpath, 'wb+') as f: 
        f.write(imgdata)
    f.close()
            
def HandleText(request):
    datapost = str(request.POST);
    #datapost = datapost[19:25]; 
    with open(datapath, 'a') as f:
        f.write(datapost);
        f.write("\n")
    f.close()
        
