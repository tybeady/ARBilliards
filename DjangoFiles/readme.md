# Django Installation for Server Communication
This section explains how to install Django and set up the server used by the Augmented Reality Billiards System to communicate with the Hololens. For more details, you may follow along with the Django documentation found here: https://docs.djangoproject.com/en/2.2/intro/tutorial01/

## Prerequisites
* Python3 installed

## Initial Sever Setup
1. Open project in command line
2. Run `pip install django`
3. Navigate to the directory you wish to store the project
4. Run `django-admin startproject arbilliards`
5. Run `python manage.py runserver 0.0.0.0:8000` to test server and listen on all public IPs

## Create Application
1. Navigate to inside the `arbilliards` project folder
2. Copy our included `urls.py` file into the `arbilliards` folder
2. Open command line and run `python manage.py startapp billiardsmain`
3. Open the `billiardsmain` folder and replace `views.py` with our included `views.py` script
4. Copy our included `urls.py` file into the `billiardsmain` folder

## Server Usage
This server will be used for any computations or image processing that cannot be completed onboard the Hololens. 