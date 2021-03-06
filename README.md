# Dash demo!

## 1. Installation
- git clone https://github.com/JacquesGarre/dash_demo *(clonage du repo)* 
- cd dash_demo *(déplacement dans le dossier de travail)* 
- pip install virtualenv *(installation du package permettant de créer un environnement virtuel)* 
- virtualenv dash_demo *(création d'un environnement virtuel)* 

## 2. Lancer l'application web
- dash_demo\Scripts\activate *(pour activer l'environnement virtuel)* 
- python app.py *(pour lancer le serveur local)* 
- deactivate *(pour désactiver l'environnement virtuel)*

## 3. Utilisation de git

### a. Configuration initiale
- git remote -v *(permet de visualiser les remotes)*
- git remote add upstream {url} *(permet d'ajouter un upstream)*

### b. Mettre à jour et push ses modifications
- git fetch upstream *(récupère les éventuelles mises à jour)*
- git merge upstream/master *(applique les éventuelles mises à jour)*
- git add . *(ajoute tous les fichiers contenant une modification)* 
- git status *(permet de visualiser les fichiers ajoutés)* 
- git commit -m "Message de commit" *(permet de commit, avec un message de commentaire)* 
- git push origin master *(permet de push sur le repo les modifications)* 
