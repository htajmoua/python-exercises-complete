"""
TP22 - POO Avancée
Consultez le fichier instructions.md pour les consignes détaillées
"""

from contextlib import contextmanager


# ============= PARTIE 1 : HÉRITAGE MULTIPLE =============

# Exercice 1 - MRO (Method Resolution Order)

# TODO: Créer la classe A avec une méthode qui affiche "Méthode de A"

# TODO: Créer la classe B qui hérite de A
#       - Redéfinir la méthode
#       - Afficher "Méthode de B"
#       - Appeler super().methode()

# TODO: Créer la classe C qui hérite de A (structure similaire à B)

# TODO: Créer la classe D qui hérite de B et C (héritage multiple)


# ============= PARTIE 2 : CONTEXT MANAGERS =============

# Exercice 2 - Context Manager basique

# TODO: Créer la classe FileManager
#       - __init__(self, filename, mode)
#       - __enter__(self): ouvrir le fichier et le retourner
#       - __exit__(self, exc_type, exc_val, exc_tb): fermer le fichier


# Exercice 3 - Context Manager avec contextlib

# TODO: Créer le context manager timer() avec @contextmanager
#       - Mesurer le temps avec time.time()
#       - yield
#       - Afficher le temps écoulé dans finally

# TODO: Créer le context manager open_file(filename, mode) avec @contextmanager
#       - Ouvrir le fichier
#       - yield le fichier
#       - Fermer dans finally


# ============= PARTIE 3 : MÉTACLASSES =============

# Exercice 4 - Comprendre les métaclasses

# TODO: Créer MyClass avec type()
#       MyClass = type('MyClass', (), {'x': 5, 'method': lambda self: "Hello"})


# ============= TP FINAL : MÉTACLASSE SINGLETON =============

# TODO: Créer la métaclasse SingletonMeta
#       - Attribut de classe _instances = {}
#       - Redéfinir __call__(cls, *args, **kwargs)
#       - Vérifier si cls est dans _instances
#       - Si non, créer et sauvegarder l'instance
#       - Retourner l'instance

# TODO: Créer la classe Database qui utilise SingletonMeta
#       - __init__: afficher "Initialisation de la base de données"
#       - self.connection = "Connected"


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Tests POO Avancée ===\n")
    
    # Test 1 : MRO
    print("Test 1 : MRO (Method Resolution Order)")
    # TODO: Créer une instance de D et appeler methode()
    # TODO: Afficher D.__mro__
    
    # Test 2 : Context Manager
    print("\nTest 2 : Context Manager basique")
    # TODO: Utiliser FileManager pour écrire dans 'test.txt'
    
    # Test 3 : Timer context manager
    print("\nTest 3 : Timer")
    # TODO: Utiliser timer() pour mesurer sum(range(1000000))
    
    # Test 4 : Métaclasses
    print("\nTest 4 : type()")
    # TODO: Créer obj = MyClass() et afficher obj.x et obj.method()
    
    # TP : Singleton
    print("\n=== TP : Singleton ===")
    # TODO: Créer db1 et db2 avec Database()
    # TODO: Vérifier que db1 is db2
