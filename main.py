def main():
    password_path = "passwords/password.txt"
    password = get_password(password_path)
    most_common_passwords = ['qwerty', 'password', 'qwerty123', 'aa12345678', 'abc123', 'password1', 'qwertyuiop', 'password123']
    length_strength = check_length(password)
    uppercase_count = check_capitalisation_count(password)
    digit_count = check_digit_count(password)
    special_count = check_special_count(password)
    print (" ")
    print ("-----------------Password Strength Checker-----------------")
    print (" ")
    password_strength_report(uppercase_count, digit_count, special_count, length_strength, password)
    print (" ")
    print ("-----------------------------------------------------------")

def get_password(password_path):
    with open (password_path) as password:
        return password.read()

def check_length(password):
    length_strength = 0
    if len(password) > 32:
        raise Exception ("Password cannot contain more than 32 characters")
    if len(password) < 8:
        raise Exception ("Password cannot contain less than 8 characters")
    if len(password) <= 16:
        length_strength += 1
    return (length_strength)
        
        
def check_capitalisation_count(password):
    uppercase_count = 0
    for char in password:
        if char.isupper():
            uppercase_count += 1
    return (uppercase_count)
        
def check_digit_count(password):
    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1
    return (digit_count)

def check_special_count(password):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    special_count = 0
    for char in password:
        if char in special_characters:
            special_count += 1
    return (special_count)
        
    
def password_strength_report(uppercase_count, digit_count, special_count, length_strength, password): #very weak #weak #normal #strong #very strong
    password_strength = uppercase_count + digit_count + special_count + length_strength
    if password_strength == 0:
        print (f" Your password: '{password}' is very Weak.")
    if password_strength == 1:
        print (f" Your password: '{password}' is Weak.")
    if password_strength == 2:
        print (f" Your password: '{password}' is normal.\n")
    if password_strength == 3:
        print (f" Your password: '{password}' is strong, great job but you \n"
               f" can still do better.")
    if password_strength == 4:
        print (f" Your password: '{password}' is very strong, great job!")
























main()