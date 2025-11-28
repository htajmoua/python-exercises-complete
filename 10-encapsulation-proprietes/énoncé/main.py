# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

# Exercice 1 - Attributs protégés
class CompteBancaire:
    def __init__(self, titulaire, solde):
        # À compléter avec attributs protégés
        pass


# Exercice 3 - Décorateur @property
class Personne:
    def __init__(self):
        self._age = 0
    
    @property
    def age(self):
        # À compléter
        pass
    
    @age.setter
    def age(self, valeur):
        # À compléter avec validation
        pass


# Ajoutez vos autres classes...


# Tests
if __name__ == "__main__":
    # Testez vos classes ici
    pass
