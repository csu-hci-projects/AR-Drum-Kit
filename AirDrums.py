import numpy as np 
import time
import cv2
from pygame import mixer
import turtle

def state_machine(sumation,sound):

	# Check if blue color object present in the ROI 	
	yes = (sumation) > Hatt_thickness[0]*Hatt_thickness[1]*0.8

	# If present play the respective instrument.
	if yes and sound==1:
		drum_clap.play()
		
	elif yes and sound==2:
		drum_snare.play()
		time.sleep(0.001)
	elif yes and sound == 3:
		drum_bass.play()
		time.sleep(0.1)
	elif yes and sound == 4:
		drum_symbol.play()
		time.sleep(0.1)

def ROI_analysis(frame,sound, color_selected):
	# converting the image into HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# generating mask for 
	if color_selected == 'b':
		mask = cv2.inRange(hsv, blueLower, blueUpper)
	elif color_selected == 'g':
		mask = cv2.inRange(hsv, greenLower, greenUpper)
	else:
		mask = cv2.inRange(hsv, redLower, redUpper)
	 
	
	# Calculating the nuber of white pixels depecting the blue color pixels in the ROI
	sumation = np.sum(mask)
	# Function that decides to play the instrument or not.
	state_machine(sumation,sound)
	return mask



#shows region of intrest when true, shows drums when false
Verbsoe = False

#Import audio files here
#Potentially can test shorter and longer sounds
mixer.init()
drum_clap = mixer.Sound('batterrm.wav')
drum_snare = mixer.Sound('button-2.ogg')
drum_bass = mixer.Sound('BassKick.wav')
drum_symbol = mixer.Sound('symbol_sound.wav')

# HSV range for detecting blue color
#Change these values to test other colors and see result
blueLower = (80, 150, 50)
blueUpper = (120, 255, 255)

redLower = (170, 80, 70)
redUpper = (255, 120, 230)

greenLower = (40, 100, 100)
greenUpper = (80, 255, 255)


#frame accusation from webcam/ usb camera
camera = cv2.VideoCapture(0)
ret, frame = camera.read()


#Shows the images of the drums on the screen
# Also can change this for testing
#to read an image the syntax is cv2.imread("path of the image") to reshape the image as per 
#desired shape we use cv2.resize(image,(width,heigh),interpolation=INTERPOLATION_METHOD_FLAG_VALUE) 
#The size for augmenting the objects is decided based on the ROI.

Hatt = cv2.resize(cv2.imread('Hatt.png'), (200,100), interpolation=cv2.INTER_CUBIC)
Snare = cv2.resize(cv2.imread('Snare.png'), (200,100), interpolation=cv2.INTER_CUBIC)
Symbol = cv2.resize(cv2.imread('cymbal.png'), (200,100), interpolation=cv2.INTER_CUBIC)
Bass = cv2.resize(cv2.imread('BDrum.png'), (200,100), interpolation=cv2.INTER_CUBIC)

# Setting the corners of ROI for blue colour detection
#To detect blue colour we need to perform certain operations on each captured frame. 
# These operations need some computations to be performed by the processor. 
# Since our instruments are fixed in this application and we want to play the sound only if 
# the blue colour object hits the instrument (detected inside the ROI) it is a good idea to 
# perform all these operations only inside the ROI.

