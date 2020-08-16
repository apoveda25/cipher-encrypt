from reverse_cipher import reverse_cipher
from caesar_cipher import (
    caesar_cipher_encrypt,
    caesar_cipher_decrypt,
    caesar_cipher_hacking,
)
from rot13_cipher import rot13_cipher_encrypt, rot13_cipher_decrypt
import atbash


print(reverse_cipher("message"))
print(reverse_cipher(reverse_cipher("message")))
print(caesar_cipher_encrypt("Alfredo Poveda", 9))
print(caesar_cipher_decrypt(caesar_cipher_encrypt("Alfredo Poveda", 18), 18))
print(caesar_cipher_hacking(caesar_cipher_encrypt("Alfredo Poveda", 9)))
print(rot13_cipher_encrypt("ROT13 Algorithm"))
print(rot13_cipher_decrypt(rot13_cipher_encrypt("ROT13 Algorithm")))
print(atbash.encrypt("Hola Mundo!"))
print(atbash.decrypt(atbash.encrypt("Hola Mundo!")))
