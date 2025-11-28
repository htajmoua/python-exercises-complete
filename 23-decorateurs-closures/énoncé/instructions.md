# Instructions - Décorateurs et Closures

Les décorateurs et closures sont des concepts puissants de Python permettant de modifier le comportement de fonctions de manière élégante.

## Partie 1 - Closures

### Exercice 1 - Comprendre les closures

**Créez** une closure simple :

```python
def creer_multiplicateur(n):
    def multiplicateur(x):
        return x * n  # n vient du scope externe
    return multiplicateur

fois_trois = creer_multiplicateur(3)
fois_cinq = creer_multiplicateur(5)

print(fois_trois(10))  # 30
print(fois_cinq(10))   # 50

# Vérifier la closure
print(fois_trois.__closure__)
print(fois_trois.__closure__[0].cell_contents)  # 3
```

### Exercice 2 - Closures avec state

**Créez** un compteur avec closure :

```python
def creer_compteur():
    count = 0
    
    def incrementer():
        nonlocal count  # Modifier la variable du scope externe
        count += 1
        return count
    
    return incrementer

compteur = creer_compteur()
print(compteur())  # 1
print(compteur())  # 2
print(compteur())  # 3
```

### Exercice 3 - Closure factory

**Créez** une factory de validateurs :

```python
def creer_validateur(min_val, max_val):
    def valider(valeur):
        return min_val <= valeur <= max_val
    return valider

valider_age = creer_validateur(0, 120)
valider_note = creer_validateur(0, 20)

print(valider_age(25))   # True
print(valider_age(150))  # False
print(valider_note(15))  # True
```

## Partie 2 - Décorateurs de base

### Exercice 4 - Premier décorateur

**Créez** un décorateur simple :

```python
def mon_decorateur(func):
    def wrapper(*args, **kwargs):
        print("Avant l'appel")
        result = func(*args, **kwargs)
        print("Après l'appel")
        return result
    return wrapper

@mon_decorateur
def dire_bonjour(nom):
    print(f"Bonjour, {nom}!")

dire_bonjour("Alice")
# Avant l'appel
# Bonjour, Alice!
# Après l'appel
```

### Exercice 5 - Décorateur de timing

**Mesurez** le temps d'exécution :

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)  # Préserve les métadonnées
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} a pris {end - start:.4f}s")
        return result
    return wrapper

@timer
def calcul_lent():
    time.sleep(1)
    return "Terminé"

calcul_lent()
```

### Exercice 6 - Décorateur de logging

**Loggez** les appels de fonction :

```python
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__} avec args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} a retourné {result}")
        return result
    return wrapper

@logger
def addition(a, b):
    return a + b

addition(5, 3)
```

## Partie 3 - Décorateurs avec paramètres

### Exercice 7 - Décorateur paramétré

**Créez** un décorateur avec paramètres :

```python
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def dire_hello():
    return "Hello"

print(dire_hello())  # ['Hello', 'Hello', 'Hello']
```

### Exercice 8 - Décorateur de retry

**Réessayez** en cas d'échec :

```python
def retry(max_attempts=3, delay=1):
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

@retry(max_attempts=3, delay=0.5)
def fonction_instable():
    import random
    if random.random() < 0.7:
        raise ValueError("Erreur aléatoire")
    return "Succès"

print(fonction_instable())
```

## Partie 4 - Décorateurs de classe

### Exercice 9 - Décorateur de classe simple

**Décorez** une classe :

```python
def singleton(cls):
    instances = {}
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Connexion à la base de données")

db1 = Database()  # Connexion à la base de données
db2 = Database()  # Pas de nouvelle connexion
print(db1 is db2)  # True
```

### Exercice 10 - Décorateur avec classe

**Utilisez** une classe comme décorateur :

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Appel #{self.count} de {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # Appel #1
say_hello()  # Appel #2
say_hello()  # Appel #3
```

## Partie 5 - Chaînage de décorateurs

### Exercice 11 - Chaîner plusieurs décorateurs

**Combinez** des décorateurs :

```python
def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@uppercase
@exclamation
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # HELLO, ALICE!
```

## Partie 6 - Design Patterns avec décorateurs

### Exercice 12 - Pattern Observer

**Implémentez** un système d'événements :

