import RPi.GPIO as GPIO
import time
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)

# Luetaan pinnissa 18 kiinni olevaa PIR sensoria.
pirPin = 18
GPIO.setup(pirPin, GPIO.IN)
camera = PiCamera()
counter = 1

loppu = time.time() + 1000
while time.time() < loppu:
    i=GPIO.input(pirPin)
    if i==0:
        print "Ei havaita liiketta"
        time.sleep(0.1)
    elif i==1:
        try: 
            camera.start_preview()
            time.sleep(1)
            camera.capture('/home/anka/image%s.jpg' % counter)
            counter = counter + 1
            camera.stop_preview()
        except:
            camera.stop_preview()
        print "Liiketta havaittu"
        time.sleep(0.1)

GPIO.cleanup()
