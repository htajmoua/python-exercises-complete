# Module 09 - Expressions Régulières et Bases de Données

## Objectifs
- Maîtriser les expressions régulières (regex) en Python
- Comprendre le module `re`
- Manipuler une base de données SQLite
- Effectuer des opérations CRUD (Create, Read, Update, Delete)
- Combiner regex et bases de données dans un projet pratique

---

## Partie 1 : Expressions Régulières (Regex)

### Exercice 1 : Introduction aux regex
Créez des fonctions pour valider :
- Une adresse email
- Un numéro de téléphone français (format: 06 12 34 56 78 ou 06-12-34-56-78)
- Un code postal français (5 chiffres)
- Une date au format JJ/MM/AAAA

**Exemple :**
```python
import re

def valider_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Test
print(valider_email("alice@example.com"))  # True
print(valider_email("invalid.email"))       # False
```

### Exercice 2 : Recherche et extraction
À partir d'un texte contenant plusieurs emails et numéros de téléphone, extrayez :
- Tous les emails
- Tous les numéros de téléphone
- Toutes les URLs

**Exemple de texte :**
```
Contactez-nous sur contact@entreprise.fr ou au 01 23 45 67 89.
Notre site : https://www.entreprise.fr
Support : support@entreprise.com - Tél : 06-12-34-56-78
```

### Exercice 3 : Remplacement avec regex
Écrivez des fonctions pour :
- Masquer les numéros de carte bancaire (garder les 4 derniers chiffres)
  - `1234 5678 9012 3456` → `**** **** **** 3456`
- Nettoyer un texte en supprimant les caractères spéciaux
- Remplacer toutes les dates au format JJ/MM/AAAA par le format AAAA-MM-JJ

### Exercice 4 : Validation de mots de passe
Créez une fonction qui vérifie qu'un mot de passe contient :
- Au moins 8 caractères
- Au moins une majuscule
- Au moins une minuscule
- Au moins un chiffre
- Au moins un caractère spécial (@, #, $, %, etc.)

### Exercice 5 : Parsing de logs
Analysez un fichier de logs au format :
```
[2024-01-15 14:30:25] INFO: User alice logged in from 192.168.1.10
[2024-01-15 14:35:42] ERROR: Failed login attempt for user bob
[2024-01-15 14:40:18] WARNING: High memory usage detected
```

Extrayez :
- La date et l'heure
- Le niveau (INFO, ERROR, WARNING)
- Le message
- Les adresses IP mentionnées

---

## Partie 2 : Base de Données SQLite

### Exercice 6 : Créer une base de données
Créez une base de données SQLite `bibliotheque.db` avec 3 tables :

**Table `auteurs` :**
- id (INTEGER PRIMARY KEY AUTOINCREMENT)
- nom (TEXT NOT NULL)
- prenom (TEXT NOT NULL)
- date_naissance (TEXT)
- nationalite (TEXT)

**Table `livres` :**
- id (INTEGER PRIMARY KEY AUTOINCREMENT)
- titre (TEXT NOT NULL)
- auteur_id (INTEGER, FOREIGN KEY vers auteurs)
- annee_publication (INTEGER)
- isbn (TEXT UNIQUE)
- genre (TEXT)

**Table `emprunts` :**
- id (INTEGER PRIMARY KEY AUTOINCREMENT)
- livre_id (INTEGER, FOREIGN KEY vers livres)
- emprunteur (TEXT NOT NULL)
- date_emprunt (TEXT NOT NULL)
- date_retour (TEXT)
- statut (TEXT DEFAULT 'en_cours')

### Exercice 7 : Insérer des données
Ajoutez des données dans les tables :
- Au moins 5 auteurs
- Au moins 10 livres
- Au moins 5 emprunts

**Exemple :**
```python
import sqlite3

conn = sqlite3.connect('bibliotheque.db')
cursor = conn.cursor()

# Insérer un auteur
cursor.execute('''
    INSERT INTO auteurs (nom, prenom, nationalite)
    VALUES (?, ?, ?)
''', ('Hugo', 'Victor', 'Française'))

conn.commit()
conn.close()
```

### Exercice 8 : Requêtes SELECT
Écrivez des requêtes pour :
- Afficher tous les livres
- Afficher tous les livres d'un auteur spécifique
- Afficher les livres publiés après 2000
- Afficher les emprunts en cours
- Afficher les livres les plus empruntés

### Exercice 9 : Jointures
Créez des requêtes avec JOIN pour :
- Afficher tous les livres avec le nom de leur auteur
- Afficher tous les emprunts avec les titres des livres
- Afficher les auteurs qui ont des livres actuellement empruntés

**Exemple :**
```python
cursor.execute('''
    SELECT livres.titre, auteurs.nom, auteurs.prenom
    FROM livres
    JOIN auteurs ON livres.auteur_id = auteurs.id
''')
```

### Exercice 10 : UPDATE et DELETE
Implémentez des fonctions pour :
- Mettre à jour le statut d'un emprunt (retourné)
- Supprimer un livre
- Modifier les informations d'un auteur

---

## Partie 3 : Projet Complet - Système de Gestion

### Exercice 11 : Application CLI complète
Créez une application en ligne de commande qui permet de :

**Menu principal :**
```
=== Gestion de Bibliothèque ===
1. Ajouter un auteur
2. Ajouter un livre
3. Rechercher un livre (avec regex)
4. Emprunter un livre
5. Retourner un livre
6. Afficher les statistiques
7. Exporter les données (CSV)
8. Quitter
```

**Fonctionnalités :**
- Validation des entrées avec regex (email, ISBN, dates)
- Recherche de livres par titre, auteur, genre (avec regex)
- Gestion complète des emprunts
- Statistiques (nombre de livres, auteurs, emprunts en cours)

### Exercice 12 : Recherche avancée avec regex
Implémentez une fonction de recherche qui accepte :
- Recherche par pattern regex dans les titres
- Recherche floue (ignorer la casse, accents)
- Recherche multi-critères (titre + auteur + genre)

**Exemple :**
```python
def rechercher_livres(pattern, champ='titre'):
    """
    Recherche des livres avec une expression régulière
    
    Args:
        pattern: Expression régulière à rechercher
        champ: 'titre', 'auteur', ou 'genre'
    
    Returns:
        Liste de livres correspondants
    """
    # À implémenter
    pass
```

### Exercice 13 : Import de données avec validation
Créez une fonction qui importe des livres depuis un fichier texte et valide :
- Format ISBN avec regex
- Format de date
- Validation des données avant insertion

**Format du fichier :**
```
Titre: Le Petit Prince
Auteur: Antoine de Saint-Exupéry
ISBN: 978-2-07-061275-8
Année: 1943
Genre: Fiction

Titre: 1984
Auteur: George Orwell
ISBN: 978-0-452-28423-4
Année: 1949
Genre: Dystopie
```

### Exercice 14 : Logging et audit
Ajoutez une table `logs` pour tracer toutes les opérations :
- Date et heure de l'opération
- Type d'opération (INSERT, UPDATE, DELETE)
- Table concernée
- Utilisateur (si applicable)

Utilisez regex pour parser et analyser les logs.

### Exercice 15 : Sauvegarde et restauration
Implémentez :
- Export de la base en SQL
- Export des données en JSON
- Import depuis JSON avec validation regex
- Vérification d'intégrité des données

---

## Bonus : Défis avancés

### Défi 1 : Validation complexe d'ISBN
L'ISBN-13 a une formule de validation (checksum). Implémentez la validation complète.

### Défi 2 : Recherche full-text
Utilisez FTS5 (Full-Text Search) de SQLite pour une recherche rapide.

### Défi 3 : Migration de données
Créez un script qui migre les données d'une ancienne structure vers la nouvelle.

### Défi 4 : API REST
Créez une petite API Flask qui expose les opérations de la base de données.

---

## Ressources

### Regex
- Documentation Python `re` : https://docs.python.org/3/library/re.html
- Regex101 (tester vos regex) : https://regex101.com/
- Cheat sheet regex : https://www.rexegg.com/regex-quickstart.html

### SQLite
- Documentation Python `sqlite3` : https://docs.python.org/3/library/sqlite3.html
- SQLite Tutorial : https://www.sqlitetutorial.net/
- DB Browser for SQLite : https://sqlitebrowser.org/

---

## Critères d'évaluation
-  Validation correcte avec regex
-  Structure de base de données cohérente
-  Gestion des erreurs (try/except)
-  Code propre et commenté
-  Utilisation de fonctions réutilisables
-  Tests des fonctionnalités principales
-  Documentation des regex complexes

**Bon courage !** 