```python
class EventManager:
    def __init__(self):
        self.subscribers = {}
    
    def subscribe(self, event_name):
        def decorator(func):
            if event_name not in self.subscribers:
                self.subscribers[event_name] = []
            self.subscribers[event_name].append(func)
            return func
        return decorator
    
    def trigger(self, event_name, *args, **kwargs):
        if event_name in self.subscribers:
            for subscriber in self.subscribers[event_name]:
                subscriber(*args, **kwargs)

# Utilisation
events = EventManager()

@events.subscribe("user_login")
def send_welcome_email(user):
    print(f"Email envoyé à {user}")

@events.subscribe("user_login")
def log_login(user):
    print(f"Login loggé pour {user}")

events.trigger("user_login", "Alice")
# Email envoyé à Alice
# Login loggé pour Alice
```

## TP Final - Pipeline de consommateurs de données

**Créez** un pipeline de traitement de données :

```python
def pipeline(*decorators):
    """Combine plusieurs décorateurs en un pipeline"""
    def decorator(func):
        for dec in reversed(decorators):
            func = dec(func)
        return func
    return decorator

# Consommateurs de données
def filter_even(func):
    @wraps(func)
    def wrapper(data):
        filtered = [x for x in data if x % 2 == 0]
        return func(filtered)
    return wrapper

def multiply_by_two(func):
    @wraps(func)
    def wrapper(data):
        multiplied = [x * 2 for x in data]
        return func(multiplied)
    return wrapper

def sum_all(func):
    @wraps(func)
    def wrapper(data):
        total = sum(data)
        return func(total)
    return wrapper

@pipeline(filter_even, multiply_by_two, sum_all)
def process_data(result):
    return result

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(process_data(data))  # 60 (2+4+6+8+10)*2 summed
```

### TP - Système d'abonnement aux événements

**Créez** un système complet :

```python
class EventSystem:
    def __init__(self):
        self.events = {}
    
    def on(self, event_name, priority=0):
        """Décorateur pour s'abonner à un événement"""
        def decorator(func):
            if event_name not in self.events:
                self.events[event_name] = []
            self.events[event_name].append((priority, func))
            self.events[event_name].sort(key=lambda x: x[0], reverse=True)
            return func
        return decorator
    
    def emit(self, event_name, *args, **kwargs):
        """Déclencher un événement"""
        if event_name in self.events:
            for priority, func in self.events[event_name]:
                func(*args, **kwargs)

# Utilisation
app = EventSystem()

@app.on("user_register", priority=10)
def create_user_account(username, email):
    print(f"Compte créé pour {username}")

@app.on("user_register", priority=5)
def send_confirmation_email(username, email):
    print(f"Email de confirmation envoyé à {email}")

@app.on("user_register", priority=1)
def log_registration(username, email):
    print(f"Inscription loggée : {username}")

app.emit("user_register", "Alice", "alice@example.com")
# Compte créé pour Alice
# Email de confirmation envoyé à alice@example.com
# Inscription loggée : Alice
```

### TP - Générateurs et pipeline

**Créez** un pipeline avec générateurs :

```python
def generator_pipeline(*steps):
    """Pipeline de générateurs"""
    def decorator(generator):
        @wraps(generator)
        def wrapper(*args, **kwargs):
            data = generator(*args, **kwargs)
            for step in steps:
                data = step(data)
            return data
        return wrapper
    return decorator

def filter_positives(data):
    for item in data:
        if item > 0:
            yield item

def square(data):
    for item in data:
        yield item ** 2

def limit(n):
    def limiter(data):
        count = 0
        for item in data:
            if count >= n:
                break
            yield item
            count += 1
    return limiter

@generator_pipeline(filter_positives, square, limit(5))
def number_stream():
    for i in range(-10, 20):
        yield i

for num in number_stream():
    print(num)
```

## Checklist de validation

- ✅ Closures comprises et utilisées
- ✅ Décorateurs simples créés
- ✅ Décorateurs avec paramètres maîtrisés
- ✅ Décorateurs de classe implémentés
- ✅ Chaînage de décorateurs fonctionnel
- ✅ Pattern Observer implémenté
- ✅ TP pipeline de consommateurs réalisé
- ✅ TP système d'événements complet
- ✅ Générateurs dans pipeline utilisés
