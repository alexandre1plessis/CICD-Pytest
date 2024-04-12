# CICD-Pytest

Ce projet est configuré pour utiliser `pytest` pour l'exécution de tests automatisés.

## Prérequis

Assurez-vous que vous avez installé Python 3.12 sur votre système. Vous pouvez vérifier cela en exécutant `python --version` (ou `python3 --version` sur certains systèmes) dans votre terminal.

## Installation des dépendances

Pour installer `pytest`, exécutez la commande suivante dans votre terminal :
pip install pytest


Si vous rencontrez des problèmes de permission, vous pouvez ajouter l'option `--user` pour installer `pytest` uniquement pour votre utilisateur :
pip install --user pytest


## Exécuter les tests

Pour exécuter les tests avec `pytest`, naviguez vers la racine du projet dans votre terminal et exécutez :
pytest


`pytest` détectera automatiquement tous les fichiers de tests suivant la convention de nommage `test_*.py` ou `*_test.py` dans le répertoire de tests.

Pour des options de ligne de commande supplémentaires avec `pytest`, consultez la [documentation officielle de pytest](https://docs.pytest.org/en/stable/usage.html).

## Contribuer

Pour contribuer à ce projet, veuillez suivre les étapes suivantes :

1. Forker le dépôt.
2. Créer une nouvelle branche pour vos modifications.
3. Faites vos modifications et écrivez des tests pour accompagner les changements si nécessaire.
4. Exécutez les tests pour vous assurer qu'ils passent.
5. Soumettez une pull request avec une description détaillée de vos changements.
