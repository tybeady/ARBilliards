import cv2
import numpy as np
from Smoother import Smooth
from Smoother import Edges
from HoughCircles import getCircles
import time
import pickle


# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture("Balls.mov")

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))


print((frame_width,frame_height))
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))

# Read until video is completed
start_time = time.time()



centers = []

while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    #frame = Smooth(frame)
    frame,c = getCircles(frame)
    centers.extend(c)
    cv2.imshow('Frame',frame)
    out.write(frame)
    cv2.imwrite('PosterOut.jpg', frame)
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()
out.release()
with open('centers.p','wb') as fp:
	pickle.dump(centers, fp)
print("--- %s seconds ---" % (time.time() - start_time))
# Closes all the frames
cv2.destroyAllWindows()
