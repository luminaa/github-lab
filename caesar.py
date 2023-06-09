import sys


def caesar_encrypt(text, shift):
    result = []
    text = text.upper().strip()

    block_size = 5
    block_count = 0
    line_size = 10

    for i in range(len(text)):
        char = text[i]

        if char == " ":
            continue

        shifted_char = chr(((ord(char) + shift - 65) % 26) + 65)
        result.append(shifted_char)
        block_count += 1

        if block_count % block_size == 0:
            result.append(" ")
        if block_count % (block_size * line_size) == 0:
            result.append("\n")

    return ''.join(result)


text = sys.argv[1]
shift = int(sys.argv[2])
print(f"Text  : \n{text}")
print(f"Shift : {shift}")
print(f"Cipher: \n{caesar_encrypt(text, shift)}")
