# Caesar Cipher

This code takes two arguments from the command line: a string of text to encrypt and the number of positions to shift each letter by. The program then encrypts the text using the Caesar Cipher method and prints the result to the console. The encrypted text is printed in blocks of five letters and a maximun of 10 blocks per line.

## About Caesar Cipher

This cipher is a type of substitution cipher. The idea of a Caesar cipher is this: you encode a message by shifting each letter some number of places. Thus, if the shift is 2, then A becomes C, B becomes D, and so on. Like this:

![Example of Caesar Cipher](github-lab\pictures\example.jpg)

## How To Use

1. Clone the repository:

    ```bash
    git clone https://github.com/luminaa/github-lab
    ```

2. Then go to the file directory:

    ```bash
    cd ./github-lab
    ```

3. To use `caesar.py`, run it from the command line and provide the string to encrypt and the number of positions to shift as arguments. For example:

    ```shell
    python caesar.py "Encrypt this text" 3
    ```

    The above command will encrypt the string "Encrypt this text" using a shift of 3 and print the encrypted result to the console. This would be "HQFUB SWWKL VWHAW"

4. Alternatively, you can use the bash script `caesar.sh`. First, you have to make it executable. Run the following command in your shell.

    ```bash
    chmod +x caesar.sh
    ```

    After that, you can run the script by typing the following command:

    ```bash
    ./caesar.sh
    ```