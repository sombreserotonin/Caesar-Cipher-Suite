def caeser_encrypt(user_input: str, shift_key: int, counter: int) -> str:
    alphabet_matrix = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] # Map to compare to user input
    encrypted_matrix = [] # Final Array of calculated alphabet shifts
    for characters in user_input: # Split string user_input into chars
        #print(characters, type(user_input), shift_key, type(shift_key))
        if characters in alphabet_matrix: # If the characters from user_input match the alphabet_matrix THEN do following
            alphabet_index = alphabet_matrix.index(characters)
            #print("Should output each one", alphabet_index)
            alphabet_index = alphabet_index + shift_key - (26 * ((alphabet_index + shift_key) // 26)) 
            # Add shift_key (99) to alphabet_index to get the new shift value (e.g 2 = [C] + 99 = 101)
            # Divide (alphabet_index + shift_key) by 26 to find how many full cycles fit within 26 (e.g 101 // 26 = 3) - // rounding DOWN to closest whole number, we can't handle float
            # Now multiplication occurs where 26 * 3 = 78
            # Subtract the total value of alphabet_index + shift_key = 101 with 78 (101 - 78 = 23)
            # [23] is the true shift value alphabet_index and does not exceed [25] (would cause out of bounds error otherwise)
            #print("Should be Updated Number ", alphabet_index)
            alphabet_cipher = alphabet_matrix[alphabet_index] # True shift value used to access the corresponding index of a character inside alphabet_matrix and passed into alphabet_cipher
            encrypted_matrix.append(alphabet_cipher) # Add each new indexed character to encrypted matrix array 
        else: # Otherwise everything else, wherever in the loop position as was entered by the user, is appended before joining
            encrypted_matrix.append(characters)

    cipher_output = "".join(encrypted_matrix) # Join list of characters inside encrypted_matrix to form a string
    print(f" Your New Ciphertext: {cipher_output} \n Your ShiftKey: {shift_key} \nRemember to not lose your shift key for decryption!\n")
    counter += 1 # Add 1 to counter
    user_option_menu(counter) # Restart Menu and pass updated counter back

def caesar_decrypt(user_input: str, shift_key: int, counter: int) -> str:
    alphabet_matrix = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] # Same as above
    decrypted_matrix = []
    for characters in user_input:
        if characters in alphabet_matrix: 
            alphabet_index = alphabet_matrix.index(characters)
            alphabet_index = alphabet_index - shift_key  # Reversed operation, Shifting backwards rather than forwards since we are decrypting
            while alphabet_index < 0:  # Keep adjusting until within in range of [0] - [25]
                alphabet_index += 26 # Keep adding 26 until within range
            alphabet_cipher = alphabet_matrix[alphabet_index] # Same as above, True shift value is mapped to corresponding index of a character inside alphabet_matrix
            decrypted_matrix.append(alphabet_cipher)
        else:
            decrypted_matrix.append(characters)

    decrypted_cipher_output = "".join(decrypted_matrix) # Join list of characters inside encrypted_matrix to form a string
    print(f" Your Decrypted Ciphertext: {decrypted_cipher_output}\n Based on given Ciphertext: ({user_input}) & Shift Key: ({shift_key})\n")
    counter += 1
    user_option_menu(counter)

def user_option_menu(counter: int) -> None:
    if counter == 0: # When 0, which it is at the start, after user progression with program, this Initial Welcome Message will no longer appear since counter will be > 0
        print("Hello & Welcome to my Caesar Cipher Suite Personal Project!")
    user_option_input = input("-[Suite Menu]-\n Please Enter [1] for Encryption: \n Please Enter [2] for Decryption:\n To Exit, Please Type either of the following: [stop, quit, exit, q] \n Your Choice: ")
    if user_option_input in ["1"]: # Encrypt Option, check user_option_input for exactly the string '1' + auto sanitisation
        user_string_input = input("-[Encryption Menu]-\n Please Enter A Sentence or Word You Would Like To Encrypt: ").upper()
        while True: # Begin Loop until broken
            try: # handle NaN inputs if necessary
                shiftkey_input = int(input(" Please Enter A Number For Creating Your Unique Ciphertext: ")) # Convert input to integer
                if shiftkey_input < 0:
                    raise ValueError(" [Error]: Input can not be Negative\n")
                break # Exit loop if input is a number
            except ValueError as Errors: # If NaN | If negative
                err = str(Errors) # Convert ValueError to string 
                if "[Error]: Input can not be Negative" in err: # Check for my own message in string err to satisfy condition
                    print(Errors) # Print the original Negative number error message as passed onto ValueError
                else:
                    print(" [Error]: Input is not a Number\n") # NaN error message
        #print(" Your Sentence/Word:", string_input, "\n Your Shift Key:", shiftkey_input)
        caeser_encrypt(user_string_input, shiftkey_input, counter) # Pass parameters into caesar_encrypt()
    elif user_option_input in ["2"]: # Decrypt Option, Same as above
        user_string_input = input("-[Decryption Menu]-\n Please Enter The Ciphertext You Would Like To Decrypt: " ).upper()
        while True:
            try:
                shiftkey_input = int(input(" Please Enter A Number For Creating Your Unique Ciphertext: ")) # Convert input to integer
                if shiftkey_input < 0:
                    raise ValueError(" [Error]: Input can not be Negative\n")
                break
            except ValueError as Errors:
                err = str(Errors)
                if "[Error]: Input can not be Negative" in err:
                    print(Errors)
                else:
                    print(" [Error]: Input is not a Number\n")
        caesar_decrypt(user_string_input, shiftkey_input, counter) # Pass parameters into caesar_decrypt()
    elif user_option_input.lower() in ["quit","stop","exit","q"]: # if any text entered with matching strings, after .lower conversion, then do following
        print("Exiting Caesar Cipher Suite")
        StopIteration # Stop Program
    else: # If none of the above
        print("Please Enter A Valid Option!\n")
        user_option_menu(counter) # Easy Loop call function

user_option_menu(counter = 0) # Open the menu for the user with counter set to 0