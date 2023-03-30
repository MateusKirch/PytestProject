def get_username_input():
    username = input("Digite um nome de usuário: ")
    return username

def validate_username_uppercase(username):
    if username[0].isupper():
        return True
    else:
        return False

def validate_username_no_whitespace(username):
    if ' ' in username:
        return False
    else:
        return True

def validate_username_no_special_chars(username):
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>/?'
    for char in username:
        if char in special_chars:
            return False
    return True

def validate_username_length(username):
    if len(username) > 30:
        return False
    else:
        return True

def validate_username():
    while True:
        username = get_username_input()
        if validate_username_uppercase(username) and validate_username_no_whitespace(username) and validate_username_no_special_chars(username) and validate_username_length(username):
            return username
        else:
            print("O nome de usuário deve começar com uma letra maiúscula, não deve conter espaços em branco, caracteres especiais e não deve ter mais de 30 caracteres. Tente novamente.")

username = validate_username()
print("O nome de usuário válido é:", username)

#VALIDA SENHA#

def get_password_input():
    password = input("Digite uma senha: ")
    return password

def validate_password_length(password):
    if len(password) < 10:
        return False
    else:
        return True

def validate_password_special_chars(password):
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>/?'
    for char in password:
        if char in special_chars:
            return True
    return False

def validate_password_number(password):
    numbers = '123456789'
    for char in password:
        if char in numbers:
            return True
    return False


def validate_password():
    while True:
        password = get_password_input()
        if validate_password_length(password) and validate_password_special_chars(password) and validate_password_number(password):
            return password
        else:
            print("A senha deve ter pelo menos 10 caracteres, um caracter especial, um número, ao menos uma letra maiúscula e uma letra minúscula. Tente novamente")

password = validate_password()
print("A senha de usuário válida é:", password)     