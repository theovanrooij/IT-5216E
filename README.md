# 22_E5_IT_5216E - Développement web full stack 
## Projet DrapQuiz
\
![](/quiz-ui/src/assets/favicon.ico "icon")

Réalisé par VAN ROOIJ Théo, TA Christophe et DANG Méline

## Introduction

Notre projet vise à réaliser un Quiz en ligne. Ce projet doit permettre à ses visiteurs de répondre à une liste de questions établie et modifiable dans une partie administateur.

Notre quiz contient des questions sur les drapeaux de pays. L'utilisateur doit trouver le pays correspondant à un drapeau affiché parmi 4 choix possibles.

Le projet est constitué d'une base de données SQLite, d'une API Flask, et d'un front en VueJS.
Le développement de l'API se base sur du TDD (Test-Driven Development) qui a été réalisé avec le logiciel Postman.


## Installation de Git et récupération des fichiers

Vérifiez tout d'abord que vous avez installé [Git](https://git-scm.com/) pour la récupération des fichiers.

Nous allons maintenant cloner le projet dans le répertoire de votre choix. Pour cela, cliquez sur votre répertoire et faites clique-droit `Git Bash Here`.

Une fois Git Bash ouvert, nous allons cloner le répertoire en ligne où se trouve le projet. Cliquez sur le bouton `Clone or Download` et copiez l'adresse HTTPS du [répertoire](https://github.com/theovanrooij/IT-5216E.git).
Une fois copié, retournez dans Git Bash et tapez la commande `git clone` (adresse du répertoire) et cela vous donnera un accès de téléchargement au répertoire.
Finalement, tapez la commande `git pull` et vous aurez à votre disposition tous les fichiers du projet. 

## Installation des packages nécessaires et lancement

Voici trois manières différentes pour lancer le projet :

