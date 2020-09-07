def MDecode(message):
    binary_int = int(message, 2)
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    return binary_array.decode()

def MEncode(message):
    byte_array = str((message).ljust(83, '_')).encode()
    binary_int = int.from_bytes(byte_array, "big")
    return str(format(binary_int, '664b')).replace(" ", "0")
