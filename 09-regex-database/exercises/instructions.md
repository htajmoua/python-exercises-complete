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
**✅ CODE FOURNI** - La fonction `creer_tables()` est déjà implémentée.

Elle crée une base de données SQLite `bibliotheque.db` avec 3 tables :

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
**✅ CODE FOURNI** - La fonction `inserer_donnees_exemple()` est déjà implémentée.

Elle insère des données d'exemple dans les tables :
- **7 auteurs** : Hugo, Camus, Rowling, Orwell, Saint-Exupéry, Dumas, Zola
- **14 livres** : Variété de romans, fantasy, dystopie, contes, etc.
- **7 emprunts** : 4 en cours, 3 retournés

**Pour initialiser la base de données :**
```python
# Décommentez dans main.py :
test_database()
```

Consultez `README_DB.md` pour voir toutes les données insérées.

### Exercice 8 : Requêtes SELECT
**📝 TEMPLATES FOURNIS** - Des templates commentés sont disponibles dans le code.

Implémentez les fonctions suivantes :

1. **`afficher_tous_livres()`** - Afficher tous les livres
   - Template : `SELECT * FROM livres`

2. **`livres_par_auteur(auteur_id)`** - Livres d'un auteur spécifique
   - Template : `SELECT * FROM livres WHERE auteur_id = ?`

3. **`livres_apres_annee(annee)`** - Livres publiés après une année
   - Template : `SELECT * FROM livres WHERE annee_publication > ?`

4. **`emprunts_en_cours()`** - Emprunts actuellement en cours
   - Template : `SELECT * FROM emprunts WHERE statut = ?`

💡 **Conseil :** Décommentez les templates dans `main.py` et adaptez-les.

### Exercice 9 : Jointures
**📝 TEMPLATES FOURNIS** - Des templates commentés sont disponibles dans le code.

Implémentez les fonctions suivantes :

1. **`livres_avec_auteurs()`** - Livres avec le nom de leur auteur
   - Template : Jointure simple entre `livres` et `auteurs`
   ```python
   SELECT livres.titre, auteurs.nom, auteurs.prenom
   FROM livres
   JOIN auteurs ON livres.auteur_id = auteurs.id
   ```

2. **`emprunts_avec_details()`** - Emprunts avec détails complets
   - Template : Double jointure `emprunts` → `livres` → `auteurs`
   ```python
   SELECT emprunts.emprunteur, livres.titre, auteurs.nom
   FROM emprunts
   JOIN livres ON emprunts.livre_id = livres.id
   JOIN auteurs ON livres.auteur_id = auteurs.id
   ```

💡 **Conseil :** Les templates complets sont dans `main.py`. Consultez aussi `SOLUTION_EXERCICES_8_9.md` après vos tentatives.

---

## Partie 3 : Combinaison Regex et Base de Données

### Exercice 10 : Recherche avancée avec regex
Implémentez des fonctions de recherche qui utilisent les expressions régulières pour filtrer les résultats de la base de données.

**Objectif :** Combiner SQL et regex Python pour des recherches puissantes et flexibles.

#### Fonction 1 : Rechercher des livres par pattern
```python
def rechercher_livres_par_titre(self, pattern):
    """
    Recherche des livres dont le titre correspond à un pattern regex
    Pattern fourni : r'harry.*potter' pour trouver tous les Harry Potter
    """
    pass
```

#### Fonction 2 : Rechercher des auteurs par nationalité
```python
def rechercher_auteurs_par_pays(self, pattern_pays):
    """
    Recherche des auteurs selon un pattern de nationalité
    Pattern fourni : r'Fran[cç]ais[e]?' pour Français/Française
    """
    pass
```

#### Fonction 3 : Filtrer les emprunts par date
```python
def emprunts_par_periode(self, pattern_date):
    """
    Trouve les emprunts selon un pattern de date
    Pattern fourni : r'2024-11-.*' pour novembre 2024
    """
    pass
```

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
