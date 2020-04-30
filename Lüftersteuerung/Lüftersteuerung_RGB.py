# Lüftersteuerung
# Version 0.1
# Geschrieben von: Fabian Riegeer

# Bibliotheken importieren
import RPi.GPIO as GPIO
import time

# Variablen
# Lüfter Startwert
fan = 0
# Nachlaufzeit Lüfter
timer = 10
# Intervall Messungen
sec = 1

# Temperaturen
normal = 56
warm = 58
heiss = 60

# GPIO Startwerte setzen
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)  # LED rot
GPIO.setup(24, GPIO.OUT)  # LED grün
GPIO.setup(25, GPIO.OUT)  # LED blau
GPIO.setup(17, GPIO.OUT)  # Lüfter

# GPIO auf 0 setzen
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)
GPIO.output(17, GPIO.LOW)

# Programmstart
while 1:

    # Temperatur abfragen, umwandeln und ausgeben
    tempData = "/sys/class/thermal/thermal_zone0/temp"
    dateilesen = open(tempData, "r")
    temperatur = dateilesen.readline(2)
    dateilesen.close()
    print("Deine CPU hat " + temperatur + " Grad")
    temperatur = int(temperatur)

    # Zustandsabfrage für LED und Lüfter
    # Abfrage bei Lüfter aus
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
    # Abfrage bei Lüfter an
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

    # Lüfter nachlaufen lassen
    if fan == timer and GPIO.input(23) == GPIO.HIGH:
        GPIO.output(17, GPIO.LOW)
        fan = 0

    # Ausgabe Lüfternachlauf
    if fan != 0:
        print(fan)

    # Zeit zwischen erneuter Abfrage
    time.sleep(sec)

# GPIO Zustand zurücksetzen
GPIO.cleanup()
