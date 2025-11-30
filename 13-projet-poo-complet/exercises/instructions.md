# Instructions - Projet POO Complet

Ce module final vous propose plusieurs projets complets intégrant tous les concepts de POO : classes, encapsulation, héritage, polymorphisme, et méthodes spéciales.

## Projet 1 - Système de gestion de bibliothèque 

### Objectif
Créer un système complet de gestion de bibliothèque avec livres, membres, emprunts et pénalités.

### Classes à créer

#### Classe `Livre`
- Attributs : `titre`, `auteur`, `isbn`, `disponible` (True par défaut)
- Property `statut` : retourne "Disponible" ou "Emprunté"
- Méthode `__str__()` : affichage formaté
- Méthode `emprunter()` : marque comme non disponible
- Méthode `retourner()` : marque comme disponible

#### Classe `Membre`
- Attributs : `nom`, `numero_membre`, `livres_empruntes` (liste)
- Attribut de classe : `prochain_numero = 1` (auto-incrémentation)
- Property `nombre_emprunts` : retourne le nombre de livres empruntés
- Méthode `peut_emprunter()` : max 3 livres
- Méthode `__str__()`

#### Classe `Emprunt`
- Attributs : `livre`, `membre`, `date_emprunt`, `date_retour_prevue`, `date_retour_reel`
- Méthode `calculer_penalite()` : 0.50€ par jour de retard
- Property `est_en_retard` : vérifie si en retard
- Méthode `__str__()`

#### Classe `Bibliotheque`
- Attributs : `nom`, `livres` (liste), `membres` (liste), `emprunts` (liste)
- Méthode `ajouter_livre(livre)`
- Méthode `inscrire_membre(nom)` : crée et ajoute un membre
- Méthode `emprunter_livre(isbn, numero_membre)` : gère l'emprunt
- Méthode `retourner_livre(isbn, numero_membre)` : gère le retour
- Méthode `afficher_livres_disponibles()`
- Méthode `afficher_statistiques()` : nombre de livres, membres, emprunts actifs

### Fonctionnalités attendues
- Validation des emprunts (livre disponible, limite de 3 livres)
- Calcul automatique des pénalités
- Statistiques de la bibliothèque

---

## Projet 2 - Système de gestion d'école 🎓

### Objectif
Créer un système de gestion avec étudiants, professeurs, cours et notes.

### Classes à créer

#### Classe `Personne` (classe parent)
- Attributs : `nom`, `prenom`, `date_naissance`
- Property `age` : calcule l'âge
- Méthode abstraite `se_presenter()`
- Méthode `__str__()`

#### Classe `Etudiant` (hérite de `Personne`)
- Attributs : `numero_etudiant`, `notes` (dictionnaire {matiere: liste_notes})
- Property `moyenne_generale` : calcule la moyenne de toutes les matières
- Méthode `ajouter_note(matiere, note)` : valide la note (0-20)
- Méthode `obtenir_mention()` : retourne mention selon moyenne
- Override `se_presenter()`

#### Classe `Professeur` (hérite de `Personne`)
- Attributs : `matiere`, `salaire`
- Attribut de classe : `matieres_disponibles` (liste)
- Méthode `donner_note(etudiant, note)` : ajoute note à l'étudiant
- Override `se_presenter()`

#### Classe `Cours`
- Attributs : `nom_cours`, `professeur`, `etudiants` (liste), `capacite_max`
- Méthode `inscrire_etudiant(etudiant)` : vérifie capacité
- Méthode `retirer_etudiant(etudiant)`
- Property `nombre_etudiants` : compte les étudiants
- Property `est_plein` : vérifie si capacité atteinte
- Méthode `afficher_liste_etudiants()`

#### Classe `Ecole`
- Attributs : `nom`, `etudiants`, `professeurs`, `cours`
- Méthode `recruter_professeur(professeur)`
- Méthode `inscrire_etudiant(etudiant)`
- Méthode `creer_cours(nom, professeur, capacite)`
- Méthode `afficher_tableau_honneur()` : top 10 étudiants par moyenne

### Fonctionnalités attendues
- Gestion complète des inscriptions
- Calculs de moyennes et mentions
- Tableau d'honneur

---

## Projet 3 - Système de e-commerce 🛒

### Objectif
Créer une plateforme de commerce en ligne avec produits, panier, commandes et paiements.

### Classes à créer

#### Classe `Produit`
- Attributs : `nom`, `description`, `prix`, `stock`, `categorie`
- Property `disponible` : vérifie si stock > 0
- Méthode `reduire_stock(quantite)` : valide et réduit
- Méthode `appliquer_reduction(pourcentage)` : retourne nouveau prix
- Méthode `__str__()` et `__repr__()`

#### Sous-classes de `Produit`
- `ProduitPhysique` : ajoute `poids`, `dimensions`
- `ProduitNumerique` : ajoute `taille_fichier`, `lien_telechargement`
- `ProduitPerissable` : ajoute `date_peremption`, méthode `est_perime()`

#### Classe `LignePanier`
- Attributs : `produit`, `quantite`
- Property `sous_total` : calcule prix × quantité
- Méthode `modifier_quantite(nouvelle_quantite)`

