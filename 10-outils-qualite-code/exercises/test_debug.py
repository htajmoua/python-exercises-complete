"""
Fichier de test pour apprendre à déboguer avec ipdb
"""

from calculatrice import addition, division, puissance


def test_operations():
    """Fonction de test avec point d'arrêt pour le débogage"""
    
    # Test 1 : Addition simple
    a = 10
    b = 5
    breakpoint()  # Point d'arrêt - explorez les variables a et b
    
    resultat_add = addition(a, b)
    print(f"Addition: {a} + {b} = {resultat_add}")
    
    # Test 2 : Division
    x = 20
    y = 4
    resultat_div = division(x, y)
    print(f"Division: {x} / {y} = {resultat_div}")
    
    # Test 3 : Puissance
    base = 2
    exp = 3
    resultat_pow = puissance(base, exp)
    print(f"Puissance: {base}^{exp} = {resultat_pow}")
    
    return resultat_add, resultat_div, resultat_pow


def test_erreur():
    """Test avec une erreur intentionnelle pour l'analyse post-mortem"""
    try:
        # Ceci va générer une erreur
        resultat = division(10, 0)
        print(f"Résultat: {resultat}")
    except Exception as e:
        print(f"Erreur capturée: {e}")
        # Décommentez la ligne suivante pour l'analyse post-mortem
        # import ipdb; ipdb.post_mortem()
        raise


if __name__ == "__main__":
    print("=== Test des opérations ===")
    test_operations()
    
    print("\n=== Test avec erreur ===")
    # Décommentez pour tester l'analyse post-mortem
    # test_erreur()
