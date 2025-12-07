# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

# Exercice 1 - Sets : Opérations et propriétés
def tester_sets_operations():
    """Testez les opérations sur les sets"""
    # Créez deux sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    # À compléter : testez les opérations suivantes
    # 1. Union : set1 | set2 ou set1.union(set2)
    # 2. Intersection : set1 & set2 ou set1.intersection(set2)
    # 3. Différence : set1 - set2 ou set1.difference(set2)
    # 4. Différence symétrique : set1 ^ set2 ou set1.symmetric_difference(set2)
    # 5. Testez issubset, issuperset, isdisjoint
    # 6. Ajoutez/supprimez des éléments avec add(), remove(), discard()
    pass


def comparer_performance_set_vs_liste():
    """Compare la performance de recherche entre set et liste"""
    import timeit
    
    # À compléter :
    # 1. Créez une liste de 10000 éléments : liste = list(range(10000))
    # 2. Créez un set avec les mêmes éléments : ensemble = set(range(10000))
    # 3. Cherchez un élément (ex: 9999) dans la liste et le set
    # 4. Utilisez timeit pour mesurer :
    #    temps_liste = timeit.timeit(lambda: 9999 in liste, number=10000)
    #    temps_set = timeit.timeit(lambda: 9999 in ensemble, number=10000)
    # 5. Affichez la différence de performance
    pass


# Exercice 2 - Sets avancés : frozenset et cas d'usage
def tester_frozenset():
    """Testez les frozensets"""
    # À compléter :
    # 1. Créez un frozenset : fs = frozenset([1, 2, 3, 4])
    # 2. Essayez de le modifier avec add() ou remove() - vous aurez une erreur !
    # 3. Utilisez un frozenset comme clé de dictionnaire :
    #    dict_avec_frozenset = {frozenset([1, 2]): "valeur1"}
    # 4. Créez un set de frozensets (impossible avec des sets normaux) :
    #    set_de_sets = {frozenset([1, 2]), frozenset([3, 4])}
    pass


def elements_uniques_plusieurs_listes(*listes):
    """Retourne les éléments présents dans une seule liste
    
    Utilisez les opérations d'ensembles pour trouver les éléments
    qui sont dans une liste mais pas dans les autres.
    """
    # Hints :
    # 1. Convertissez chaque liste en set
    # 2. Pour chaque set, trouvez les éléments qui ne sont dans aucun autre set
    # 3. Utilisez la différence : set1 - set2 - set3 ...
    # Exemple : si listes = ([1,2,3], [2,3,4], [3,4,5])
    #           éléments uniques à la première liste : {1}
    #           tous les éléments uniques : {1, 5}
    # 4. Utilisez set.union() ou | pour combiner tous les résultats
    pass


def valider_entree(valeur, valeurs_autorisees):
    """Valide si une valeur est dans un ensemble de valeurs autorisées
    
    Utilisez un set pour une validation rapide O(1).
    """
    # Hints :
    # 1. Convertissez valeurs_autorisees en set si ce n'est pas déjà un set
    #    (pour garantir la performance O(1))
    # 2. Vérifiez : return valeur in valeurs_autorisees
    # Exemple d'utilisation :
    #   valeurs_valides = {1, 2, 3, 4, 5}
    #   valider_entree(3, valeurs_valides)  # True
    #   valider_entree(10, valeurs_valides)  # False
    pass


# Exercice 3 - Protocole d'itération et itérateurs
class CompteurIterateur:
    """Itérateur personnalisé qui compte de debut à fin
    
    Un itérateur doit implémenter :
    - __iter__() : retourne self
    - __next__() : retourne le prochain élément ou lève StopIteration
    """
    def __init__(self, debut, fin):
        self.debut = debut
        self.fin = fin
        # À compléter : initialiser un compteur actuel
        pass
    
    def __iter__(self):
        """Retourne l'itérateur lui-même"""
        # À compléter
        pass
    
    def __next__(self):
        """Retourne le prochain nombre ou lève StopIteration"""
        # À compléter :
        # 1. Vérifier si on a atteint la fin
        # 2. Si oui, lever StopIteration
        # 3. Sinon, retourner la valeur actuelle et incrémenter
        pass


def tester_iterateur():
    """Testez votre itérateur personnalisé"""
    print("Test de l'itérateur :")
    # Hints :
    # 1. Créez une instance : compteur = CompteurIterateur(1, 5)
    # 2. Utilisez-la dans une boucle for :
    #    for nombre in compteur:
    #        print(nombre)
    # 3. Résultat attendu : 1, 2, 3, 4, 5
    # 4. Testez aussi avec next() manuellement :
    #    it = CompteurIterateur(1, 3)
    #    print(next(it))  # 1
    #    print(next(it))  # 2
    #    print(next(it))  # 3
    #    print(next(it))  # StopIteration
    pass


