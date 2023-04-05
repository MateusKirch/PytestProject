from input import *

#Testes Username

def test_validate_username_uppercase():
    assert validate_username_uppercase("Mateus") == True
    assert validate_username_uppercase("mateus") == False

def test_validate_username_no_whitespace():
    assert validate_username_no_whitespace("Mateus") == True
    assert validate_username_no_whitespace("Mat eus") == False

def test_validate_username_no_special_chars():
    assert validate_username_no_special_chars("Mateus") == True
    assert validate_username_no_special_chars("Mateus!") == False

def test_validate_username_length():
    assert validate_username_length("Mateus") == True
    assert validate_username_length("Mateus1234567890098765432112345678900") == False

#Testes Password

def test_validate_password_length():
    assert validate_password_length("1234567890!Aa") == True
    assert validate_password_length("12345!Aa") == False

def test_validate_password_special_chars():
    assert validate_password_special_chars("1234567890!Aa") == True
    assert validate_password_special_chars("1234567890Aa") == False

def test_validate_password_number():
    assert validate_password_number("1234567890!Aa") == True
    assert validate_password_number("aaaaaaaaaa!Aa") == False

def test_validate_password_uppercase():
    assert validate_password_uppercase("1234567890!Aa") == True
    assert validate_password_uppercase("aaaaaaaaaa!125a") == False

#Testes Mensagem

def validate_message_length():
    assert validate_message_length("Essa é a minha mensagem") == True
    assert validate_message_length("Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == False