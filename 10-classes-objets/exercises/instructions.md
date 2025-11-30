# Instructions - Classes et Objets

Bienvenue dans le monde de la Programmation Orientée Objet (POO) ! Ce module vous introduira aux concepts fondamentaux des classes et objets en Python.

## Concepts de base

**Classe** : Un modèle/plan pour créer des objets  
**Objet** : Une instance d'une classe  
**Attribut** : Une variable appartenant à un objet  
**Méthode** : Une fonction appartenant à une classe

## Exercice 1 - Première classe simple

**Créez** une classe `Personne` avec :
- Attributs : `nom`, `age`
- Une méthode `se_presenter()` qui affiche : `"Bonjour, je m'appelle {nom} et j'ai {age} ans."`

**Testez** :
```python
personne1 = Personne("Alice", 25)
personne1.se_presenter()
# Affiche : "Bonjour, je m'appelle Alice et j'ai 25 ans."
```

## Exercice 2 - Constructeur __init__

**Créez** une classe `Livre` avec :
- Constructeur `__init__(self, titre, auteur, pages)`
- Méthode `afficher_info()` qui affiche toutes les informations du livre

**Testez** :
```python
livre1 = Livre("1984", "George Orwell", 328)
livre1.afficher_info()
```

## Exercice 3 - Méthodes avec calculs

**Créez** une classe `Rectangle` avec :
- Attributs : `longueur`, `largeur`
- Méthode `calculer_aire()` qui retourne l'aire
- Méthode `calculer_perimetre()` qui retourne le périmètre
- Méthode `est_carre()` qui retourne `True` si c'est un carré

**Testez** :
```python
rect = Rectangle(5, 3)
print(rect.calculer_aire())  # 15
print(rect.calculer_perimetre())  # 16
print(rect.est_carre())  # False
```

## Exercice 4 - Attributs de classe vs instance

**Créez** une classe `CompteBancaire` avec :
- Attribut de classe : `taux_interet = 0.03` (3%)
- Attributs d'instance : `titulaire`, `solde`
- Méthode `deposer(montant)` : ajoute au solde
- Méthode `retirer(montant)` : retire du solde si suffisant
- Méthode `appliquer_interets()` : ajoute les intérêts au solde
- Méthode `afficher_solde()` : affiche le solde actuel

**Testez** :
```python
compte = CompteBancaire("Alice", 1000)
compte.deposer(500)
compte.retirer(200)
compte.appliquer_interets()
compte.afficher_solde()
```

## Exercice 5 - Plusieurs instances

**Créez** une classe `Voiture` avec :
- Attributs : `marque`, `modele`, `annee`, `kilometrage`
- Méthode `rouler(distance)` : ajoute la distance au kilométrage
- Méthode `afficher_info()` : affiche toutes les infos

**Créez** 3 voitures différentes et faites-les rouler.

## Exercice 6 - Liste d'objets

**Créez** une classe `Etudiant` avec :
- Attributs : `nom`, `notes` (liste de notes)
- Méthode `ajouter_note(note)` : ajoute une note
- Méthode `calculer_moyenne()` : retourne la moyenne des notes
- Méthode `obtenir_mention()` : retourne la mention selon la moyenne

**Créez** une liste de 5 étudiants et affichez leurs moyennes.

## Exercice 7 - Méthode __str__

**Créez** une classe `Produit` avec :
- Attributs : `nom`, `prix`, `quantite`
- Méthode `__str__()` pour affichage formaté
- Méthode `valeur_stock()` : retourne prix × quantité
- Méthode `vendre(quantite)` : diminue le stock

**Testez** avec `print(produit)` pour voir le `__str__` en action.

## Exercice 8 - Compteur d'instances

**Créez** une classe `Robot` avec :
- Attribut de classe `nombre_robots = 0`
- Attributs d'instance : `nom`, `energie` (100 par défaut)
- Dans `__init__`, incrémenter `nombre_robots`
- Méthode de classe `afficher_population()` : affiche le nombre total de robots
- Méthode `recharger()` : remet l'énergie à 100
- Méthode `travailler()` : diminue l'énergie de 20

**Créez** plusieurs robots et vérifiez le compteur.

## Exercice 9 - Interactions entre objets

**Créez** une classe `Joueur` avec :
- Attributs : `nom`, `points_vie`, `force`
- Méthode `attaquer(autre_joueur)` : enlève `force` points de vie à l'autre joueur
- Méthode `est_vivant()` : retourne `True` si points_vie > 0

**Créez** 2 joueurs et simulez un combat tour par tour.

## Exercice 10 - Mini-projet : Gestion de tâches

**Créez** une classe `Tache` avec :
- Attributs : `titre`, `description`, `terminee` (False par défaut)
- Méthode `marquer_terminee()` : passe `terminee` à True
- Méthode `afficher()` : affiche les infos avec statut

**Créez** une classe `GestionnaireTaches` avec :
- Attribut : `taches` (liste)
- Méthode `ajouter_tache(tache)` : ajoute une tâche
- Méthode `afficher_toutes()` : affiche toutes les tâches
- Méthode `afficher_en_cours()` : affiche les tâches non terminées
- Méthode `nombre_terminees()` : retourne le nombre de tâches terminées

**Testez** avec un scénario complet.

## Exercices bonus

### Exercice 11 - Classe Cercle
**Créez** une classe `Cercle` avec :
- Attribut : `rayon`
- Attribut de classe : `PI = 3.14159`
- Méthode `calculer_aire()`
- Méthode `calculer_circonference()`
- Méthode `__str__()`

### Exercice 12 - Classe Date
**Créez** une classe `Date` avec :
- Attributs : `jour`, `mois`, `annee`
- Méthode `est_bissextile()` : vérifie si l'année est bissextile
- Méthode `afficher_format_fr()` : affiche "JJ/MM/AAAA"
- Méthode `afficher_format_texte()` : affiche "1 janvier 2024"
