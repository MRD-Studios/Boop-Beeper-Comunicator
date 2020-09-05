import numpy as np, json, time, struct, datetime, Message
#A message contains 2048 bits of data
#16 bit data Start code
#1 error check
#7 bit data mode
#64 bit UTC
#Hashed (reciever ID as key):
# - 128 bit receiver ID
# - 128 bit sender ID
# - 664 message data
#16 bit data end
dataStart = format(61680, '16b') #sets dataStart Code
dataEnd = format(65280, '16b') #sets dataEnd Code

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
    now = datetime.datetime.now() #Gets The Time
    stamp = time.mktime(now.timetuple())
    binarydatetime = struct.pack('<L', int(stamp))
    recoverbinstamp = struct.unpack('<L', binarydatetime)[0]
    return format(recoverbinstamp, '64b') #Outputs time as binary

def getID():
    settings = open("Resources/Settings.json", 'r')#Opens JSON file
    settingsJSON = json.load(settings) #Imports JSON data
    ID = settingsJSON["ID"][0]["IDbin"] #Looks for ID
    settings.close()#Closes JSON
    return ID 

def getAllContacts():
    contacts = open("Resources/Contacts.json", 'r') #Opens JSON
    contactsJSON = json.load(contacts) #Imports JSON
    contacts.close() #Closes JSON
    return contactsJSON["Contacts"] #Returns all Contacts

def getContact(Name, IDType):
    contacts = open("Resources/Contacts.json", 'r') #opens JSON
    contactsJSON = json.load(contacts) #Imports JSON
    x=0
    for i in contactsJSON["Contacts"]:
        if contactsJSON["Contacts"][x]["Name"] == Name: #Looks For Name entered in json file
            x=x
            break
        else:
            x=x+1
    if IDType == "ascii": contactID = contactsJSON["Contacts"][x]["IDascii"] #Returns Ascii ID
    elif IDType == "hex": contactID = contactsJSON["Contacts"][x]["IDhex"] #Returns Hex ID
    elif IDType == "bin": contactID = contactsJSON["Contacts"][x]["IDbin"] #Returns Binary ID
    else: contactID = contactsJSON["Contacts"][x]["IDascii"] #Returns Ascii ID
    contacts.close() #Closes JSON File
    return contactID #Returns Contact ID.
