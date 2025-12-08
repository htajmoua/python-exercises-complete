# Instructions - POO Avancée

Ce module couvre les concepts avancés de la Programmation Orientée Objet en Python : héritage multiple, context managers et métaclasses.

## Partie 1 - Héritage Multiple

### Exercice 1 - MRO (Method Resolution Order)

**Objectif** : Comprendre l'ordre de résolution des méthodes en héritage multiple

**Concept** : Le MRO (Method Resolution Order) détermine l'ordre dans lequel Python cherche les méthodes dans une hiérarchie de classes.

**Structure à créer** :
```python
class A:
    def methode(self):
        # TODO: Afficher "Méthode de A"

class B(A):  # Hérite de A
    def methode(self):
        # TODO: Afficher "Méthode de B"
        # TODO: Appeler la méthode parente avec super()

class C(A):  # Hérite de A
    def methode(self):
        # TODO: Afficher "Méthode de C"
        # TODO: Appeler la méthode parente avec super()

class D(B, C):  # Héritage multiple
    def methode(self):
        # TODO: Afficher "Méthode de D"
        # TODO: Appeler la méthode parente avec super()
```

**Syntaxe super()** : Appelle la méthode suivante dans le MRO

**Pour visualiser le MRO** :
```python
print(D.__mro__)  # ou D.mro()
```

**Ordre attendu** : D → B → C → A

## Partie 2 - Context Managers

### Exercice 2 - Context Manager basique

**Objectif** : Implémenter un context manager avec `__enter__` et `__exit__`

**Concept** : Un context manager gère automatiquement l'allocation et la libération de ressources.

**Syntaxe** :
```python
class MonContextManager:
    def __enter__(self):
        # TODO: Initialiser/acquirir la ressource
        # TODO: Retourner la ressource
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Libérer/nettoyer la ressource
        # return False pour propager les exceptions
        pass
```

**À faire - Créer FileManager** :

1. **`__init__`** :
   - Paramètres : `filename`, `mode`
   - Sauvegarder les paramètres
   - Initialiser `self.file = None`

2. **`__enter__`** :
   - Ouvrir le fichier : `self.file = open(...)`
   - Retourner `self.file`

3. **`__exit__`** :
   - Vérifier si `self.file` existe
   - Fermer le fichier
   - Retourner `False`

**Utilisation** :
```python
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
# Le fichier est automatiquement fermé
```

### Exercice 3 - Context Manager avec contextlib

**Objectif** : Utiliser `@contextmanager` pour simplifier la création

**Concept** : `@contextmanager` transforme un générateur en context manager.

**Syntaxe** :
```python
from contextlib import contextmanager

@contextmanager
def mon_context():
    # Code AVANT (comme __enter__)
    try:
        yield valeur  # Valeur retournée au with
    finally:
        # Code APRÈS (comme __exit__)
        pass
```

**À faire** :

1. **Créer un timer** :
   ```python
   @contextmanager
   def timer():
       # TODO: Importer time
       # TODO: Sauvegarder start = time.time()
       try:
           yield  # Pas de valeur à retourner
       finally:
           # TODO: Calculer et afficher le temps écoulé
   ```

2. **Créer un gestionnaire de fichier** :
   ```python
   @contextmanager
   def open_file(filename, mode):
       # TODO: Ouvrir le fichier
       try:
           yield f  # Retourne le fichier
       finally:
           # TODO: Fermer le fichier
   ```

**Test** :
```python
with timer():
    sum(range(1000000))  # Mesure le temps

with open_file('test.txt', 'w') as f:
    f.write('Test')  # Fichier auto-fermé
```

## Partie 3 - Métaclasses

### Exercice 4 - Comprendre les métaclasses

**Objectif** : Découvrir que `type` est la métaclasse par défaut

**Concept** : En Python, tout est objet, même les classes ! Une métaclasse est "une classe de classe".

**Syntaxe de `type()` pour créer une classe** :
```python
MaClasse = type('NomClasse', (BaseClasses,), {'attribut': valeur})
```

**À faire** :

1. **Créer une classe avec `type()`** :
   ```python
   # TODO: Créer MyClass avec type()
   # - Nom : 'MyClass'
   # - Pas de classe de base : ()
   # - Attributs : {'x': 5, 'method': lambda self: "Hello"}
   MyClass = type(...)
   
   obj = MyClass()
   # TODO: Afficher obj.x et obj.method()
   ```

2. **Explorer la hiérarchie** :
   ```python
   class NormalClass:
       pass
   
   # TODO: Afficher type(NormalClass)
   # TODO: Afficher type(type)
   # Résultat : type est sa propre métaclasse !
   ```

**Conclusion** : `type` crée les classes, c'est la métaclasse par défaut.

## TP Final - Métaclasse Singleton

**Objectif** : Implémenter le pattern Singleton avec une métaclasse

**Concept** : Un Singleton garantit qu'une classe n'a qu'une seule instance.

**Principe** : Redéfinir `__call__` dans la métaclasse pour contrôler la création d'instances.

**À faire** :

1. **Créer SingletonMeta** :
   ```python
   class SingletonMeta(type):
       # TODO: Créer un attribut de classe _instances = {}
       
       def __call__(cls, *args, **kwargs):
           # TODO: Vérifier si cls est dans cls._instances
           # TODO: Si non :
           #       - Créer instance avec super().__call__(*args, **kwargs)
           #       - Sauvegarder dans cls._instances[cls]
           # TODO: Retourner cls._instances[cls]
   ```

2. **Utiliser SingletonMeta** :
   ```python
   class Database(metaclass=SingletonMeta):
       def __init__(self):
           print("Initialisation de la base de données")
           self.connection = "Connected"
   ```

**Test** :
```python
db1 = Database()  # Affiche "Initialisation..."
db2 = Database()  # N'affiche rien
print(db1 is db2)  # True - même instance !
print(id(db1) == id(db2))  # True
```

**Explication** : `__call__` est appelé quand on fait `Database()`. La métaclasse intercepte cet appel.

## Checklist de validation

-  Héritage multiple et MRO compris
-  Context Managers implémentés (basique et contextlib)
-  Métaclasses comprises (type)
-  TP Singleton avec métaclasse réalisé
