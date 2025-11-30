# Instructions - Projet Django Complet

Ce module final vous propose plusieurs projets complets intégrant tous les concepts Django : models, views, templates, forms, admin, authentification et API REST.

## Projet 1 - Plateforme de Blog Avancée 

### Objectif
Créer une plateforme de blogging complète avec auteurs, articles, commentaires, catégories et système de likes.

### Fonctionnalités requises

#### Modèles
- **Auteur** : profil étendu avec bio, photo, réseaux sociaux
- **Catégorie** : organisation des articles
- **Article** : titre, slug, contenu, image, statut (brouillon/publié), featured
- **Commentaire** : système de commentaires avec modération
- **Like** : système de likes pour articles
- **Tag** : tags pour articles (ManyToMany)

#### Fonctionnalités frontend
-  Page d'accueil avec articles featured et derniers articles
-  Liste d'articles avec pagination, filtres et recherche
-  Détail d'article avec commentaires
-  Page auteur avec tous ses articles
-  Archives par catégorie, tag, date
-  Système de like (AJAX)
-  Formulaire de commentaire
-  Newsletter subscription

#### Fonctionnalités backend
-  Interface admin personnalisée
-  Dashboard pour auteurs (mes articles, statistiques)
-  Création/édition d'articles avec rich text editor
-  Upload d'images avec preview
-  Modération des commentaires
-  Gestion des catégories et tags

#### API REST
-  CRUD complet pour articles
-  Endpoints pour commentaires
-  Endpoint pour likes
-  Filtrage par catégorie, tag, auteur
-  Recherche full-text
-  Documentation Swagger

#### Authentification
-  Inscription/Connexion
-  Profil utilisateur éditable
-  Reset de mot de passe
-  Permissions (auteur, éditeur, admin)

### Bonus
- Système de vues/lectures
- Temps de lecture estimé
- Articles similaires
- Partage sur réseaux sociaux
- Export PDF d'articles
- Dark mode

---

## Projet 2 - Plateforme E-learning 🎓

### Objectif
Créer une plateforme de cours en ligne avec instructeurs, étudiants, cours, modules et quiz.

### Fonctionnalités requises

#### Modèles
- **Instructeur** : profil, spécialités, cours créés
- **Etudiant** : profil, cours suivis, progression
- **Cours** : titre, description, niveau, prix, durée
- **Module** : chapitres d'un cours
- **Leçon** : contenu vidéo/texte d'un module
- **Quiz** : évaluation par cours
- **Question/Réponse** : questions à choix multiples
- **Enrollment** : inscription étudiant à un cours
- **Progression** : tracking de progression

#### Fonctionnalités frontend
-  Catalogue de cours avec filtres
-  Page de détail de cours
-  Processus d'inscription
-  Dashboard étudiant (mes cours, progression)
-  Lecteur de cours avec navigation
-  Passage de quiz
-  Certificat de completion

