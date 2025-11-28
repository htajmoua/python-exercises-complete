# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Module 02 - Variables et Types de Données
Exercices sur la déclaration, manipulation et affichage de variables
"""

# ============= EXERCICE 1 : DÉCLARER DES VARIABLES =============

def exercice1_variables_simples():
    """Exercice 1 : Déclarer et afficher des variables"""
    # À compléter
    nom = "Alice"
    age = 25
    taille = 1.65
    est_etudiant = True
    
    print(f"Nom: {nom}")
    print(f"Âge: {age}")
    print(f"Taille: {taille}m")
    print(f"Étudiant: {est_etudiant}")


def exercice2_types_variables():
    """Exercice 2 : Identifier les types de variables"""
    # À compléter
    entier = 42
    decimal = 3.14
    texte = "Hello"
    booleen = True
    
    print(f"{entier} est de type {type(entier)}")
    print(f"{decimal} est de type {type(decimal)}")
    print(f"{texte} est de type {type(texte)}")
    print(f"{booleen} est de type {type(booleen)}")


# ============= EXERCICE 2 : MODIFIER DES VARIABLES =============

def exercice3_modification():
    """Exercice 3 : Modifier la valeur d'une variable"""
    # À compléter
    compteur = 0
    print(f"Compteur initial: {compteur}")
    
    compteur = 5
    print(f"Compteur modifié: {compteur}")
    
    compteur = compteur + 10
    print(f"Compteur incrémenté: {compteur}")


def exercice4_operations_variables():
    """Exercice 4 : Opérations avec variables"""
    # À compléter
    a = 10
    b = 3
    
    somme = a + b
    difference = a - b
    produit = a * b
    quotient = a / b
    
    print(f"a = {a}, b = {b}")
    print(f"Somme: {somme}")
    print(f"Différence: {difference}")
    print(f"Produit: {produit}")
    print(f"Quotient: {quotient:.2f}")


# ============= EXERCICE 3 : INPUT UTILISATEUR =============

def exercice5_input_simple():
    """Exercice 5 : Demander le nom de l'utilisateur"""
    # À compléter (décommenter pour tester)
    # nom = input("Quel est votre nom ? ")
    # print(f"Bonjour, {nom} !")
    
    # Version sans input pour les tests automatiques
    nom = "Alice"
    print(f"Bonjour, {nom} !")


def exercice6_input_age():
    """Exercice 6 : Calculer l'année de naissance"""
    # À compléter (décommenter pour tester)
    # age = int(input("Quel est votre âge ? "))
    # annee_actuelle = 2024
    # annee_naissance = annee_actuelle - age
    # print(f"Vous êtes né(e) en {annee_naissance}")
    
    # Version sans input
    age = 25
    annee_actuelle = 2024
    annee_naissance = annee_actuelle - age
    print(f"Vous êtes né(e) en {annee_naissance}")


# ============= EXERCICE 4 : FORMATAGE DE CHAÎNES =============

def exercice7_f_strings():
    """Exercice 7 : Utiliser les f-strings"""
    # À compléter
    prenom = "Alice"
    nom = "Dupont"
    age = 25
    
    # Différentes façons de formatter
    print(f"Je m'appelle {prenom} {nom}")
    print(f"J'ai {age} ans")
    print(f"Dans 10 ans, j'aurai {age + 10} ans")


def exercice8_format_nombres():
    """Exercice 8 : Formater des nombres"""
    # À compléter
    prix = 19.99
    quantite = 3
    total = prix * quantite
    
    print(f"Prix unitaire: {prix:.2f}€")
    print(f"Quantité: {quantite}")
    print(f"Total: {total:.2f}€")
    
    # Formater avec espaces
    grand_nombre = 1234567
    print(f"Grand nombre: {grand_nombre:,}")


# ============= EXERCICE 5 : ÉCHANGE DE VARIABLES =============

def exercice9_echange():
    """Exercice 9 : Échanger deux variables"""
    # À compléter
    a = 5
    b = 10
    
    print(f"Avant: a = {a}, b = {b}")
    
    # Méthode Python (swap)
    a, b = b, a
    
    print(f"Après: a = {a}, b = {b}")


def exercice10_affectation_multiple():
    """Exercice 10 : Affectation multiple"""
    # À compléter
    # Déclarer plusieurs variables en une ligne
    x, y, z = 1, 2, 3
    print(f"x = {x}, y = {y}, z = {z}")
    
    # Même valeur pour toutes
    a = b = c = 0
    print(f"a = {a}, b = {b}, c = {c}")


# ============= EXERCICES BONUS =============

def bonus_calcul_imc():
    """Bonus : Calculer l'IMC"""
    # À compléter
    poids = 70  # kg
    taille = 1.75  # m
    imc = poids / (taille ** 2)
    
    print(f"Poids: {poids}kg")
    print(f"Taille: {taille}m")
    print(f"IMC: {imc:.2f}")


def bonus_conversion_unites():
    """Bonus : Convertir des unités"""
    # À compléter
    kilometres = 5
    metres = kilometres * 1000
    centimetres = metres * 100
    
    print(f"{kilometres}km = {metres}m = {centimetres}cm")
    
    # Conversion inverse
    pouces = 10
    centimetres = pouces * 2.54
    print(f"{pouces} pouces = {centimetres}cm")


def bonus_calcul_interet():
    """Bonus : Calculer les intérêts composés"""
    # À compléter
    capital = 1000
    taux = 0.05  # 5%
    duree = 10  # années
    
    montant_final = capital * (1 + taux) ** duree
    interets = montant_final - capital
    
    print(f"Capital initial: {capital}€")
    print(f"Taux: {taux * 100}%")
    print(f"Durée: {duree} ans")
    print(f"Montant final: {montant_final:.2f}€")
    print(f"Intérêts gagnés: {interets:.2f}€")


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Module 02 : Variables ===\n")
    
    print("--- Exercice 1 : Variables simples ---")
    exercice1_variables_simples()
    
    print("\n--- Exercice 2 : Types de variables ---")
    exercice2_types_variables()
    
    print("\n--- Exercice 3 : Modification ---")
    exercice3_modification()
    
    print("\n--- Exercice 4 : Opérations ---")
    exercice4_operations_variables()
    
    print("\n--- Exercice 5 : Input simple ---")
    exercice5_input_simple()
    
    print("\n--- Exercice 6 : Input âge ---")
    exercice6_input_age()
    
    print("\n--- Exercice 7 : F-strings ---")
    exercice7_f_strings()
    
    print("\n--- Exercice 8 : Format nombres ---")
    exercice8_format_nombres()
    
    print("\n--- Exercice 9 : Échange ---")
    exercice9_echange()
    
    print("\n--- Exercice 10 : Affectation multiple ---")
    exercice10_affectation_multiple()
    
    print("\n=== EXERCICES BONUS ===")
    
    print("\n--- Bonus : Calcul IMC ---")
    bonus_calcul_imc()
    
    print("\n--- Bonus : Conversion unités ---")
    bonus_conversion_unites()
    
    print("\n--- Bonus : Intérêts composés ---")
    bonus_calcul_interet()
    
    print("\n✅ Tous les exercices sont terminés !")
    print("Consultez instructions.md pour plus de détails.")