# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Module 05 - Dictionnaires
Exercices sur les dictionnaires et dict comprehensions
"""

# ============= EXERCICE 1 : CRÉER ET MANIPULER DES DICTIONNAIRES =============

def exercice1_creer_dictionnaires():
    """Exercice 1 : Créer différents dictionnaires"""
    # À compléter
    personne = {
        "nom": "Dupont",
        "prenom": "Alice",
        "age": 25,
        "ville": "Paris"
    }
    
    notes = {"math": 15, "physique": 17, "informatique": 18}
    vide = {}
    
    print(f"Personne : {personne}")
    print(f"Notes : {notes}")
    print(f"Vide : {vide}")


def exercice2_acceder_valeurs():
    """Exercice 2 : Accéder aux valeurs"""
    # À compléter
    personne = {"nom": "Dupont", "prenom": "Alice", "age": 25}
    
    # Accès direct
    print(f"Nom : {personne['nom']}")
    print(f"Age : {personne['age']}")
    
    # Avec get (plus sûr)
    print(f"Ville : {personne.get('ville', 'Non renseignée')}")
    
    # Toutes les clés et valeurs
    print(f"Clés : {list(personne.keys())}")
    print(f"Valeurs : {list(personne.values())}")
    print(f"Items : {list(personne.items())}")


# ============= EXERCICE 2 : MODIFIER DES DICTIONNAIRES =============

def exercice3_ajouter_modifier():
    """Exercice 3 : Ajouter et modifier des éléments"""
    # À compléter
    personne = {"nom": "Dupont", "age": 25}
    print(f"Initial : {personne}")
    
    # Ajouter
    personne["ville"] = "Paris"
    print(f"Après ajout ville : {personne}")
    
    # Modifier
    personne["age"] = 26
    print(f"Après modification age : {personne}")
    
    # Update (ajouter plusieurs)
    personne.update({"email": "alice@example.com", "tel": "0123456789"})
    print(f"Après update : {personne}")


def exercice4_supprimer():
    """Exercice 4 : Supprimer des éléments"""
    # À compléter
    personne = {"nom": "Dupont", "prenom": "Alice", "age": 25, "ville": "Paris"}
    print(f"Initial : {personne}")
    
    # Del
    del personne["ville"]
    print(f"Après del ville : {personne}")
    
    # Pop (retourne la valeur)
    age = personne.pop("age")
    print(f"Après pop age : {personne}, âge supprimé : {age}")
    
    # Pop avec valeur par défaut
    email = personne.pop("email", "Non trouvé")
    print(f"Pop email : {email}")


# ============= EXERCICE 3 : PARCOURIR DES DICTIONNAIRES =============

def exercice5_parcourir():
    """Exercice 5 : Parcourir un dictionnaire"""
    # À compléter
    notes = {"math": 15, "physique": 17, "informatique": 18, "anglais": 14}
    
    # Parcourir les clés
    print("Matières :")
    for matiere in notes:
        print(f"  {matiere}")
    
    # Parcourir clés et valeurs
    print("\nNotes :")
    for matiere, note in notes.items():
        print(f"  {matiere}: {note}/20")
    
    # Parcourir les valeurs
    print(f"\nMoyenne : {sum(notes.values()) / len(notes):.2f}")


def exercice6_verifier_existence():
    """Exercice 6 : Vérifier l'existence d'une clé"""
    # À compléter
    personne = {"nom": "Dupont", "prenom": "Alice", "age": 25}
    
    # Avec in
    if "nom" in personne:
        print(f"Le nom est : {personne['nom']}")
    
    if "email" not in personne:
        print("Email non renseigné")
    
    # Avec get
    ville = personne.get("ville")
    if ville:
        print(f"Ville : {ville}")
    else:
        print("Ville non renseignée")


# ============= EXERCICE 4 : DICT COMPREHENSIONS =============

def exercice7_dict_comprehension_base():
    """Exercice 7 : Dict comprehension de base"""
    # À compléter
    # Méthode classique
    carres1 = {}
    for i in range(5):
        carres1[i] = i ** 2
    print(f"Méthode classique : {carres1}")
    
    # Dict comprehension
    carres2 = {i: i ** 2 for i in range(5)}
    print(f"Dict comprehension : {carres2}")


def exercice8_dict_comprehension_condition():
    """Exercice 8 : Dict comprehension avec condition"""
    # À compléter
    notes = {"math": 15, "physique": 17, "informatique": 18, "anglais": 12}
    
    # Filtrer notes >= 15
    bonnes_notes = {matiere: note for matiere, note in notes.items() if note >= 15}
    print(f"Bonnes notes (>=15) : {bonnes_notes}")
    
    # Inverser clés et valeurs
    inverse = {note: matiere for matiere, note in notes.items()}
    print(f"Inversé : {inverse}")


def exercice9_dict_comprehension_avancee():
    """Exercice 9 : Dict comprehension avancée"""
    # À compléter
    # Créer un dictionnaire depuis deux listes
    matieres = ["math", "physique", "informatique"]
    notes = [15, 17, 18]
    
    notes_dict = {matiere: note for matiere, note in zip(matieres, notes)}
    print(f"Depuis deux listes : {notes_dict}")
    
    # Transformer les valeurs
    notes_sur_100 = {matiere: note * 5 for matiere, note in notes_dict.items()}
    print(f"Notes sur 100 : {notes_sur_100}")


# ============= EXERCICE 5 : DICTIONNAIRES IMBRIQUÉS =============

def exercice10_dictionnaires_imbriques():
    """Exercice 10 : Dictionnaires imbriqués"""
    # À compléter
    etudiants = {
        "alice": {
            "age": 20,
            "notes": {"math": 15, "physique": 17}
        },
        "bob": {
            "age": 22,
            "notes": {"math": 14, "physique": 16}
        }
    }
    
    # Accès
    print(f"Age d'Alice : {etudiants['alice']['age']}")
    print(f"Note de math de Bob : {etudiants['bob']['notes']['math']}")
    
    # Parcourir
    for nom, infos in etudiants.items():
        moyenne = sum(infos['notes'].values()) / len(infos['notes'])
        print(f"{nom.capitalize()}: {infos['age']} ans, moyenne: {moyenne:.2f}")


# ============= EXERCICES BONUS =============

def bonus_comptage():
    """Bonus : Compter les occurrences"""
    # À compléter
    texte = "python est génial python est puissant"
    mots = texte.split()
    
    # Méthode 1 : Boucle
    compteur1 = {}
    for mot in mots:
        compteur1[mot] = compteur1.get(mot, 0) + 1
    print(f"Compteur (boucle) : {compteur1}")
    
    # Méthode 2 : Dict comprehension
    mots_uniques = set(mots)
    compteur2 = {mot: mots.count(mot) for mot in mots_uniques}
    print(f"Compteur (comprehension) : {compteur2}")
    
    # Méthode 3 : Counter (module collections)
    from collections import Counter
    compteur3 = Counter(mots)
    print(f"Compteur (Counter) : {dict(compteur3)}")
    print(f"Mots les plus fréquents : {compteur3.most_common(2)}")


def bonus_fusion_dicts():
    """Bonus : Fusionner des dictionnaires"""
    # À compléter
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    dict3 = {"b": 20, "e": 5}  # 'b' existe déjà
    
    # Méthode 1 : Update
    fusion1 = dict1.copy()
    fusion1.update(dict2)
    print(f"Fusion avec update : {fusion1}")
    
    # Méthode 2 : Unpacking (Python 3.5+)
    fusion2 = {**dict1, **dict2, **dict3}
    print(f"Fusion avec unpacking : {fusion2}")
    
    # Méthode 3 : Union (Python 3.9+)
    fusion3 = dict1 | dict2 | dict3
    print(f"Fusion avec | : {fusion3}")


def bonus_manipulation_complexe():
    """Bonus : Manipulation complexe de dictionnaires"""
    # À compléter
    produits = [
        {"nom": "Laptop", "prix": 1000, "categorie": "Informatique"},
        {"nom": "Souris", "prix": 25, "categorie": "Informatique"},
        {"nom": "Chaise", "prix": 150, "categorie": "Mobilier"},
        {"nom": "Bureau", "prix": 300, "categorie": "Mobilier"},
    ]
    
    # Regrouper par catégorie
    par_categorie = {}
    for produit in produits:
        cat = produit["categorie"]
        if cat not in par_categorie:
            par_categorie[cat] = []
        par_categorie[cat].append(produit["nom"])
    
    print("Produits par catégorie :")
    for cat, noms in par_categorie.items():
        print(f"  {cat}: {noms}")
    
    # Prix moyen par catégorie
    prix_par_cat = {}
    for produit in produits:
        cat = produit["categorie"]
        if cat not in prix_par_cat:
            prix_par_cat[cat] = []
        prix_par_cat[cat].append(produit["prix"])
    
    moyennes = {cat: sum(prix) / len(prix) for cat, prix in prix_par_cat.items()}
    print(f"\nPrix moyens : {moyennes}")


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Module 05 : Dictionnaires ===\n")
    
    print("--- Exercice 1 : Créer dictionnaires ---")
    exercice1_creer_dictionnaires()
    
    print("\n--- Exercice 2 : Accéder aux valeurs ---")
    exercice2_acceder_valeurs()
    
    print("\n--- Exercice 3 : Ajouter et modifier ---")
    exercice3_ajouter_modifier()
    
    print("\n--- Exercice 4 : Supprimer ---")
    exercice4_supprimer()
    
    print("\n--- Exercice 5 : Parcourir ---")
    exercice5_parcourir()
    
    print("\n--- Exercice 6 : Vérifier existence ---")
    exercice6_verifier_existence()
    
    print("\n--- Exercice 7 : Dict comprehension base ---")
    exercice7_dict_comprehension_base()
    
    print("\n--- Exercice 8 : Dict comprehension condition ---")
    exercice8_dict_comprehension_condition()
    
    print("\n--- Exercice 9 : Dict comprehension avancée ---")
    exercice9_dict_comprehension_avancee()
    
    print("\n--- Exercice 10 : Dictionnaires imbriqués ---")
    exercice10_dictionnaires_imbriques()
    
    print("\n=== EXERCICES BONUS ===")
    
    print("\n--- Bonus : Comptage ---")
    bonus_comptage()
    
    print("\n--- Bonus : Fusion dicts ---")
    bonus_fusion_dicts()
    
    print("\n--- Bonus : Manipulation complexe ---")
    bonus_manipulation_complexe()
    
    print("\n Tous les exercices sont terminés !")
    print("Consultez instructions.md pour plus de détails.")