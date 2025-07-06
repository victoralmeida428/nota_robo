import secrets
from string import ascii_letters, digits

symbols = ''
alphabet = ascii_letters + digits + symbols
password = ""
size = 24

while len(password) < size:
    password += secrets.choice(alphabet)

print(password)
