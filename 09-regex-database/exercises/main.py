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
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def valider_telephone(telephone):
    """Valide un numéro de téléphone français"""
    # Formats acceptés: 06 12 34 56 78, 06-12-34-56-78, 0612345678
    pattern = r'^0[1-9](\s?|-?)\d{2}(\s?|-?)\d{2}(\s?|-?)\d{2}(\s?|-?)\d{2}$'
    return bool(re.match(pattern, telephone))


def valider_code_postal(code_postal):
    """Valide un code postal français (5 chiffres)"""
    pattern = r'^\d{5}$'
    return bool(re.match(pattern, code_postal))


def valider_date(date_str):
    """Valide une date au format JJ/MM/AAAA"""
    pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
    return bool(re.match(pattern, date_str))


# Exercice 2 : Extraction
def extraire_emails(texte):
    """Extrait tous les emails d'un texte"""
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, texte)


def extraire_telephones(texte):
    """Extrait tous les numéros de téléphone"""
    pattern = r'0[1-9](?:\s?|-?)\d{2}(?:\s?|-?)\d{2}(?:\s?|-?)\d{2}(?:\s?|-?)\d{2}'
    return re.findall(pattern, texte)


def extraire_urls(texte):
    """Extrait toutes les URLs"""
    pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
    return re.findall(pattern, texte)


# Exercice 3 : Remplacement
def masquer_carte_bancaire(numero):
    """Masque un numéro de carte bancaire"""
    # Garde seulement les 4 derniers chiffres
    pattern = r'\d{4}\s?\d{4}\s?\d{4}\s?(\d{4})'
    return re.sub(pattern, r'**** **** **** \1', numero)


def nettoyer_texte(texte):
    """Supprime les caractères spéciaux"""
    pattern = r'[^a-zA-Z0-9\s]'
    return re.sub(pattern, '', texte)


def convertir_date_format(date_str):
    """Convertit JJ/MM/AAAA en AAAA-MM-JJ"""
    pattern = r'(\d{2})/(\d{2})/(\d{4})'
    return re.sub(pattern, r'\3-\2-\1', date_str)


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
    if len(mdp) < 8:
        return False, "Trop court (min 8 caractères)"
    
    if not re.search(r'[A-Z]', mdp):
        return False, "Manque une majuscule"
    
    if not re.search(r'[a-z]', mdp):
        return False, "Manque une minuscule"
    
    if not re.search(r'\d', mdp):
        return False, "Manque un chiffre"
    
    if not re.search(r'[@#$%^&+=!]', mdp):
        return False, "Manque un caractère spécial (@#$%^&+=!)"
    
    return True, "Mot de passe valide"


# Exercice 5 : Parsing de logs
def parser_log(ligne_log):
    """Parse une ligne de log"""
    pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (\w+): (.+)'
    match = re.match(pattern, ligne_log)
    
    if match:
        return {
            'date': match.group(1),
            'niveau': match.group(2),
            'message': match.group(3)
        }
    return None


