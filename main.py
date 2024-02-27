def main():
    password_path = "passwords/password.txt"
    password = get_password(password_path)

def get_password(password_path):
    with open (password_path) as password:
        return password.read()

def check_length(oassword):
#8-32


main()