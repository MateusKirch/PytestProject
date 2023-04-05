from cryptographyFramework import *

initializeWrite()
username = "Mateus"
password = "123456789Aa!"
encryptedText = encryptMessage(username, password, "Minha mensagem secreta!")
saveNewLine(encryptedText)
# encryptedText = encryptMessage(user, password, "Minha segunda mensagem secreta!")
# saveNewLine(encryptedText)