### Lancement avec Docker
Pour lancer de cette manière, vous devez avoir l'application [`Docker`](https://www.docker.com/get-started), permettant de construire sur votre ordinateur les mêmes images sur lesquelles nous avons développé. Assurez également d'avoir installé [`WSL 2`](https://docs.microsoft.com/fr-fr/windows/wsl/install) permettant une couche de compatibilité entre les éxecutables Linux et le système Windows.

Après avoir lancé Docker, lancez l'API :
- Ouvrez un terminal et rendez-vous dans le dossier [`quiz-api`](https://github.com/theovanrooij/IT-5216E/tree/main/quiz-api).
- Tapez la commande `docker image build -t quiz-local-api .` pour construire l'image de l'API.
- Tapez la commande `docker container run -it --rm -p 5000:5000 --name quiz-local-api quiz-local-api` pour lancer un conteneur contenant l'image API.

Ensuite, lancez l'interface utilisateur :
- Ouvrez un nouveau terminal et rendez-vous dans le dossier [`quiz-ui`](https://github.com/theovanrooij/IT-5216E/tree/main/quiz-ui).
- Tapez la commande `docker image build -t quiz-local-ui .` pour construire l'image de l'interface.
- Tapez la commande `docker container run -it --rm -p 3000:80 --name quiz-local-ui quiz-local-ui` pour lancer un conteneur contenant l'image de l'interface.

Vous pourrez ensuite accéder au site en vous rendant sur  [`localhost:3000`](localhost:3000).


### Lancement manuel
Pour lancer de cette manière, vérifiez tout d'abord si vous disposez de la bonne version de Python. Pour cela:
- Ouvrez un terminal.
- Tapez la commande `python --version`.
- Vérifiez si la version est à jour, de préférence la version `3.10`.

Vous aurez aussi besoin du module nodeJS que vous pourrez installer à l'URL [`https://nodejs.org/en/`] et en choisissant la version `LTS`.

Si vous voulez utiliser un environnement virtuel :
- Ouvrez un terminal et rendez-vous à la racine du projet.
- Tapez la commande `python -m venv venv`.
- Tapez la commande `source venv/Scripts/activate`

Pour lancer l'API :
- Ouvrez un terminal et rendez-vous dans le dossier [`quiz-api`](https://github.com/theovanrooij/IT-5216E/tree/main/quiz-api).
- Tapez la commande `pip install -r requirements.txt` pour installer les librairies nécessaires.
- Tapez la commande `python app.py` le code de l'API.

Ensuite, lancez l'interface utilisateur :
- Ouvrez un nouveaut terminal et rendez-vous dans le dossier [`quiz-ui`](https://github.com/theovanrooij/IT-5216E/tree/main/quiz-ui).
- Tapez la commande `npm install vite` pour installer l'outil Vite.
- Tapez la commande `npm run build` pour lancer l'interface.

Vous pourrez ensuite accéder au site en vous rendant sur  [`localhost:3000`](localhost:3000).

### Lancement avec les images Docker en ligne
Pour lancer de cette manière, vous n'aurez pas besoin d'importer les fichiers sur votre ordinateur à l'aide de git. Vous devrez avoir l'application [`Docker`](https://www.docker.com/get-started), permettant de construire sur votre ordinateur les mêmes images sur lesquelles nous avons développé. Assurez également d'avoir installé [`WSL 2`](https://docs.microsoft.com/fr-fr/windows/wsl/install) permettant une couche de compatibilité entre les éxecutables Linux et le système Windows.

Les images Docker peuvent être consultées sur les liens suivants :
- API : ['https://hub.docker.com/r/theovanrooij/quiz-prod-api'](https://hub.docker.com/r/theovanrooij/quiz-prod-api)
- UI : [`https://hub.docker.com/r/theovanrooij/quiz-prod-ui`](https://hub.docker.com/r/theovanrooij/quiz-prod-ui)

Pour les lancer :
- Ouvrez un terminal et tapez la commande `docker container run -it --rm -p 5000:5000 --name quiz-prod-api theovanrooij/quiz-prod-api`
- Ouvrez un nouveau terminal et tapez la commande `docker container run -it --rm -p 3000:80 --name quiz-prod-ui theovanrooij/quiz-prod-ui`

Vous pourrez ensuite accéder au site en vous rendant sur  [`localhost:3000`](localhost:3000).

## Comprendre les fichiers

L'architecture du projet peut se décrire par 3 grandes sous-parties que nous allons expliquer.

### API
Le dossier [`quiz-api`](https://github.com/theovanrooij/IT-5216E/tree/main/quiz-api) contient la partie API du projet (partie back-end). Vous pourrez notamment y trouver :
- le fichier [app.py](https://github.com/theovanrooij/IT-5216E/blob/main/quiz-api/app.py) qui permet de lancer l'application, faire la liaison avec la base de données et établir les différentes routes de notre site.
- le fichier [services.py](https://github.com/theovanrooij/IT-5216E/blob/main/quiz-api/services.py) qui contient l'ensemble des méthodes nécessaires pour insérer, extraire, supprimer et modifier les informations dans la base de données.
- le fichier [models.py](https://github.com/theovanrooij/IT-5216E/blob/main/quiz-api/models.py) contenant les classes Python associées à la base de données.
- le fichier [jwt_utils.py](https://github.com/theovanrooij/IT-5216E/blob/main/quiz-api/jwt_utils.py) qui permet de gérer la connexion au site pour la partie administrateur.

### Front
Le dossier [`quiz-ui`](https://github.com/theovanrooij/IT-5216E/tree/main/quiz-ui) contient la partie interface de notre site (partie front-end). Vous pourrez notamment y trouver :
- le fichier ['App.vue'](https://github.com/theovanrooij/IT-5216E/blob/main/quiz-ui/src/App.vue) qui contient les informations pour l'application web en général.
- le dossier [`views`](https://github.com/theovanrooij/IT-5216E/tree/main/quiz-ui/src/views) qui contient l'ensembles des vues pour des pages spécifiques.
- le dossier [`services`](https://github.com/theovanrooij/IT-5216E/tree/main/quiz-ui/src/services) qui permet de faire le lien avec les méthodes de l'API.
- le fichier [`router/index.js`](https://github.com/theovanrooij/IT-5216E/blob/main/quiz-ui/src/router/index.js) qui permet d'associer nos vues à des routes et ainsi à naviguer à travers différentes pages.

### Questions
Le dossier ['Questions'](https://github.com/theovanrooij/IT-5216E/tree/main/Questions) contient les éléments concernant les questions du site.
- le fichier [`randomizerquest.py`](https://github.com/theovanrooij/IT-5216E/blob/main/Questions/Drapeaux%20avec%20noms%20de%20pays/randomizerquest.py) nous a permis de générer nos questions, en prenant pour chaque question un drapeau de manière aléatoire parmis tous les drapeaux du dossier [`jpg`](https://github.com/theovanrooij/IT-5216E/tree/main/Questions/Drapeaux%20avec%20noms%20de%20pays/jpg).
- le fichier [`convertbase64.py`](https://github.com/theovanrooij/IT-5216E/blob/main/Questions/Drapeaux%20avec%20noms%20de%20pays/convertbase64.py) nous permet d'utiliser nos drapeaux en les convertissant du format `jpg` en base 64 en format `txt` dans le dossier [`base64`](https://github.com/theovanrooij/IT-5216E/tree/main/Questions/Drapeaux%20avec%20noms%20de%20pays/base64).
- le fichier [`Quiz Drapeau.postman_collection.json`](https://github.com/theovanrooij/IT-5216E/blob/main/Questions/Quiz%20Drapeau.postman_collection.json) contient une série de 10 questions à insérer, sous la forme d'une collection Postman.


## Utilisation du site web
Il est possible d'accéder à trois onglets principaux depuis notre barre de navigation :
- la page d'accueil : c'est ici où nous expliquons brièvement le Quiz et ses règles. Un bonton cliquable "Jouer" permettant de lancer le Quiz. Nous avons aussi un podium comportant les noms des trois visiteurs ayant produit les meilleurs scores, ainsi qu'une table repertoriant tous les visiteurs, leurs scores, leur position dans le classement ainsi que la date à laquelle ils ont effectué le quiz trié en fonction de leur score de manière descendante (les meilleurs scores sont tout en haut, et les moins bons se trouvent en dessous) ;
- la page du commencement de Quiz qui est accessible en cliquant sur DRAPQUIZ (ou Jouer depuis l'accueil) : c'est ici que le Quiz se lance, les visiteurs n'ont plus qu'à répondre aux questions et suivre son déroulé ;
- la page Admin : il est possible d'y accéder en rentrant le code 'flask2023'. À partir de cette page, nous pouvons modifier les questions et leurs réponses, ainsi que leur image et position. Il est possible de modifier et supprimer individuellement les questions, d'en ajouter, ou bien de supprimer toutes les questions ou supprimer toutes les participations.

