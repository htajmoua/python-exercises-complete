# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

"""
Module 09 - Expressions Régulières et Bases de Données
Exercices sur regex et SQLite
"""

import re
import sqlite3
from datetime import datetime
import os

# ============= PARTIE 1 : EXPRESSIONS RÉGULIÈRES =============

# Exercice 1 : Validation
def valider_email(email):
    """Valide une adresse email"""
    # À compléter
    pass


def valider_telephone(telephone):
    """Valide un numéro de téléphone français"""
    # Formats acceptés: 06 12 34 56 78, 06-12-34-56-78, 0612345678
    # À compléter
    pass


def valider_code_postal(code_postal):
    """Valide un code postal français (5 chiffres)"""
    # À compléter
    pass


def valider_date(date_str):
    """Valide une date au format JJ/MM/AAAA"""
    # À compléter
    pass


# Exercice 2 : Extraction
def extraire_emails(texte):
    """Extrait tous les emails d'un texte"""
    # À compléter
    pass


def extraire_telephones(texte):
    """Extrait tous les numéros de téléphone"""
    # À compléter
    pass


def extraire_urls(texte):
    """Extrait toutes les URLs"""
    # À compléter
    pass


# Exercice 3 : Remplacement
def masquer_carte_bancaire(numero):
    """Masque un numéro de carte bancaire"""
    # Garde seulement les 4 derniers chiffres
    # À compléter
    pass


def nettoyer_texte(texte):
    """Supprime les caractères spéciaux"""
    # À compléter
    pass


def convertir_date_format(date_str):
    """Convertit JJ/MM/AAAA en AAAA-MM-JJ"""
    # À compléter
    pass


# Exercice 4 : Validation de mot de passe
def valider_mot_de_passe(mdp):
    """
    Vérifie qu'un mot de passe contient:
    - Au moins 8 caractères
    - Au moins une majuscule
    - Au moins une minuscule
    - Au moins un chiffre
    - Au moins un caractère spécial
    """
    # À compléter
    pass


# Exercice 5 : Parsing de logs
def parser_log(ligne_log):
    """Parse une ligne de log"""
    # À compléter
    pass


def extraire_ips(texte):
    """Extrait les adresses IP d'un texte"""
    # À compléter
    pass


# ============= PARTIE 2 : BASE DE DONNÉES SQLITE =============

