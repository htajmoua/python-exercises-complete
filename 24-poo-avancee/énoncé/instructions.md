# Instructions - POO Avancée

Ce module couvre les concepts avancés de la Programmation Orientée Objet en Python : itérateurs, héritage multiple, context managers, classes abstraites et métaclasses.

## Partie 1 - Itérateurs

### Exercice 1 - Créer un itérateur personnalisé

**Implémentez** les méthodes `__iter__` et `__next__` :

```python
class Compteur:
    def __init__(self, debut, fin):
        self.current = debut
        self.fin = fin
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.fin:
            raise StopIteration
        self.current += 1
        return self.current - 1

for i in Compteur(1, 5):
    print(i)  # 1, 2, 3, 4, 5
```

### Exercice 2 - Itérateur avec état

**Créez** un itérateur Fibonacci :

```python
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

for num in Fibonacci(10):
    print(num)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

### Exercice 3 - Générateurs (alternative aux itérateurs)

**Utilisez** `yield` :

```python
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci_generator(10):
    print(num)

# Générateur infini
def nombres_pairs():
    n = 0
    while True:
        yield n
        n += 2

# Utiliser avec itertools
from itertools import islice
for num in islice(nombres_pairs(), 10):
    print(num)
```

## Partie 2 - Héritage Multiple

### Exercice 4 - MRO (Method Resolution Order)

**Comprenez** l'ordre de résolution des méthodes :

```python
class A:
    def methode(self):
        print("Méthode de A")

class B(A):
    def methode(self):
        print("Méthode de B")
        super().methode()

class C(A):
    def methode(self):
        print("Méthode de C")
        super().methode()

class D(B, C):
    def methode(self):
        print("Méthode de D")
        super().methode()

d = D()
d.methode()
# Méthode de D
# Méthode de B
# Méthode de C
# Méthode de A

# Voir le MRO
print(D.__mro__)
# ou
print(D.mro())
```

### Exercice 5 - Diamond Problem

**Résolvez** le problème du diamant :

```python
class Base:
    def __init__(self):
        print("Base.__init__")
        self.value = "base"

class Left(Base):
    def __init__(self):
        print("Left.__init__")
        super().__init__()
        self.left = "left"

class Right(Base):
    def __init__(self):
        print("Right.__init__")
        super().__init__()
        self.right = "right"

class Bottom(Left, Right):
    def __init__(self):
        print("Bottom.__init__")
        super().__init__()

b = Bottom()
# Bottom.__init__
# Left.__init__
# Right.__init__
# Base.__init__
```

### Exercice 6 - Mixins

**Créez** des mixins réutilisables :

```python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class XMLMixin:
    def to_xml(self):
        xml = f"<{self.__class__.__name__}>"
        for key, value in self.__dict__.items():
            xml += f"<{key}>{value}</{key}>"
        xml += f"</{self.__class__.__name__}>"
        return xml

class Person(JSONMixin, XMLMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.to_json())
print(p.to_xml())
```

## Partie 3 - Context Managers

### Exercice 7 - Context Manager basique

**Implémentez** `__enter__` et `__exit__` :

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Retourner False pour propager les exceptions
        return False

with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
```

### Exercice 8 - Context Manager avec gestion d'erreurs

**Gérez** les exceptions :

```python
class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.connection = None
    
    def __enter__(self):
        print(f"Connexion à {self.host}")
        self.connection = f"Connected to {self.host}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Déconnexion de {self.host}")
        if exc_type is not None:
            print(f"Une erreur s'est produite : {exc_val}")
        return False  # Propage l'exception

with DatabaseConnection("localhost"):
    print("Travail avec la base de données")
    # Si erreur ici, __exit__ la gère
```

### Exercice 9 - Context Manager avec contextlib

**Utilisez** le module `contextlib` :

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Temps écoulé : {end - start:.4f}s")

with timer():
    # Code à mesurer
    sum(range(1000000))

# Ou avec gestion de ressources
@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with open_file('test.txt', 'w') as f:
    f.write('Test')
