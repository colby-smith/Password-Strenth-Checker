def main():
    password_path = "passwords/password.txt"
    password = get_password(password_path)
    
    check_length(password)
    check_capitalisation(password)
    check_digits(password)
    check_special_count(password)

def get_password(password_path):
    with open (password_path) as password:
        return password.read()

def check_length(password):
    if len(password) > 32:
        raise Exception ("Password cannot contain more than 32 characters")
    if len(password) < 8:
        raise Exception ("Password cannot contain less than 8 characters")
        
    
def check_capitalisation(password):
    uppercase_count = 0
    for char in password:
        if char.isupper():
            uppercase_count += 1
    if uppercase_count >= 1:
        print (f"your password contains {uppercase_count} capitalised characters")

def check_digits(password):
    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1
    if digit_count >= 1:
        print (f"your password contains {digit_count} numerial characters")

def check_special_count(password):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    special_count = 0
    for char in password:
        if char in special_characters:
            special_count += 1
    if special_count >= 1:
        print(f"Your password contains {special_count} valid special characters")

            
    

























main()