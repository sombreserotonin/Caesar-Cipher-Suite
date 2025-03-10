#!/usr/bin/env python3
"""
Caesar Cipher Suite - A simple and flexible command line-based Python implementation of the Caesar cipher.
This program provides encryption and decryption capabilities for text using the Caesar cipher technique.
"""

import sys
from typing import List, Optional, Union

# Constants
ALPHABET_MATRIX = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
WELCOME_MESSAGE = "Hello & Welcome to my Caesar Cipher Suite Personal Project!"
MENU_PROMPT = "-[Suite Menu]-\n Please Enter [1] for Encryption: \n Please Enter [2] for Decryption:\n To Exit, Please Type either of the following: [stop, quit, exit, q] \n Your Choice: "
ENCRYPTION_PROMPT = "-[Encryption Menu]-\n Please Enter A Sentence or Word You Would Like To Encrypt: "
DECRYPTION_PROMPT = "-[Decryption Menu]-\n Please Enter The Ciphertext You Would Like To Decrypt: "
SHIFT_KEY_PROMPT = " Please Enter A Number For Creating Your Unique Ciphertext: "
ERROR_NOT_NUMBER = " [Error]: Input is not a Number\n"
ERROR_NEGATIVE = " [Error]: Input can not be Negative\n"
ERROR_INVALID_OPTION = "Please Enter A Valid Option!\n"
EXIT_MESSAGE = "Exiting Caesar Cipher Suite"


def caesar_encrypt(user_input: str, shift_key: int) -> str:
    """
    Encrypt the input text using the Caesar cipher algorithm.
    
    Args:
        user_input: The text to encrypt
        shift_key: The number of positions to shift each letter
        
    Returns:
        The encrypted text
    """
    encrypted_matrix = []  # Final Array of calculated alphabet shifts
    
    for character in user_input:  # Split string user_input into chars
        if character in ALPHABET_MATRIX:  # If the character from user_input matches the alphabet_matrix
            alphabet_index = ALPHABET_MATRIX.index(character)
            # Simplified algorithm using modulo
            new_index = (alphabet_index + shift_key) % 26
            alphabet_cipher = ALPHABET_MATRIX[new_index]
            encrypted_matrix.append(alphabet_cipher)
        else:  # Otherwise preserve the character as is
            encrypted_matrix.append(character)

    cipher_output = "".join(encrypted_matrix)  # Join list of characters to form a string
    print(f" Your New Ciphertext: {cipher_output} \n Your ShiftKey: {shift_key} \nRemember to not lose your shift key for decryption!\n")
    return cipher_output


def caesar_decrypt(user_input: str, shift_key: int) -> str:
    """
    Decrypt the input text using the Caesar cipher algorithm.
    
    Args:
        user_input: The encrypted text to decrypt
        shift_key: The number of positions each letter was shifted during encryption
        
    Returns:
        The decrypted text
    """
    decrypted_matrix = []
    
    for character in user_input:
        if character in ALPHABET_MATRIX:
            alphabet_index = ALPHABET_MATRIX.index(character)
            # Simplified algorithm using modulo
            new_index = (alphabet_index - shift_key) % 26
            alphabet_cipher = ALPHABET_MATRIX[new_index]
            decrypted_matrix.append(alphabet_cipher)
        else:
            decrypted_matrix.append(character)

    decrypted_cipher_output = "".join(decrypted_matrix)
    print(f" Your Decrypted Ciphertext: {decrypted_cipher_output}\n Based on given Ciphertext: ({user_input}) & Shift Key: ({shift_key})\n")
    return decrypted_cipher_output


def get_shift_key() -> int:
    """
    Get a valid shift key from the user.
    
    Returns:
        A positive integer to use as the shift key
    """
    while True:
        try:
            shift_key = int(input(SHIFT_KEY_PROMPT))
            if shift_key < 0:
                raise ValueError(ERROR_NEGATIVE)
            return shift_key
        except ValueError as error:
            err = str(error)
            if ERROR_NEGATIVE in err:
                print(error)
            else:
                print(ERROR_NOT_NUMBER)


def main() -> None:
    """
    Main function to run the Caesar Cipher Suite.
    Handles the menu system and user interaction.
    """
    show_welcome = True
    
    while True:
        # Show welcome message only on first run
        if show_welcome:
            print(WELCOME_MESSAGE)
            show_welcome = False
            
        user_option_input = input(MENU_PROMPT)
        
        if user_option_input == "1":  # Encrypt Option
            user_string_input = input(ENCRYPTION_PROMPT).upper()
            shift_key = get_shift_key()
            caesar_encrypt(user_string_input, shift_key)
            
        elif user_option_input == "2":  # Decrypt Option
            user_string_input = input(DECRYPTION_PROMPT).upper()
            shift_key = get_shift_key()
            caesar_decrypt(user_string_input, shift_key)
            
        elif user_option_input.lower() in ["quit", "stop", "exit", "q"]:
            print(EXIT_MESSAGE)
            sys.exit()
            
        else:
            print(ERROR_INVALID_OPTION)


if __name__ == "__main__":
    main()
