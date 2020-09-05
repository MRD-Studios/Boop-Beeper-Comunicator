import pyfirmata
import time

#board = pyfirmata.Arduino('/dev/ttyACM0')

while True:
    #board.digital[13].write(1)
    print("On")
    time.sleep(1)
    #board.digital[13].write(0)
    print("Off")
    time.sleep(1)