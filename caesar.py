import sys


def caesar_encrpyt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr(((ord(char) + shift-65) % 26) + 65)
        else:
            result += chr(((ord(char) + shift-97) % 26) + 97)

    return result


if __name__ == '__main__':
    text = sys.argv[1]
    shift = int(sys.argv[2])
    print("Text  : " + text)
    print("Shift : " + str(shift))
    print("Cipher: " + caesar_encrpyt(text, shift))