#### Classe `Panier`
- Attributs : `lignes` (liste de LignePanier), `code_promo`
- Méthode `ajouter_produit(produit, quantite)`
- Méthode `retirer_produit(produit)`
- Méthode `vider()`
- Property `total_ht` : somme des sous-totaux
- Property `total_ttc` : avec TVA 20%
- Méthode `appliquer_code_promo(code)` : applique réduction

#### Classe `Client`
- Attributs : `nom`, `email`, `adresse`, `panier`, `historique_commandes`
- Méthode `passer_commande()` : crée une commande depuis le panier
- Property `total_depense` : somme de toutes les commandes

#### Classe `Commande`
- Attributs : `numero_commande`, `client`, `lignes`, `date`, `statut`, `total`
- Attribut de classe : `prochain_numero = 1000`
- Méthode `calculer_frais_livraison()` : selon poids total
- Méthode `changer_statut(nouveau_statut)` : "En préparation", "Expédiée", "Livrée"
- Méthode `__str__()`

#### Classe abstraite `Paiement`
- Méthode abstraite `traiter(montant)`
- Méthode abstraite `rembourser(montant)`

#### Sous-classes de `Paiement`
- `PaiementCarte` : avec validation de numéro
- `PaiementPaypal` : avec email
- `PaiementVirement` : avec IBAN

### Fonctionnalités attendues
- Gestion complète du panier
- Système de commandes avec numérotation
- Plusieurs types de paiements polymorphes
- Calcul de frais de livraison
- Historique client

---

## Projet 4 - Jeu de combat RPG ⚔️

### Objectif
Créer un jeu de combat complet avec personnages, équipements, compétences et système de combat.

### Classes à créer

#### Classe `Statistiques`
- Attributs : `force`, `defense`, `agilite`, `intelligence`
- Méthode `__add__()` : additionner deux ensembles de stats
- Méthode `__str__()`

#### Classe `Equipement`
- Attributs : `nom`, `type`, `bonus_stats` (objet Statistiques)
- Types : "arme", "armure", "accessoire"
- Méthode `__str__()`

#### Classe `Competence`
- Attributs : `nom`, `cout_mana`, `puissance`, `type_competence`
- Types : "attaque", "soin", "buff"
- Méthode `utiliser(lanceur, cible)`

#### Classe `Personnage`
- Attributs : `nom`, `niveau`, `points_vie`, `points_mana`, `stats_base`, `equipement`, `competences`
- Property `stats_totales` : stats_base + bonus équipement
- Property `est_vivant` : PV > 0
- Méthode `equiper(equipement)` : remplace équipement actuel
- Méthode `apprendre_competence(competence)`
- Méthode `attaque_basique(cible)` : dégâts basés sur stats
- Méthode `utiliser_competence(competence, cible)` : vérifie mana
- Méthode `recevoir_degats(degats)` : applique défense
- Méthode `se_soigner(montant)`
- Méthode `gagner_experience(xp)` : peut monter de niveau

#### Sous-classes de `Personnage`
- `Guerrier` : bonus force, compétence "Coup puissant"
- `Mage` : bonus intelligence et mana, compétence "Boule de feu"
- `Paladin` : équilibré, compétence "Soin divin"
- `Assassin` : bonus agilité, compétence "Attaque furtive"

#### Classe `Combat`
- Attributs : `combattant1`, `combattant2`, `tour_actuel`
- Méthode `demarrer()` : lance le combat tour par tour
- Méthode `tour(attaquant, defenseur)` : gère un tour
- Méthode `afficher_etat()` : affiche PV et mana des deux
- Property `est_termine` : vérifie si quelqu'un est KO
- Méthode `declarer_vainqueur()` : annonce le gagnant

#### Classe `Inventaire`
- Attributs : `equipements`, `consommables`, `capacite_max`
- Méthode `ajouter(objet)` : vérifie capacité
- Méthode `retirer(objet)`
- Property `poids_total` : si objets ont un poids
- Méthode `trier_par_type()`

### Fonctionnalités attendues
- Système de combat tour par tour complet
- Gestion des équipements et stats
- Système de compétences avec coût mana
- Montée de niveau et expérience
- Plusieurs classes de personnages avec spécialités

---

## Méthodes spéciales à implémenter

Pour tous les projets, implémentez ces méthodes spéciales où pertinent :

- `__str__()` : représentation lisible pour print()
- `__repr__()` : représentation technique pour debug
- `__eq__()` : comparaison d'égalité
- `__lt__()`, `__le__()`, `__gt__()`, `__ge__()` : comparaisons
- `__add__()`, `__sub__()` : opérations arithmétiques si pertinent
- `__len__()` : pour les collections
- `__contains__()` : pour l'opérateur `in`
- `__getitem__()`, `__setitem__()` : accès par index si pertinent

## Critères d'évaluation

Votre projet doit :
-  Utiliser au moins 8 classes différentes
-  Implémenter l'héritage (au moins 3 niveaux)
-  Utiliser des properties avec validation
-  Implémenter le polymorphisme
-  Utiliser des méthodes spéciales appropriées
-  Avoir une encapsulation correcte (attributs protégés/privés)
-  Inclure de la documentation (docstrings)
-  Créer un script de démonstration complet

## Bonus

- Interface utilisateur en console (menu interactif)
- Sauvegarde/chargement des données (fichiers JSON ou CSV)
- Tests unitaires pour les classes principales
- Gestion d'erreurs avec try/except personnalisés
