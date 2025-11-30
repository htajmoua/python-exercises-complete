# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Module 13 - Projet POO Complet

Choisissez un des 4 projets proposés :
1. Système de gestion de bibliothèque
2. Système de gestion d'école
3. Système de e-commerce
4. Jeu de combat RPG

Implémentez toutes les classes demandées avec :
- Encapsulation (attributs protégés/privés)
- Properties avec validation
- Héritage et polymorphisme
- Méthodes spéciales (__str__, __repr__, etc.)
- Documentation (docstrings)
"""

# ============================================================
# PROJET 1 - SYSTÈME DE GESTION DE BIBLIOTHÈQUE
# ============================================================

class Livre:
    """Représente un livre dans la bibliothèque."""
    
    def __init__(self, titre, auteur, isbn):
        # À compléter
        pass
    
    @property
    def statut(self):
        """Retourne 'Disponible' ou 'Emprunté'"""
        # À compléter
        pass
    
    def emprunter(self):
        """Marque le livre comme emprunté"""
        # À compléter
        pass
    
    def retourner(self):
        """Marque le livre comme disponible"""
        # À compléter
        pass
    
    def __str__(self):
        """Affichage formaté du livre"""
        # À compléter
        pass


class Membre:
    """Représente un membre de la bibliothèque."""
    prochain_numero = 1
    
    def __init__(self, nom):
        # À compléter (auto-incrémenter prochain_numero)
        pass
    
    @property
    def nombre_emprunts(self):
        """Retourne le nombre de livres empruntés"""
        # À compléter
        pass
    
    def peut_emprunter(self):
        """Vérifie si le membre peut emprunter (max 3 livres)"""
        # À compléter
        pass
    
    def __str__(self):
        """Affichage formaté du membre"""
        # À compléter
        pass


class Emprunt:
    """Représente un emprunt de livre."""
    
    def __init__(self, livre, membre, date_emprunt, date_retour_prevue):
        # À compléter
        pass
    
    def calculer_penalite(self):
        """Calcule la pénalité (0.50€ par jour de retard)"""
        # À compléter
        pass
    
    @property
    def est_en_retard(self):
        """Vérifie si l'emprunt est en retard"""
        # À compléter
        pass
    
    def __str__(self):
        """Affichage formaté de l'emprunt"""
        # À compléter
        pass


class Bibliotheque:
    """Gère l'ensemble de la bibliothèque."""
    
    def __init__(self, nom):
        # À compléter
        pass
    
    def ajouter_livre(self, livre):
        """Ajoute un livre à la bibliothèque"""
        # À compléter
        pass
    
    def inscrire_membre(self, nom):
        """Crée et ajoute un nouveau membre"""
        # À compléter
        pass
    
    def emprunter_livre(self, isbn, numero_membre):
        """Gère l'emprunt d'un livre"""
        # À compléter
        pass
    
    def retourner_livre(self, isbn, numero_membre):
        """Gère le retour d'un livre"""
        # À compléter
        pass
    
    def afficher_livres_disponibles(self):
        """Affiche tous les livres disponibles"""
        # À compléter
        pass
    
    def afficher_statistiques(self):
        """Affiche les statistiques de la bibliothèque"""
        # À compléter
        pass


# ============================================================
# PROJET 2 - SYSTÈME DE GESTION D'ÉCOLE
# ============================================================

class Personne:
    """Classe parent pour Etudiant et Professeur."""
    
    def __init__(self, nom, prenom, date_naissance):
        # À compléter
        pass
    
    @property
    def age(self):
        """Calcule l'âge à partir de la date de naissance"""
        # À compléter
        pass
    
    def se_presenter(self):
        """Méthode abstraite - à override"""
        # À compléter
        raise NotImplementedError
    
    def __str__(self):
        """Affichage formaté"""
        # À compléter
        pass


class Etudiant(Personne):
    """Représente un étudiant."""
    
    def __init__(self, nom, prenom, date_naissance, numero_etudiant):
        # À compléter
        pass
    
    @property
    def moyenne_generale(self):
        """Calcule la moyenne de toutes les matières"""
        # À compléter
        pass
    
    def ajouter_note(self, matiere, note):
        """Ajoute une note (validation 0-20)"""
        # À compléter
        pass
    
    def obtenir_mention(self):
        """Retourne la mention selon la moyenne"""
        # À compléter
        pass
    
    def se_presenter(self):
        """Override : présentation d'un étudiant"""
        # À compléter
        pass


