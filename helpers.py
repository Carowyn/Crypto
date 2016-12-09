def alphabet_position(letter):
    """Returns a 0-based numerical position of a given letter within the alphabet based on upper or lower case."""
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"                               # lower case reference
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                               # upper case reference
    position = 0
    found = False
    if letter in alphabet_lower:                                                # checks if letter is lowercase
        while position < len(alphabet_lower) and not found:
            if alphabet_lower[position] == letter:
                found = True                                                    # stops when letter is found
            else:
                position = position + 1
        if found:
            return position                                                     # returns the position of the letter in the lower case alphabet
    if letter in alphabet_upper:                                                # checks if letter is uppercase
        while position < len(alphabet_upper) and not found:
            if alphabet_upper[position] == letter:
                found = True                                                    # stops when letter is found
            else:
                position = position + 1
        if found:
            return position                                                     # returns the position of the letter in the upper case alphabet

def rotate_character(char, rot):
    """Receives a character and rotates it a given amount to the right."""
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"                               # lower case reference
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                               # upper case reference
    char_pos = alphabet_position(char)
    if char in alphabet_lower:                                                  # checks if letter is lower case
        rotated = char_pos + rot
        if rotated >= 26:
            rotated = (char_pos + rot) % 26                                     # loops around to the beginning if it reaches the end of the alphabet
            return alphabet_lower[rotated]                                      # returns the character in the rotated position (maintaining case)
        else:
            return alphabet_lower[rotated]                                      # returns the character in the rotated position (maintaining case)

    elif char in alphabet_upper:                                                # checks if letter is upper case
        rotated = char_pos + rot
        if rotated >= 26:
            rotated = (char_pos + rot) % 26                                     # loops around to the beginning if it reaches the end of the alphabet
            return alphabet_upper[rotated]                                      # returns the character in the rotated position (maintaining case)
        else:
            return alphabet_upper[rotated]                                      # returns the character in the rotated position (maintaining case)

    else:
        rotated = char
        return char                                                             # returns the original character if it is anything other than an
