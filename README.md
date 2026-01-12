# Dashboard Football - Projet Multidisciplinaire E3-FI

## Le projet

Ce dashboard interactif permet de visualiser les stats des 5 grands championnats européens de football sur la saison 2024-2025. L'idée est de pouvoir comparer les ligues, voir où sont les stades sur une carte, et analyser les performances des équipes.

Le projet a été développé pour le Projet Multidisciplinaire de E3-FI.

## Ce qui est possible

- **Consulter les classements** : on affiche le tableau de chaque ligue avec les stats classiques (victoires, nuls, défaites, buts, points...)
- **Visualiser les stades sur une carte** : grâce à OpenStreetMap, on peut voir où se trouvent les stades de chaque championnat, avec leur capacité.
- **Analyser les performances** : quelques graphiques pour voir les buts par journée, la comparaison domicile/extérieur et les meilleures attaques

## Les ligues disponibles

On couvre les 5 grands championnats :
- FR Ligue 1 (France)
- AN Premier League (Angleterre)
- DE Bundesliga (Allemagne)
- ES La Liga (Espagne)
- IT Serie A (Italie)

## Comment lancer le projet

#### Prérequis

Il faut avoir Python installé sur le PC.

### Installation

1. Cloner le repository ou télécharger les fichiers

2. Installer les dépendances :
```bash
pip install -r requirement.txt
```

3. Lancer l'application :
```bash
python main.py
```

4. Ouvrir ton navigateur à l'adresse `http://127.0.0.1:8050`

Et voilà, normalement le dashboard devrait s'afficher !

## Technologies utilisées

- **Dash** : pour créer le dashboard
- **Plotly** : pour les graphiques interactifs
- **Pandas** : pour la manipulation des données
- **OpenStreetMap** : pour afficher la carte des stades

## D'où viennent les données ?

On a récupéré les données de matchs sur GitHub. Ensuite on les a nettoyées et transformées en CSV pour pouvoir les exploiter. Les fichiers sources sont dans le dossier `data/raw/` et les versions clean dans `data/cleaned/`.

## Quelques difficultés rencontrées

- Le moyen de mettre en place la carte avec les marqueurs de taille variable selon la capacité des stades.
- Organisation du code pour garder le code maintenable.

## Améliorations possibles

- Mettre en place un système de prédiction de résultats.
- Intégrer les données en temps réel.

## Auteurs

- **Rémy Kouniali**
- **Noé Lautridou**