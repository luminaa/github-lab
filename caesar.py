import sys


def caesar_encrpyt(text, shift):
    result = ""
    text = text.upper()

    # loop over each character in the input text
    for i in range(len(text)):
        char = text[i]

        # remove spaces and skip non-alphabetic characters
        if char == " ":
            continue
        # if not char.isalpha():
        #     result += char
        #     continue

        # shifts the characters by specified number of places
        result += chr(((ord(char) + shift-65) % 26) + 65)

    # split the result into blocks of 5 characters and join them with spaces
    blocks = [result[i:i+5] for i in range(0, len(result), 5)]
    blocks = [' '.join(blocks[i:i+10]) for i in range(0, len(blocks), 5)]
    result = '\n'.join(blocks)

    return result


if __name__ == '__main__':
    text = sys.argv[1]
    shift = int(sys.argv[2])
    print(f"Text  : {text}")
    print(f"Shift : {shift}")
    print(f"Cipher: {caesar_encrpyt(text, shift)}")