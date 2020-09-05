import numpy as np, json
#A message contains 2048 bits of data
#16 bit data Start code
#1 error check
#7 bit data mode
#8 bit data option
#64 bit UTC
#Hashed (reciever ID as key):
# - 128 bit sender ID
# - 128 bit receiver ID
# - 1680 message data
#16 bit data end
dataStart = format(61680, '16b')
print (str(dataStart))
dataEnd = format(65280, '16b')
print (str(dataEnd))