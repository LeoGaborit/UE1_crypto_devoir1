import unittest
from crypto_utils import aes_cbc_decrypt, aes_cbc_encrypt
from rsa_utils import generer_paire_rsa, rsa_chiffrer_cle, rsa_dechiffrer_cle


class MyTestCase(unittest.TestCase):

    def test_aes_cbc_encrypt_decrypt(self):
        # Test AES-CBC encryption and decryption
        message = b"Message pas chiffre"
        cle = b'0123456789abcdef'  # cle AES-128

        iv, message_chiffre = aes_cbc_encrypt(message, cle)
        message_dechiffre = aes_cbc_decrypt(iv, message_chiffre, cle)
        self.assertEqual(message, message_dechiffre)

    def test_generation_chiffrage_dechiffrage_rsa(self):
        # Test RSA key generation, encryption, and decryption
        private_key, public_key = generer_paire_rsa()
        message = b"Message a chiffrer"
        cle = b'0123456789abcdef'  # cle AES-128

        # Chiffrer la clé AES avec RSA
        cle_chiffree = rsa_chiffrer_cle(cle, public_key)

        # Déchiffrer la clé AES avec RSA
        cle_dechiffree = rsa_dechiffrer_cle(cle_chiffree, private_key)

        # Chiffrer le message avec la clé déchiffrée
        iv, message_chiffre = aes_cbc_encrypt(message, cle_dechiffree)
        message_dechiffre = aes_cbc_decrypt(iv, message_chiffre, cle_dechiffree)

        self.assertEqual(message, message_dechiffre)

    def test_verification_hmac(self):
        # Test HMAC generation and verification
        from crypto_utils import compute_hmac, verify_hmac
        import os

        key = os.urandom(32)
        message = b"Transfert 1000 euros a Bob"
        send_hmac = compute_hmac(key, message)
        recv_hmac = verify_hmac(key, message, send_hmac)
        self.assertTrue(recv_hmac)

    def test_messenger(self):
        # Test the send_message and receive_message functions
        from messenger import send_message, receive_message
        private_key, public_key = generer_paire_rsa()
        message = b"Message a envoyer"

        packet = send_message(message, public_key)
        received_message = receive_message(packet, private_key)

        self.assertEqual(message, received_message)

if __name__ == '__main__':
    unittest.main()
