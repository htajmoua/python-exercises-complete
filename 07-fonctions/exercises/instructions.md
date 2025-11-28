# Instructions - Fonctions et Algorithmes

Ce module vous permettra de maîtriser les fonctions en Python à travers des exercices algorithmiques.

## Exercices de base

### Exercice 1 - Fonction simple
**Créez** une fonction `dire_bonjour(nom)` qui :
- Prend un nom en paramètre
- Retourne la chaîne `"Bonjour, {nom} !"`
- Testez la fonction avec plusieurs noms

### Exercice 2 - Fonction avec calcul
**Créez** une fonction `calculer_aire_rectangle(longueur, largeur)` qui :
- Prend deux paramètres : longueur et largeur
- Retourne l'aire du rectangle (longueur × largeur)
- Testez avec `calculer_aire_rectangle(5, 3)` → doit retourner 15

### Exercice 3 - Fonction avec valeur par défaut
**Créez** une fonction `calculer_prix_ttc(prix_ht, tva=0.20)` qui :
- Prend le prix HT en paramètre obligatoire
- Prend le taux de TVA en paramètre optionnel (par défaut 20%)
- Retourne le prix TTC : `prix_ht * (1 + tva)`
- Testez avec et sans le paramètre tva

### Exercice 4 - Fonction avec conditions
**Créez** une fonction `determiner_mention(note)` qui :
- Prend une note sur 20 en paramètre
- Retourne :
  - "Très bien" si note >= 16
  - "Bien" si note >= 14
  - "Assez bien" si note >= 12
  - "Passable" si note >= 10
  - "Insuffisant" si note < 10

## Exercices algorithmiques

### Exercice 5 - Nombre pair ou impair
**Créez** une fonction `est_pair(nombre)` qui :
- Prend un nombre en paramètre
- Retourne `True` si le nombre est pair, `False` sinon
- Utilisez l'opérateur modulo `%`

### Exercice 6 - Maximum de trois nombres
**Créez** une fonction `max_trois(a, b, c)` qui :
- Prend trois nombres en paramètres
- Retourne le plus grand des trois
- N'utilisez PAS la fonction `max()` intégrée

### Exercice 7 - Factorielle (récursif)
**Créez** une fonction **récursive** `factorielle(n)` qui :
- Prend un nombre entier n en paramètre
- Retourne la factorielle de n
- Cas de base : si n == 0 ou n == 1, retourner 1
- Cas récursif : retourner n × factorielle(n-1)

### Exercice 8 - Compter les voyelles
**Créez** une fonction `compter_voyelles(texte)` qui :
- Prend une chaîne de caractères en paramètre
- Retourne le nombre de voyelles (a, e, i, o, u, y) dans le texte
- Ignorez la casse (majuscules/minuscules)

### Exercice 9 - Nombre premier
**Créez** une fonction `est_premier(nombre)` qui :
- Prend un nombre entier en paramètre
- Retourne `True` si le nombre est premier, `False` sinon
- Un nombre premier est divisible uniquement par 1 et par lui-même

### Exercice 10 - Somme des chiffres
**Créez** une fonction `somme_chiffres(nombre)` qui :
- Prend un nombre entier en paramètre
- Retourne la somme de ses chiffres
- Exemple : `somme_chiffres(1234)` → retourne 10 (1+2+3+4)

### Exercice 11 - Palindrome
**Créez** une fonction `est_palindrome(texte)` qui :
- Prend une chaîne de caractères en paramètre
- Retourne `True` si c'est un palindrome, `False` sinon
- Un palindrome se lit de la même façon dans les deux sens
- Exemples : "radar", "kayak", "été"
- Ignorez les espaces et la casse

### Exercice 12 - FizzBuzz
**Créez** une fonction `fizzbuzz(n)` qui :
- Prend un nombre n en paramètre
- Retourne une liste des nombres de 1 à n avec les règles suivantes :
  - Si le nombre est divisible par 3 : remplacer par "Fizz"
  - Si le nombre est divisible par 5 : remplacer par "Buzz"
  - Si divisible par 3 ET 5 : remplacer par "FizzBuzz"
  - Sinon : garder le nombre
- Exemple : `fizzbuzz(15)` → `[1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]`

### Exercice 13 - Tri à bulles
**Créez** une fonction `tri_bulles(liste)` qui :
- Prend une liste de nombres en paramètre
- Retourne la liste triée en ordre croissant
- Implémentez l'algorithme du tri à bulles :
  - Comparez les éléments adjacents
  - Échangez-les s'ils sont dans le mauvais ordre
  - Répétez jusqu'à ce que la liste soit triée

### Exercice 14 - PGCD (Plus Grand Commun Diviseur)
**Créez** une fonction `pgcd(a, b)` qui :
- Prend deux nombres entiers en paramètres
- Retourne leur PGCD en utilisant l'algorithme d'Euclide :
  - Tant que b ≠ 0 :
    - temp = b
    - b = a % b
    - a = temp
  - Retourner a

## Exercices bonus

### Exercice 15 - Anagrammes
**Créez** une fonction `sont_anagrammes(mot1, mot2)` qui :
- Prend deux mots en paramètres
- Retourne `True` s'ils sont des anagrammes, `False` sinon
- Deux mots sont anagrammes s'ils contiennent les mêmes lettres dans un ordre différent
- Exemples : "chien" et "niche", "écouter" et "écrouté"

### Exercice 16 - Suite de Fibonacci (récursif avec mémoïsation)
**Créez** une fonction `fibonacci_memo(n, memo={})` qui :
- Calcule le n-ième nombre de Fibonacci de manière récursive
- Utilise la mémoïsation pour optimiser les calculs
- Retourne le résultat

### Exercice 17 - Conversion nombre en texte
**Créez** une fonction `nombre_en_texte(n)` qui :
- Prend un nombre de 0 à 99 en paramètre
- Retourne sa représentation en texte français
- Exemples : 
  - `nombre_en_texte(42)` → "quarante-deux"
  - `nombre_en_texte(75)` → "soixante-quinze"
  - `nombre_en_texte(17)` → "dix-sept"
