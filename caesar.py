import sys


def caesar_encrpyt(text, shift):
    result = ""
    text = text.upper()

    for i in range(len(text)):
        char = text[i]
        if char == " ":
            continue
        if not char.isalpha():
            result += char
            continue
        result += chr(((ord(char) + shift-65) % 26) + 65)

    blocks = [result[i:i+5] for i in range(0, len(result), 5)]
    result = ' '.join(blocks)

    return result


if __name__ == '__main__':
    text = sys.argv[1]
    shift = int(sys.argv[2])
    print(f"Text  : {text}")
    print(f"Shift : {shift}")
    print(f"Cipher: {caesar_encrpyt(text, shift)}")