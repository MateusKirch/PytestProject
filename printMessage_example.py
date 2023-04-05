from cryptographyFramework import *

initializeRead()
username = "Mateus"
password = "123456789Aa!"
line1 = readNextLine()
print(line1)
print(decryptMessage(username, password, line1))
# line2 = readNextLine()
# print(line2)
# print(decryptMessage(user, password, line2))