class BibliothequeDB:
    """Classe pour gérer la base de données de la bibliothèque"""
    
    def __init__(self, db_name='bibliotheque.db'):
        """Initialise la connexion à la base de données"""
        self.db_name = db_name
        self.conn = None
        self.cursor = None
    
    def connecter(self):
        """Établit la connexion à la base de données"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
    
    def deconnecter(self):
        """Ferme la connexion"""
        if self.conn:
            self.conn.close()
    
    def creer_tables(self):
        """Crée les tables de la bibliothèque"""
        # Table auteurs
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS auteurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                date_naissance TEXT,
                nationalite TEXT
            )
        ''')
        
        # Table livres
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livres (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT NOT NULL,
                auteur_id INTEGER,
                annee_publication INTEGER,
                isbn TEXT UNIQUE,
                genre TEXT,
                FOREIGN KEY (auteur_id) REFERENCES auteurs(id)
            )
        ''')
        
        # Table emprunts
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS emprunts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                livre_id INTEGER,
                emprunteur TEXT NOT NULL,
                date_emprunt TEXT NOT NULL,
                date_retour TEXT,
                statut TEXT DEFAULT 'en_cours',
                FOREIGN KEY (livre_id) REFERENCES livres(id)
            )
        ''')
        
        self.conn.commit()
        print("Tables créées avec succès !")
    
    def inserer_donnees_exemple(self):
        """Insère des données d'exemple"""
        # Insérer des auteurs
        auteurs = [
            ('Hugo', 'Victor', '1802-02-26', 'Française'),
            ('Camus', 'Albert', '1913-11-07', 'Française'),
            ('Rowling', 'J.K.', '1965-07-31', 'Britannique'),
            ('Orwell', 'George', '1903-06-25', 'Britannique'),
            ('Saint-Exupéry', 'Antoine de', '1900-06-29', 'Française'),
            ('Dumas', 'Alexandre', '1802-07-24', 'Française'),
            ('Zola', 'Émile', '1840-04-02', 'Française')
        ]
        
        self.cursor.executemany('''
            INSERT INTO auteurs (nom, prenom, date_naissance, nationalite)
            VALUES (?, ?, ?, ?)
        ''', auteurs)
        
        # Insérer des livres
        livres = [
            ('Les Misérables', 1, 1862, '978-2-253-09633-4', 'Roman'),
            ('Notre-Dame de Paris', 1, 1831, '978-2-253-00699-0', 'Roman'),
            ('L\'Étranger', 2, 1942, '978-2-07-036002-4', 'Roman'),
            ('La Peste', 2, 1947, '978-2-07-036001-7', 'Roman'),
            ('Harry Potter à l\'école des sorciers', 3, 1997, '978-2-07-054120-0', 'Fantasy'),
            ('Harry Potter et la Chambre des secrets', 3, 1998, '978-2-07-054121-7', 'Fantasy'),
            ('1984', 4, 1949, '978-0-452-28423-4', 'Dystopie'),
            ('La Ferme des animaux', 4, 1945, '978-2-07-037516-5', 'Fable'),
            ('Le Petit Prince', 5, 1943, '978-2-07-061275-8', 'Conte'),
            ('Vol de nuit', 5, 1931, '978-2-07-036088-8', 'Roman'),
            ('Les Trois Mousquetaires', 6, 1844, '978-2-253-00811-6', 'Aventure'),
            ('Le Comte de Monte-Cristo', 6, 1844, '978-2-253-09811-6', 'Aventure'),
            ('Germinal', 7, 1885, '978-2-253-00429-3', 'Roman'),
            ('L\'Assommoir', 7, 1877, '978-2-253-00428-6', 'Roman')
        ]
        
        self.cursor.executemany('''
            INSERT INTO livres (titre, auteur_id, annee_publication, isbn, genre)
            VALUES (?, ?, ?, ?, ?)
        ''', livres)
        
        # Insérer des emprunts
        emprunts = [
            (1, 'Alice Dupont', '2024-11-01', '2024-11-15', 'retourné'),
            (3, 'Bob Martin', '2024-11-10', None, 'en_cours'),
            (5, 'Charlie Bernard', '2024-11-15', None, 'en_cours'),
            (7, 'Diana Laurent', '2024-11-05', '2024-11-20', 'retourné'),
            (9, 'Emma Petit', '2024-11-20', None, 'en_cours'),
            (2, 'Frank Dubois', '2024-10-15', '2024-11-01', 'retourné'),
            (11, 'Grace Moreau', '2024-11-18', None, 'en_cours')
        ]
        
        self.cursor.executemany('''
            INSERT INTO emprunts (livre_id, emprunteur, date_emprunt, date_retour, statut)
            VALUES (?, ?, ?, ?, ?)
        ''', emprunts)
        
        self.conn.commit()
        print("Données d'exemple insérées avec succès !")
        print(f"- {len(auteurs)} auteurs")
        print(f"- {len(livres)} livres")
        print(f"- {len(emprunts)} emprunts")
    
    # Exercice 8 : Requêtes SELECT
    def afficher_tous_livres(self):
        """Affiche tous les livres"""
        # TODO : Sélectionnez tous les livres
        # Template :
        # self.cursor.execute('SELECT * FROM livres')
        # livres = self.cursor.fetchall()
        # 
        # for livre in livres:
        #     print(f"[{livre[0]}] {livre[1]} - Année: {livre[3]}")
        # 
        # return livres
        pass
    
    def livres_par_auteur(self, auteur_id):
        """Affiche les livres d'un auteur"""
        # TODO : Sélectionnez les livres d'un auteur spécifique
        # Template :
        # self.cursor.execute('''
        #     SELECT * FROM livres
        #     WHERE auteur_id = ?
        # ''', (auteur_id,))
        # livres = self.cursor.fetchall()
        # 
        # for livre in livres:
        #     print(f"  - {livre[1]} ({livre[3]})")
        # 
        # return livres
        pass
    
    def livres_apres_annee(self, annee):
        """Livres publiés après une année"""
        # TODO : Sélectionnez les livres publiés après une année donnée
        # Template :
        # self.cursor.execute('''
        #     SELECT * FROM livres
        #     WHERE annee_publication > ?
        # ''', (annee,))
        # livres = self.cursor.fetchall()
        # 
        # for livre in livres:
        #     print(f"  - {livre[1]} ({livre[3]})")
        # 
        # return livres
        pass
    
    def emprunts_en_cours(self):
        """Emprunts actuellement en cours"""
        # TODO : Sélectionnez les emprunts avec statut = 'en_cours'
        # Template :
        # self.cursor.execute('''
        #     SELECT * FROM emprunts
        #     WHERE statut = ?
        # ''', ('en_cours',))
        # emprunts = self.cursor.fetchall()
        # 
        # for emprunt in emprunts:
        #     print(f"  Livre #{emprunt[1]} emprunté par {emprunt[2]} le {emprunt[3]}")
        # 
        # return emprunts
        pass
    
    # Exercice 9 : Jointures
    def livres_avec_auteurs(self):
        """Livres avec nom de l'auteur"""
        # TODO : Jointure entre livres et auteurs
        # Template :
        # self.cursor.execute('''
        #     SELECT livres.titre, auteurs.nom, auteurs.prenom, livres.annee_publication
        #     FROM livres
        #     JOIN auteurs ON livres.auteur_id = auteurs.id
        # ''')
        # resultats = self.cursor.fetchall()
        # 
        # for livre in resultats:
        #     print(f"  - {livre[0]} par {livre[1]} {livre[2]} ({livre[3]})")
        # 
        # return resultats
        pass
    
    def emprunts_avec_details(self):
        """Emprunts avec détails du livre et auteur"""
        # TODO : Jointure entre emprunts, livres et auteurs
        # Template :
        # self.cursor.execute('''
        #     SELECT emprunts.emprunteur, livres.titre, auteurs.nom, auteurs.prenom,
        #            emprunts.date_emprunt, emprunts.statut
        #     FROM emprunts
        #     JOIN livres ON emprunts.livre_id = livres.id
        #     JOIN auteurs ON livres.auteur_id = auteurs.id
        # ''')
        # resultats = self.cursor.fetchall()
        # 
        # for emprunt in resultats:
        #     print(f"  - {emprunt[0]} a emprunté '{emprunt[1]}' de {emprunt[2]} {emprunt[3]} ({emprunt[5]})")
        # 
        # return resultats
        pass
    
    # ============= PARTIE 3 : COMBINAISON REGEX ET BASE DE DONNÉES =============
    
    # Exercice 10 : Recherche avancée avec regex
    def rechercher_livres_par_titre(self, pattern):
        """Recherche des livres dont le titre correspond à un pattern regex"""
        # Pattern fourni pour vous aider
        # Exemple : r'harry.*potter' (insensible à la casse)
        
        # ÉTAPE 1 : Récupérer tous les livres
        self.cursor.execute('SELECT id, titre, auteur_id, annee_publication, genre FROM livres')
        tous_les_livres = self.cursor.fetchall()
        
        # ÉTAPE 2 : Filtrer avec regex
        # TODO : Utilisez re.search() ou re.match() pour filtrer
        # Compilez le pattern avec re.IGNORECASE pour ignorer la casse
        
        # Exemple de structure :
        # import re
        # regex = re.compile(pattern, re.IGNORECASE)
        # livres_trouves = []
        # for livre in tous_les_livres:
        #     if regex.search(livre[1]):  # livre[1] est le titre
        #         livres_trouves.append(livre)
        # return livres_trouves
        
        pass
    
    def rechercher_auteurs_par_pays(self, pattern_pays):
        """Recherche des auteurs selon un pattern de nationalité"""
        # Pattern fourni : r'Fran[cç]ais[e]?' pour Français/Française
        
        # TODO : Récupérer les auteurs et filtrer par nationalité
        # self.cursor.execute('SELECT * FROM auteurs')
        # Appliquez le pattern regex sur la colonne nationalite
        
        pass
    
    def emprunts_par_periode(self, pattern_date):
        """Trouve les emprunts selon un pattern de date"""
        # Pattern fourni : r'2024-11-.*' pour novembre 2024
        # Pattern : r'2024-.*' pour toute l'année 2024
        
        # TODO : Récupérer les emprunts et filtrer par date
        # self.cursor.execute('SELECT * FROM emprunts')
        # Appliquez le pattern sur date_emprunt
        
        pass
    
    # Statistiques
    def afficher_statistiques(self):
        """Affiche des statistiques sur la bibliothèque"""
        # TODO : Comptez les livres, auteurs, emprunts en cours
        # Utilisez des requêtes SELECT COUNT(*)
        pass


