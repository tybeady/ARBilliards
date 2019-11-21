# Image Processing
This section holds the Image Processing part of the AR Billiards project. There are two major parts here the first is the ball detection code where the user inputs an image and the code returns a size and location of circles found in the image. The second is the camera angle vector calculations which translates pixels in an image to real world 3D locations.

## Prerequisites
* Python3 installed

## Setup
1. Open project in command line
2. Run `pip install virtualenv`
3. Run `python -m venv env`
4. Run `env\Scripts\activate`
5. Run `pip install -r requirements.txt`

## Ball Detection Basic Usage

With the virtual enviroment active run `python VIDEOS.py` (NOTE: to quit the simulation press and hold `q` until the popup closes). Once running the code will pop open a window showing a billiards table with some balls on it and pink circles around the balls (and occasionally randomly about the image). This is the codes best prediction of where the balls are in each frame of the video.
