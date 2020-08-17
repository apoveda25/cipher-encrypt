from string import ascii_letters, digits

alphabet = ascii_letters + digits


def encrypt(text_plain: str, key: int = 0):
    text_encrypt = ""

    for char in text_plain:
        if char in alphabet:
            text_encrypt += alphabet[(alphabet.index(char) + key) % len(alphabet)]
        else:
            text_encrypt += char

    return text_encrypt


def decrypt(text_encrypt: str, key: int = 0):
    text_plain = ""

    for char in text_encrypt:
        if char in alphabet:
            text_plain += alphabet[(alphabet.index(char) - key) % len(alphabet)]
        else:
            text_plain += char

    return text_plain


def hacking(text_encrypt: str):
    results = []

    for key in range(len(alphabet)):
        text_plain = ""

        for char in text_encrypt:
            if char in alphabet:
                text_plain += alphabet[(alphabet.index(char) - key) % len(alphabet)]
            else:
                text_plain += char

        results.append(text_plain)

    return results
