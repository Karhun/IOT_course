
import RPi.GPIO as GPIO
import time
import signal
import sys

# Työ liikennevalot
# Raspberry pi, valopinnit 3 kpl, painike.
# Jos painiketta painetaan, vaihtuu valot keltaiseksi ja sitten punaiseksi.
# Tämän jälkeen jalankulkijoiden valo vaihtuu vihreäksi.
# Jalankulkijoiden valo vaihtuu 2sek jälkeen keltaiseksi, sitten punaiseksi.
# Samalla autoilijoiden valo vaihtuu vihreäksi.

#autoilijat
LED_PA=4
LED_VA=21
LED_KA=16
#jalankulkijat
LED_PJ=13
LED_KJ=19
LED_VJ=26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_VA, GPIO.OUT)
GPIO.setup(LED_KA, GPIO.OUT)
GPIO.setup(LED_PA, GPIO.OUT)
GPIO.setup(LED_PJ, GPIO.OUT)
GPIO.setup(LED_KJ, GPIO.OUT)
GPIO.setup(LED_VJ, GPIO.OUT)
GPIO.setup(5, GPIO.IN)#painike

# Sammutetaan kaikki valot, kun ohjelma pysaytetaan.
def allLightsOff(signal, frame):
    GPIO.output(LED_PA, False)
    GPIO.output(LED_VA, False)
    GPIO.output(LED_KA, False)
    GPIO.output(LED_VJ, False)
    GPIO.output(LED_PJ, False)
    GPIO.output(LED_KJ, False)
    GPIO.cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT, allLightsOff)


#Alkuasetelma,jalankulkijoille pun, autoilijoille vihr.
GPIO.output(LED_VA,True)
GPIO.output(LED_PJ,True)
GPIO.output(LED_PA,False)
GPIO.output(LED_KA,False)
GPIO.output(LED_VJ,False)
GPIO.output(LED_KJ,False)


#Funktio liikennevalojen vaihtuminen, kun painiketta painetaan.
def liikennevalot():
        if GPIO.input(5):
                GPIO.output(LED_VA,False)
                GPIO.output(LED_KA,True)
                GPIO.output(LED_KJ,True)
                GPIO.output(LED_PA,True)
                time.sleep(2)
                GPIO.output(LED_VA,False)
                GPIO.output(LED_PA,True)
                GPIO.output(LED_KJ,False)
                GPIO.output(LED_PJ,False)
                GPIO.output(LED_KA,False)
                GPIO.output(LED_VJ,True)
                time.sleep(3)
                GPIO.output(LED_PA,True)
                GPIO.output(LED_KA,True)
                GPIO.output(LED_PJ,True)
                GPIO.output(LED_KJ,True)
                GPIO.output(LED_VJ,False)
                time.sleep(1)
                GPIO.output(LED_VA,True)
                GPIO.output(LED_PJ,True)
                GPIO.output(LED_VJ,False)
                GPIO.output(LED_KJ,False)
                GPIO.output(LED_PA,False)
                GPIO.output(LED_KA,False)
        time.sleep(0.1)

loppu = time.time() , 25
while time.time() < loppu:
        liikennevalot()

GPIO.cleanup()


