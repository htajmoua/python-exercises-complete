# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

import time
from functools import wraps

# ============= PARTIE 1 : CLOSURES =============

# Exercice 1 - Closure simple
def creer_multiplicateur(n):
    """Créez une closure qui multiplie par n"""
    def multiplicateur(x):
        return x * n
    return multiplicateur


# Exercice 2 - Closure avec state
def creer_compteur():
    """Créez un compteur avec closure"""
    count = 0
    
    def incrementer():
        nonlocal count
        count += 1
        return count
    
    return incrementer


# Exercice 3 - Closure factory
def creer_validateur(min_val, max_val):
    """Factory de validateurs"""
    def valider(valeur):
        return min_val <= valeur <= max_val
    return valider


# ============= PARTIE 2 : DÉCORATEURS DE BASE =============

# Exercice 4 - Premier décorateur
def mon_decorateur(func):
    """Décorateur simple"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Avant l'appel")
        result = func(*args, **kwargs)
        print("Après l'appel")
        return result
    return wrapper


# Exercice 5 - Décorateur de timing
def timer(func):
    """Mesure le temps d'exécution"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} a pris {end - start:.4f}s")
        return result
    return wrapper


# Exercice 6 - Décorateur de logging
def logger(func):
    """Logue les appels de fonction"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__} avec args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} a retourné {result}")
        return result
    return wrapper


# ============= PARTIE 3 : DÉCORATEURS AVEC PARAMÈTRES =============

# Exercice 7 - Décorateur paramétré
def repeat(times):
    """Répète l'exécution d'une fonction"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator


# Exercice 8 - Décorateur de retry
def retry(max_attempts=3, delay=1):
    """Réessaye en cas d'échec"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Tentative {attempt + 1} échouée : {e}")
                    time.sleep(delay)
        return wrapper
    return decorator


# ============= PARTIE 4 : DÉCORATEURS DE CLASSE =============

# Exercice 9 - Singleton avec décorateur
def singleton(cls):
    """Pattern Singleton"""
    instances = {}
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


# Exercice 10 - Classe comme décorateur
class CountCalls:
    """Compte les appels de fonction"""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Appel #{self.count} de {self.func.__name__}")
        return self.func(*args, **kwargs)


# ============= PARTIE 5 : DESIGN PATTERNS =============

# Exercice 12 - Pattern Observer avec événements
class EventManager:
    """Système d'événements avec décorateurs"""
    def __init__(self):
        self.subscribers = {}
    
    def subscribe(self, event_name):
        """Décorateur pour s'abonner à un événement"""
        def decorator(func):
            if event_name not in self.subscribers:
                self.subscribers[event_name] = []
            self.subscribers[event_name].append(func)
            return func
        return decorator
    
    def trigger(self, event_name, *args, **kwargs):
        """Déclenche un événement"""
        if event_name in self.subscribers:
            for subscriber in self.subscribers[event_name]:
                subscriber(*args, **kwargs)


# ============= TP FINAL : PIPELINE =============

def pipeline(*decorators):
    """Combine plusieurs décorateurs en pipeline"""
    def decorator(func):
        for dec in reversed(decorators):
            func = dec(func)
        return func
    return decorator


# Consommateurs de données pour le pipeline
def filter_even(func):
    """Filtre les nombres pairs"""
    @wraps(func)
    def wrapper(data):
        filtered = [x for x in data if x % 2 == 0]
        return func(filtered)
    return wrapper


def multiply_by_two(func):
    """Multiplie par 2"""
    @wraps(func)
    def wrapper(data):
        multiplied = [x * 2 for x in data]
        return func(multiplied)
    return wrapper


def sum_all(func):
    """Somme tous les éléments"""
    @wraps(func)
    def wrapper(data):
        total = sum(data)
        return func(total)
    return wrapper


# ============= EXEMPLES D'UTILISATION =============

@mon_decorateur
def dire_bonjour(nom):
    print(f"Bonjour, {nom}!")
    return f"Salut {nom}"


@timer
def calcul_lent():
    time.sleep(0.5)
    return "Terminé"


@repeat(3)
def dire_hello():
    return "Hello"


@singleton
class Database:
    def __init__(self):
        print("Connexion à la base de données")
        self.connection = "Connected"


@CountCalls
def say_hello():
    print("Hello!")


@pipeline(filter_even, multiply_by_two, sum_all)
def process_data(result):
    """Pipeline complet"""
    return result


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Tests Décorateurs et Closures ===\n")
    
    # Test 1 : Closures
    print("Test 1 : Closures")
    fois_trois = creer_multiplicateur(3)
    print(f"5 × 3 = {fois_trois(5)}")
    
    compteur = creer_compteur()
    print(f"Compteur: {compteur()}, {compteur()}, {compteur()}")
    
    # Test 2 : Décorateurs simples
    print("\nTest 2 : Décorateurs simples")
    dire_bonjour("Alice")
    
    # Test 3 : Timer
    print("\nTest 3 : Timer")
    calcul_lent()
    
    # Test 4 : Repeat
    print("\nTest 4 : Repeat")
    print(dire_hello())
    
    # Test 5 : Singleton
    print("\nTest 5 : Singleton")
    db1 = Database()
    db2 = Database()
    print(f"db1 is db2: {db1 is db2}")
    
    # Test 6 : CountCalls
    print("\nTest 6 : CountCalls")
    say_hello()
    say_hello()
    say_hello()
    
    # Test 7 : EventManager
    print("\nTest 7 : EventManager")
    events = EventManager()
    
    @events.subscribe("user_login")
    def send_email(user):
        print(f"Email envoyé à {user}")
    
    @events.subscribe("user_login")
    def log_login(user):
        print(f"Login loggé pour {user}")
    
    events.trigger("user_login", "Alice")
    
    # TP : Pipeline
    print("\n=== TP : Pipeline de données ===")
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = process_data(data)
    print(f"Résultat du pipeline : {result}")