def extraire_ips(texte):
    """Extrait les adresses IP d'un texte"""
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return re.findall(pattern, texte)


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
                auteur_id INTEGER NOT NULL,
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
                livre_id INTEGER NOT NULL,
                emprunteur TEXT NOT NULL,
                date_emprunt TEXT NOT NULL,
                date_retour TEXT,
                statut TEXT DEFAULT 'en_cours',
                FOREIGN KEY (livre_id) REFERENCES livres(id)
            )
        ''')
        
        self.conn.commit()
        print("✅ Tables créées avec succès")
    
    def inserer_donnees_exemple(self):
        """Insère des données d'exemple"""
        
        # Auteurs
        auteurs = [
            ('Hugo', 'Victor', '1802-02-26', 'Française'),
            ('Orwell', 'George', '1903-06-25', 'Britannique'),
            ('Saint-Exupéry', 'Antoine', '1900-06-29', 'Française'),
            ('Dumas', 'Alexandre', '1802-07-24', 'Française'),
            ('Verne', 'Jules', '1828-02-08', 'Française'),
        ]
        
        self.cursor.executemany('''
            INSERT INTO auteurs (nom, prenom, date_naissance, nationalite)
            VALUES (?, ?, ?, ?)
        ''', auteurs)
        
        # Livres
        livres = [
            ('Les Misérables', 1, 1862, '978-2-253-09633-1', 'Roman'),
            ('Notre-Dame de Paris', 1, 1831, '978-2-253-09614-0', 'Roman'),
            ('1984', 2, 1949, '978-0-452-28423-4', 'Dystopie'),
            ('La Ferme des animaux', 2, 1945, '978-2-07-037516-8', 'Fable'),
            ('Le Petit Prince', 3, 1943, '978-2-07-061275-8', 'Conte'),
            ('Les Trois Mousquetaires', 4, 1844, '978-2-253-00814-0', 'Aventure'),
            ('Le Comte de Monte-Cristo', 4, 1844, '978-2-253-09862-5', 'Aventure'),
            ('Vingt mille lieues sous les mers', 5, 1870, '978-2-253-00655-9', 'Science-fiction'),
            ('Le Tour du monde en 80 jours', 5, 1873, '978-2-253-00658-0', 'Aventure'),
            ('Voyage au centre de la Terre', 5, 1864, '978-2-253-00654-2', 'Science-fiction'),
        ]
        
        self.cursor.executemany('''
            INSERT INTO livres (titre, auteur_id, annee_publication, isbn, genre)
            VALUES (?, ?, ?, ?, ?)
        ''', livres)
        
        # Emprunts
        emprunts = [
            (1, 'Alice Dupont', '2024-01-15', None, 'en_cours'),
            (3, 'Bob Martin', '2024-01-10', '2024-01-25', 'retourne'),
            (5, 'Charlie Durand', '2024-01-20', None, 'en_cours'),
            (7, 'Diana Petit', '2024-01-05', '2024-01-20', 'retourne'),
            (9, 'Eve Bernard', '2024-01-18', None, 'en_cours'),
        ]
        
        self.cursor.executemany('''
            INSERT INTO emprunts (livre_id, emprunteur, date_emprunt, date_retour, statut)
            VALUES (?, ?, ?, ?, ?)
        ''', emprunts)
        
        self.conn.commit()
        print("✅ Données d'exemple insérées")
    
    # Exercice 7 : Ajouter des données
    def ajouter_auteur(self, nom, prenom, date_naissance=None, nationalite=None):
        """Ajoute un auteur"""
        self.cursor.execute('''
            INSERT INTO auteurs (nom, prenom, date_naissance, nationalite)
            VALUES (?, ?, ?, ?)
        ''', (nom, prenom, date_naissance, nationalite))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def ajouter_livre(self, titre, auteur_id, annee=None, isbn=None, genre=None):
        """Ajoute un livre"""
        self.cursor.execute('''
            INSERT INTO livres (titre, auteur_id, annee_publication, isbn, genre)
            VALUES (?, ?, ?, ?, ?)
        ''', (titre, auteur_id, annee, isbn, genre))
        self.conn.commit()
        return self.cursor.lastrowid
    
    # Exercice 8 : Requêtes SELECT
    def afficher_tous_livres(self):
        """Affiche tous les livres"""
        self.cursor.execute('SELECT * FROM livres')
        return self.cursor.fetchall()
    
    def livres_par_auteur(self, auteur_id):
        """Affiche les livres d'un auteur"""
        self.cursor.execute('''
            SELECT * FROM livres WHERE auteur_id = ?
        ''', (auteur_id,))
        return self.cursor.fetchall()
    
    def livres_apres_annee(self, annee):
        """Livres publiés après une année"""
        self.cursor.execute('''
            SELECT * FROM livres WHERE annee_publication > ?
        ''', (annee,))
        return self.cursor.fetchall()
    
    def emprunts_en_cours(self):
        """Emprunts actuellement en cours"""
        self.cursor.execute('''
            SELECT * FROM emprunts WHERE statut = 'en_cours'
        ''')
        return self.cursor.fetchall()
    
    # Exercice 9 : Jointures
    def livres_avec_auteurs(self):
        """Livres avec nom de l'auteur"""
        self.cursor.execute('''
            SELECT livres.titre, auteurs.nom, auteurs.prenom,
                   livres.annee_publication, livres.genre
            FROM livres
            JOIN auteurs ON livres.auteur_id = auteurs.id
            ORDER BY livres.titre
        ''')
        return self.cursor.fetchall()
    
    def emprunts_avec_details(self):
        """Emprunts avec détails du livre et auteur"""
        self.cursor.execute('''
            SELECT emprunts.emprunteur, livres.titre,
                   auteurs.nom || ' ' || auteurs.prenom as auteur,
                   emprunts.date_emprunt, emprunts.statut
            FROM emprunts
            JOIN livres ON emprunts.livre_id = livres.id
            JOIN auteurs ON livres.auteur_id = auteurs.id
            ORDER BY emprunts.date_emprunt DESC
        ''')
        return self.cursor.fetchall()
    
    # Exercice 10 : UPDATE et DELETE
    def retourner_livre(self, emprunt_id, date_retour=None):
        """Marque un emprunt comme retourné"""
        if date_retour is None:
            date_retour = datetime.now().strftime('%Y-%m-%d')
        
        self.cursor.execute('''
            UPDATE emprunts
            SET statut = 'retourne', date_retour = ?
            WHERE id = ?
        ''', (date_retour, emprunt_id))
        self.conn.commit()
    
    def supprimer_livre(self, livre_id):
        """Supprime un livre"""
        self.cursor.execute('DELETE FROM livres WHERE id = ?', (livre_id,))
        self.conn.commit()
    
    def modifier_auteur(self, auteur_id, **kwargs):
        """Modifie les informations d'un auteur"""
        for key, value in kwargs.items():
            self.cursor.execute(f'''
                UPDATE auteurs SET {key} = ? WHERE id = ?
            ''', (value, auteur_id))
        self.conn.commit()
    
    # Exercice 12 : Recherche avec regex
    def rechercher_livres_regex(self, pattern, champ='titre'):
        """Recherche des livres avec une expression régulière"""
        if champ == 'titre':
            self.cursor.execute('SELECT * FROM livres')
        else:
            self.cursor.execute('''
                SELECT livres.*
                FROM livres
                JOIN auteurs ON livres.auteur_id = auteurs.id
            ''')
        
        resultats = []
        for row in self.cursor.fetchall():
            if champ == 'titre':
                texte = row[1]  # titre
            elif champ == 'auteur':
                # On doit faire une autre requête pour avoir le nom de l'auteur
                continue
            else:
                texte = row[5]  # genre
            
            if re.search(pattern, texte, re.IGNORECASE):
                resultats.append(row)
        
        return resultats
    
    # Statistiques
    def afficher_statistiques(self):
        """Affiche des statistiques"""
        stats = {}
        
        self.cursor.execute('SELECT COUNT(*) FROM auteurs')
        stats['auteurs'] = self.cursor.fetchone()[0]
        
        self.cursor.execute('SELECT COUNT(*) FROM livres')
        stats['livres'] = self.cursor.fetchone()[0]
        
        self.cursor.execute("SELECT COUNT(*) FROM emprunts WHERE statut = 'en_cours'")
        stats['emprunts_en_cours'] = self.cursor.fetchone()[0]
        
        return stats


# ============= TESTS =============

def test_regex():
    """Tests des fonctions regex"""
    print("=== Tests Regex ===\n")
    
    # Test validation email
    print("1. Validation email:")
    emails = ["alice@example.com", "bob.martin@gmail.fr", "invalid.email", "test@"]
    for email in emails:
        print(f"  {email}: {valider_email(email)}")
    
    # Test validation téléphone
    print("\n2. Validation téléphone:")
    tels = ["06 12 34 56 78", "06-12-34-56-78", "0612345678", "12345"]
    for tel in tels:
        print(f"  {tel}: {valider_telephone(tel)}")
    
    # Test extraction
    print("\n3. Extraction:")
    texte = """
    Contactez-nous sur contact@entreprise.fr ou au 01 23 45 67 89.
    Notre site : https://www.entreprise.fr
    Support : support@entreprise.com - Tél : 06-12-34-56-78
    Serveur IP : 192.168.1.10
    """
    print(f"  Emails: {extraire_emails(texte)}")
    print(f"  Téléphones: {extraire_telephones(texte)}")
    print(f"  URLs: {extraire_urls(texte)}")
    print(f"  IPs: {extraire_ips(texte)}")
    
    # Test masquage carte
    print("\n4. Masquage carte bancaire:")
    carte = "1234 5678 9012 3456"
    print(f"  {carte} → {masquer_carte_bancaire(carte)}")
    
    # Test mot de passe
    print("\n5. Validation mot de passe:")
    mdps = ["Abc123!", "faible", "SANSMINUSCULE1!", "SansChiffre!", "SansSpecial1"]
    for mdp in mdps:
        valide, msg = valider_mot_de_passe(mdp)
        print(f"  {mdp}: {msg}")


def test_database():
    """Tests de la base de données"""
    print("\n=== Tests Base de Données ===\n")
    
    # Supprimer l'ancienne base si elle existe
    if os.path.exists('bibliotheque.db'):
        os.remove('bibliotheque.db')
    
    # Créer et initialiser la base
    db = BibliothequeDB()
    db.connecter()
    db.creer_tables()
    db.inserer_donnees_exemple()
    
    # Test SELECT
    print("\n1. Tous les livres:")
    livres = db.afficher_tous_livres()
    for livre in livres[:3]:  # Afficher les 3 premiers
        print(f"  {livre[1]} ({livre[3]})")
    print(f"  ... et {len(livres) - 3} autres")
    
    # Test JOIN
    print("\n2. Livres avec auteurs:")
    livres_auteurs = db.livres_avec_auteurs()
    for livre in livres_auteurs[:5]:
        print(f"  '{livre[0]}' par {livre[1]} {livre[2]} ({livre[3]})")
    
    # Test emprunts
    print("\n3. Emprunts en cours:")
    emprunts = db.emprunts_en_cours()
    for emprunt in emprunts:
        print(f"  Emprunt #{emprunt[0]} - Livre #{emprunt[1]} par {emprunt[2]}")
    
    # Statistiques
    print("\n4. Statistiques:")
    stats = db.afficher_statistiques()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    db.deconnecter()
    print("\n✅ Base de données créée: bibliotheque.db")


def menu_principal():
    """Menu principal de l'application (simplifié)"""
    print("\n" + "="*50)
    print("  GESTION DE BIBLIOTHÈQUE")
    print("="*50)
    print("\n1. Tests Regex")
    print("2. Tests Base de Données")
    print("3. Quitter")
    print("\nPour un menu complet, voir exercice 11 dans instructions.md")


if __name__ == "__main__":
    print("=== Module 09 : Regex et Base de Données ===\n")
    
    # Lancer les tests
    test_regex()
    test_database()
    
    print("\n" + "="*50)
    print("✅ Tous les tests sont terminés !")
    print("="*50)
    print("\nFichiers créés :")
    print("  - bibliotheque.db (base de données SQLite)")
    print("\nConsultez instructions.md pour les exercices complets.")
