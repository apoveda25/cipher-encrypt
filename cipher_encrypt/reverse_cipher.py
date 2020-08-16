def reverse_cipher(text: str):
    translated = ""

    for i in range(len(text) - 1, -1, -1):
        translated += text[i]

    return translated
