from cryptographyFramework import *


initializeWrite()
user = "Fulano"
password = "1234"
encryptedText = encryptMessage(user, password, message)
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Minha segunda é maravilhosa!")
saveNewLine(encryptedText)

