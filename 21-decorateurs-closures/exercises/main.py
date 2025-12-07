# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

import time
from functools import wraps

# ============= PARTIE 1 : CLOSURES =============

# Exercice 1 - Closure factory
def creer_validateur(min_val, max_val):
    """Factory de validateurs
    
    Hints :
    - Créez une fonction interne valider(valeur)
    - Retournez min_val <= valeur <= max_val
    """
    # À compléter
    pass


# ============= PARTIE 2 : DÉCORATEURS DE BASE =============

# Exercice 2 - Premier décorateur
def mon_decorateur(func):
    """Décorateur simple
    
    Hints :
    - Définissez une fonction wrapper(*args, **kwargs)
    - Affichez "Avant l'appel"
    - Appelez func(*args, **kwargs) et stockez le résultat
    - Affichez "Après l'appel"
    - Retournez le résultat
    - N'oubliez pas @wraps(func)
    """
    # À compléter
    pass


# Exercice 3 - Décorateur de timing
def timer(func):
    """Mesure le temps d'exécution
    
    Hints :
    - start = time.time() avant l'appel
    - Appelez la fonction
    - end = time.time() après l'appel
    - Affichez f"{func.__name__} a pris {end - start:.4f}s"
    """
    # À compléter
    pass


# Exercice 4 - Décorateur de logging
def logger(func):
    """Logue les appels de fonction
    
    Hints :
    - Affichez avant : f"Appel de {func.__name__} avec args={args}, kwargs={kwargs}"
    - Exécutez la fonction et capturez le résultat
    - Affichez après : f"{func.__name__} a retourné {result}"
    - Retournez le résultat
    """
    # À compléter
    pass


# ============= PARTIE 3 : DÉCORATEURS AVEC PARAMÈTRES =============

# Exercice 5 - Décorateur paramétré
def repeat(times):
    """Répète l'exécution d'une fonction
    
    Hints :
    - 3 niveaux : repeat(times) -> decorator(func) -> wrapper(*args, **kwargs)
    - Dans wrapper : bouclez times fois
    - Stockez chaque résultat dans une liste
    - Retournez la liste
    """
    # À compléter
    pass


# Exercice 6 - Décorateur de retry
def retry(max_attempts=3, delay=1):
    """Réessaye en cas d'échec
    
    Hints :
    - 3 niveaux de fonctions
    - for attempt in range(max_attempts):
    - try: return func(*args, **kwargs)
    - except Exception as e:
    -   Si dernière tentative : raise
    -   Sinon : afficher message et time.sleep(delay)
    """
    # À compléter
    pass


# ============= PARTIE 4 : DÉCORATEURS DE CLASSE =============

# Exercice 7 - Singleton avec décorateur
def singleton(cls):
    """Pattern Singleton
    
    Hints :
    - Créez un dictionnaire instances = {}
    - Définissez get_instance(*args, **kwargs)
    - if cls not in instances: instances[cls] = cls(*args, **kwargs)
    - return instances[cls]
    """
    # À compléter
    pass


# Exercice 8 - Classe comme décorateur
class CountCalls:
    """Compte les appels de fonction
    
    Hints :
    - __init__(self, func): stocker func et initialiser count à 0
    - __call__(self, *args, **kwargs):
    -   Incrémenter self.count
    -   Afficher f"Appel #{self.count} de {self.func.__name__}"
    -   Retourner self.func(*args, **kwargs)
    """
    # À compléter
    pass


# ============= PARTIE 5 : CHAÎNAGE DE DÉCORATEURS =============

# Exercice 9 - Chaîner plusieurs décorateurs
def uppercase(func):
    """Transforme le résultat en majuscules
    
    Hints :
    - wrapper doit appeler func(*args, **kwargs)
    - Retourner result.upper()
    - N'oubliez pas @wraps(func)
    """
    # À compléter
    pass


def exclamation(func):
    """Ajoute un point d'exclamation
    
    Hints :
    - wrapper doit appeler func(*args, **kwargs)
    - Retourner result + "!"
    """
    # À compléter
    pass


# Exemple d'utilisation :
# @uppercase
# @exclamation
# def greet(name):
#     return f"Hello, {name}"
# 
# print(greet("Alice"))  # "HELLO, ALICE!"


# ============= PARTIE 6 : DESIGN PATTERNS =============

# Exercice 10 - Pattern Observer avec événements
class EventManager:
    """Système d'événements avec décorateurs
    
    Hints pour __init__ :
    - self.subscribers = {}
    
    Hints pour subscribe(self, event_name) :
    - Retourner un décorateur
    - Le décorateur ajoute func à self.subscribers[event_name]
    - Créer la liste si elle n'existe pas
    
    Hints pour trigger(self, event_name, *args, **kwargs) :
    - Vérifier si event_name in self.subscribers
    - Boucler sur tous les subscribers et les appeler
    """
    # À compléter
    pass


# ============= TP FINAL : PIPELINE =============

