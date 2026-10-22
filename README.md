# Messagerie sécurisée — UE1 Cryptographie

Ce projet a été réalisé dans le cadre de l'UE1 « Fondamentaux de la cryptographie appliquée à la sécurité des systèmes d'information » (GUARDIA, M1). L'objectif est de mettre en pratique quelques notions de cryptographie en construisant une petite messagerie pédagogique en Python.

L'application illustre trois outils complémentaires : AES pour chiffrer le contenu d'un message, RSA pour protéger les clés secrètes utilisées, et HMAC pour vérifier que le message n'a pas été modifié. Le programme se pilote depuis un menu dans le terminal et propose un mode histoire, une démonstration interactive et un mode d'apprentissage.

> **À noter :** il s'agit d'une démonstration pédagogique, et non d'une messagerie prête à être utilisée pour échanger de vrais messages confidentiels.

## Fonctionnalités

- **Mode Histoire** : présente les rôles d'AES, RSA et HMAC à travers une courte histoire autour d'Alice, Bob et Eve.
- **Mode Express** : permet de saisir un message et de simuler son envoi à Bob. On peut choisir de modifier le paquet en transit pour voir la vérification HMAC le rejeter.
- **Mode Apprentissage** : donne une explication synthétique des trois mécanismes et de la manière dont ils sont associés dans le projet.

## Comment se déroule un échange ?

1. L'expéditeur génère une clé AES et une clé HMAC aléatoires.
2. AES chiffre le message avec un IV aléatoire et un remplissage PKCS#7.
3. HMAC-SHA-256 est calculé sur la concaténation de l'IV et du texte chiffré.
4. Les clés AES et HMAC sont chiffrées avec la clé publique RSA du destinataire.
5. Le destinataire déchiffre ces clés avec sa clé privée, puis vérifie le HMAC.
6. Si la vérification réussit, le message est déchiffré avec AES. Sinon, le paquet est rejeté.

La paire RSA générée par le projet fait 2048 bits. Le chiffrement RSA des clés utilise OAEP avec SHA-256. Pour le HMAC, la comparaison du code reçu et du code recalculé utilise `hmac.compare_digest`.

## Organisation des fichiers

| Fichier | Rôle |
| --- | --- |
| `main.py` | Menu et parcours interactifs des trois modes. |
| `messenger.py` | Création du paquet d'envoi et réception avec vérification du HMAC avant le déchiffrement AES. |
| `crypto_utils.py` | Chiffrement et déchiffrement AES-CBC, calcul et vérification HMAC-SHA-256. |
| `rsa_utils.py` | Génération d'une paire RSA et chiffrement/déchiffrement des clés avec OAEP. |
| `tests.py` | Tests des opérations AES, RSA, HMAC et de l'échange via `messenger`. |
| `.run/START.run.xml` | Configuration d'exécution PyCharm pour lancer `main.py` dans le terminal intégré. |

## Installation et lancement

Le projet nécessite Python 3 et la bibliothèque [`cryptography`](https://pypi.org/project/cryptography/).

```bash
python -m pip install cryptography
python main.py
```

Dans le menu, choisir `1`, `2` ou `3` pour démarrer un mode, ou `4` pour quitter. Le mode Express demande un message et permet de choisir si le paquet doit être intercepté et modifié.

### Lancer avec la configuration PyCharm

Le projet contient également une configuration d'exécution nommée **START**. Dans PyCharm, ouvrir le projet, sélectionner **START** dans la liste des configurations, puis cliquer sur **Run** (ou utiliser le raccourci d'exécution). La configuration lance `main.py` depuis le dossier du projet et active l'émulation du terminal pour permettre les saisies interactives.

## Lancer les tests

Depuis le dossier du projet, exécuter :

```bash
python -m unittest -v
```

Les tests vérifient notamment qu'un message chiffré puis déchiffré est retrouvé, qu'une paire RSA permet de protéger une clé et qu'un paquet portant un HMAC invalide déclenche une erreur.

## Limites de la démonstration

Le programme simule l'échange dans un seul processus : il n'envoie pas réellement de données sur un réseau et ne gère ni comptes ni stockage de clés. Le mode Express simule l'interception en modifiant directement le paquet en mémoire. Enfin, AES-CBC nécessite une vérification d'intégrité séparée, ici assurée par le HMAC ; pour une application réelle, il faudrait s'appuyer sur une conception et une gestion des clés adaptées à la production.
