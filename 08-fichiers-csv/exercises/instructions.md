# Contexte

Supposons que vous soyez un **bibliothécaire** et que vous deviez **créer un fichier** contenant les informations sur les livres empruntés. Nous allons lire dans un fichier **CSV** les titres des livres et le nombre de jours d'emprunt, puis **créer** un autre **fichier CSV** avec les *frais de retard calculés*.

# Instructions  

## Exercices de base

1. **Écrivez** un script pour lire le contenu du fichier `input.csv` au format suivant :

| titre                | jours_emprunt |
| -------------------- | :-----------: |
| Le Petit Prince      |    **21**     |
| 1984                 |    **35**     |
| L'Étranger           |    **14**     |

**Conseil** : Créez une fonction `extract()` qui retourne les données du fichier `input.csv`

2. **Créez** un nouveau fichier CSV appelé `output.csv` qui devrait avoir le format suivant :

* Les **frais de retard** sont calculés ainsi : 
  - Si `jours_emprunt <= 14` : frais = 0
  - Si `jours_emprunt > 14` : frais = (jours_emprunt - 14) × 0.50 euros par jour
  
*(Attention : les clés doivent être en minuscule pour que les tests passent)*

| titre                | frais   |
| -------------------- | :-----: |
| Le Petit Prince      | **3.5** |
| 1984                 | **10.5**|
| L'Étranger           | **0**   |

**Conseil** : Créez une fonction `transform()` qui sera responsable de la **transformation** des données et du calcul des frais. Ensuite, créez une fonction `load()` qui va charger les nouvelles données dans le fichier `output.csv`.

## Questions supplémentaires

3. **Ajoutez** une fonction `main()` qui orchestre les appels aux fonctions `extract()`, `transform()` et `load()`.

4. **Modifiez** la fonction `transform()` pour ajouter une colonne `"statut"` dans le fichier de sortie :
   - Si frais = 0 : statut = "À temps"
   - Si frais > 0 : statut = "En retard"

## Question bonus

5. Créez une fonction `statistiques()` qui lit le fichier `output.csv` et affiche :
   - Le nombre total de livres
   - Le montant total des frais
   - Le nombre de livres en retard