```

## Partie 4 - Classes Abstraites (ABC)

### Exercice 10 - Classe abstraite basique

**Créez** une classe abstraite :

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return f"Shape with area {self.area()}"

# shape = Shape()  # TypeError: Can't instantiate abstract class

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area())  # 15
print(rect.describe())
```

### Exercice 11 - Propriétés abstraites

**Combinez** ABC et properties :

```python
class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    @property
    def sound(self):
        return "Woof!"
    
    def move(self):
        return "Running on four legs"

dog = Dog()
print(dog.sound)
print(dog.move())
```

## Partie 5 - Métaclasses

### Exercice 12 - Comprendre les métaclasses

**Explorez** `type` :

```python
# type() comme métaclasse
MyClass = type('MyClass', (), {'x': 5, 'method': lambda self: "Hello"})
obj = MyClass()
print(obj.x)  # 5
print(obj.method())  # Hello

# Tout est un objet, y compris les classes
class NormalClass:
    pass

print(type(NormalClass))  # <class 'type'>
print(type(type))  # <class 'type'>
```

### Exercice 13 - Créer une métaclasse

**Implémentez** une métaclasse personnalisée :

```python
class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # Convertir tous les attributs en majuscules
        uppercase_attrs = {}
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith('__'):
                uppercase_attrs[attr_name.upper()] = attr_value
            else:
                uppercase_attrs[attr_name] = attr_value
        
        return super().__new__(cls, name, bases, uppercase_attrs)

class MyClass(metaclass=UpperAttrMetaclass):
    x = 5
    def hello(self):
        return "Hello"

obj = MyClass()
print(obj.X)  # 5
print(obj.HELLO())  # Hello
# print(obj.x)  # AttributeError
```

## TP Final - Métaclasse Singleton

**Implémentez** le pattern Singleton avec une métaclasse :

```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Initialisation de la base de données")
        self.connection = "Connected"

# Test
db1 = Database()  # Initialisation de la base de données
db2 = Database()  # Pas d'initialisation
print(db1 is db2)  # True
```

### TP - Métaclasse de validation

**Validez** les attributs automatiquement :

```python
class ValidatedMeta(type):
    def __new__(cls, name, bases, attrs):
        # Vérifier que toutes les méthodes ont des docstrings
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                if not attr_value.__doc__:
                    raise ValueError(f"La méthode {attr_name} doit avoir une docstring")
        
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=ValidatedMeta):
    def method_with_doc(self):
        """Cette méthode a une docstring"""
        pass
    
    # def method_without_doc(self):  # ValueError!
    #     pass
```

### TP - ORM simplifié avec métaclasse

**Créez** un mini-ORM :

```python
class Field:
    def __init__(self, field_type):
        self.field_type = field_type

class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        # Collecter les champs
        fields = {}
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, Field):
                fields[attr_name] = attr_value
        
        attrs['_fields'] = fields
        return super().__new__(cls, name, bases, attrs)

class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for field_name in self._fields:
            setattr(self, field_name, kwargs.get(field_name))
    
    def save(self):
        print(f"Sauvegarde de {self.__class__.__name__}")
        for field_name in self._fields:
            print(f"  {field_name}: {getattr(self, field_name)}")

class User(Model):
    name = Field(str)
    age = Field(int)
    email = Field(str)

user = User(name="Alice", age=30, email="alice@example.com")
user.save()
```

## Exercices bonus

### Exercice 14 - Descriptors

**Créez** des descriptors :

```python
class Validator:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} doit être >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} doit être <= {self.max_value}")
        instance.__dict__[self.name] = value

class Person:
    age = Validator(min_value=0, max_value=150)
    
    def __init__(self, age):
        self.age = age

p = Person(30)
# p.age = -5  # ValueError
# p.age = 200  # ValueError
```

## Checklist de validation

- ✅ Itérateurs personnalisés créés
- ✅ Générateurs maîtrisés
- ✅ Héritage multiple et MRO compris
- ✅ Mixins utilisés
- ✅ Context Managers implémentés
- ✅ Classes abstraites (ABC) créées
- ✅ Métaclasses comprises
- ✅ TP Singleton avec métaclasse réalisé
- ✅ TP ORM simplifié implémenté
- ✅ Descriptors explorés (bonus)
