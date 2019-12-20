# Tehtava 4.7, naaman tunnistus kuvasta.
import cv2
import sys
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

#polku xml tiedostoon
cascPath = "haarcascade_frontalface_default.xml"

# Luodaan haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread('face.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kasvojen tunnistus kuvasta
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

print("Tunnistettiin {0} kasvot!".format(len(faces)))

# Piirretaan naaman kohdalle nelio.
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

#Tallennetaan kuva
plt.imsave('naama.jpg', image)
