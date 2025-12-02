# Tests pour la calculatrice avec Pytest

import pytest
from calculatrice import (
    addition,
    soustraction,
    multiplication,
    division,
    puissance,
    moyenne,
    calculer_operation,
    Calculatrice,
)


# Tests de base
def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0


def test_soustraction():
    assert soustraction(5, 3) == 2
    assert soustraction(0, 5) == -5
    assert soustraction(10, 10) == 0


def test_multiplication():
    assert multiplication(3, 4) == 12
    assert multiplication(-2, 3) == -6
    assert multiplication(0, 100) == 0


def test_division():
    assert division(10, 2) == 5
    assert division(7, 2) == 3.5
    assert division(-10, 2) == -5


def test_division_par_zero():
    """Test que la division par zéro lève une exception"""
    with pytest.raises(ValueError, match="Division par zéro"):
        division(10, 0)


def test_puissance():
    assert puissance(2, 3) == 8
    assert puissance(5, 0) == 1
    assert puissance(10, 2) == 100


def test_moyenne():
    assert moyenne([1, 2, 3, 4, 5]) == 3
    assert moyenne([10, 20]) == 15
    assert moyenne([5]) == 5
    assert moyenne([]) == 0  # Cas limite


# Tests paramétriques
@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, -1, -2),
    (100, 200, 300),
])
def test_addition_parametrique(a, b, expected):
    assert addition(a, b) == expected


@pytest.mark.parametrize("operation,a,b,expected", [
    ("addition", 5, 3, 8),
    ("soustraction", 10, 4, 6),
    ("multiplication", 3, 7, 21),
    ("division", 15, 3, 5),
])
def test_calculer_operation(operation, a, b, expected):
    assert calculer_operation(operation, a, b) == expected


def test_operation_inconnue():
    """Test avec une opération qui n'existe pas"""
    with pytest.raises(ValueError, match="Opération inconnue"):
        calculer_operation("modulo", 10, 3)


# Tests de la classe Calculatrice
def test_calculatrice_init():
    """Test de l'initialisation"""
    calc = Calculatrice()
    assert calc.get_historique() == []


def test_calculatrice_historique():
    """Test de l'ajout à l'historique"""
    calc = Calculatrice()
    calc.ajouter_operation("2 + 3", 5)
    calc.ajouter_operation("10 - 4", 6)
    
    historique = calc.get_historique()
    assert len(historique) == 2
    assert historique[0]["resultat"] == 5
    assert historique[1]["resultat"] == 6


def test_calculatrice_effacer_historique():
    """Test de l'effacement de l'historique"""
    calc = Calculatrice()
    calc.ajouter_operation("2 + 3", 5)
    calc.effacer_historique()
    assert calc.get_historique() == []


# Fixture pour réutiliser une calculatrice
@pytest.fixture
def calculatrice():
    """Fixture qui fournit une calculatrice fraîche pour chaque test"""
    return Calculatrice()


def test_avec_fixture(calculatrice):
    """Test utilisant la fixture"""
    calculatrice.ajouter_operation("5 * 5", 25)
    assert len(calculatrice.get_historique()) == 1


# Tests de cas limites
class TestCasLimites:
    """Tests des cas limites et edge cases"""
    
    def test_tres_grands_nombres(self):
        assert addition(10**100, 10**100) == 2 * (10**100)
    
    def test_nombres_negatifs(self):
        assert multiplication(-5, -5) == 25
        assert division(-10, -2) == 5
    
    def test_moyenne_liste_vide(self):
        assert moyenne([]) == 0
    
    def test_moyenne_un_element(self):
        assert moyenne([42]) == 42


# TODO: Ajoutez vos propres tests ici
# Exercice : Testez les cas suivants
# - Division avec des nombres décimaux
# - Puissance avec exposant négatif
# - Moyenne avec des nombres négatifs
# - Calculatrice avec beaucoup d'opérations dans l'historique
