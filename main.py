from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""
import sys
from password_manager import change_password, add_login, encrypt_passwords_in_file

def main():
    filename = input("Enter the CSV file name:\n")
    encrypt_passwords_in_file(filename)

    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        option = input().strip()

        if option == "1":
            print("Enter the website and the new password:")
            data = input().split()
            if len(data) < 2:
                print("Input is in the wrong format!")
                continue
            website, new_password = data[0], data[1]
            if len(new_password) < 12:
                print("Password is too short!")
                continue
            ok = change_password(filename, website, new_password)
            if ok:
                print("Password changed.")
            else:
                print("Website not found! Operation failed.")

        elif option == "2":
            print("Enter the website, username, and password:")
            data = input().split()
            if len(data) < 3:
                print("Input is in the wrong format!")
                continue
            website, username, password = data[0], data[1], data[2]
            if len(password) < 12:
                print("Password is too short!")
                continue
            add_login(filename, website, username, password)
            print("Login added.")

        elif option == "3":
            sys.exit(0)

        else:
            print("Invalid option selected!")

if __name__ == "__main__":
    main()