#4 drum set up bottom 2
Hatt_center_4 = [np.shape(frame)[1]*3//9,np.shape(frame)[0]*8//9]
Snare_center_4 = [np.shape(frame)[1]*6//9,np.shape(frame)[0]*8//9]
Bass_center = [np.shape(frame)[1]*2//10,np.shape(frame)[0]*3//8]
Symbol_center = [np.shape(frame)[1]*8//10,np.shape(frame)[0]*3//8]

# 3 Drum set up
Hatt_center_3 = [np.shape(frame)[1]*8//10,np.shape(frame)[0]*4//8]
Snare_center_3 = [np.shape(frame)[1]*2//10,np.shape(frame)[0]*4//8]
Bass_center_3 = [np.shape(frame)[1]*5//10,np.shape(frame)[0]*8//9]

# 2 drum set up
Hatt_center = [np.shape(frame)[1]*2//8,np.shape(frame)[0]*6//8]
Snare_center = [np.shape(frame)[1]*6//8,np.shape(frame)[0]*6//8]

# DRUMSET OF 4
Bass_thickness = [200,100]
Bass_top = [Bass_center[0]-Bass_thickness[0]//2,Bass_center[1]-Bass_thickness[1]//2]
Bass_btm = [Bass_center[0]+Bass_thickness[0]//2,Bass_center[1]+Bass_thickness[1]//2]

Symbol_thickness = [200,100]
Symbol_top = [Symbol_center[0]-Symbol_thickness[0]//2,Symbol_center[1]-Symbol_thickness[1]//2]
Symbol_btm = [Symbol_center[0]+Symbol_thickness[0]//2,Symbol_center[1]+Symbol_thickness[1]//2]

Hatt_thickness = [200,100]
Hatt_top_4 = [Hatt_center_4[0]-Hatt_thickness[0]//2,Hatt_center_4[1]-Hatt_thickness[1]//2]
Hatt_btm_4 = [Hatt_center_4[0]+Hatt_thickness[0]//2,Hatt_center_4[1]+Hatt_thickness[1]//2]

Snare_thickness = [200,100]
Snare_top_4 = [Snare_center_4[0]-Snare_thickness[0]//2,Snare_center_4[1]-Snare_thickness[1]//2]
Snare_btm_4 = [Snare_center_4[0]+Snare_thickness[0]//2,Snare_center_4[1]+Snare_thickness[1]//2]

# Drumset of 3
Hatt_top_3 = [Hatt_center_3[0]-Hatt_thickness[0]//2,Hatt_center_3[1]-Hatt_thickness[1]//2]
Hatt_btm_3 = [Hatt_center_3[0]+Hatt_thickness[0]//2,Hatt_center_3[1]+Hatt_thickness[1]//2]

Snare_top_3 = [Snare_center_3[0]-Snare_thickness[0]//2,Snare_center_3[1]-Snare_thickness[1]//2]
Snare_btm_3 = [Snare_center_3[0]+Snare_thickness[0]//2,Snare_center_3[1]+Snare_thickness[1]//2]

Bass_top_3 = [Bass_center_3[0]-Bass_thickness[0]//2,Bass_center_3[1]-Bass_thickness[1]//2]
Bass_btm_3 = [Bass_center_3[0]+Bass_thickness[0]//2,Bass_center_3[1]+Bass_thickness[1]//2]
#DRUMSET OF 2

Hatt_top = [Hatt_center[0]-Hatt_thickness[0]//2,Hatt_center[1]-Hatt_thickness[1]//2]
Hatt_btm = [Hatt_center[0]+Hatt_thickness[0]//2,Hatt_center[1]+Hatt_thickness[1]//2]

Snare_top = [Snare_center[0]-Snare_thickness[0]//2,Snare_center[1]-Snare_thickness[1]//2]
Snare_btm = [Snare_center[0]+Snare_thickness[0]//2,Snare_center[1]+Snare_thickness[1]//2]

time.sleep(1)
color = "b"
numDrums = 2
print("Press 'b' for blue drumsticks, 'r' for red, or 'g' for green. Press '2' for two drums, '3' for three drums, and '4' for four drums. When you are done press 'q' to quit.")

while True:
	
	# grab the current frame
	ret, frame = camera.read()
	frame = cv2.flip(frame,1)

	if not(ret):
		break
	# Selecting ROI corresponding to drums selecteed
	if numDrums ==2:
		snare_ROI = np.copy(frame[Snare_top[1]:Snare_btm[1],Snare_top[0]:Snare_btm[0]])
		hatt_ROI = np.copy(frame[Hatt_top[1]:Hatt_btm[1],Hatt_top[0]:Hatt_btm[0]])

	elif numDrums == 3:
		snare_ROI = np.copy(frame[Snare_top_3[1]:Snare_btm_3[1],Snare_top_3[0]:Snare_btm_3[0]])
		hatt_ROI = np.copy(frame[Hatt_top_3[1]:Hatt_btm_3[1],Hatt_top_3[0]:Hatt_btm_3[0]])
		bass_ROI = np.copy(frame[Bass_top_3[1]:Bass_btm_3[1],Bass_top_3[0]:Bass_btm_3[0]])
  
	elif numDrums == 4:
		snare_ROI = np.copy(frame[Snare_top_4[1]:Snare_btm_4[1],Snare_top_4[0]:Snare_btm_4[0]])
		hatt_ROI = np.copy(frame[Hatt_top_4[1]:Hatt_btm_4[1],Hatt_top_4[0]:Hatt_btm_4[0]])
		bass_ROI = np.copy(frame[Bass_top[1]:Bass_btm[1],Bass_top[0]:Bass_btm[0]])
		symbol_ROI = np.copy(frame[Symbol_top[1]:Symbol_btm[1],Symbol_top[0]:Symbol_btm[0]])
		# Selecting ROI corresponding to Hatt


	mask = ROI_analysis(snare_ROI,1, color)
	mask = ROI_analysis(hatt_ROI,2,color)
 
 	# Selecting ROI corresponding to bass
	if numDrums == 4:
		mask = ROI_analysis(bass_ROI,3,color)
		mask = ROI_analysis(symbol_ROI,4,color)
	elif numDrums == 3:
		mask = ROI_analysis(bass_ROI,3,color)

	# A writing text on an image.
	cv2.putText(frame,'Project: AR DrumKit',(10,30),2,1,(20,20,20),2)
	
	# Display the ROI to view the blue colour being detected
	if Verbsoe:
		# Displaying the ROI in the Image
		if numDrums == 2:
			frame[Snare_top[1]:Snare_btm[1],Snare_top[0]:Snare_btm[0]] = cv2.bitwise_and(frame[Snare_top[1]:Snare_btm[1],Snare_top[0]:Snare_btm[0]],frame[Snare_top[1]:Snare_btm[1],Snare_top[0]:Snare_btm[0]], mask=mask[Snare_top[1]:Snare_btm[1],Snare_top[0]:Snare_btm[0]])
			frame[Hatt_top[1]:Hatt_btm[1],Hatt_top[0]:Hatt_btm[0]] = cv2.bitwise_and(frame[Hatt_top[1]:Hatt_btm[1],Hatt_top[0]:Hatt_btm[0]],frame[Hatt_top[1]:Hatt_btm[1],Hatt_top[0]:Hatt_btm[0]],mask=mask[Hatt_top[1]:Hatt_btm[1],Hatt_top[0]:Hatt_btm[0]])
		#Allows for 4 drums
		elif numDrums == 4:
			frame[Snare_top_4[1]:Snare_btm_4[1],Snare_top_4[0]:Snare_btm_4[0]] = cv2.bitwise_and(frame[Snare_top_4[1]:Snare_btm_4[1],Snare_top_4[0]:Snare_btm_4[0]],frame[Snare_top_4[1]:Snare_btm_4[1],Snare_top_4[0]:Snare_btm_4[0]], mask=mask[Snare_top_4[1]:Snare_btm_4[1],Snare_top_4[0]:Snare_btm_4[0]])
			frame[Hatt_top_4[1]:Hatt_btm_4[1],Hatt_top_4[0]:Hatt_btm_4[0]] = cv2.bitwise_and(frame[Hatt_top_4[1]:Hatt_btm_4[1],Hatt_top_4[0]:Hatt_btm_4[0]],frame[Hatt_top_4[1]:Hatt_btm_4[1],Hatt_top_4[0]:Hatt_btm_4[0]],mask=mask[Hatt_top_4[1]:Hatt_btm_4[1],Hatt_top_4[0]:Hatt_btm_4[0]])
			frame[Bass_top[1]:Bass_btm[1],Bass_top[0]:Bass_btm[0]] = cv2.bitwise_and(frame[Bass_top[1]:Bass_btm[1],Bass_top[0]:Bass_btm[0]],frame[Bass_top[1]:Bass_btm[1],Bass_top[0]:Bass_btm[0]], mask=mask[Bass_top[1]:Bass_btm[1],Bass_top[0]:Bass_btm[0]])
			frame[Symbol_top[1]:Symbol_btm[1],Symbol_top[0]:Symbol_btm[0]] = cv2.bitwise_and(frame[Symbol_top[1]:Symbol_btm[1],Symbol_top[0]:Symbol_btm[0]],frame[Symbol_top[1]:Symbol_btm[1],Symbol_top[0]:Symbol_btm[0]],mask=mask[Symbol_top[1]:Symbol_btm[1],Symbol_top[0]:Symbol_btm[0]])
		elif numDrums == 3:	
			frame[Snare_top_3[1]:Snare_btm_3[1],Snare_top_3[0]:Snare_btm_3[0]] = cv2.bitwise_and(frame[Snare_top_3[1]:Snare_btm_3[1],Snare_top_3[0]:Snare_btm_3[0]],frame[Snare_top_3[1]:Snare_btm_3[1],Snare_top_3[0]:Snare_btm_3[0]], mask=mask[Snare_top_3[1]:Snare_btm_3[1],Snare_top_3[0]:Snare_btm_3[0]])
			frame[Hatt_top_3[1]:Hatt_btm_3[1],Hatt_top_3[0]:Hatt_btm_3[0]] = cv2.bitwise_and(frame[Hatt_top_3[1]:Hatt_btm_3[1],Hatt_top_3[0]:Hatt_btm_3[0]],frame[Hatt_top_3[1]:Hatt_btm_3[1],Hatt_top_3[0]:Hatt_btm_3[0]],mask=mask[Hatt_top_3[1]:Hatt_btm_3[1],Hatt_top_3[0]:Hatt_btm_3[0]])
			frame[Bass_top_3[1]:Bass_btm_3[1],Bass_top_3[0]:Bass_btm_3[0]] = cv2.bitwise_and(frame[Bass_top_3[1]:Bass_btm_3[1],Bass_top_3[0]:Bass_btm_3[0]],frame[Bass_top_3[1]:Bass_btm_3[1],Bass_top_3[0]:Bass_btm_3[0]], mask=mask[Bass_top_3[1]:Bass_btm_3[1],Bass_top_3[0]:Bass_btm_3[0]])
	# Augmenting the instruments in the output frame.
	else:
		# Augmenting the image of the instruments on the frame.
		if numDrums == 2:
			frame[Snare_top[1]:Snare_btm[1],Snare_top[0]:Snare_btm[0]] = cv2.addWeighted(Snare, 1, frame[Snare_top[1]:Snare_btm[1],Snare_top[0]:Snare_btm[0]], 1, 0)
			frame[Hatt_top[1]:Hatt_btm[1],Hatt_top[0]:Hatt_btm[0]] = cv2.addWeighted(Hatt, 1, frame[Hatt_top[1]:Hatt_btm[1],Hatt_top[0]:Hatt_btm[0]], 1, 0)
		#allows for 4 drums
		elif numDrums == 4:
			frame[Snare_top_4[1]:Snare_btm_4[1],Snare_top_4[0]:Snare_btm_4[0]] = cv2.addWeighted(Snare, 1, frame[Snare_top_4[1]:Snare_btm_4[1],Snare_top_4[0]:Snare_btm_4[0]], 1, 0)
			frame[Hatt_top_4[1]:Hatt_btm_4[1],Hatt_top_4[0]:Hatt_btm_4[0]] = cv2.addWeighted(Hatt, 1, frame[Hatt_top_4[1]:Hatt_btm_4[1],Hatt_top_4[0]:Hatt_btm_4[0]], 1, 0)
			frame[Bass_top[1]:Bass_btm[1],Bass_top[0]:Bass_btm[0]] = cv2.addWeighted(Bass, 1, frame[Bass_top[1]:Bass_btm[1],Bass_top[0]:Bass_btm[0]], 1, 0)
			frame[Symbol_top[1]:Symbol_btm[1],Symbol_top[0]:Symbol_btm[0]] = cv2.addWeighted(Symbol, 1, frame[Symbol_top[1]:Symbol_btm[1],Symbol_top[0]:Symbol_btm[0]], 1, 0)
		elif numDrums == 3:
			frame[Snare_top_3[1]:Snare_btm_3[1],Snare_top_3[0]:Snare_btm_3[0]] = cv2.addWeighted(Snare, 1, frame[Snare_top_3[1]:Snare_btm_3[1],Snare_top_3[0]:Snare_btm_3[0]], 1, 0)
			frame[Hatt_top_3[1]:Hatt_btm_3[1],Hatt_top_3[0]:Hatt_btm_3[0]] = cv2.addWeighted(Hatt, 1, frame[Hatt_top_3[1]:Hatt_btm_3[1],Hatt_top_3[0]:Hatt_btm_3[0]], 1, 0)
			frame[Bass_top_3[1]:Bass_btm_3[1],Bass_top_3[0]:Bass_btm_3[0]] = cv2.addWeighted(Bass, 1, frame[Bass_top_3[1]:Bass_btm_3[1],Bass_top_3[0]:Bass_btm_3[0]], 1, 0)
			
	cv2.imshow('Output',frame)
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
	elif key == ord("b"):
		color = "b"
	elif key == ord("g"):
		color = "g"
	elif key == ord("r"):
		color = "r"
	elif key == ord("2"):
		numDrums = 2
	elif key == ord("3"):
		numDrums = 3
	elif key == ord("4"):
		numDrums = 4
 
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()