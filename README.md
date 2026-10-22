# Messagerie sécurisée — UE1 Cryptographie

Nous avons réalisé ce projet dans le cadre de l'UE1 : Fondamentaux de la cryptographie appliquée à la sécurité des systèmes d'information (GUARDIA, M1). Notre objectif était de mettre en pratique quelques notions de cryptographie en construisant messagerie sécurisée en Python.

Le projet présente trois outils complémentaires : AES pour chiffrer le contenu d'un message, RSA pour protéger les clés secrètes utilisées, et HMAC pour vérifier que le message n'a pas été modifié. 

Notre programme se pilote depuis un menu dans le terminal et propose un mode histoire, une démonstration interactive et un mode d'apprentissage.

## Fonctionnalités

- **Mode Histoire** : nous présentons les rôles d'AES, RSA et HMAC à travers une courte histoire autour d'Alice, Bob et Eve (le Roi).
- **Mode Express** : nous pouvons saisir un message et simuler son envoi à Bob. Nous pouvons aussi modifier le paquet en transit pour voir la vérification HMAC le rejeter.
- **Mode Apprentissage** : nous expliquons brièvement les trois mécanismes et la manière dont nous les associons dans le projet.

## Comment se déroule un échange ?

1. Le programme génère une clé AES et une clé HMAC aléatoires pour l'expéditeur.
2. Il chiffre le message avec AES, un IV aléatoire et un remplissage PKCS#7.
3. Il calcule HMAC-SHA-256 sur la concaténation de l'IV et du texte chiffré.
4. Il chiffre les clés AES et HMAC avec la clé publique RSA du destinataire.
5. À la réception, il déchiffre ces clés avec la clé privée, puis il vérifie le HMAC.
6. Si la vérification réussit, il déchiffre le message avec AES. Sinon, il rejete le paquet.

Le programme génère une paire RSA de 2048 bits et utilise OAEP avec SHA-256 pour chiffrer les clés. Pour le HMAC, il compare le code reçu et le code recalculé avec `hmac.compare_digest`.

## Organisation des fichiers

| Fichier | Rôle |
| --- | --- |
| `main.py` | Menu et parcours interactifs des trois modes. |
| `messenger.py` | Création du paquet d'envoi et réception avec vérification du HMAC avant le déchiffrement AES. |
| `crypto_utils.py` | Chiffrement et déchiffrement AES-CBC, calcul et vérification HMAC-SHA-256. |
| `rsa_utils.py` | Génération d'une paire RSA et chiffrement/déchiffrement des clés avec OAEP. |
| `tests.py` | Tests des opérations AES, RSA, HMAC et de l'échange via `messenger`. |
| `.run/START.run.xml` | Configuration d'exécution PyCharm pour lancer `main.py` dans le terminal intégré. |

## Historique Git et organisation des branches

Nous avons organisé le développement autour de branches de fonctionnalités, ensuite réunies dans `dev`. `main` est la version finale du projet, tandis que `dev` nous a servi à rassembler et stabiliser nos développements avant leur publication.

| Branche | Travail associé dans l'historique |
| --- | --- |
| `main` | Nous l'avons créée comme base initiale et nous allonrs l'exposer la version finale. |
| `dev` | Nous y avons intégré les fonctionnalités, les tests et les nettoyages avant publication. |
| `feature-AES` | Nous y avons posé une étape de travail sur AES et ajouté le `.gitignore`. L'implémentation AES apparaît aussi dans les commits de base du projet. |
| `feature-RSA` | Nous y avons ajouté les méthodes RSA pour générer une paire de clés et chiffrer/déchiffrer les clés. |
| `messenger_dev` | Nous y avons développé le système de transfert de paquets de la messagerie. |
| `feature-tests` | Nous y avons ajouté et corrigé les tests des fonctions cryptographiques et de la messagerie. |
| `feature_main` | Nous y avons ajouté les modes interactifs, dont le mode Histoire, et la configuration PyCharm `START`. |
Nous avons d'abord créé la structure de départ, puis ajouté les fonctions cryptographiques et le transfert de messages. Nous avons ensuite ajouté les tests et les modes interactifs, avant de fusionner les branches de fonctionnalités dans `dev` et d'y nettoyer et mettre en forme le code avant l'envoi en version finale.

### Contributions visibles dans les commits

Les commits Git utilisent plusieurs comptes : **Adrien Capdeville et `donbixa1` désignent la même personne**, tout comme **LeoGaborit et `XterS`**. Nous regroupons ci-dessous nos contributions sous nos noms.

- **Adrien Capdeville (`donbixa1`)** : de mon côté, j'ai travaillé sur la structure initiale, les premières fonctions cryptographiques, HMAC, le transfert des messages ainsi que les premières versions et explications du README. J'ai aussi réalisé une fusion de la branche de messagerie.
- **LeoGaborit (`XterS`)** : J'ai travaillé sur les méthodes RSA, l'ajout et la correction des tests, le menu ainsi que les 3 modes interactifs, la configuration PyCharm et le nettoyage du code. J'ai créé le commit initial et réalisé des fusions de branches.

## Installation et lancement

Pour lancer le projet, nous avons besoin de Python 3 et de la bibliothèque [`cryptography`](https://pypi.org/project/cryptography/).

```bash
python -m pip install cryptography
python main.py
```

Dans le menu, nous choisissons `1`, `2` ou `3` pour démarrer un mode, ou `4` pour quitter. Le mode Express nous demande un message et nous permet de choisir si le paquet doit être intercepté et modifié.

### Lancer avec la configuration PyCharm

Nous avons également inclus une configuration d'exécution nommée **START**. Dans PyCharm, il suffit d'ouvrir le projet, de sélectionner **START** dans la liste des configurations, puis de cliquer sur **Run** (ou d'utiliser le raccourci d'exécution). Cette configuration lance `main.py` depuis le dossier du projet et active l'émulation du terminal pour permettre les saisies interactives.

## Tester le projet

Depuis le dossier du projet, nous lançons les tests avec :

```bash
python -m unittest -v
```

Les tests vérifient notamment que nous retrouvons un message après chiffrement et déchiffrement, qu'une paire RSA permet de protéger une clé et qu'un paquet portant un HMAC invalide déclenche une erreur.

## Limites de la démonstration
###### *rajouté par IA*

Dans notre programme, l'échange est simulé dans un seul processus : nous n'envoyons pas réellement de données sur un réseau et nous ne gérons ni comptes ni stockage de clés. En mode Express, nous simulons l'interception en modifiant directement le paquet en mémoire. Enfin, AES-CBC nécessite une vérification d'intégrité séparée, que nous assurons ici avec le HMAC. Pour une application réelle, nous devrions nous appuyer sur une conception et une gestion des clés adaptées à la production.
