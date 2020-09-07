import encryption as key, Metadata as md, ErrorCheck as ecc, Message as msg
#A message contains 1024 bits of data
#16 bit data Start code
#1 error check
#7 bit data mode
#64 bit UTC
#Hashed (reciever ID as key):
# - 128 bit receiver ID
# - 128 bit sender ID
# - 664 message data
#16 bit data end
def DataCondense(Receiver, message, dataMode):
    dataStart = format(61680, '16b') #sets dataStart Code
    dataEnd = format(65280, '16b') #sets dataEnd Code
    data = md.dataMode(dataMode) + md.UTCBin() + key.Encrypt(Receiver, md.getID(), message)
    data = data.split()
    x = 0
    for i in data:
        data[x] = int(data[x])
        x=x+1
        i=i
    dataWParity = ecc.encode(data)
    data = str(dataWParity)
    dataOut = dataStart + data + dataEnd
    return dataOut

DataCondense("Self", msg.MEncode("Hi"), 3)
