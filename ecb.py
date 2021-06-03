def stringToBinary(string):
    #input string
    #output binary    
    binary = ''.join(format(ord(i), '08b') for i in string) # 8bit plain text
    return binary

def binaryToDecimal(binary):
    #input binary representation
    #output string of decimal
    str_decimal = int(binary, 2)
    return str_decimal

def binaryToString(binary):
    #input binary representation
    #output string
    str_data = ""
    for i in range(0, len(binary), 8):
        temp = binary[i:i + 8]
        decimal = binaryToDecimal(temp)
        str_data = str_data + chr(decimal)
    
    return str_data

def enc(string, key):
    #input plaintext, binary key
    #output ciphertext
    binary_string = stringToBinary(string)
    xor_operation = bin(int(binary_string, 2) ^ int(key, 2)).replace("0b", "")
    shifted = bin(int(xor_operation, 2) << 1).replace("0b", "")
    ciphertext = binaryToString(shifted)
    return ciphertext

def dec(encrypted, key):
    #input ciphertext, binary key
    #output string plaintext
    encrypted_binary = stringToBinary(encrypted)
    shifted = bin(int(encrypted_binary, 2) >> 1).replace("b", "")
    xor_operation = bin(int(shifted, 2) ^ int(key, 2)).replace("b", "")
    plain_text = binaryToString(xor_operation)
    return plain_text
