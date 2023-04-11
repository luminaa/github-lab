import sys


def caesar_encrpyt(text, shift):
    result = ""
    text = text.upper()
    
    for i in range(len(text)):
        char = text[i]
        result += chr(((ord(char) + shift-65) % 26) + 65)

    return result


if __name__ == '__main__':
    text = sys.argv[1]
    shift = int(sys.argv[2])
    print("Text  : " + text)
    print("Shift : " + str(shift))
    print("Cipher: " + caesar_encrpyt(text, shift))