# Q26. Caesar Cipher
# Encrypt and decrypt a message using the Caesar Cipher algorithm.

message = input("Enter message: ")
shift = int(input("Enter shift: "))

encrypted = ""

for ch in message:
    if ch.isalpha():
        encrypted += chr((ord(ch.lower()) - 97 + shift) % 26 + 97)
    else:
        encrypted += ch

print("Encrypted message =", encrypted)

decrypted = ""

for ch in encrypted:
    if ch.isalpha():
        decrypted += chr((ord(ch.lower()) - 97 - shift) % 26 + 97)
    else:
        decrypted += ch

print("Decrypted message =", decrypted)