class Professeur(Personne):
    """Représente un professeur."""
    matieres_disponibles = ["Mathématiques", "Physique", "Français", "Histoire"]
    
    def __init__(self, nom, prenom, date_naissance, matiere, salaire):
        # À compléter
        pass
    
    def donner_note(self, etudiant, note):
        """Ajoute une note à un étudiant"""
        # À compléter
        pass
    
    def se_presenter(self):
        """Override : présentation d'un professeur"""
        # À compléter
        pass


class Cours:
    """Représente un cours."""
    
    def __init__(self, nom_cours, professeur, capacite_max):
        # À compléter
        pass
    
    def inscrire_etudiant(self, etudiant):
        """Inscrit un étudiant (vérifie la capacité)"""
        # À compléter
        pass
    
    def retirer_etudiant(self, etudiant):
        """Retire un étudiant du cours"""
        # À compléter
        pass
    
    @property
    def nombre_etudiants(self):
        """Retourne le nombre d'étudiants inscrits"""
        # À compléter
        pass
    
    @property
    def est_plein(self):
        """Vérifie si le cours est plein"""
        # À compléter
        pass
    
    def afficher_liste_etudiants(self):
        """Affiche la liste des étudiants"""
        # À compléter
        pass


class Ecole:
    """Gère l'ensemble de l'école."""
    
    def __init__(self, nom):
        # À compléter
        pass
    
    def recruter_professeur(self, professeur):
        """Recrute un professeur"""
        # À compléter
        pass
    
    def inscrire_etudiant(self, etudiant):
        """Inscrit un étudiant"""
        # À compléter
        pass
    
    def creer_cours(self, nom, professeur, capacite):
        """Crée un nouveau cours"""
        # À compléter
        pass
    
    def afficher_tableau_honneur(self):
        """Affiche le top 10 des étudiants"""
        # À compléter
        pass


# ============================================================
# PROJET 3 - SYSTÈME DE E-COMMERCE
# ============================================================

class Produit:
    """Classe de base pour les produits."""
    
    def __init__(self, nom, description, prix, stock, categorie):
        # À compléter
        pass
    
    @property
    def disponible(self):
        """Vérifie si le produit est en stock"""
        # À compléter
        pass
    
    def reduire_stock(self, quantite):
        """Réduit le stock (avec validation)"""
        # À compléter
        pass
    
    def appliquer_reduction(self, pourcentage):
        """Retourne le nouveau prix avec réduction"""
        # À compléter
        pass
    
    def __str__(self):
        """Affichage formaté"""
        # À compléter
        pass
    
    def __repr__(self):
        """Représentation technique"""
        # À compléter
        pass


class ProduitPhysique(Produit):
    """Produit physique avec poids et dimensions."""
    
    def __init__(self, nom, description, prix, stock, categorie, poids, dimensions):
        # À compléter
        pass


class ProduitNumerique(Produit):
    """Produit numérique téléchargeable."""
    
    def __init__(self, nom, description, prix, stock, categorie, taille_fichier, lien_telechargement):
        # À compléter
        pass


class ProduitPerissable(Produit):
    """Produit périssable avec date de péremption."""
    
    def __init__(self, nom, description, prix, stock, categorie, date_peremption):
        # À compléter
        pass
    
    def est_perime(self):
        """Vérifie si le produit est périmé"""
        # À compléter
        pass


class LignePanier:
    """Ligne de panier (produit + quantité)."""
    
    def __init__(self, produit, quantite):
        # À compléter
        pass
    
    @property
    def sous_total(self):
        """Calcule le sous-total (prix × quantité)"""
        # À compléter
        pass
    
    def modifier_quantite(self, nouvelle_quantite):
        """Modifie la quantité"""
        # À compléter
        pass


