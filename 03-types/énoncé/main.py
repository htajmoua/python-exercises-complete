# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Module 03 - Types de Données
Exercices sur les strings, nombres, bool

éens et conversions de types
"""

# ============= EXERCICE 1 : STRINGS (CHAÎNES) =============

def exercice1_manipulation_strings():
    """Exercice 1 : Manipuler des chaînes de caractères"""
    # À compléter
    texte = "Python est génial"
    
    # Méthodes de base
    print(f"Texte : {texte}")
    print(f"Majuscules : {texte.upper()}")
    print(f"Minuscules : {texte.lower()}")
    print(f"Longueur : {len(texte)}")
    print(f"Commence par 'Python' : {texte.startswith('Python')}")
    print(f"Se termine par 'génial' : {texte.endswith('génial')}")


def exercice2_concatenation():
    """Exercice 2 : Concaténer des chaînes"""
    # À compléter
    prenom = "Alice"
    nom = "Dupont"
    
    # Différentes méthodes
    nom_complet1 = prenom + " " + nom
    nom_complet2 = f"{prenom} {nom}"
    nom_complet3 = " ".join([prenom, nom])
    
    print(nom_complet1)
    print(nom_complet2)
    print(nom_complet3)


def exercice3_slicing():
    """Exercice 3 : Découper des chaînes (slicing)"""
    # À compléter
    texte = "Python"
    
    print(f"Premier caractère : {texte[0]}")
    print(f"Dernier caractère : {texte[-1]}")
    print(f"3 premiers : {texte[:3]}")
    print(f"3 derniers : {texte[-3:]}")
    print(f"Du 2e au 4e : {texte[1:4]}")
    print(f"Inverse : {texte[::-1]}")


# ============= EXERCICE 2 : NOMBRES =============

def exercice4_operations_nombres():
    """Exercice 4 : Opérations sur les nombres"""
    # À compléter
    a = 10
    b = 3
    
    print(f"Addition : {a} + {b} = {a + b}")
    print(f"Soustraction : {a} - {b} = {a - b}")
    print(f"Multiplication : {a} * {b} = {a * b}")
    print(f"Division : {a} / {b} = {a / b:.2f}")
    print(f"Division entière : {a} // {b} = {a // b}")
    print(f"Modulo : {a} % {b} = {a % b}")
    print(f"Puissance : {a} ** {b} = {a ** b}")


def exercice5_fonctions_math():
    """Exercice 5 : Fonctions mathématiques"""
    # À compléter
    import math
    
    x = 16
    y = -5.7
    
    print(f"Racine carrée de {x} : {math.sqrt(x)}")
    print(f"Valeur absolue de {y} : {abs(y)}")
    print(f"Arrondi de {y} : {round(y)}")
    print(f"Plafond de {y} : {math.ceil(y)}")
    print(f"Plancher de {y} : {math.floor(y)}")
    print(f"Pi : {math.pi}")


# ============= EXERCICE 3 : BOOLÉENS =============

def exercice6_booleens():
    """Exercice 6 : Opérations booléennes"""
    # À compléter
    a = True
    b = False
    
    print(f"a = {a}, b = {b}")
    print(f"a AND b : {a and b}")
    print(f"a OR b : {a or b}")
    print(f"NOT a : {not a}")
    
    # Comparaisons
    x = 10
    y = 5
    print(f"\n{x} > {y} : {x > y}")
    print(f"{x} < {y} : {x < y}")
    print(f"{x} == {y} : {x == y}")
    print(f"{x} != {y} : {x != y}")


def exercice7_comparaisons():
    """Exercice 7 : Comparaisons avancées"""
    # À compléter
    age = 25
    
    # Conditions
    est_majeur = age >= 18
    est_senior = age >= 65
    
    print(f"Âge : {age}")
    print(f"Est majeur : {est_majeur}")
    print(f"Est senior : {est_senior}")
    
    # Comparaisons multiples
    est_adulte_actif = 18 <= age < 65
    print(f"Est adulte actif (18-64) : {est_adulte_actif}")


# ============= EXERCICE 4 : CONVERSIONS =============

def exercice8_conversions_types():
    """Exercice 8 : Convertir entre types"""
    # À compléter
    # String vers int
    age_str = "25"
    age_int = int(age_str)
    print(f"String '{age_str}' → int {age_int}")
    
    # Int vers string
    nombre = 42
    nombre_str = str(nombre)
    print(f"Int {nombre} → string '{nombre_str}'")
    
    # String vers float
    prix_str = "19.99"
    prix_float = float(prix_str)
    print(f"String '{prix_str}' → float {prix_float}")
    
    # Float vers int (troncature)
    decimal = 3.14
    entier = int(decimal)
    print(f"Float {decimal} → int {entier}")


def exercice9_conversions_avancees():
    """Exercice 9 : Conversions avancées"""
    # À compléter
    # Booléen vers int
    vrai = True
    faux = False
    print(f"True → int : {int(vrai)}")
    print(f"False → int : {int(faux)}")
    
    # Int vers booléen
    print(f"0 → bool : {bool(0)}")
    print(f"1 → bool : {bool(1)}")
    print(f"42 → bool : {bool(42)}")
    
    # String vers booléen
    print(f"'' (vide) → bool : {bool('')}")
    print(f"'hello' → bool : {bool('hello')}")


# ============= EXERCICE 5 : TYPE() ET ISINSTANCE() =============

def exercice10_verifier_types():
    """Exercice 10 : Vérifier les types de données"""
    # À compléter
    variables = [
        42,
        3.14,
        "hello",
        True,
        [1, 2, 3],
        {"nom": "Alice"}
    ]
    
    for var in variables:
        print(f"{var} est de type {type(var).__name__}")
        
        # isinstance
        if isinstance(var, int) and not isinstance(var, bool):
            print(f"  → C'est un entier")
        elif isinstance(var, float):
            print(f"  → C'est un nombre décimal")
        elif isinstance(var, str):
            print(f"  → C'est une chaîne")
        elif isinstance(var, bool):
            print(f"  → C'est un booléen")


# ============= EXERCICES BONUS =============

def bonus_manipulation_avancee_strings():
    """Bonus : Manipulation avancée de strings"""
    # À compléter
    texte = "  Python est génial  "
    
    print(f"Original : '{texte}'")
    print(f"Strip (enlever espaces) : '{texte.strip()}'")
    print(f"Replace : '{texte.replace('génial', 'super')}'")
    print(f"Split : {texte.strip().split()}")
    print(f"Count 'a' : {texte.count('a')}")
    print(f"Find 'est' : {texte.find('est')}")


def bonus_formatage_nombres():
    """Bonus : Formatage avancé de nombres"""
    # À compléter
    nombre = 1234567.89
    
    print(f"Nombre : {nombre}")
    print(f"2 décimales : {nombre:.2f}")
    print(f"Avec séparateurs : {nombre:,.2f}")
    print(f"Pourcentage : {0.857:.2%}")
    print(f"Scientifique : {nombre:.2e}")
    
    # Alignement
    for i in range(1, 101, 10):
        print(f"{i:3d} | {i**2:5d} | {i**3:7d}")


def bonus_validation_input():
    """Bonus : Valider les entrées utilisateur"""
    # À compléter
    # Simuler une entrée utilisateur
    age_input = "25"
    
    # Vérifier si c'est un nombre
    if age_input.isdigit():
        age = int(age_input)
        print(f"Âge valide : {age}")
    else:
        print(f"Erreur : '{age_input}' n'est pas un nombre")
    
    # Vérifier différents types de strings
    exemples = ["123", "abc", "abc123", "ABC", "  "]
    for ex in exemples:
        print(f"'{ex}' :", end=" ")
        if ex.isdigit():
            print("est un chiffre")
        elif ex.isalpha():
            print("est alphabétique")
        elif ex.isalnum():
            print("est alphanumérique")
        elif ex.isspace():
            print("est un espace")
        else:
            print("est mixte")


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Module 03 : Types de Données ===\n")
    
    print("--- Exercice 1 : Manipulation strings ---")
    exercice1_manipulation_strings()
    
    print("\n--- Exercice 2 : Concaténation ---")
    exercice2_concatenation()
    
    print("\n--- Exercice 3 : Slicing ---")
    exercice3_slicing()
    
    print("\n--- Exercice 4 : Opérations nombres ---")
    exercice4_operations_nombres()
    
    print("\n--- Exercice 5 : Fonctions math ---")
    exercice5_fonctions_math()
    
    print("\n--- Exercice 6 : Booléens ---")
    exercice6_booleens()
    
    print("\n--- Exercice 7 : Comparaisons ---")
    exercice7_comparaisons()
    
    print("\n--- Exercice 8 : Conversions types ---")
    exercice8_conversions_types()
    
    print("\n--- Exercice 9 : Conversions avancées ---")
    exercice9_conversions_avancees()
    
    print("\n--- Exercice 10 : Vérifier types ---")
    exercice10_verifier_types()
    
    print("\n=== EXERCICES BONUS ===")
    
    print("\n--- Bonus : Manipulation avancée strings ---")
    bonus_manipulation_avancee_strings()
    
    print("\n--- Bonus : Formatage nombres ---")
    bonus_formatage_nombres()
    
    print("\n--- Bonus : Validation input ---")
    bonus_validation_input()
    
    print("\n✅ Tous les exercices sont terminés !")
    print("Consultez instructions.md pour plus de détails.")