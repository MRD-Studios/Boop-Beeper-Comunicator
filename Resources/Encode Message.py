import numpy as np, json, time, struct, datetime
#A message contains 2048 bits of data
#16 bit data Start code
#1 error check
#7 bit data mode
#64 bit UTC
#Hashed (reciever ID as key):
# - 128 bit sender ID
# - 128 bit receiver ID
# - 1688 message data
#16 bit data end
dataStart = format(61680, '16b')
dataEnd = format(65280, '16b')

def dataMode(mode):
    dataOut=format(65, '7b') #Everyone In range Message
    if mode == 0:
        dataOut=format(66, '7b') #Ping, non hashed
    elif mode == 1:
        dataOut=format(67, '7b') #Ping, hashed
    elif mode == 2:
        dataOut=format(68, '7b') #Message, non hashed
    elif mode == 3:
        dataOut=format(69, '7b') #Message, hashed
    elif mode == 4:
        dataOut=format(70, '7b') #Message Received, non hashed
    elif mode == 5:
        dataOut=format(71, '7b') #Message Received, 
    return dataOut

def UTCBin():
    now = datetime.datetime.now()
    stamp = time.mktime(now.timetuple())
    binarydatetime = struct.pack('<L', int(stamp))
    recoverbinstamp = struct.unpack('<L', binarydatetime)[0]
    return format(recoverbinstamp, '64b')

def getID():
    settings = open("Resources/Settings.json", 'r')
    settingsJSON = json.load(settings)
    ID = settingsJSON['IDbin']
    settings.close()
    return ID

def getAllContacts():
    contacts = open("Resources/Contacts.json", 'r')
    contactsJSON = json.load(contacts)
    contacts.close()
    return contactsJSON

def getContact(Name, IDType, get):
    contacts = open("Resources/Contacts.json", 'r')
    contactsJSON = json.load(contacts)
    x=0
    for i in contactsJSON["Contacts"]:
        if contactsJSON["Contacts"][x]["Name"] == Name:
            contactName = contactsJSON["Contacts"][x]["Name"]
            break
        x=x+1
    if IDType == "ascii": contactID = contactsJSON["Contacts"][x]["IDascii"]
    elif IDType == "hex": contactID = contactsJSON["Contacts"][x]["IDhex"]
    elif IDType == "bin": contactID = contactsJSON["Contacts"][x]["IDbin"]
    else: contactID = contactsJSON["Contacts"][x]["IDascii"]
    contacts.close()
    if get == "Name": return contactName
    elif get == "ID": return contactID
    else: return contactID