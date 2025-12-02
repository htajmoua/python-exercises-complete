# Calculatrice simple - À annoter avec des types pour Mypy

def addition(a, b):
    """Additionne deux nombres"""
    return a + b


def soustraction(a, b):
    """Soustrait b de a"""
    return a - b


def multiplication(a, b):
    """Multiplie deux nombres"""
    return a * b


def division(a, b):
    """Divise a par b"""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b


def puissance(base, exposant):
    """Calcule base^exposant"""
    return base ** exposant


def moyenne(nombres):
    """Calcule la moyenne d'une liste de nombres"""
    if not nombres:
        return 0
    return sum(nombres) / len(nombres)


def calculer_operation(operation, a, b):
    """Effectue une opération selon le type spécifié"""
    operations = {
        "addition": addition,
        "soustraction": soustraction,
        "multiplication": multiplication,
        "division": division,
    }
    
    if operation not in operations:
        raise ValueError(f"Opération inconnue: {operation}")
    
    return operations[operation](a, b)


class Calculatrice:
    """Classe calculatrice avec historique"""
    
    def __init__(self):
        self.historique = []
    
    def ajouter_operation(self, operation, resultat):
        """Ajoute une opération à l'historique"""
        self.historique.append({
            "operation": operation,
            "resultat": resultat
        })
    
    def get_historique(self):
        """Retourne l'historique des opérations"""
        return self.historique
    
    def effacer_historique(self):
        """Efface l'historique"""
        self.historique = []
