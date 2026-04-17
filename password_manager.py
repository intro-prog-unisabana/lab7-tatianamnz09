import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    
    with open(filename, "r") as f:
        password = f.readline().strip()
        
        encrypted_password = caesar_encrypt(password)

        with open(filename, "w") as f:
            f.write(encrypted_password)

if __name__ == "__main__":

    encrypt_single_pass("examples/example1.txt")


def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""

    with open (filename, "r") as file:
        lector = csv.reader(file)

        data = []
        for row in lector:
            data.append(row)

        for index, row in enumerate(data):
            if index != 0:
                row[2] = caesar_encrypt(row[2])

        with open(filename, "w") as file:
            writer = csv.writer(file)
            writer.writerows(data)



def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
