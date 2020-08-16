from reverse_cipher import reverse_cipher
from caesar_cipher import (
    caesar_cipher_encrypt,
    caesar_cipher_decrypt,
    caesar_cipher_hacking,
)

print(reverse_cipher("message"))
print(reverse_cipher(reverse_cipher("message")))
print(caesar_cipher_encrypt("Alfredo Poveda", 9))
print(caesar_cipher_decrypt(caesar_cipher_encrypt("Alfredo Poveda", 18), 18))
print(caesar_cipher_hacking(caesar_cipher_encrypt("Alfredo Poveda", 9)))
