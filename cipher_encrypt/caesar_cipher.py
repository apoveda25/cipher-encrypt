upper_index_init = 65
lower_index_init = 97
length_alphabet = 26

upper_alphabet = "".join(
    map(chr, range(upper_index_init, upper_index_init + length_alphabet))
)
lower_alphabet = "".join(
    map(chr, range(lower_index_init, lower_index_init + length_alphabet))
)


def caesar_cipher_encrypt(text_plain: str, step: int):
    result = ""
    # transverse the plain text
    for i in range(len(text_plain)):
        char_plain = text_plain[i]
        # Encrypt uppercase characters in plain text

        if char_plain.isupper():
            result += chr(
                (ord(char_plain) + step - upper_index_init) % length_alphabet
                + upper_index_init
            )
        # Encrypt lowercase characters in plain text
        else:
            result += chr(
                (ord(char_plain) + step - lower_index_init) % length_alphabet
                + lower_index_init
            )

    return result


def caesar_cipher_decrypt(text_encrypt: str, step: int):
    result = ""
    # transverse the encrypt text
    for i in range(len(text_encrypt)):
        char_encrypt = text_encrypt[i]
        # Decrypt uppercase characters in plain text
        if char_encrypt.isupper():
            char_encrypt_index = (
                ord(char_encrypt) - step
                if ord(char_encrypt) - step - upper_index_init >= 0
                else ord(char_encrypt) - step + length_alphabet
            )
            result += chr(char_encrypt_index)

        # Decrypt lowercase characters in plain text
        elif char_encrypt.islower():
            char_encrypt_index = (
                ord(char_encrypt) - step
                if ord(char_encrypt) - step - lower_index_init >= 0
                else ord(char_encrypt) - step + length_alphabet
            )
            result += chr(char_encrypt_index)
        else:
            result += chr(ord(char_encrypt) - step)

    return result


def caesar_cipher_hacking(text_encrypt: str):
    translated = ""

    for step in range(length_alphabet):
        for char_encrypt in text_encrypt:
            if char_encrypt.isupper():
                char_encrypt_index = upper_alphabet.find(char_encrypt)

                char_plain_index = char_encrypt_index - step

                translated += (
                    upper_alphabet[char_plain_index + length_alphabet]
                    if char_plain_index < 0
                    else upper_alphabet[char_plain_index]
                )
            elif char_encrypt.islower():
                char_encrypt_index = lower_alphabet.find(char_encrypt)

                char_plain_index = char_encrypt_index - step

                translated += (
                    lower_alphabet[char_plain_index + length_alphabet]
                    if char_plain_index < 0
                    else lower_alphabet[char_plain_index]
                )
            else:
                translated += char_encrypt

        translated += "\n"

    return translated