# ============= TESTS =============

def test_regex():
    """Tests des fonctions regex"""
    # À compléter
    # Testez vos fonctions regex ici
    pass


def test_database():
    """Tests de la base de données"""
    print("\n=== Test de la base de données ===\n")
    
    # Créer et initialiser la base de données
    db = BibliothequeDB()
    db.connecter()
    
    # Créer les tables
    print("1. Création des tables...")
    db.creer_tables()
    
    # Insérer les données d'exemple
    print("\n2. Insertion des données d'exemple...")
    db.inserer_donnees_exemple()
    
    print("\nBase de données initialisée !")
    print("Vous pouvez maintenant travailler sur les exercices 8 et 9.")
    print("Les fonctions à compléter : afficher_tous_livres(), livres_par_auteur(), etc.")
    
    db.deconnecter()


def test_exercice_10():
    """Tests pour l'exercice 10 : Recherche avancée avec regex"""
    print("\n=== Test Exercice 10 : Recherche avec Regex ===\n")
    
    db = BibliothequeDB()
    db.connecter()
    
    print("Test 1 : Rechercher des livres par pattern de titre")
    print("-" * 60)
    print("Pattern : r'harry.*potter' (tous les livres Harry Potter)")
    
    # TODO : Décommentez après implémentation
    # resultats = db.rechercher_livres_par_titre(r'harry.*potter')
    # print(f"Trouvé {len(resultats)} livre(s) :")
    # for livre in resultats:
    #     print(f"  - {livre[1]}")
    
    print("ATTENTION : Implémentez rechercher_livres_par_titre() puis décommentez\n")
    
    print("Test 2 : Rechercher des auteurs par nationalité")
    print("-" * 60)
    print("Pattern : r'Fran[cç]ais[e]?' (Français ou Française)")
    
    # TODO : Décommentez après implémentation
    # auteurs = db.rechercher_auteurs_par_pays(r'Fran[cç]ais[e]?')
    # print(f"Trouvé {len(auteurs)} auteur(s) français :")
    # for auteur in auteurs:
    #     print(f"  - {auteur[2]} {auteur[1]}")
    
    print("ATTENTION : Implémentez rechercher_auteurs_par_pays() puis décommentez\n")
    
    print("Test 3 : Emprunts par période")
    print("-" * 60)
    print("Pattern : r'2024-11-.*' (novembre 2024)")
    
    # TODO : Décommentez après implémentation
    # emprunts = db.emprunts_par_periode(r'2024-11-.*')
    # print(f"Trouvé {len(emprunts)} emprunt(s) en novembre 2024")
    
    print("ATTENTION : Implémentez emprunts_par_periode() puis décommentez\n")
    
    print("=" * 60)
    print("CONSEIL : Utilisez re.compile() avec re.IGNORECASE")
    print("   pour des recherches insensibles à la casse !")
    
    db.deconnecter()


if __name__ == "__main__":
    print("=== Module 09 : Regex et Base de Données ===\n")
    
    print("Pour initialiser la base de données, décommentez la ligne suivante :")
    print(">>> test_database()\n")
    
    # Décommentez pour initialiser la base de données avec les tables et données d'exemple :
    # test_database()
    
    # Décommentez pour tester vos fonctions regex :
    # test_regex()
    
    # Décommentez pour tester l'exercice 10 (Recherche avec Regex) :
    # test_exercice_10()
