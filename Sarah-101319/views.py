from django.http import HttpResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
#import io
#from PIL import Image

datapath = 'C:/Users/Sarah Medved/Desktop/Tests/points.txt'
imgpath = 'C:/Users/Sarah Medved/Desktop/Tests/Images/testimage.jpg'

url = "http://craphound.com/images/1006884_2adf8fc7.jpg"
#url = "http://localhost:8000/billiards_main/TSB.jpg"

@csrf_exempt 
def index(request):
    if request.method == 'POST':
        HandleText(request)
        HandleImage(request)
        return HttpResponse("POST")
    else:
        return HttpResponse("GET")

#####################################################
def HandleImage(request):
#    r = requests.get(url)
#    r.content
#    i = Image.open(io(r.content))
    imgpost = requests.get(url)
    #imgpost = request.POST; doesnt work
    if imgpost.status_code == 200: #sucess, OK
        with open(imgpath, 'wb') as f:
            f.write(imgpost.content)
        f.close()
            
def HandleText(request):
    datapost = str(request.POST);
    datapost = datapost[19:25]; #dirty way to only print needed data
    with open(datapath, 'a') as f:
        f.write(datapost);
        f.write("\n")
    f.close()
        
