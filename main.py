def main():
    password_path = "passwords/password.txt"
    password = get_password(password_path)
    check_length(password)

def get_password(password_path):
    with open (password_path) as password:
        return password.read()

def check_length(password):
    if len(password) > 32:
        raise Exception ("Password cannot contain more than 32 characters")
    if len(password) < 8:
        raise Exception ("Password cannot contain less than 8 characters")
    else:
        pass






























main()