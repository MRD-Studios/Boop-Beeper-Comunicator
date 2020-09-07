import Metadata, Message
def Encrypt(Receiver, Sender, Message):
    key = (str(Metadata.getContact(Receiver, "bin"))*15)+"100010101111110011001001"
    key = format(int(key, 2), '920b')
    Data = (str(Metadata.getContact(Receiver, "bin")) + str(Sender) + str(Message)).replace(" ", "0")
    Data = format(int(Data, 2), '920b')
    Encrypted = int(key, 2)^int(Data,2)
    Encrypted = format(Encrypted, '920b')
    return Encrypted

def Decrypt(Receiver, DataIn):
    key = (str(Metadata.getContact(Receiver, "bin"))*15)+"100010101111110011001001"
    key = format(int(key, 2), '920b')
    Encrypted = format(int(DataIn, 2), '920b')
    Decrypted = str(format((int(key, 2)^int(Encrypted,2)), '920b')).replace(" ", "0")
    Message = str(Decrypted[256:]).replace(" ", "0")
    Sender = str(Decrypted[128:-664]).replace(" ", "0")
    Receiver = str(Decrypted[:-792]).replace(" ", "0")
    return Sender, Message, Receiver
