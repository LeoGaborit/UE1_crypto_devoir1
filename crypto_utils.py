import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import hmac, hashlib

def aes_cbc_encrypt(plaintext: bytes, key: bytes) -> tuple[bytes, bytes]:
    iv = os.urandom(16)                    # nouvel IV à chaque appel
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext) + padder.finalize()
    enc = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
    return iv, enc.update(padded) + enc.finalize()

def aes_cbc_decrypt(iv: bytes, ciphertext: bytes, key: bytes) -> bytes:
    dec = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
    padded = dec.update(ciphertext) + dec.finalize()
    unpadder = padding.PKCS7(128).unpadder()   # retire le padding
    return unpadder.update(padded) + unpadder.finalize()

def compute_hmac(hmac_key, data) -> bytes:
    """ Generate HMAC """
    mac = hmac.new(hmac_key, data, hashlib.sha256).digest()
    return mac

def verify_hmac(hmac_key, data, mac) -> bool:
    """ Verify HMAC """
    recieved_verification = hmac.new(hmac_key, data, hashlib.sha256).digest()
    verification = hmac.compare_digest(recieved_verification, mac)
    return verification

# HMAC verification test
# key = os.urandom(32)
# message = b"Transfert 1000 euros a Bob"
# send_hmac = compute_hmac(key, message)
# recv_hmac = verify_hmac(key, message, send_hmac)
# print(recv_hmac)

