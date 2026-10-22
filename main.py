import os
import subprocess

import messenger
import rsa_utils


def consoleClear():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def main():
    choix: int = 0

    while choix != 4:
        consoleClear()
        print("\t~ Bienvenue dans la messagerie la plus sécurisée au monde ! (à peu près) ~")
        print("")
        print("\t                     ┃  Que souhaitez-vous faire ? ┃                      ")
        print("\t                     ┃   1 - Mode Histoire         ┃                      ")
        print("\t                     ┃   2 - Mode Express          ┃                      ")
        print("\t                     ┃   3 - Mode Apprentissage    ┃                      ")
        print("\t                     ┃   4 - Quitter le programme  ┃                      ")
        print("\t                                                                          ")
        print("\t                         ↓                                                ")
        choix = int(input("\t                         "))
        while choix not in (1, 2, 3, 4):  # Condition menu existant
            print("")
            print("Vous devez choisir un menu existant !")
            choix = int(input(">>> "))

        consoleClear()

        if choix == 1:
            choix = 0

            print("\t                           ~ Mode Histoire activé ! ~                        ")
            print("")
            print("\t    Commençons, je suis sur le point de vous conter une histoire ancienne,   ")
            print("\t tellement ancienne qu'elle est incrite dans les anciens livres poussiéreux. ")
            print("\n")
            input("\t- Appuyez sur Entrée pour continuer... ")

            consoleClear()

            print(
                "\t                  ~ Il était une fois Alice et Bob, une jeune princesse et un chevalier ~                ")
            print("")
            print(
                "\t    Alice et Bob sont deux jeunes amoureux qui vivent au Moyen-Âge, ils s'aiment passionnément mais,     ")
            print(
                "\t      le père d'Alice, le roi, n'apprécie pas cette relation et souhaite séparer les deux amoureux.      ")
            print("")
            print(
                "\t Ils devaient donc trouver un moyen de communiquer secrètement, sans que le roi ne puisse les espionner. ")
            print("\n")
            input("\t- Appuyez sur Entrée pour continuer... ")

            consoleClear()

            print(
                "\t ~ Alice avait déjà tenté d'envoyer des lettres à Bob, mais toutes les lettres étaient interceptées par le roi ~ ")
            print("")
            print(
                "\t     Elle devait donc trouver un moyen de communiquer avec Bob sans que le roi ne puisse lire ses messages.      ")
            print("")
            print(
                "\t          Elle se souvient alors d'une technique de cryptographie, qui permet de chiffrer les messages,          ")
            print(
                "\t            afin que seules les personnes qui connaissaient la traduction, puisse les lire clairement              ")
            print(
                "\t                 Cette magie très puissante qui transforme les mots en charabia s'appelle AES.                   ")
            print("\n")
            input("\t- Appuyez sur Entrée pour continuer... ")

            consoleClear()

            print(
                "\t                          ~ AES est une technique de cryptographie symétrique ~                          ")
            print("")
            print(
                "\t Elle permet de traduire un message en une langue étrangère à ceux qui ne connaissent pas sa traduction. ")
            print(
                "\t          De cette manière, le roi ne pourra pas comprendre les messages qu'Alice envoie à Bob.          ")
            print(
                "\t        Alors que Bob si, mais comment envoyer la traduction à Bob sans que le roi l'intercepte...       ")
            print("")
            print(
                "\t                   C'est là qu'intervient une autre magie très puissante, appelée RSA.                   ")
            print("\n")
            input("\t- Appuyez sur Entrée pour continuer... ")

            consoleClear()

            print(
                "\t                       ~ RSA est une technique de cryptographie asymétrique ~                       ")
            print("")
            print(
                "\t  Elle permet de créer un cadenas qui possède une clé pour l'ouvrir et une deuxième pour le fermer  ")
            print(
                "\t       La clé pour fermer le cadenas est publique, tandis que celle pour l'ouvrir est privée.      ")
            print("")
            print(
                "\t   Elle pourrait envoyer ce cadenas à Bob avec la clé publique, le roi ne pourrait rien en faire    ")
            print("\t  Et Bob pourrait fermer son message avec, et seule Alice pourrait l'ouvrir avec sa clé privée  ")
            print(
                "\t Et une fois le message reçu, Bob envoie son propre cadenas, de cette manière le canal est sécurisé ")
            print("\n")
            input("\t- Appuyez sur Entrée pour continuer... ")

            consoleClear()

            print(
                "\t               ~ Ces deux magies sont très efficaces, mais il manque une dernière chose ~                ")
            print("")
            print(
                "\t    Il manque une magie qui permet d'être certain que le message reçu est bien celui qui a été envoyé    ")
            print(
                "\t        Et que le message n'a pas été modifié en route par le roi, qui pourrait vouloir piéger Bob       ")
            print("")
            print(
                "\t Cette magie s'appelle HMAC, elle permet de vérifier l'intégrité du message et qu'il n'a pas été modifié ")
            print("\n")
            input("\t- Appuyez sur Entrée pour continuer... ")

            consoleClear()

            print(
                "\t ~ Alice et Bob maîtrisaient enfin toutes les magies nécessaires pour établir une communication sûre ~ ")
            print("")
            print(
                "\t  Alice créa son cadenas, Bob le sien, ils se l'envoyèrent afin d'ouvrir le message de chacun avec RSA ")
            print(
                "\t           Ils créèrent leur langage secret avec AES, afin de ne pas être compris par le roi           ")
            print(
                "\t   Et enfin, ils utilisèrent HMAC pour vérifier que les messages n'avaient pas été modifiés en route   ")
            print("")
            print(
                "\t      ~ Ils vécurent heureux et eurent beaucoup d'enfants, grâce à la magie de la Cryptographie ~      ")
            print("\n")
            input("\t- Appuyez sur Entrée pour revenir au menu principal ")

        if choix == 2:
            choix = 0

            intercept: int
            message: str
            paquet: dict

            print("\t ~ Mode Express activé ! ~")
            print("")
            print("\t Le mode express va montrer un échange interactif sécurisé entre vous et Bob ")
            print("")
            print("\t Voulez vous que l'échange soit intercepté et modifié ? (test itégrité HMAC) ")
            print("\t 1 = Oui | 2 = Non\n")
            intercept = int(input("\t - Votre choix : "))

            consoleClear()

            print("\t [Bob] Génération des clés RSA...\n")
            private_key, public_key = rsa_utils.generer_paire_rsa()

            message = input("\t- Veuillez rentrer un message à transmettre à Bob : ")
            paquet = messenger.send_message(message.encode(), public_key)
            print("\n\t [Vous] Envoi du message : " + message)

            print("")

            if intercept == 1:
                print("\t [Eve] Interception du message !")
                print("\t [Eve] Modification du message... \n")
                paquet["ciphertext"] = b"message modifie"
                paquet["hmac"] = b"invalid_hmac"

            try:
                messenger.receive_message(paquet, private_key)
            except ValueError as _:
                print(f"\t [Bob] ALERTE : HMAC invalide, message rejeté")
                print("\t [OK] Manipulation détectée")
            else:
                print("\t [Bob] Message reçu avec succès : " + message)
                print("\t [OK] Message identique")

            input("\n Appuyez sur [Entrée] pour continuer")

        if choix == 3:
            choix = 0

            print("\t                ~ Mode Apprentissage activé ! ~                ")
            print("")
            print("\t Dans ce mode, nous allons découvrir les trois outils utilisés ")
            print("\t         pour protéger les messages : AES, RSA et HMAC.        ")
            print("\n")
            input("\t - Appuyez sur Entrée pour continuer... ")

            consoleClear()

            print("\t         ~ AES : chiffrer le contenu du message ~         ")
            print("")
            print("\t AES est une méthode de chiffrement symétrique : Alice et Bob ")
            print("\t   utilisent la même clé secrète pour chiffrer et déchiffrer. ")
            print("")
            print("\t Sans cette clé, le message chiffré ressemble à du charabia ")
            print("\t  et ne peut pas être compris par une personne extérieure.  ")
            print("\n")
            input("\t - Appuyez sur Entrée pour continuer... ")

            consoleClear()

            print("\t            ~ RSA : partager les clés de manière sécurisée ~            ")
            print("")
            print("\t       RSA est une méthode de chiffrement asymétrique qui utilise       ")
            print("\t             une paire de clés liées l'une à l'autre.                   ")
            print("")
            print("\t    La clé publique peut être partagée pour chiffrer une clé secrète.   ")
            print("\t      Seule la clé privée correspondante peut alors la déchiffrer.      ")
            print("\t Dans notre messagerie, RSA protège les clés utilisées par AES et HMAC. ")
            print("\n")
            input("\t - Appuyez sur Entrée pour continuer... ")

            consoleClear()

            print("\t          ~ HMAC : vérifier l'intégrité et l'authenticité ~           ")
            print("")
            print("\t HMAC est un code calculé à partir d'un message et d'une clé secrète. ")
            print("\t    Le destinataire recalcule ce code et le compare à celui reçu.     ")
            print("")
            print("\t           Si le message a été modifié, les deux codes HMAC           ")
            print("\t            ne correspondent plus et le message est rejeté.           ")
            print("")
            print("\t   HMAC ne chiffre pas le message : il sert à vérifier qu'il n'a pas  ")
            print("\t        été modifié en cours de route et qu'il est authentique.       ")
            print("\n")
            input("\t - Appuyez sur Entrée pour continuer... ")

            consoleClear()

            print("\t        ~ Comment ces outils travaillent ensemble ~       ")
            print("")
            print("\t   AES chiffre le message, RSA protège les clés secrètes, ")
            print("\t       et HMAC permet de détecter toute modification.     ")
            print("")
            print("\t  Chacun a donc un rôle différent pour protéger l'échange.")
            print("\n")
            input("\t - Appuyez sur Entrée pour revenir au menu principal ")

    print("\t ~ Vous avez quitté le programme. A bientôt ! ~ \n")


if __name__ == "__main__":
    main()