class Panier:
    """Panier d'achat."""
    
    def __init__(self):
        # À compléter
        pass
    
    def ajouter_produit(self, produit, quantite):
        """Ajoute un produit au panier"""
        # À compléter
        pass
    
    def retirer_produit(self, produit):
        """Retire un produit du panier"""
        # À compléter
        pass
    
    def vider(self):
        """Vide le panier"""
        # À compléter
        pass
    
    @property
    def total_ht(self):
        """Calcule le total HT"""
        # À compléter
        pass
    
    @property
    def total_ttc(self):
        """Calcule le total TTC (TVA 20%)"""
        # À compléter
        pass
    
    def appliquer_code_promo(self, code):
        """Applique un code promo"""
        # À compléter
        pass


class Client:
    """Représente un client."""
    
    def __init__(self, nom, email, adresse):
        # À compléter
        pass
    
    def passer_commande(self):
        """Crée une commande depuis le panier"""
        # À compléter
        pass
    
    @property
    def total_depense(self):
        """Retourne le total des dépenses"""
        # À compléter
        pass


class Commande:
    """Représente une commande."""
    prochain_numero = 1000
    
    def __init__(self, client, lignes, date):
        # À compléter (auto-incrémenter prochain_numero)
        pass
    
    def calculer_frais_livraison(self):
        """Calcule les frais de livraison selon le poids"""
        # À compléter
        pass
    
    def changer_statut(self, nouveau_statut):
        """Change le statut de la commande"""
        # À compléter
        pass
    
    def __str__(self):
        """Affichage formaté"""
        # À compléter
        pass


class PaiementBase:
    """Classe abstraite pour les paiements."""
    
    def traiter(self, montant):
        """Méthode abstraite - à override"""
        # À compléter
        raise NotImplementedError
    
    def rembourser(self, montant):
        """Méthode abstraite - à override"""
        # À compléter
        raise NotImplementedError


class PaiementCarte(PaiementBase):
    """Paiement par carte bancaire."""
    
    def __init__(self, numero_carte):
        # À compléter
        pass
    
    def traiter(self, montant):
        """Override : traite le paiement par carte"""
        # À compléter
        pass
    
    def rembourser(self, montant):
        """Override : rembourse par carte"""
        # À compléter
        pass


class PaiementPaypal(PaiementBase):
    """Paiement par PayPal."""
    
    def __init__(self, email):
        # À compléter
        pass
    
    def traiter(self, montant):
        """Override : traite le paiement PayPal"""
        # À compléter
        pass
    
    def rembourser(self, montant):
        """Override : rembourse par PayPal"""
        # À compléter
        pass


class PaiementVirement(PaiementBase):
    """Paiement par virement bancaire."""
    
    def __init__(self, iban):
        # À compléter
        pass
    
    def traiter(self, montant):
        """Override : traite le virement"""
        # À compléter
        pass
    
    def rembourser(self, montant):
        """Override : rembourse par virement"""
        # À compléter
        pass


# ============================================================
# PROJET 4 - JEU DE COMBAT RPG
# ============================================================

class Statistiques:
    """Représente les statistiques d'un personnage."""
    
    def __init__(self, force, defense, agilite, intelligence):
        # À compléter
        pass
    
    def __add__(self, other):
        """Addition de deux ensembles de stats"""
        # À compléter
        pass
    
    def __str__(self):
        """Affichage formaté"""
        # À compléter
        pass


class Equipement:
    """Représente un équipement."""
    
    def __init__(self, nom, type_equipement, bonus_stats):
        # À compléter
        # Types: "arme", "armure", "accessoire"
        pass
    
    def __str__(self):
        """Affichage formaté"""
        # À compléter
        pass


class Competence:
    """Représente une compétence."""
    
    def __init__(self, nom, cout_mana, puissance, type_competence):
        # À compléter
        # Types: "attaque", "soin", "buff"
        pass
    
    def utiliser(self, lanceur, cible):
        """Utilise la compétence"""
        # À compléter
        pass


class PersonnageRPG:
    """Classe de base pour les personnages RPG."""
    
    def __init__(self, nom, niveau, points_vie, points_mana, stats_base):
        # À compléter
        pass
    
    @property
    def stats_totales(self):
        """Calcule stats_base + bonus équipement"""
        # À compléter
        pass
    
    @property
    def est_vivant(self):
        """Vérifie si le personnage est vivant"""
        # À compléter
        pass
    
    def equiper(self, equipement):
        """Équipe un objet"""
        # À compléter
        pass
    
    def apprendre_competence(self, competence):
        """Apprend une nouvelle compétence"""
        # À compléter
        pass
    
    def attaque_basique(self, cible):
        """Attaque basique basée sur les stats"""
        # À compléter
        pass
    
    def utiliser_competence(self, competence, cible):
        """Utilise une compétence (vérifie le mana)"""
        # À compléter
        pass
    
    def recevoir_degats(self, degats):
        """Reçoit des dégâts (applique la défense)"""
        # À compléter
        pass
    
    def se_soigner(self, montant):
        """Se soigne"""
        # À compléter
        pass
    
    def gagner_experience(self, xp):
        """Gagne de l'expérience (peut monter de niveau)"""
        # À compléter
        pass


