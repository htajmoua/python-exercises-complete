# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Module 05 - Dictionnaires
Exercices sur les dictionnaires et dict comprehensions
"""

# ============= EXERCICES DE BASE =============

def exercice1_a_6():
    """Exercices 1 à 6 : Créer et manipuler un dictionnaire de notes"""
    # 1. Créez un dictionnaire `notes` avec les clés "Alice", "Bob" et "Charlie" 
    #    et les valeurs 15, 12 et 18
    
    
    # 2. Ajoutez la clé "Diana" avec la valeur 16 au dictionnaire `notes`
    
    
    # 3. Accédez à la valeur de "Bob" et stockez-la dans une variable `note_bob`
    
    
    # 4. Modifiez la valeur de "Alice" pour 17 (elle a amélioré sa note)
    
    
    # 5. Supprimez la clé "Charlie" du dictionnaire `notes` (utilisez del ou .pop())
    
    
    # 6. Affichez les clés restantes dans le dictionnaire (utilisez .keys())
    
    pass


# ============= QUESTIONS SUPPLÉMENTAIRES =============

def exercice7_a_10():
    """Exercices 7 à 10 : Parcourir et analyser le dictionnaire"""
    # Note: Reprenez le dictionnaire notes de l'exercice précédent
    
    # 7. Affichez toutes les valeurs du dictionnaire (utilisez .values())
    
    
    # 8. Affichez tous les couples clé-valeur (utilisez .items())
    
    
    # 9. Vérifiez si "Alice" existe dans le dictionnaire (utilisez in) et affichez True ou False
    
    
    # 10. Calculez et affichez la moyenne des notes (somme des valeurs / nombre de valeurs)
    
    pass


# ============= QUESTION BONUS =============

def exercice11_bonus():
    """Exercice 11 : Créer un dictionnaire de commentaires"""
    # Note: Reprenez le dictionnaire notes
    
    # 11. Créez un nouveau dictionnaire `commentaires` avec les mêmes clés que `notes` 
    #     mais avec des valeurs textuelles (ex: "Très bien", "Bien", etc.). Affichez ce dictionnaire.
    
    pass


# ============= DICTIONARY COMPREHENSION =============

def exercice12_a_17():
    """Exercices 12 à 17 : Dictionary comprehensions"""
    # 12. Créez une liste `etudiants` contenant ["Emma", "Lucas", "Léa", "Hugo"]
    
    
    # 13. Créez un dictionnaire `absences` où chaque étudiant a 0 absence 
    #     en utilisant une dictionary comprehension
    #     Exemple : {"Emma": 0, "Lucas": 0, "Léa": 0, "Hugo": 0}
    #     Syntaxe : {etudiant: 0 for etudiant in etudiants}
    
    
    # 14. Créez un dictionnaire `notes_sur_100` où chaque note est multipliée par 5
    #     en utilisant une dictionary comprehension
    
    
    # 15. Créez un dictionnaire `reussite` contenant uniquement les étudiants ayant une note >= 15
    #     en utilisant une dictionary comprehension avec condition
    #     Syntaxe : {nom: note for nom, note in notes.items() if note >= 15}
    
    
    # 16. Créez un dictionnaire `carres_dict` contenant les nombres de 1 à 5 comme clés 
    #     et leurs carrés comme valeurs en utilisant une dictionary comprehension
    #     Exemple : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    #     Syntaxe : {n: n**2 for n in range(1, 6)}
    
    
    # 17. Créez un dictionnaire `mentions` avec une condition ternaire imbriquée :
    #     - Si note >= 16 : "Très bien"
    #     - Si note >= 14 : "Bien"
    #     - Sinon : "Assez bien"
    
    pass


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Module 05 : Dictionnaires ===\n")
    
    # Décommentez pour tester vos fonctions :
    # exercice1_a_6()
    # exercice7_a_10()
    # exercice11_bonus()
    # exercice12_a_17()