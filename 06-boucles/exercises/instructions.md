# Instructions - Boucles et Algorithmes

Ce module vous permettra de maîtriser les boucles `for` et `while` à travers des exercices algorithmiques.

## Exercices de base - Boucle FOR

1. **Créez** une boucle `for` qui affiche tous les nombres de 1 à 10.

2. **Créez** une boucle `for` qui affiche tous les nombres **pairs** de 0 à 20.

3. **Créez** une liste `prix = [19.99, 45.50, 12.75, 89.00, 5.25]` et utilisez une boucle `for` pour afficher chaque prix avec le message : `"Article : X euros"`

4. **Calculez** la somme de tous les nombres de 1 à 100 en utilisant une boucle `for`.
   - Initialisez une variable `somme = 0`
   - Ajoutez chaque nombre à la somme
   - Affichez le résultat final

## Exercices de base - Boucle WHILE

5. **Créez** une variable `compteur = 0` et utilisez une boucle `while` pour afficher les nombres de 0 à 5.

6. **Créez** un programme qui demande un nombre à l'utilisateur et continue de demander tant que le nombre n'est pas égal à 0.
   - Utilisez `input()` pour récupérer la saisie
   - Convertissez en `int()`
   - Affichez "Fin du programme" quand l'utilisateur entre 0

## Exercices algorithmiques

### Exercice 7 - Table de multiplication
**Créez** un programme qui affiche la table de multiplication de 7 (de 7×1 à 7×10).
- Format d'affichage : `"7 x 1 = 7"`

### Exercice 8 - Nombre premier
**Écrivez** un algorithme qui vérifie si un nombre donné est premier.
- Créez une variable `nombre = 29`
- Un nombre premier n'est divisible que par 1 et par lui-même
- Utilisez une boucle pour tester les diviseurs
- Affichez `"Le nombre X est premier"` ou `"Le nombre X n'est pas premier"`

### Exercice 9 - Factorielle
**Calculez** la factorielle d'un nombre.
- Créez une variable `n = 5`
- La factorielle de 5 est : 5 × 4 × 3 × 2 × 1 = 120
- Utilisez une boucle pour calculer le résultat
- Affichez : `"La factorielle de 5 est 120"`

### Exercice 10 - Suite de Fibonacci
**Générez** les 10 premiers nombres de la suite de Fibonacci.
- La suite commence par : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
- Chaque nombre est la somme des deux précédents
- Stockez les résultats dans une liste
- Affichez la liste complète

### Exercice 11 - Recherche dans une liste
**Créez** une liste `temperatures = [18, 22, 19, 25, 17, 30, 28, 21]`
- Trouvez et affichez la **température maximale**
- Trouvez et affichez la **température minimale**
- Calculez et affichez la **température moyenne**
- N'utilisez PAS les fonctions `max()`, `min()`, `sum()` - utilisez des boucles !

### Exercice 12 - Compter les occurrences
**Créez** une chaîne de caractères `texte = "Python est un langage de programmation"`
- Comptez combien de fois la lettre "a" apparaît (utilisez une boucle)
- Affichez le résultat

### Exercice 13 - Pyramide d'étoiles
**Créez** un programme qui affiche une pyramide d'étoiles de hauteur 5 :
```
*
**
***
****
*****
```
- Utilisez une boucle `for` et la multiplication de chaînes

## Exercices bonus

### Exercice 14 - Inversion de nombre
**Écrivez** un programme qui inverse un nombre.
- Exemple : 12345 devient 54321
- Utilisez une boucle `while` et les opérateurs modulo `%` et division entière `//`

### Exercice 15 - Nombres parfaits
**Trouvez** tous les nombres parfaits inférieurs à 1000.
- Un nombre parfait est égal à la somme de ses diviseurs (sauf lui-même)
- Exemple : 6 = 1 + 2 + 3 (donc 6 est parfait)
- Stockez les résultats dans une liste et affichez-la
