from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization


def generer_paire_rsa() -> tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
    """ Generer paire clés RSA """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return (private_key, public_key)

def rsa_chiffrer_cle(cles: bytes, rsa_public_key: rsa.RSAPublicKey) -> bytes:
    """ Chiffrer clé par RSA """
    oaep = padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),label=None)
    chiffre = rsa_public_key.encrypt(cles, oaep)
    return chiffre

def rsa_dechiffrer_cle(cles_chiffrees: bytes, rsa_private_key: rsa.RSAPrivateKey) -> bytes:
    """ Déchiffrer clé par RSA """
    oaep = padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),label=None)
    dechiffre = rsa_private_key.decrypt(cles_chiffrees, oaep)
    return dechiffre

#----------------------------------------------------------------------------------


def main():
    # PEM généré par Copilot
    private_key, public_key = generer_paire_rsa()

    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    print("Clé privée (PEM) :")
    print(private_key_pem.decode("utf-8"))
    print("Clé publique (PEM) :")
    print(public_key_pem.decode("utf-8"))


if __name__ == "__main__":
    main()