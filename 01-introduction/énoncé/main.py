# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Module 01 - Introduction à Python
Exercices de base sur print, calculs et types de données
"""

# ============= EXERCICE 1 : AFFICHER DU TEXTE =============

def exercice1_hello_world():
    """Exercice 1 : Afficher 'Hello, World!'"""
    # À compléter
    print("Hello, World!")


def exercice2_mon_nom():
    """Exercice 2 : Afficher votre nom"""
    # À compléter
    nom = "Alice"
    print(f"Je m'appelle {nom}")


# ============= EXERCICE 2 : CALCULS SIMPLES =============

def exercice3_addition():
    """Exercice 3 : Additionner deux nombres"""
    # À compléter
    a = 5
    b = 3
    resultat = a + b
    print(f"{a} + {b} = {resultat}")


def exercice4_operations():
    """Exercice 4 : Toutes les opérations mathématiques"""
    # À compléter
    x = 10
    y = 3
    
    print(f"Addition: {x} + {y} = {x + y}")
    print(f"Soustraction: {x} - {y} = {x - y}")
    print(f"Multiplication: {x} * {y} = {x * y}")
    print(f"Division: {x} / {y} = {x / y}")
    print(f"Division entière: {x} // {y} = {x // y}")
    print(f"Modulo: {x} % {y} = {x % y}")
    print(f"Puissance: {x} ** {y} = {x ** y}")


# ============= EXERCICE 3 : CALCULATRICE SIMPLE =============

def exercice5_calculatrice():
    """Exercice 5 : Calculatrice avec input (optionnel)"""
    # À compléter
    # Décommentez pour tester avec input utilisateur
    # a = float(input("Premier nombre : "))
    # b = float(input("Deuxième nombre : "))
    # print(f"Somme : {a + b}")
    pass


# ============= EXERCICE 4 : AFFICHER PLUSIEURS LIGNES =============

def exercice6_plusieurs_lignes():
    """Exercice 6 : Afficher plusieurs lignes"""
    # À compléter
    print("Ligne 1")
    print("Ligne 2")
    print("Ligne 3")
    
    # Ou avec triple quotes
    print("""
    Ceci est un texte
    sur plusieurs lignes
    avec des sauts de ligne
    """)


# ============= EXERCICE 5 : COMMENTAIRES =============

def exercice7_commentaires():
    """Exercice 7 : Utiliser des commentaires"""
    # Ceci est un commentaire sur une ligne
    
    """
    Ceci est un commentaire
    sur plusieurs lignes
    (docstring)
    """
    
    x = 5  # Commentaire en fin de ligne
    print(x)


# ============= EXERCICES BONUS =============

def bonus_ascii_art():
    """Bonus : Créer un dessin ASCII"""
    # À compléter
    print("""
     /\\_/\\
    ( o.o )
     > ^ <
    """)


def bonus_table_multiplication():
    """Bonus : Table de multiplication de 5"""
    # À compléter
    n = 5
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def bonus_conversion_temperature():
    """Bonus : Convertir Celsius en Fahrenheit"""
    # À compléter
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Module 01 : Introduction à Python ===\n")
    
    print("--- Exercice 1 : Hello World ---")
    exercice1_hello_world()
    
    print("\n--- Exercice 2 : Mon nom ---")
    exercice2_mon_nom()
    
    print("\n--- Exercice 3 : Addition ---")
    exercice3_addition()
    
    print("\n--- Exercice 4 : Opérations ---")
    exercice4_operations()
    
    print("\n--- Exercice 6 : Plusieurs lignes ---")
    exercice6_plusieurs_lignes()
    
    print("\n--- Exercice 7 : Commentaires ---")
    exercice7_commentaires()
    
    print("\n=== EXERCICES BONUS ===")
    
    print("\n--- Bonus : ASCII Art ---")
    bonus_ascii_art()
    
    print("\n--- Bonus : Table de multiplication ---")
    bonus_table_multiplication()
    
    print("\n--- Bonus : Conversion température ---")
    bonus_conversion_temperature()
    
    print("\n✅ Tous les exercices sont terminés !")
    print("Consultez instructions.md pour plus de détails.")