#### Fonctionnalités backend
-  Dashboard instructeur
-  Création de cours (wizard multi-étapes)
-  Upload de vidéos
-  Création de quiz
-  Gestion des inscriptions
-  Statistiques (nombre d'étudiants, taux de completion)

#### API REST
-  API cours et modules
-  API progression
-  API quiz et résultats
-  API inscriptions

#### Authentification
-  Rôles : admin, instructeur, étudiant
-  Permissions par rôle
-  Profile avec avatar

### Bonus
- Système de paiement (Stripe)
- Forum de discussion par cours
- Live chat instructeur-étudiant
- Certificats PDF
- Reviews et ratings

---

## Projet 3 - Réseau Social 👥

### Objectif
Créer un mini réseau social avec profils, posts, likes, commentaires et friendships.

### Fonctionnalités requises

#### Modèles
- **UserProfile** : extension de User avec bio, avatar, cover
- **Post** : contenu, images, visibilité
- **Comment** : commentaires sur posts
- **Like** : likes sur posts et commentaires
- **Friendship** : relation d'amitié
- **FriendRequest** : demandes d'ami
- **Notification** : notifications utilisateur

#### Fonctionnalités frontend
-  Timeline (feed d'actualités)
-  Profil utilisateur
-  Création de posts (texte + images)
-  Système de likes et commentaires
-  Gestion d'amis (ajouter, accepter, refuser)
-  Recherche d'utilisateurs
-  Notifications en temps réel
-  Messages privés (optionnel)

#### Fonctionnalités backend
-  Admin pour modération
-  Gestion des signalements
-  Statistiques utilisateurs

#### API REST
-  CRUD posts
-  API commentaires et likes
-  API friendships
-  API notifications
-  WebSocket pour temps réel (bonus)

#### Authentification
-  Inscription avec email confirmation
-  Login social (Google, Facebook)
-  Profil privé/public

### Bonus
- Stories (24h)
- Hashtags
- Mentions (@user)
- Chat en temps réel
- Groupes
- Events

---

## Projet 4 - Système de Gestion de Tâches (Task Manager) 

### Objectif
Créer un gestionnaire de tâches collaboratif type Trello/Asana.

### Fonctionnalités requises

#### Modèles
- **Workspace** : espace de travail d'une équipe
- **Board** : tableau de bord (projet)
- **List** : colonne de tâches (À faire, En cours, Terminé)
- **Card** : tâche/carte
- **Label** : étiquettes colorées
- **Member** : membres d'un workspace
- **Comment** : commentaires sur cartes
- **Attachment** : fichiers joints
- **Activity** : historique des actions

#### Fonctionnalités frontend
-  Vue Kanban (drag & drop)
-  Vue liste
-  Vue calendrier
-  Détail de carte (modal)
-  Ajout/modification de cartes
-  Assignation de membres
-  Dates limites
-  Checklists

#### Fonctionnalités backend
-  Gestion des workspaces
-  Invitation de membres
-  Permissions (owner, admin, member)
-  Historique complet

#### API REST
-  API complète CRUD
-  Réorganisation drag & drop
-  Upload de fichiers
-  Recherche avancée

#### Authentification
-  Teams et workspaces
-  Invitations par email
-  Permissions granulaires

### Bonus
- Templates de boards
- Récurrence de tâches
- Rapports et statistiques
- Intégrations (Slack, GitHub)
- Export CSV/JSON

---

## Critères d'évaluation (tous projets)

### Architecture & Code Quality
-  Structure de projet claire et organisée
-  Séparation des concerns (models, views, templates)
-  Code DRY (Don't Repeat Yourself)
-  Nommage cohérent et explicite
-  Commentaires et docstrings
-  PEP 8 respecté

### Base de données
-  Modèles bien conçus avec relations appropriées
-  Indexes pour performance
-  Migrations propres
-  Données de test (fixtures ou management command)

### Frontend
-  Templates organisés avec héritage
-  Design responsive (Bootstrap/Tailwind)
-  UX intuitive
-  Messages flash pour feedback utilisateur
-  Gestion des erreurs 404, 500

### Backend
-  Admin personnalisé et fonctionnel
-  Forms avec validation
-  Gestion d'erreurs appropriée
-  Logging configuré
-  Settings pour dev/prod

### Sécurité
-  CSRF protection
-  XSS prevention
-  SQL injection prevention (ORM)
-  Authentification sécurisée
-  Permissions bien définies

### Performance
-  Requêtes optimisées (select_related, prefetch_related)
-  Pagination
-  Caching (optionnel)
-  Static files configurés

### Tests
-  Tests unitaires pour models
-  Tests pour views
-  Tests pour API
-  Coverage > 70%

### Documentation
-  README complet
-  Requirements.txt
-  Instructions de setup
-  Documentation API (Swagger)
-  Diagramme de BDD (optionnel)

### Déploiement (bonus)
- Configuration pour production
- Variables d'environnement
- Staticfiles collectés
- Base de données PostgreSQL
- Déploiement sur Heroku/Railway/PythonAnywhere

---

## Livrables attendus

Pour chaque projet :

1. **Code source complet**
   - Projet Django configuré
   - Toutes les apps nécessaires
   - Templates et static files
   - Requirements.txt

2. **Base de données**
   - Fixtures avec données de démonstration
   - Ou script de populate

3. **Documentation**
   - README avec :
     - Description du projet
     - Installation
     - Configuration
     - Utilisation
     - API endpoints (si applicable)
   - Captures d'écran

4. **Tests**
   - Tests unitaires
   - Tests d'intégration
   - Script de run tests

5. **Démonstration**
   - Vidéo de démonstration (optionnel)
   - Ou présentation PowerPoint/PDF

---

## Méthodologie de travail

1. **Phase de conception** (1-2 jours)
   - Diagramme de base de données
   - Wireframes des pages principales
   - Liste des fonctionnalités priorisées

2. **Setup projet** (1/2 jour)
   - Créer projet et apps
   - Configuration settings
   - Git init et .gitignore

3. **Modèles** (1-2 jours)
   - Créer tous les modèles
   - Migrations
   - Admin basique

4. **Backend** (3-4 jours)
   - Views et URLs
   - Forms
   - Admin personnalisé
   - Authentification

5. **Frontend** (3-4 jours)
   - Templates base
   - Pages principales
   - CSS/JS
   - Responsive

6. **API** (2-3 jours)
   - Serializers
   - ViewSets
   - Permissions
   - Documentation

7. **Tests** (2 jours)
   - Tests models
   - Tests views
   - Tests API

8. **Polish** (1-2 jours)
   - Corrections bugs
   - Optimisations
   - Documentation

---

**Durée estimée :** 2-3 semaines à temps plein  
**Niveau :** Intermédiaire à Avancé  
**Technologies :** Django 4.x, PostgreSQL, DRF, Bootstrap/Tailwind, JavaScript