# Exercice 4 - Générateurs avec yield
def fibonacci(n):
    """Générateur qui produit les n premiers nombres de Fibonacci
    
    Suite de Fibonacci : 0, 1, 1, 2, 3, 5, 8, 13, ...
    Chaque nombre est la somme des deux précédents.
    
    Utilisez yield pour retourner chaque nombre un par un.
    """
    # Hints :
    # 1. Initialisez les deux premiers nombres : a, b = 0, 1
    # 2. Bouclez n fois
    # 3. À chaque itération :
    #    - yield a (retourne la valeur actuelle)
    #    - Calculez le suivant : a, b = b, a + b
    # Exemple de structure :
    #   a, b = 0, 1
    #   for _ in range(n):
    #       yield a
    #       a, b = b, a + b
    pass


def nombres_pairs(max_valeur):
    """Générateur qui produit tous les nombres pairs de 0 à max_valeur
    
    Exemple : nombres_pairs(10) génère 0, 2, 4, 6, 8, 10
    """
    # Hints :
    # Méthode 1 (simple) : Boucle avec range et step=2
    #   for i in range(0, max_valeur + 1, 2):
    #       yield i
    #
    # Méthode 2 : Boucle avec condition
    #   for i in range(max_valeur + 1):
    #       if i % 2 == 0:
    #           yield i
    #
    # La méthode 1 est plus efficace (pas de test à chaque itération)
    pass


def lire_lignes_fichier(chemin_fichier):
    """Générateur qui lit un fichier ligne par ligne
    
    Avantage : ne charge pas tout le fichier en mémoire.
    Utilisez yield pour retourner chaque ligne.
    """
    # À compléter :
    # 1. Ouvrir le fichier avec 'with open(...) as f:'
    # 2. Pour chaque ligne, yield la ligne
    pass


def tester_generateurs():
    """Testez vos générateurs"""
    print("\nTest des générateurs :")
    
    # Test Fibonacci
    print("Fibonacci (10 premiers) :")
    # À compléter : afficher les 10 premiers nombres de Fibonacci
    
    # Test nombres pairs
    print("\nNombres pairs jusqu'à 20 :")
    # À compléter : afficher tous les nombres pairs jusqu'à 20
    
    pass


# Exercice 5 - Expressions génératrices et optimisation
def comparer_memoire():
    """Compare l'utilisation mémoire entre list comprehension et expression génératrice"""
    import sys
    
    # List comprehension - crée toute la liste
    liste = [x**2 for x in range(10000)]
    taille_liste = sys.getsizeof(liste)
    
    # Expression génératrice - crée un générateur
    gen = (x**2 for x in range(10000))
    taille_gen = sys.getsizeof(gen)
    
    print(f"Taille de la liste : {taille_liste} bytes")
    print(f"Taille du générateur : {taille_gen} bytes")
    print(f"Différence : {taille_liste - taille_gen} bytes")
    print(f"Ratio : {taille_liste / taille_gen:.1f}x")


def somme_carres_pairs(n):
    """Calcule la somme des carrés des nombres pairs de 0 à n
    
    Utilisez une expression génératrice avec sum().
    Ne créez PAS de liste intermédiaire.
    """
    # À compléter : return sum(...)
    pass


def pipeline_generateurs():
    """Démonstration d'un pipeline de générateurs
    
    Créez un pipeline qui :
    1. Génère les nombres de 0 à 100
    2. Garde seulement les nombres divisibles par 3
    3. Calcule le carré de chaque nombre
    4. Somme le tout
    
    Tout cela sans créer de listes intermédiaires !
    """
    # Hint : Vous pouvez chaîner plusieurs expressions génératrices,
    # ou tout combiner en une seule expression avec sum() et une condition if.
    # Résultat attendu : 171700
    pass


def tester_expressions_generatrices():
    """Testez les expressions génératrices"""
    print("\nTest des expressions génératrices :")
    
    print("\nComparaison mémoire :")
    comparer_memoire()
    
    # Test somme carrés pairs
    print(f"\nSomme des carrés des pairs jusqu'à 100 : {somme_carres_pairs(100)}")
    
    # Test pipeline
    print(f"Pipeline de générateurs : {pipeline_generateurs()}")


# Exercice 6 - Affectation par référence vs copie
import copy

def test_references():
    """Testez la différence entre référence et copie"""
    list1 = [1, 2, 3]
    list2 = list1  # Référence
    list3 = list1.copy()  # Copie superficielle
    list4 = copy.deepcopy([[1, 2], [3, 4]])  # Copie profonde
    
    # À compléter
    pass


# Exercice 7 - Types mutables vs immutables
def est_mutable(obj):
    """Retourne True si un objet est mutable, False sinon
    
    Astuce : Les objets immutables sont hashables (sauf exceptions).
    Utilisez hash() dans un try/except.
    """
    # À compléter
    pass


def test_mutabilite():
    """Testez les types mutables et immutables"""
    # À compléter
    pass


# Exercice 8 - Passage d'arguments avancé
def somme_flexible(*args):
    """Fonction avec *args : accepte un nombre variable d'arguments"""
    # À compléter : calculez la somme de tous les arguments
    pass


def afficher_infos(**kwargs):
    """Fonction avec **kwargs : accepte un nombre variable d'arguments nommés"""
    # À compléter : affichez toutes les paires clé-valeur
    pass


