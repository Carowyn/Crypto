def get_initials(fullname):
    """Given a person's name, return the person's (uppercase) initials."""
    capname = fullname.title()
    initials = ""
    for char in capname:
        if ord(char) >=65 and ord(char) <= 90:
            initials = initials + char
    return initials

def main():
    fullname = input("What is your full name?")

    print(get_initials(fullname))

if __name__ == '__main__':
    main()
