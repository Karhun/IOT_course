# Tehtava 4.8 picameralla kasvojentunnistus
import numpy as np
import time
import picamera
import cv2

# Tehtävä 4: Asenna liiketunnistin ja kamera raspberry pihin.
# Ota kuva, kun liikettä havaittu ja tallenna eri tiedostoon kuin oletustiedosto.

camera = picamera.PiCamera()

print "Kamera paalla."
time.sleep(5)
kuva = camera.capture('naamakuva.jpg')

print "Kuva tulostuu 15 sekunissa"
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

img = cv2.imread('naamakuva.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	
plt.imsave('naamaraja.jpg', img)   
cv2.imshow('img',img)
cv2.waitKey(15000)
cv2.destroyAllWindows()
