from cryptography.hazmat.primitives.asymmetric import rsa

import crypto_utils
import rsa_utils
import os

def send_message(plaintext : bytes, rsa_public_key : rsa.RSAPublicKey) -> dict:
    """ Transforms plaintext into a packet """
    aes_key = os.urandom(256)
    hmac_key = os.urandom(32)

    encrypted_aes_key = rsa_utils.rsa_chiffrer_cle(aes_key, rsa_public_key)
    encrypted_hmac_key = rsa_utils.rsa_chiffrer_cle(hmac_key, rsa_public_key)

    encrypted_message = crypto_utils.aes_cbc_encrypt(plaintext, aes_key)
    computed_hmac = crypto_utils.compute_hmac(hmac_key, encrypted_message)

    return { "cles_chiffrees": (encrypted_aes_key, encrypted_hmac_key), "iv": encrypted_message[0], "ciphertext": encrypted_message[1], "hmac": computed_hmac }


def receive_message(packet : dict, rsa_private_key : rsa.RSAPrivateKey) -> bytes:
    """ Recieves packet message """
    # recived transfer packets
    encypted_keys = packet["cles_chiffrees"]
    recv_iv, recv_ciphertext = (packet["iv"],packet["ciphertext"])
    recv_hmac = packet["hmac"]

    decrypted_aes_key = rsa_utils.rsa_dechiffrer_cle(encypted_keys[0], rsa_private_key)
    decrypted_hmac_key = rsa_utils.rsa_dechiffrer_cle(encypted_keys[1], rsa_private_key)

    if not crypto_utils.verify_hmac(decrypted_hmac_key, recv_iv + recv_ciphertext, recv_hmac):
        raise ValueError("Calcul HMAC invalide")

    decrypted_message = crypto_utils.aes_cbc_decrypt(recv_iv, recv_ciphertext, decrypted_aes_key)
    return decrypted_message