### Organisateur de notes dans un fichier .txt

## Problématique et explication

Comment automatiser le classement, la gestion et l’archivage de notes textuelles non structurées, afin d’éviter la dispersion d’informations et faciliter la consultation thématique ?

Dans un contexte personnel ou professionnel, nous notons souvent des idées, des tâches ou des rappels dans un fichier texte unique (liste de tâches, journal de bord, notes rapides).
Mais sans classement automatique :
- Les notes s’accumulent sans ordre,
- Les thèmes se mélangent,
- Il devient difficile de retrouver une information,
- Le risque de perdre des notes importantes ou de créer des doublons augmente.

## Objectif du projet

Créer un script Python qui :

- Classe automatiquement chaque note par thème,
- Génère un fichier .txt par thème,
- Range ces fichiers dans un sous-dossier dédié,
- Archive le fichier brut pour garder une trace datée,
- Et remet le fichier principal à zéro pour accueillir de nouvelles notes.

Ainsi, l’utilisateur peut ajouter des notes sans se soucier du tri, tout en gardant un historique organisé et facilement consultable.

## En une phrase

➜ Problématique résumée : "Comment automatiser le tri et l’archivage de mes notes pour passer d’un fichier unique désordonné à une structure thématique claire, sans perte d’informations ?"

## Consignes d'utilisation

Les notes doivent être prise dans le format: #Thème: description de la note. Comme exemple:

#travail: Préparer la présentation de vendredi.
#personnel: Acheter un cadeau pour l’anniversaire.
#études: Réviser le chapitre 4 de statistiques.
...

## Structure après exécution

notes_organizer/
│
├── my_notes.txt         # Fichier source : toutes les notes non triées
├── Sub_notes/           # Dossier qui contiendra les notes par thème
│   ├── travail.txt
│   ├── personnel.txt
│   ├── études.txt
│   └── ... (autres thèmes)
├── Archives/            # Dossier qui stocke les sauvegardes datées de my_notes.txt
├── note_organizer.py         # Script Python principal
└── README.md            # Ce fichier


## Fonctionnalitées principales

1. Lecture et classification
- Parcourt my_notes.txt ligne par ligne.
- Identifie le thème grâce au # avant :.
- Regroupe chaque note dans un dictionnaire Python :
{ thème : [liste des notes] }

2. Organisation par thème
- Pour chaque thème :
    - Crée un fichier <thème>.txt (exemple : travail.txt).
    - Ajoute toutes les notes correspondantes.
- Tous les fichiers de thème sont générés directement dans le dossier Sub_notes/.

3. Archivage automatique
Après avoir trié et déplacé les notes :
- Crée un dossier Archives/ (s’il n’existe pas).
- Renomme le my_notes.txt en my_notes_YYYYMMDD.txt (date du jour).
- Déplace ce fichier renommé dans Archives/.
- Crée un nouveau my_notes.txt vide prêt pour de nouvelles notes.

## Optimisation

- Ajouter une interface utilisateur pour saisir les notes directement.
- Créer une sauvegarde compressée (zip) des archives.
- Ajouter des logs pour suivre les opérations effectuées.
- Envoyer les notes organisées par email automatiquement.

### Auteur : Pierre Z.