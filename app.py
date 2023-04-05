from input import *

#Username
def validate_username():
    while True:
        username = get_username_input()
        if validate_username_uppercase(username) and validate_username_no_whitespace(username) and validate_username_no_special_chars(username) and validate_username_length(username):
            return username
        else:
            print("O nome de usuário deve começar com uma letra maiúscula, não deve conter espaços em branco, caracteres especiais e não deve ter mais de 30 caracteres. Tente novamente.")

username = validate_username()


#Password
def validate_password():
    while True:
        password = get_password_input()
        if validate_password_length(password) and validate_password_special_chars(password) and validate_password_number(password) and validate_password_uppercase(password):
            return password
        else:
            print("A senha deve ter pelo menos 10 caracteres, um caracter especial, um número, ao menos uma letra maiúscula e uma letra minúscula. Tente novamente")

password = validate_password()

#Message
def validate_message():
    while True:
        message = get_message_input()
        if validate_message_length(message):
            return message
        else:
            print("A mensagem pode ter no máximo 70 caracteres. Tente novamente")

message = validate_message()

#Printa resultados
print("O nome de usuário válido é:", username)
print("A senha de usuário válida é:", password)
print("A mensagem a ser criptografada é: ", message)

