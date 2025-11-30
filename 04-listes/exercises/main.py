# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Module 04 - Listes
Exercices sur les listes et list comprehensions
"""

# ============= EXERCICES DE BASE =============

def exercice1_a_7():
    """Exercices 1 à 7 : Créer et manipuler une liste de langages"""
    # 1. Créez une liste nommée `langages` contenant ["Python", "JavaScript", "Java"]
    
    
    # 2. Ajoutez "Ruby" à la liste `langages` (utilisez append)
    
    
    # 3. Supprimez "Java" de la liste `langages` (utilisez remove)
    
    
    # 4. Modifiez le premier élément de la liste `langages` en "C++"
    
    
    # 5. Affichez la longueur de la liste `langages` avec len()
    
    
    # 6. Triez la liste `langages` par ordre alphabétique (utilisez sort)
    
    
    # 7. Affichez la liste complète
    
    pass


# ============= QUESTIONS SUPPLÉMENTAIRES =============

def exercice8_a_11():
    """Exercices 8 à 11 : Opérations avancées sur les listes"""
    # Note: Reprenez la liste langages de l'exercice précédent
    
    # 8. Ajoutez "Go" au début de la liste (utilisez insert avec l'index 0)
    
    
    # 9. Affichez le dernier élément de la liste (utilisez l'index -1)
    
    
    # 10. Créez une nouvelle liste `langages_web` contenant ["HTML", "CSS"] 
    #     et fusionnez-la avec `langages` (utilisez l'opérateur +). Affichez le résultat.
    
    
    # 11. Vérifiez si "Python" est dans la liste (utilisez l'opérateur in) et affichez True ou False
    
    pass


# ============= QUESTION BONUS =============

def exercice12_bonus():
    """Exercice 12 : Inverser une liste"""
    # Note: Reprenez la liste langages
    
    # 12. Inversez l'ordre de la liste `langages` (utilisez reverse) et affichez la liste inversée
    
    pass


# ============= LIST COMPREHENSION =============

def exercice13_a_17():
    """Exercices 13 à 17 : List comprehensions"""
    # 13. Créez une liste `nombres` contenant les nombres de 1 à 10 
    #     (utilisez range(1, 11) et convertissez en liste)
    
    
    # 14. Créez une liste `carres` contenant les carrés de chaque nombre en utilisant une list comprehension
    #     Exemple : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
    
    # 15. Créez une liste `pairs` contenant uniquement les nombres pairs en utilisant une list comprehension avec condition
    #     Exemple : [2, 4, 6, 8, 10]
    
    
    # 16. Créez une liste `langages_majuscules` contenant tous les langages en majuscules 
    #     en utilisant une list comprehension (utilisez .upper())
    
    
    # 17. Créez une liste `labels` qui contient "pair" si le nombre est pair, "impair" sinon
    #     Utilisez une list comprehension avec condition ternaire : ["pair" if n % 2 == 0 else "impair" for n in nombres]
    
    pass


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Module 04 : Listes ===\n")
    
    # Décommentez pour tester vos fonctions :
    # exercice1_a_7()
    # exercice8_a_11()
    # exercice12_bonus()
    # exercice13_a_17()