def fonction_complete(a, b, *args, c=10, **kwargs):
    """Fonction combinant tous les types d'arguments"""
    # À compléter : affichez a, b, args, c, kwargs
    pass


def ajouter_element_mauvais(element, liste=[]):
    """PIÈGE ! Ne jamais utiliser [] comme valeur par défaut
    
    Cette fonction a un bug classique : la liste par défaut est partagée
    entre tous les appels de la fonction.
    """
    liste.append(element)
    return liste


def ajouter_element_correct(element, liste=None):
    """Version correcte : utilisez None et créez la liste dans la fonction"""
    if liste is None:
        liste = []
    liste.append(element)
    return liste


# Exercice 9 - Variables de classe vs d'instance
class Compteur:
    """Classe pour comprendre les variables de classe"""
    total = 0  # Variable de classe (partagée par toutes les instances)
    
    def __init__(self, nom):
        self.nom = nom  # Variable d'instance (unique à chaque instance)
        # À compléter : incrémentez le compteur total
        pass
    
    @classmethod
    def afficher_total(cls):
        """Méthode de classe pour afficher le nombre total d'instances"""
        # À compléter : retournez cls.total
        pass


# Exercice 10 - Slices avancés
def tester_slices():
    """Maîtrisez les slices"""
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Basique
    print(lst[2:5])
    print(lst[::-1])  # Inversion
    
    # À compléter avec d'autres exemples
    pass


# Exercice 11 - Introspection
def explorer_objet(obj):
    """Utilisez dir(), type(), hasattr(), etc."""
    print(f"Type: {type(obj)}")
    print(f"Attributs: {dir(obj)}")
    # À compléter
    pass


# Exercice 12 - Clause else dans les structures
def chercher_avec_else(liste, valeur):
    """Utilisez la clause else avec for"""
    for item in liste:
        if item == valeur:
            print(f"Trouvé : {item}")
            break
    else:
        print("Non trouvé")


# TP FINAL - Intersection de listes
def intersection_v1_boucles(list1, list2):
    """Méthode 1 : Boucles imbriquées - O(n*m)
    
    Parcourez list1 et vérifiez si chaque élément est dans list2.
    Attention aux doublons dans le résultat !
    """
    # À compléter
    pass


def intersection_v2_set(list1, list2):
    """Méthode 2 : Set - O(n+m)
    
    Utilisez l'opérateur & entre deux sets.
    N'oubliez pas de reconvertir en liste.
    """
    # À compléter
    pass


def intersection_v3_comprehension(list1, list2):
    """Méthode 3 : List comprehension avec set - O(n+m)
    
    Convertissez list2 en set d'abord (recherche O(1)).
    Puis utilisez une list comprehension sur list1.
    Avantage : préserve l'ordre de list1.
    """
    # À compléter
    pass


def intersection_v4_builtin(list1, list2):
    """Méthode 4 : Built-in (le plus rapide)
    
    Utilisez la méthode .intersection() des sets.
    """
    # À compléter
    pass


# Tests et benchmarks
if __name__ == "__main__":
    print("=== Tests Python Avancé ===\n")
    
    # Test 1 : Sets
    print("Test 1 : Opérations sur les sets")
    tester_sets_operations()
    
    # Test 2 : frozensets
    print("\nTest 2 : frozensets et cas d'usage")
    tester_frozenset()
    
    # Test 3 : Itérateurs
    print("\nTest 3 : Itérateurs")
    tester_iterateur()
    
    # Test 4 : Générateurs
    print("\nTest 4 : Générateurs")
    tester_generateurs()
    
    # Test 5 : Expressions génératrices
    print("\nTest 5 : Expressions génératrices")
    tester_expressions_generatrices()
    
    # Test 6 : Références
    print("\nTest 6 : Références et copies")
    test_references()
    
    # Test 7 : Mutabilité
    print("\nTest 7 : Mutabilité")
    test_mutabilite()
    
    # Test 8 : Piège des arguments par défaut mutables
    print("\nTest 8 : Piège des arguments par défaut mutables")
    print("Version MAUVAISE :")
    print(ajouter_element_mauvais(1))  # [1]
    print(ajouter_element_mauvais(2))  # [1, 2] - Oups ! Liste partagée
    print("\nVersion CORRECTE :")
    print(ajouter_element_correct(1))  # [1]
    print(ajouter_element_correct(2))  # [2] - Correct !
    
    # Test 9 : Slices
    print("\nTest 9 : Slices")
    tester_slices()
    
    # TP : Comparer les performances
    print("\n=== TP : Intersection de listes ===")
    print("ATTENTION : Implémentez d'abord les 4 fonctions d'intersection avant de lancer le benchmark !\n")
    
    import timeit
    
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    
    # Décommentez ces lignes une fois vos fonctions implémentées
    # for i, func in enumerate([intersection_v1_boucles, intersection_v2_set, 
    #                            intersection_v3_comprehension, intersection_v4_builtin], 1):
    #     time = timeit.timeit(lambda: func(list1, list2), number=1000)
    #     print(f"Méthode {i} ({func.__name__}): {time:.4f}s")
