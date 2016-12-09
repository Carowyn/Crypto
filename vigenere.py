from helpers import alphabet_position, rotate_character                         # import functions needed

def encrypt(text, key):
    """Recieves text and a key word and encrypts the text using the key word as a cycling rotation amount."""
    new_text = ""                                                               # initialize variables
    sub_key = []
    non_alpha = 0
    for i in key:                                                               # build a list of the rotation amounts based on the key word
        let = alphabet_position(i)
        sub_key.append(let)

    for index in range(len(text)):                                              # set how long the loop will run based on the lenght of text
        if text[index].isalpha():                                               # if text is alpha then rotate based on the next sub key rotation
            x = (index - non_alpha) % len(sub_key)
            new_char = rotate_character(text[index], sub_key[x])
            new_text = new_text + new_char
        else:                                                                   # if text is anything other than alpha, insert the character without
            non_alpha = non_alpha + 1                                           # rotating, and add a number to let the 'if' part of the loop
            new_text = new_text + text[index]                                   # know to skip the character in rotation
    return new_text

def main():
    text = input("What message would you like to encrypt?  ")                   # USER INPUT for the message to encrypt
    key = input("What keyword would you like the encryption set to?  ")         # USER INPUT for the rotation amount
    print(encrypt(text, key))                                                   # *PRINT STATEMENT*

if __name__ == '__main__':
    main()
