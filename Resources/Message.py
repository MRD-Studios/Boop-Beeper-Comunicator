def MessageDecode(message):
    binary_int = int(message, 2)
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    return binary_array.decode()

def MessageEncode(message):
    byte_array = str(message).encode()
    binary_int = int.from_bytes(byte_array, "big")
    return format(binary_int, 'b')
