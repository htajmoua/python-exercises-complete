# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Module 04 - Listes
Exercices sur les listes, list comprehensions et manipulation de données
"""

# ============= EXERCICE 1 : CRÉER ET MANIPULER DES LISTES =============

def exercice1_creer_listes():
    """Exercice 1 : Créer différentes listes"""
    # À compléter
    nombres = [1, 2, 3, 4, 5]
    fruits = ["pomme", "banane", "orange"]
    mixte = [1, "hello", 3.14, True]
    vide = []
    
    print(f"Nombres : {nombres}")
    print(f"Fruits : {fruits}")
    print(f"Mixte : {mixte}")
    print(f"Vide : {vide}")


def exercice2_acceder_elements():
    """Exercice 2 : Accéder aux éléments"""
    # À compléter
    fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]
    
    print(f"Premier fruit : {fruits[0]}")
    print(f"Dernier fruit : {fruits[-1]}")
    print(f"3 premiers : {fruits[:3]}")
    print(f"Du 2e au 4e : {fruits[1:4]}")
    print(f"Liste inversée : {fruits[::-1]}")


# ============= EXERCICE 2 : MODIFIER DES LISTES =============

def exercice3_ajouter_elements():
    """Exercice 3 : Ajouter des éléments"""
    # À compléter
    nombres = [1, 2, 3]
    print(f"Liste initiale : {nombres}")
    
    # Append (ajouter à la fin)
    nombres.append(4)
    print(f"Après append(4) : {nombres}")
    
    # Insert (insérer à un index)
    nombres.insert(0, 0)
    print(f"Après insert(0, 0) : {nombres}")
    
    # Extend (ajouter plusieurs éléments)
    nombres.extend([5, 6, 7])
    print(f"Après extend([5, 6, 7]) : {nombres}")


def exercice4_supprimer_elements():
    """Exercice 4 : Supprimer des éléments"""
    # À compléter
    fruits = ["pomme", "banane", "orange", "banane", "kiwi"]
    print(f"Liste initiale : {fruits}")
    
    # Remove (supprimer par valeur)
    fruits.remove("banane")  # Supprime la première occurrence
    print(f"Après remove('banane') : {fruits}")
    
    # Pop (supprimer par index)
    fruit_supprime = fruits.pop(1)
    print(f"Après pop(1) : {fruits}, élément supprimé : {fruit_supprime}")
    
    # Del (supprimer par index ou slice)
    del fruits[0]
    print(f"Après del fruits[0] : {fruits}")
    
    # Clear (vider la liste)
    fruits_copy = fruits.copy()
    fruits_copy.clear()
    print(f"Après clear() : {fruits_copy}")


# ============= EXERCICE 3 : MÉTHODES DE LISTES =============

def exercice5_methodes_listes():
    """Exercice 5 : Utiliser les méthodes de listes"""
    # À compléter
    nombres = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    
    print(f"Liste : {nombres}")
    print(f"Longueur : {len(nombres)}")
    print(f"Somme : {sum(nombres)}")
    print(f"Maximum : {max(nombres)}")
    print(f"Minimum : {min(nombres)}")
    print(f"Compte de 5 : {nombres.count(5)}")
    print(f"Index de 4 : {nombres.index(4)}")
    
    # Sort et sorted
    nombres_tries = sorted(nombres)
    print(f"Sorted (nouv elle liste) : {nombres_tries}")
    
    nombres.sort(reverse=True)
    print(f"Sort (en place, décroissant) : {nombres}")


def exercice6_concatenation_repetition():
    """Exercice 6 : Concaténer et répéter des listes"""
    # À compléter
    liste1 = [1, 2, 3]
    liste2 = [4, 5, 6]
    
    # Concaténation
    liste3 = liste1 + liste2
    print(f"{liste1} + {liste2} = {liste3}")
    
    # Répétition
    liste_repetee = [0] * 5
    print(f"[0] * 5 = {liste_repetee}")


# ============= EXERCICE 4 : LIST COMPREHENSIONS =============

def exercice7_list_comprehension_base():
    """Exercice 7 : List comprehension de base"""
    # À compléter
    # Méthode classique
    carres1 = []
    for i in range(10):
        carres1.append(i ** 2)
    print(f"Méthode classique : {carres1}")
    
    # List comprehension
    carres2 = [i ** 2 for i in range(10)]
    print(f"List comprehension : {carres2}")


def exercice8_list_comprehension_condition():
    """Exercice 8 : List comprehension avec condition"""
    # À compléter
    nombres = list(range(20))
    
    # Filtrer les nombres pairs
    pairs = [n for n in nombres if n % 2 == 0]
    print(f"Nombres pairs : {pairs}")
    
    # Filtrer les multiples de 3
    multiples_3 = [n for n in nombres if n % 3 == 0]
    print(f"Multiples de 3 : {multiples_3}")
    
    # Transformer et filtrer
    carres_pairs = [n ** 2 for n in nombres if n % 2 == 0]
    print(f"Carrés des pairs : {carres_pairs}")


def exercice9_list_comprehension_avancee():
    """Exercice 9 : List comprehension avancée"""
    # À compléter
    # Nested list comprehension
    matrice = [[i * j for j in range(1, 6)] for i in range(1, 6)]
    print("Table de multiplication 5x5 :")
    for ligne in matrice:
        print(ligne)
    
    # Aplatir une liste de listes
    listes = [[1, 2], [3, 4], [5, 6]]
    aplatie = [item for sous_liste in listes for item in sous_liste]
    print(f"\nListe aplatie : {aplatie}")


# ============= EXERCICE 5 : PARCOURIR DES LISTES =============

def exercice10_parcourir_listes():
    """Exercice 10 : Différentes façons de parcourir"""
    # À compléter
    fruits = ["pomme", "banane", "orange"]
    
    # Méthode 1 : Simple
    print("Méthode 1 : Simple")
    for fruit in fruits:
        print(f"  {fruit}")
    
    # Méthode 2 : Avec index
    print("\nMéthode 2 : Avec index")
    for i in range(len(fruits)):
        print(f"  {i}: {fruits[i]}")
    
    # Méthode 3 : Avec enumerate
    print("\nMéthode 3 : Avec enumerate")
    for i, fruit in enumerate(fruits):
        print(f"  {i}: {fruit}")
    
    # Méthode 4 : Avec enumerate et start
    print("\nMéthode 4 : Enumerate avec start=1")
    for i, fruit in enumerate(fruits, start=1):
        print(f"  {i}: {fruit}")


# ============= EXERCICES BONUS =============

def bonus_statistiques():
    """Bonus : Statistiques sur une liste"""
    # À compléter
    notes = [15, 12, 18, 10, 16, 14, 11, 17]
    
    print(f"Notes : {notes}")
    print(f"Nombre d'élèves : {len(notes)}")
    print(f"Note minimale : {min(notes)}")
    print(f"Note maximale : {max(notes)}")
    print(f"Somme : {sum(notes)}")
    print(f"Moyenne : {sum(notes) / len(notes):.2f}")
    
    # Notes au-dessus de la moyenne
    moyenne = sum(notes) / len(notes)
    au_dessus = [n for n in notes if n > moyenne]
    print(f"Notes au-dessus de la moyenne : {au_dessus}")


def bonus_filtrage_donnees():
    """Bonus : Filtrer et transformer des données"""
    # À compléter
    produits = [
        {"nom": "Laptop", "prix": 1000, "stock": 5},
        {"nom": "Souris", "prix": 25, "stock": 50},
        {"nom": "Clavier", "prix": 75, "stock": 30},
        {"nom": "Écran", "prix": 300, "stock": 0},
    ]
    
    # Produits en stock
    en_stock = [p for p in produits if p["stock"] > 0]
    print(f"Produits en stock : {[p['nom'] for p in en_stock]}")
    
    # Produits chers (> 100€)
    chers = [p for p in produits if p["prix"] > 100]
    print(f"Produits chers : {[p['nom'] for p in chers]}")
    
    # Liste des noms uniquement
    noms = [p["nom"] for p in produits]
    print(f"Noms : {noms}")
    
    # Prix total du stock
    valeur_totale = sum(p["prix"] * p["stock"] for p in produits)
    print(f"Valeur totale du stock : {valeur_totale}€")


def bonus_manipulation_complexe():
    """Bonus : Manipulation complexe de listes"""
    # À compléter
    # Trouver les doublons
    nombres = [1, 2, 3, 2, 4, 5, 1, 6, 7, 3]
    doublons = [n for n in set(nombres) if nombres.count(n) > 1]
    print(f"Doublons : {sorted(doublons)}")
    
    # Supprimer les doublons (garder l'ordre)
    sans_doublons = []
    for n in nombres:
        if n not in sans_doublons:
            sans_doublons.append(n)
    print(f"Sans doublons : {sans_doublons}")
    
    # Ou avec dict (Python 3.7+)
    sans_doublons2 = list(dict.fromkeys(nombres))
    print(f"Sans doublons (dict) : {sans_doublons2}")
    
    # Intersection de deux listes
    liste1 = [1, 2, 3, 4, 5]
    liste2 = [4, 5, 6, 7, 8]
    intersection = [n for n in liste1 if n in liste2]
    print(f"Intersection : {intersection}")


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Module 04 : Listes ===\n")
    
    print("--- Exercice 1 : Créer listes ---")
    exercice1_creer_listes()
    
    print("\n--- Exercice 2 : Accéder aux éléments ---")
    exercice2_acceder_elements()
    
    print("\n--- Exercice 3 : Ajouter éléments ---")
    exercice3_ajouter_elements()
    
    print("\n--- Exercice 4 : Supprimer éléments ---")
    exercice4_supprimer_elements()
    
    print("\n--- Exercice 5 : Méthodes de listes ---")
    exercice5_methodes_listes()
    
    print("\n--- Exercice 6 : Concaténation et répétition ---")
    exercice6_concatenation_repetition()
    
    print("\n--- Exercice 7 : List comprehension base ---")
    exercice7_list_comprehension_base()
    
    print("\n--- Exercice 8 : List comprehension avec condition ---")
    exercice8_list_comprehension_condition()
    
    print("\n--- Exercice 9 : List comprehension avancée ---")
    exercice9_list_comprehension_avancee()
    
    print("\n--- Exercice 10 : Parcourir listes ---")
    exercice10_parcourir_listes()
    
    print("\n=== EXERCICES BONUS ===")
    
    print("\n--- Bonus : Statistiques ---")
    bonus_statistiques()
    
    print("\n--- Bonus : Filtrage données ---")
    bonus_filtrage_donnees()
    
    print("\n--- Bonus : Manipulation complexe ---")
    bonus_manipulation_complexe()
    
    print("\n✅ Tous les exercices sont terminés !")
    print("Consultez instructions.md pour plus de détails.")