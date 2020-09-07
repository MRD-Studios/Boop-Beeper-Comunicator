def IDConvert(AsciiID):
    byte_array = str(AsciiID).encode()
    binary_int = int.from_bytes(byte_array, "big")
    return format(binary_int, '128b')
print(IDConvert("test1234test1234"))