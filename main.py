MAX_PASSWORD_LENGTH = 32
MIN_PASSWORD_LENGTH = 8
REQUIRED_PASSWORD_LENGTH = 16
SPECIAL_CHARACTERS = "!@#$%^&*()-+?_=,<>/"

def main():
    password_path = "passwords/password.txt"
    password = get_password(password_path)
    print ("-----------------Password Strength Checker-----------------")
    password_strength_report(password)
    print ("-----------------------------------------------------------")

def get_password(password_path):
    with open (password_path) as password:
        return password.read()

def check_length(password):
    length_strength = 0
    if len(password) > MAX_PASSWORD_LENGTH:
        raise Exception ("Password cannot contain more than 32 characters")
    if len(password) < MIN_PASSWORD_LENGTH:
        raise Exception ("Password cannot contain less than 8 characters")
    if len(password) >= REQUIRED_PASSWORD_LENGTH:
        length_strength += 1
    return (length_strength)
        
def check_password_strength(password):
    uppercase_count = sum(1 for char in password if char.isupper())
    digit_count = sum(1 for char in password if char.isdigit())
    special_count = sum(1 for char in password if char in SPECIAL_CHARACTERS)
    length_strength = 1 if check_length(password) else 0
    return uppercase_count, digit_count, special_count, length_strength
    
def password_strength_report(password):
    uppercase_count, digit_count, special_count, length_strength = check_password_strength(password)
    password_strength = uppercase_count + digit_count + special_count + length_strength
    missing_strengths = []
    if length_strength == 0:
        missing_strengths.append("length (should be at least 16 characters)")
    if uppercase_count == 0:
        missing_strengths.append("contain an uppercase character")
    if digit_count == 0:
        missing_strengths.append("a digit")
    if special_count == 0:
        missing_strengths.append("a special character")
    
    if missing_strengths:
        print(f"Your password '{password}' is missing the following elements to be very strong: {', '.join(missing_strengths)}.")
    else:
        print(f"Congratulations! Your password '{password}' is very strong.")

main()