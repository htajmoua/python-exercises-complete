# Instructions - Encapsulation et Propriétés

L'encapsulation est un principe fondamental de la POO qui consiste à protéger les données d'une classe et contrôler leur accès.

## Concepts

**Attributs publics** : Accessibles partout (ex: `self.nom`)  
**Attributs protégés** : Convention `_nom` (usage interne mais accessible)  
**Attributs privés** : Convention `__nom` (name mangling par Python)  
**Properties** : Décorateur `@property` pour créer des getters/setters élégants

## Exercice 1 - Attributs protégés

**Créez** une classe `CompteBancaire` avec :
- Attributs protégés : `_titulaire`, `_solde`
- Constructeur qui initialise ces attributs
- Méthodes publiques : `deposer(montant)`, `retirer(montant)`, `consulter_solde()`
- **Validation** : ne pas permettre de retirer plus que le solde

**Testez** :
```python
compte = CompteBancaire("Alice", 1000)
compte.deposer(500)
compte.retirer(200)
print(compte.consulter_solde())  # 1300
compte.retirer(2000)  # Affiche un message d'erreur
```

## Exercice 2 - Getters et Setters manuels

**Créez** une classe `Temperature` avec :
- Attribut privé : `__celsius`
- Méthode `get_celsius()` : retourne la température
- Méthode `set_celsius(valeur)` : définit la température (validation : >= -273.15)
- Méthode `get_fahrenheit()` : retourne la conversion en Fahrenheit
- Méthode `set_fahrenheit(valeur)` : définit via Fahrenheit

**Formule** : F = C × 9/5 + 32

## Exercice 3 - Décorateur @property (basique)

**Créez** une classe `Personne` avec :
- Attribut protégé : `_age`
- `@property age` : getter qui retourne `_age`
- `@age.setter` : setter avec validation (0 <= age <= 150)

**Testez** :
```python
p = Personne()
p.age = 25  # Utilise le setter
print(p.age)  # Utilise le getter
p.age = -5  # Doit afficher une erreur
```

## Exercice 4 - Properties avec calculs

**Créez** une classe `Rectangle` avec :
- Attributs protégés : `_longueur`, `_largeur`
- Properties avec setters validés (valeurs > 0)
- Property `aire` (read-only, calculée automatiquement)
- Property `perimetre` (read-only, calculée automatiquement)

**Testez** :
```python
rect = Rectangle(5, 3)
print(rect.aire)  # 15
rect.longueur = 10
print(rect.aire)  # 30 (recalculé automatiquement)
```

## Exercice 5 - Validation complexe

**Créez** une classe `Email` avec :
- Attribut privé : `__adresse`
- `@property adresse` avec setter qui valide :
  - Contient un '@'
  - Contient un '.'
  - Pas d'espaces
  - Au moins 5 caractères
- Lève une `ValueError` si invalide

## Exercice 6 - Property read-only (calculée)

**Créez** une classe `Produit` avec :
- Attributs : `nom`, `prix_ht`, `tva` (0.20 par défaut)
- Property `prix_ttc` (read-only) : calcule automatiquement prix_ht × (1 + tva)

**Testez** :
```python
produit = Produit("Ordinateur", 1000)
print(produit.prix_ttc)  # 1200
produit.prix_ht = 1200
print(produit.prix_ttc)  # 1440 (recalculé)
```

## Exercice 7 - Encapsulation avec méthodes privées

**Créez** une classe `MotDePasse` avec :
- Attribut privé : `__hash`
- Méthode privée `__hasher(texte)` : simule un hash (inverser le texte)
- Méthode publique `definir(mdp)` : valide (8+ caractères) et hash
- Méthode publique `verifier(mdp)` : vérifie si le mdp correspond

## Exercice 8 - Propriété avec cache

**Créez** une classe `Calcul` avec :
- Attribut : `nombre`
- Attribut privé : `__cache_factorielle = None`
- Property `factorielle` qui :
  - Calcule la factorielle si pas en cache
  - Retourne le cache si déjà calculé
  - Invalide le cache quand `nombre` change

## Exercice 9 - Classe avec validation multiple

**Créez** une classe `Utilisateur` avec :
- Properties avec validation pour :
  - `nom` : 2-50 caractères, pas de chiffres
  - `age` : 13-120 ans
  - `email` : format valide
  - `telephone` : 10 chiffres exactement
- Méthode `afficher_profil()` : affiche toutes les infos

## Exercice 10 - Mini-projet : Classe Carte de crédit

**Créez** une classe `CarteBancaire` avec :
- Attributs privés : `__numero`, `__code`, `__solde`
- Properties :
  - `numero_masque` (read-only) : affiche "**** **** **** 1234"
  - `solde` : getter/setter avec validation (>= 0)
- Méthode `valider_code(code)` : vérifie le code
- Méthode `payer(montant, code)` : 
  - Vérifie le code
  - Vérifie le solde
  - Effectue le paiement

**Testez** avec un scénario complet.

## Exercices bonus

### Exercice 11 - Property avec délégation
**Créez** une classe `Voiture` avec :
- Attribut : `moteur` (objet d'une classe `Moteur`)
- Property `puissance` qui délègue à `moteur.puissance`

### Exercice 12 - Classe immuable
**Créez** une classe `Point` avec :
- Attributs privés : `__x`, `__y`
- Properties read-only pour x et y
- Méthode `deplacer(dx, dy)` qui retourne un **nouveau** Point
- Les coordonnées ne peuvent pas être modifiées après création

### Exercice 13 - Validation en chaîne
**Créez** une classe `FormulaireInscription` avec :
- Properties validées pour : nom, prenom, age, email, telephone
- Méthode `est_valide()` : retourne True si tous les champs sont valides
- Property `erreurs` : retourne la liste des erreurs de validation
