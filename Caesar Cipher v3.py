import string

def remove_spaces(text):
    return text.replace(" ", "")

def convert_to_uppercase(text):
    return text.upper()

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char == ".":
                char = 'X'
        if char.isalpha():
            if char in string.ascii_uppercase:
                index = (string.ascii_uppercase.index(char) + shift) % 26
                encrypted_text += string.ascii_uppercase[index]
            else:
                break

    encrypted_text = encrypted_text.replace(".", "")  # Remove dot after replacing
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
#
        if char.isalpha():  # Check if the character is a letter
            if char == 'X':
                decrypted_text += 'A'
            elif char in string.ascii_uppercase:
                index = (string.ascii_uppercase.index(char) - shift) % 26
                decrypted_text += string.ascii_uppercase[index]
            else:
                decrypted_text += char
    return decrypted_text

# Example usage
plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value: "))

# Encryption
plaintext = remove_spaces(plaintext)
plaintext = convert_to_uppercase(plaintext)
encrypted_text = encrypt(plaintext, shift)
print("Ciphertext:", encrypted_text)

# Decryption
ciphertext = encrypted_text
decrypted_text = decrypt(ciphertext, shift)
print("Decrypted text:", decrypted_text)
