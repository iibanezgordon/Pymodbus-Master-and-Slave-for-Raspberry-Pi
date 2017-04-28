from RPLCD import CharLCD
from RPi import GPIO
import time



#lcd = CharLCD()

#lcd.write_string('Hello world')


x = 1
while True :
    f = open('values.txt', 'r')
    for line in f:
        print line
    time.sleep(2)


