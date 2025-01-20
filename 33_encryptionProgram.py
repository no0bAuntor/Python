import random
import string

chars = " " + string.digits + string.ascii_letters + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(f"Chars: {chars}")
print(f"Keys: {key}")

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Cipher Text: {cipher_text}")