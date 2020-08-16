alphabet_origin = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
alphabet_destiny = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"


# Function to translate plain text
def rot13_cipher_encrypt(text_plain: str):
    text_translate = text_plain.maketrans(alphabet_origin, alphabet_destiny)
    return text_plain.translate(text_translate)


# Function to translate encrypt text
def rot13_cipher_decrypt(text_encrypt: str):
    text_translate = text_encrypt.maketrans(alphabet_origin, alphabet_destiny)
    return text_encrypt.translate(text_translate)