class Guerrier(PersonnageRPG):
    """Guerrier avec bonus force."""
    
    def __init__(self, nom, niveau):
        # À compléter - bonus force
        pass


class Mage(PersonnageRPG):
    """Mage avec bonus intelligence et mana."""
    
    def __init__(self, nom, niveau):
        # À compléter - bonus intelligence et mana
        pass


class Paladin(PersonnageRPG):
    """Paladin équilibré."""
    
    def __init__(self, nom, niveau):
        # À compléter - stats équilibrées
        pass


class Assassin(PersonnageRPG):
    """Assassin avec bonus agilité."""
    
    def __init__(self, nom, niveau):
        # À compléter - bonus agilité
        pass


class Combat:
    """Gère un combat entre deux personnages."""
    
    def __init__(self, combattant1, combattant2):
        # À compléter
        pass
    
    def demarrer(self):
        """Lance le combat tour par tour"""
        # À compléter
        pass
    
    def tour(self, attaquant, defenseur):
        """Gère un tour de combat"""
        # À compléter
        pass
    
    def afficher_etat(self):
        """Affiche l'état des deux combattants"""
        # À compléter
        pass
    
    @property
    def est_termine(self):
        """Vérifie si le combat est terminé"""
        # À compléter
        pass
    
    def declarer_vainqueur(self):
        """Annonce le vainqueur"""
        # À compléter
        pass


class Inventaire:
    """Gère l'inventaire d'un personnage."""
    
    def __init__(self, capacite_max):
        # À compléter
        pass
    
    def ajouter(self, objet):
        """Ajoute un objet (vérifie la capacité)"""
        # À compléter
        pass
    
    def retirer(self, objet):
        """Retire un objet"""
        # À compléter
        pass
    
    @property
    def poids_total(self):
        """Calcule le poids total"""
        # À compléter
        pass
    
    def trier_par_type(self):
        """Trie les objets par type"""
        # À compléter
        pass


# ============================================================
# SCRIPT DE DÉMONSTRATION
# ============================================================

if __name__ == "__main__":
    print("=== Module 13 : Projet POO Complet ===\n")
    print("Choisissez un projet et créez un scénario de démonstration complet !\n")
    
    # PROJET 1 - Exemple de démonstration Bibliothèque
    # biblio = Bibliotheque("Bibliothèque Centrale")
    # livre1 = Livre("1984", "George Orwell", "978-0-452-28423-4")
    # biblio.ajouter_livre(livre1)
    # membre1 = biblio.inscrire_membre("Alice Dupont")
    # biblio.emprunter_livre("978-0-452-28423-4", membre1.numero_membre)
    
    # PROJET 2 - Exemple de démonstration École
    # ecole = Ecole("Lycée Victor Hugo")
    # prof1 = Professeur("Martin", "Jean", "1980-05-15", "Mathématiques", 3000)
    # etudiant1 = Etudiant("Durand", "Sophie", "2005-03-20", "E001")
    # ecole.recruter_professeur(prof1)
    # ecole.inscrire_etudiant(etudiant1)
    
    # PROJET 3 - Exemple de démonstration E-commerce
    # client = Client("Alice", "alice@email.com", "123 Rue de Paris")
    # produit1 = ProduitPhysique("Ordinateur", "PC Gaming", 999, 10, "Informatique", 5.0, "40x30x10")
    # client.panier.ajouter_produit(produit1, 1)
    # commande = client.passer_commande()
    
    # PROJET 4 - Exemple de démonstration RPG
    # guerrier = Guerrier("Conan", 5)
    # mage = Mage("Merlin", 5)
    # combat = Combat(guerrier, mage)
    # combat.demarrer()
    
    pass
