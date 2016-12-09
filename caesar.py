from sys import argv, exit
from helpers import alphabet_position, rotate_character                         # import functions needed

def encrypt(text, rot):
    """Receives text and a rotation number, and returns an encrypted message."""
    encrypt_text = ""
    for char in text:
        letter = rotate_character(char, rot)                                    # calls the rotate_character function using (text) char and given rotation
        encrypt_text = encrypt_text + letter                                    # builds the encrypted text
    return encrypt_text

def user_input_is_valid(cl_args):
    #return len(argv) == 2 and argv[-1].isdigit()                               # Use this line to work in Powershell
    return len(cl_args) == 2 and cl_args[1].isdigit()                          # Use this line to successfully submit to Vocareum

def main():
    if user_input_is_valid(argv) == True:
        pass
    else:
        print("Please only rotate by a whole number, typed after the program name. (ex: caesar.py 5)")
        exit()

    text = input("What message would you like to encrypt?  ")                   # USER INPUT for the message to encrypt
    rot = int(argv[1])                                                          # USER INPUT for the rotation amount via command line

    #print(user_input_is_valid(argv[-1]))
    print(encrypt(text, rot))                                                   # PRINT STATEMENT

if __name__ == '__main__':
    main()
