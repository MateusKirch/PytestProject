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
    numbers = '1234567890'
    for char in password:
        if char in numbers:
            return True
    return False

def validate_password_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

#Validação mensagem

def get_message_input():
    message = input("Digite a mensagem a ser criptografada: ")
    return message

def validate_message_length(message):
    if len(message) > 70:
        return False
    else:
        return True