# Lüftersteuerung
# Version 0.1
# Geschrieben von: Fabian Riegeer

# Bibliotheken importieren
import RPi.GPIO as GPIO
import time

# Variablen
fan = 0
timer = 10

normal = 56
warm = 58
heiss = 60

# GPIO Startwerte setzen
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT) # rot
GPIO.setup(24, GPIO.OUT) # grün
GPIO.setup(25, GPIO.OUT) # blau
GPIO.setup(17, GPIO.OUT) # Lüfter

GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)
GPIO.output(17, GPIO.LOW)

# Schleife
while 1:

    # Temperatur abfragen und ausgeben
    tempData = "/sys/class/thermal/thermal_zone0/temp"
    dateilesen = open(tempData, "r")
    temperatur = dateilesen.readline(2)
    dateilesen.close()
    print("Deine CPU hat " + temperatur + " Grad")

    # Temperaturen festlegen und zu Integer umwandeln

    temperatur = int(temperatur)

    # Zustandsabfrage
    if fan == 0:
        if temperatur <= normal:
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
        elif temperatur > normal and temperatur < heiss:
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
        elif temperatur >= heiss:
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            fan = 1
    else:
        fan += 1
        if temperatur <= normal:
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
        elif temperatur > normal and temperatur < heiss:
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
        elif temperatur >= heiss:
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            fan = 1

    if fan == timer and GPIO.input(23) == GPIO.HIGH:
        GPIO.output(17, GPIO.LOW)
        fan = 0

    print(fan)
    time.sleep(1)
GPIO.cleanup()
