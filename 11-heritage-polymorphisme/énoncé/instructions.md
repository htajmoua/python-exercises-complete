# Instructions - Héritage et Polymorphisme

L'héritage permet de créer des classes basées sur d'autres classes, réutilisant et étendant leurs fonctionnalités.

## Concepts

**Classe parent (ou superclasse)** : La classe de base  
**Classe enfant (ou sous-classe)** : Hérite de la classe parent  
**Héritage** : Réutilisation du code de la classe parent  
**Override** : Redéfinir une méthode de la classe parent  
**super()** : Appeler une méthode de la classe parent  
**Polymorphisme** : Même méthode, comportements différents

## Exercice 1 - Héritage simple

**Créez** une classe parent `Animal` avec :
- Attributs : `nom`, `age`
- Méthode `se_presenter()` : affiche "Je suis {nom}, j'ai {age} ans"
- Méthode `faire_bruit()` : affiche "L'animal fait du bruit"

**Créez** une classe enfant `Chien` qui hérite de `Animal` et :
- Ajoute un attribut `race`
- Override `faire_bruit()` : affiche "Woof! Woof!"
- Ajoute une méthode `rapporter()` : affiche "Je rapporte la balle"

**Testez** :
```python
chien = Chien("Rex", 5, "Labrador")
chien.se_presenter()
chien.faire_bruit()
chien.rapporter()
```

## Exercice 2 - Utiliser super()

**Créez** une classe `Vehicule` avec :
- Attributs : `marque`, `modele`
- Méthode `afficher_info()` : affiche marque et modèle

**Créez** une classe `Voiture` qui hérite de `Vehicule` et :
- Ajoute un attribut `nombre_portes`
- Override `afficher_info()` : 
  - Appelle `super().afficher_info()`
  - Ajoute l'affichage du nombre de portes

## Exercice 3 - Hiérarchie à plusieurs niveaux

**Créez** la hiérarchie suivante :

**Classe `Employe`** :
- Attributs : `nom`, `salaire_base`
- Méthode `calculer_salaire()` : retourne `salaire_base`

**Classe `Manager` (hérite d'`Employe`)** :
- Attribut : `bonus`
- Override `calculer_salaire()` : retourne `salaire_base + bonus`

**Classe `Directeur` (hérite de `Manager`)** :
- Attribut : `actions` (nombre d'actions)
- Override `calculer_salaire()` : retourne `super().calculer_salaire() + actions * 100`

**Testez** les 3 types d'employés.

## Exercice 4 - Polymorphisme

**Créez** une classe parent `Forme` avec :
- Méthode `calculer_aire()` : retourne 0 (à override)
- Méthode `calculer_perimetre()` : retourne 0 (à override)

**Créez** des classes enfants** :
- `Rectangle` : avec longueur et largeur
- `Cercle` : avec rayon
- `Triangle` : avec base et hauteur (et côtés pour le périmètre)

**Créez** une liste de formes différentes et calculez l'aire totale :
```python
formes = [Rectangle(5, 3), Cercle(4), Triangle(6, 4, 5, 5)]
aire_totale = sum(forme.calculer_aire() for forme in formes)
```

## Exercice 5 - Méthode abstraite (simulation)

**Créez** une classe `Paiement` avec :
- Attribut : `montant`
- Méthode `traiter()` : lève une `NotImplementedError`
- Méthode `afficher_recu()` : affiche le reçu

**Créez** des sous-classes** :
- `PaiementCarte` : override `traiter()` avec logique spécifique
- `PaiementPaypal` : override `traiter()` avec logique spécifique
- `PaiementEspeces` : override `traiter()` avec logique spécifique

## Exercice 6 - Héritage avec attributs de classe

**Créez** une classe `Personnage` avec :
- Attribut de classe : `nombre_personnages = 0`
- Attributs d'instance : `nom`, `points_vie`
- Le constructeur incrémente `nombre_personnages`

**Créez** des sous-classes** :
- `Guerrier` : ajoute `force`
- `Mage` : ajoute `mana`
- `Archer` : ajoute `precision`

Vérifiez que le compteur total compte tous les types de personnages.

## Exercice 7 - Override avec validation

**Créez** une classe `CompteBancaire` avec :
- Attributs : `titulaire`, `solde`
- Méthode `retirer(montant)` : valide et retire

**Créez** une classe `CompteEpargne` qui :
- Ajoute un attribut `taux_interet`
- Override `retirer()` : autorise seulement si solde reste >= 100
- Ajoute une méthode `appliquer_interets()`

**Créez** une classe `CompteJeune` qui :
- Override `retirer()` : limite de retrait à 500 par opération

## Exercice 8 - Composition vs Héritage

**Créez** une classe `Moteur` avec :
- Attributs : `puissance`, `type_carburant`
- Méthode `demarrer()` : affiche "Moteur démarré"

**Créez** une classe `Voiture` qui **contient** un `Moteur` (composition) :
- Attributs : `marque`, `moteur` (objet Moteur)
- Méthode `demarrer()` : délègue au moteur

**Créez** une sous-classe `VoitureElectrique` :
- Le moteur a `type_carburant = "électrique"`
- Ajoute un attribut `autonomie_batterie`

## Exercice 9 - Méthodes de classe héritées

**Créez** une classe `Produit` avec :
- Attribut de classe : `tva = 0.20`
- Méthode de classe `definir_tva(nouveau_taux)`
- Méthode d'instance `calculer_prix_ttc(prix_ht)`

**Créez** une sous-classe `ProduitReduit` :
- Attribut de classe : `tva = 0.055` (taux réduit)

Vérifiez que chaque classe utilise son propre taux.

## Exercice 10 - Mini-projet : Système de jeu RPG

**Créez** une hiérarchie complète :

**Classe `Personnage`** :
- Attributs : `nom`, `points_vie`, `niveau`
- Méthode `attaquer(cible)` : attaque de base
- Méthode `recevoir_degats(degats)` : diminue PV
- Méthode `est_vivant()` : retourne True si PV > 0
- Méthode `monter_niveau()` : augmente niveau et PV

**Sous-classes** :
- `Guerrier` : 
  - Attribut `force`
  - Override `attaquer()` : dégâts = force * 2
  - Méthode spéciale `coup_puissant()` : force * 3
  
- `Mage` :
  - Attribut `mana`
  - Override `attaquer()` : dégâts normaux
  - Méthode `lancer_sort(cible)` : consomme mana, gros dégâts
  - Méthode `regenerer_mana()` : restaure mana
  
- `Archer` :
  - Attribut `precision`
  - Override `attaquer()` : peut rater selon precision
  - Méthode `tir_multiple(cibles)` : attaque plusieurs cibles

**Créez** un combat simulé entre 3 personnages différents.

## Exercices bonus

### Exercice 11 - Héritage multiple
**Créez** :
- Classe `Volant` avec méthode `voler()`
- Classe `Nageur` avec méthode `nager()`
- Classe `Canard` qui hérite des deux

### Exercice 12 - Duck typing (polymorphisme sans héritage)
**Créez** plusieurs classes sans lien d'héritage mais avec la même méthode `jouer()` :
- `Guitare`, `Piano`, `Violon`
- Fonction `concert(instruments)` qui appelle `jouer()` sur chacun

### Exercice 13 - Système de notifications
**Créez** une classe `Notification` et des sous-classes :
- `EmailNotification` : envoie par email
- `SMSNotification` : envoie par SMS
- `PushNotification` : envoie notification push
- Toutes ont une méthode `envoyer(message)` polymorphe
