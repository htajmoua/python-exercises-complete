# Instructions  

## Exercices de base

1. **Créez** un **dictionnaire** appelé `notes` avec les clés `"Alice"`, `"Bob"` et `"Charlie"`, et respectivement les valeurs `15`, `12` et `18`.
2. **Ajoutez** la clé `"Diana"` avec la valeur `16` au dictionnaire `notes`.
3. **Accédez** à la valeur correspondant à la clé `"Bob"` et stockez-la dans une variable appelée `note_bob`.
4. **Modifiez** la valeur associée à la clé `"Alice"` pour `17` (elle a amélioré sa note).
5. **Supprimez** la clé `"Charlie"` du dictionnaire `notes` (utilisez `del` ou `.pop()`).
6. **Affichez** les **clés** restantes dans le dictionnaire (utilisez `.keys()`).

## Questions supplémentaires

7. **Affichez** toutes les **valeurs** du dictionnaire (utilisez `.values()`).
8. **Affichez** tous les **couples clé-valeur** (utilisez `.items()`).
9. **Vérifiez** si la clé `"Alice"` existe dans le dictionnaire (utilisez `in`) et affichez True ou False.
10. **Calculez** et affichez la **moyenne des notes** (somme des valeurs / nombre de valeurs).

## Question bonus

11. **Créez** un nouveau dictionnaire `commentaires` avec les mêmes clés que `notes` mais avec des valeurs textuelles (par exemple "Très bien", "Bien", etc.). Affichez ce dictionnaire.

## Dictionary Comprehension

12. **Créez** une liste `etudiants` contenant `["Emma", "Lucas", "Léa", "Hugo"]`.

13. À partir de la liste `etudiants`, **créez** un dictionnaire `absences` où chaque étudiant a `0` absence en utilisant une **dictionary comprehension**.
    - Exemple : `{"Emma": 0, "Lucas": 0, "Léa": 0, "Hugo": 0}`
    - Syntaxe : `{etudiant: 0 for etudiant in etudiants}`

14. À partir du dictionnaire `notes`, **créez** un nouveau dictionnaire `notes_sur_100` où chaque note est multipliée par 5 en utilisant une **dictionary comprehension**.
    - Exemple : si Alice a 17, elle aura 85 dans le nouveau dictionnaire

15. À partir du dictionnaire `notes`, **créez** un dictionnaire `reussite` contenant uniquement les étudiants ayant une note **supérieure ou égale à 15** en utilisant une **dictionary comprehension avec condition**.
    - Syntaxe : `{nom: note for nom, note in notes.items() if note >= 15}`

16. **Créez** un dictionnaire `carres_dict` contenant les nombres de 1 à 5 comme clés et leurs **carrés** comme valeurs en utilisant une **dictionary comprehension**.
    - Exemple : `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}`
    - Syntaxe : `{n: n**2 for n in range(1, 6)}`

17. À partir du dictionnaire `notes`, **créez** un dictionnaire `mentions` où :
    - Si note >= 16 : "Très bien"
    - Si note >= 14 : "Bien"
    - Sinon : "Assez bien"
    - Utilisez une **dictionary comprehension avec condition ternaire imbriquée**