from string import ascii_letters, digits

alphabet = ascii_letters + digits
cypher_alphabet = alphabet[-1::-1]


def encrypt(text_plain: str):
    text_encrypt = ""

    for char in text_plain:
        if char in alphabet:
            text_encrypt += cypher_alphabet[alphabet.index(char)]
        else:
            text_encrypt += char

    return text_encrypt


def decrypt(text_encrypt: str):
    text_plain = ""

    for char in text_encrypt:
        if char in cypher_alphabet:
            text_plain += alphabet[cypher_alphabet.index(char)]
        else:
            text_plain += char

    return text_plain
