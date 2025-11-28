# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

from abc import ABC, abstractmethod
from contextlib import contextmanager

# ============= PARTIE 1 : ITÉRATEURS =============

# Exercice 1 - Itérateur personnalisé
class Compteur:
    """Itérateur simple de compteur"""
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


# Exercice 2 - Itérateur Fibonacci
class Fibonacci:
    """Itérateur pour la suite de Fibonacci"""
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


# Exercice 3 - Générateurs
def fibonacci_generator(n):
    """Générateur pour Fibonacci (plus simple qu'itérateur)"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def nombres_pairs():
    """Générateur infini de nombres pairs"""
    n = 0
    while True:
        yield n
        n += 2


# ============= PARTIE 2 : HÉRITAGE MULTIPLE =============

# Exercice 4 - MRO (Method Resolution Order)
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


# Exercice 6 - Mixins
class JSONMixin:
    """Mixin pour conversion JSON"""
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class XMLMixin:
    """Mixin pour conversion XML"""
    def to_xml(self):
        xml = f"<{self.__class__.__name__}>"
        for key, value in self.__dict__.items():
            xml += f"<{key}>{value}</{key}>"
        xml += f"</{self.__class__.__name__}>"
        return xml


class Person(JSONMixin, XMLMixin):
    """Personne avec mixins de sérialisation"""
    def __init__(self, name, age):
        self.name = name
        self.age = age


# ============= PARTIE 3 : CONTEXT MANAGERS =============

# Exercice 7 - Context Manager basique
class FileManager:
    """Context manager pour fichiers"""
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
        return False


# Exercice 8 - Context Manager avec gestion d'erreurs
class DatabaseConnection:
    """Context manager pour connexion DB"""
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
        return False


# Exercice 9 - Context Manager avec contextlib
@contextmanager
def timer():
    """Context manager pour mesurer le temps"""
    import time
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Temps écoulé : {end - start:.4f}s")


# ============= PARTIE 4 : CLASSES ABSTRAITES (ABC) =============

# Exercice 10 - Classe abstraite basique
class Shape(ABC):
    """Forme géométrique abstraite"""
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return f"Shape with area {self.area()}"


class Rectangle(Shape):
    """Rectangle concret"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


# Exercice 11 - Propriétés abstraites
class Animal(ABC):
    """Animal abstrait"""
    @property
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    """Chien concret"""
    @property
    def sound(self):
        return "Woof!"
    
    def move(self):
        return "Running on four legs"


# ============= PARTIE 5 : MÉTACLASSES =============

# Exercice 13 - Métaclasse personnalisée
class UpperAttrMetaclass(type):
    """Métaclasse qui met les attributs en majuscules"""
    def __new__(cls, name, bases, attrs):
        uppercase_attrs = {}
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith('__'):
                uppercase_attrs[attr_name.upper()] = attr_value
            else:
                uppercase_attrs[attr_name] = attr_value
        
        return super().__new__(cls, name, bases, uppercase_attrs)


class MyClass(metaclass=UpperAttrMetaclass):
    """Classe avec métaclasse"""
    x = 5
    def hello(self):
        return "Hello"


# ============= TP FINAL : MÉTACLASSE SINGLETON =============

class SingletonMeta(type):
    """Métaclasse pour le pattern Singleton"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """Base de données Singleton"""
    def __init__(self):
        print("Initialisation de la base de données")
        self.connection = "Connected"


# TP : Métaclasse de validation
class ValidatedMeta(type):
    """Métaclasse qui valide les docstrings"""
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                if not attr_value.__doc__:
                    raise ValueError(f"La méthode {attr_name} doit avoir une docstring")
        
        return super().__new__(cls, name, bases, attrs)


# TP : ORM simplifié
class Field:
    """Champ de modèle"""
    def __init__(self, field_type):
        self.field_type = field_type


class ModelMeta(type):
    """Métaclasse pour ORM"""
    def __new__(cls, name, bases, attrs):
        fields = {}
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, Field):
                fields[attr_name] = attr_value
        
        attrs['_fields'] = fields
        return super().__new__(cls, name, bases, attrs)


class Model(metaclass=ModelMeta):
    """Modèle de base pour ORM"""
    def __init__(self, **kwargs):
        for field_name in self._fields:
            setattr(self, field_name, kwargs.get(field_name))
    
    def save(self):
        print(f"Sauvegarde de {self.__class__.__name__}")
        for field_name in self._fields:
            print(f"  {field_name}: {getattr(self, field_name)}")


class User(Model):
    """Modèle User"""
    name = Field(str)
    age = Field(int)
    email = Field(str)


# ============= TESTS =============

if __name__ == "__main__":
    print("=== Tests POO Avancée ===\n")
    
    # Test 1 : Itérateurs
    print("Test 1 : Itérateurs")
    for i in Compteur(1, 5):
        print(i, end=" ")
    print()
    
    # Test 2 : Fibonacci
    print("\nTest 2 : Fibonacci (itérateur)")
    for num in Fibonacci(10):
        print(num, end=" ")
    print()
    
    print("\nTest 2bis : Fibonacci (générateur)")
    for num in fibonacci_generator(10):
        print(num, end=" ")
    print()
    
    # Test 3 : MRO
    print("\nTest 3 : MRO (Method Resolution Order)")
    d = D()
    d.methode()
    print(f"MRO: {[cls.__name__ for cls in D.__mro__]}")
    
    # Test 4 : Mixins
    print("\nTest 4 : Mixins")
    p = Person("Alice", 30)
    print(p.to_json())
    print(p.to_xml())
    
    # Test 5 : Context Managers
    print("\nTest 5 : Context Manager")
    with DatabaseConnection("localhost"):
        print("Travail avec la base de données")
    
    # Test 6 : Timer context manager
    print("\nTest 6 : Timer")
    with timer():
        sum(range(1000000))
    
    # Test 7 : Classes abstraites
    print("\nTest 7 : Classes abstraites")
    rect = Rectangle(5, 3)
    print(f"Aire: {rect.area()}")
    print(f"Périmètre: {rect.perimeter()}")
    print(rect.describe())
    
    # Test 8 : Métaclasses
    print("\nTest 8 : Métaclasse UpperAttr")
    obj = MyClass()
    print(f"obj.X = {obj.X}")
    print(f"obj.HELLO() = {obj.HELLO()}")
    
    # TP : Singleton
    print("\n=== TP : Singleton ===")
    db1 = Database()
    db2 = Database()
    print(f"db1 is db2: {db1 is db2}")
    
    # TP : ORM
    print("\n=== TP : ORM simplifié ===")
    user = User(name="Alice", age=30, email="alice@example.com")
    user.save()