def pipeline(*decorators):
    """Combine plusieurs décorateurs en pipeline
    
    Hints :
    - Définir decorator(func)
    - for dec in reversed(decorators): func = dec(func)
    - return func
    - return decorator
    
    Pourquoi reversed ? Les décorateurs s'appliquent de bas en haut
    """
    # À compléter
    pass


# Consommateurs de données pour le pipeline
def filter_even(func):
    """Filtre les nombres pairs
    
    Hints :
    - wrapper(data) reçoit les données
    - filtered = [x for x in data if x % 2 == 0]
    - return func(filtered)
    """
    # À compléter
    pass


def multiply_by_two(func):
    """Multiplie par 2
    
    Hints :
    - multiplied = [x * 2 for x in data]
    - return func(multiplied)
    """
    # À compléter
    pass


def sum_all(func):
    """Somme tous les éléments
    
    Hints :
    - total = sum(data)
    - return func(total)
    """
    # À compléter
    pass


# TP 2 : Système d'événements avec priorités
class EventSystem:
    """Système d'événements avancé avec priorités
    
    Hints pour on(self, event_name, priority=0) :
    - Retourner un décorateur
    - Ajouter (priority, func) à self.events[event_name]
    - Trier : self.events[event_name].sort(key=lambda x: x[0], reverse=True)
    
    Hints pour emit(self, event_name, *args, **kwargs) :
    - Pour chaque (priority, func) dans self.events[event_name]
    - Appeler func(*args, **kwargs)
    """
    # À compléter
    pass


# TP 3 : Pipeline de générateurs
def generator_pipeline(*steps):
    """Pipeline de générateurs
    
    Hints :
    - decorator(generator) -> wrapper(*args, **kwargs)
    - data = generator(*args, **kwargs)
    - for step in steps: data = step(data)
    - return data
    """
    # À compléter
    pass


def filter_positives(data):
    """Générateur qui filtre les positifs
    
    Hints :
    - for item in data:
    -     if item > 0:
    -         yield item
    """
    # À compléter
    pass


def square(data):
    """Générateur qui calcule les carrés
    
    Hints :
    - for item in data:
    -     yield item ** 2
    """
    # À compléter
    pass


def limit(n):
    """Factory qui crée un limiteur
    
    Hints :
    - Retourner une fonction limiter(data)
    - count = 0
    - for item in data:
    -     if count >= n: break
    -     yield item
    -     count += 1
    """
    # À compléter
    pass


# ============= EXEMPLES D'UTILISATION (à décommenter après implémentation) =============

# @mon_decorateur
# def dire_bonjour(nom):
#     print(f"Bonjour, {nom}!")
#     return f"Salut {nom}"


# @timer
# def calcul_lent():
#     time.sleep(0.5)
#     return "Terminé"


# @repeat(3)
# def dire_hello():
#     return "Hello"


# @singleton
# class Database:
#     def __init__(self):
#         print("Connexion à la base de données")
#         self.connection = "Connected"


# @CountCalls
# def say_hello():
#     print("Hello!")


# @uppercase
# @exclamation
# def greet(name):
#     return f"Hello, {name}"


# @pipeline(filter_even, multiply_by_two, sum_all)
# def process_data(result):
#     """Pipeline complet"""
#     return result


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Tests Décorateurs et Closures ===\n")
    
    # Décommentez les tests au fur et à mesure de votre progression
    
    # Test 1 : Closure factory
    # print("Test 1 : Closure factory")
    # valider_age = creer_validateur(0, 120)
    # print(f"valider_age(25): {valider_age(25)}")  # True
    # print(f"valider_age(150): {valider_age(150)}")  # False
    
    # Test 2 : Décorateurs simples
    # print("\nTest 2 : Décorateurs simples")
    # dire_bonjour("Alice")
    
    # Test 3 : Timer
    # print("\nTest 3 : Timer")
    # calcul_lent()
    
    # Test 4 : Repeat
    # print("\nTest 4 : Repeat")
    # print(dire_hello())
    
    # Test 5 : Singleton
    # print("\nTest 5 : Singleton")
    # db1 = Database()
    # db2 = Database()
    # print(f"db1 is db2: {db1 is db2}")
    
    # Test 6 : CountCalls
    # print("\nTest 6 : CountCalls")
    # say_hello()
    # say_hello()
    # say_hello()
    
    # Test 7 : Chaînage de décorateurs
    # print("\nTest 7 : Chaînage de décorateurs")
    # print(greet("Alice"))  # HELLO, ALICE!
    
    # Test 8 : EventManager
    # print("\nTest 8 : EventManager")
    # events = EventManager()
    # 
    # @events.subscribe("user_login")
    # def send_email(user):
    #     print(f"Email envoyé à {user}")
    # 
    # @events.subscribe("user_login")
    # def log_login(user):
    #     print(f"Login loggé pour {user}")
    # 
    # events.trigger("user_login", "Alice")
    
    # TP : Pipeline
    # print("\n=== TP : Pipeline de données ===")
    # data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # result = process_data(data)
    # print(f"Résultat du pipeline : {result}")  # Attendu : 60
    
    print("\nDécommentez les tests au fur et à mesure de votre progression !")
