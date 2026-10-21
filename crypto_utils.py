import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def aes_cbc_encrypt(plaintext: bytes, key: bytes) -> tuple[bytes, bytes]:
    iv = os.urandom(16)                    # nouvel IV à chaque appel
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext) + padder.finalize()
    enc = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
    return iv, enc.update(padded) + enc.finalize()

def aes_cbc_decrypt(iv: bytes, ciphertext: bytes, key: bytes) -> str:
    dec = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
    padded = dec.update(ciphertext) + dec.finalize()
    unpadder = padding.PKCS7(128).unpadder()   # retire le padding
    return unpadder.update(padded) + unpadder.finalize()

def compute_hmac(hmac_key, data) -> bytes:
    """ Generate HMAC """

def verify_hmac(hmac_key, data, mac) -> bytes:
    """ Verify HMAC """