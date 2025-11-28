# Instructions  

## Exercices de base

1. **Créez** une liste nommée `langages` contenant les éléments `"Python"`, `"JavaScript"` et `"Java"`.
2. **Ajoutez** `"Ruby"` à la liste `langages` (utilisez la méthode `append`).
3. **Supprimez** `"Java"` de la liste `langages` (utilisez la méthode `remove`).
4. **Modifiez** le **premier** élément de la liste `langages` en `"C++"`.
5. **Affichez** la **longueur** de la liste `langages` avec `len()`.
6. **Triez** la liste `langages` par ordre alphabétique (utilisez la méthode `sort`).
7. **Affichez** la liste complète.

## Questions supplémentaires

8. **Ajoutez** `"Go"` au **début** de la liste (utilisez `insert` avec l'index 0).
9. **Affichez** le **dernier** élément de la liste (utilisez l'index -1).
10. **Créez** une nouvelle liste `langages_web` contenant `["HTML", "CSS"]` et **fusionnez-la** avec la liste `langages` (utilisez l'opérateur `+`). Affichez le résultat.
11. **Vérifiez** si `"Python"` est dans la liste (utilisez l'opérateur `in`) et affichez True ou False.

## Question bonus

12. **Inversez** l'ordre de la liste `langages` (utilisez la méthode `reverse`) et affichez la liste inversée.

## List Comprehension

13. **Créez** une liste `nombres` contenant les nombres de 1 à 10 (utilisez `range(1, 11)` et convertissez en liste).

14. À partir de la liste `nombres`, **créez** une nouvelle liste `carres` contenant les **carrés** de chaque nombre en utilisant une **list comprehension**.
    - Exemple : `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`

15. À partir de la liste `nombres`, **créez** une nouvelle liste `pairs` contenant uniquement les **nombres pairs** en utilisant une **list comprehension avec condition**.
    - Exemple : `[2, 4, 6, 8, 10]`

16. **Créez** une liste `langages_majuscules` contenant tous les langages de la liste `langages` en **majuscules** en utilisant une **list comprehension**.
    - Utilisez la méthode `.upper()` sur chaque élément

17. À partir de la liste `nombres`, **créez** une liste `labels` qui contient :
    - `"pair"` si le nombre est pair
    - `"impair"` si le nombre est impair
    - Utilisez une **list comprehension avec condition ternaire** : `["pair" if n % 2 == 0 else "impair" for n in nombres]`