"""
Module 22 - Django avec PostgreSQL
Fichier de test pour les exercices

Utilisez le shell Django pour tester :
    python manage.py shell
"""

# ============= IMPORTS =============

from django.db import models, connection
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.indexes import GinIndex, BTreeIndex

# Vos imports
# from blog.models import Article, Auteur


# ============= EXERCICES CONFIGURATION =============

def test_connexion_postgresql():
    """Tester la connexion à PostgreSQL"""
    from django.db import connection
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"Version PostgreSQL : {version[0]}")
        
        cursor.execute("SELECT current_database();")
        db_name = cursor.fetchone()
        print(f"Base de données : {db_name[0]}")


def voir_tables():
    """Lister toutes les tables"""
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        tables = cursor.fetchall()
        print("Tables dans la base :")
        for table in tables:
            print(f"  - {table[0]}")


# ============= EXERCICES ARRAYFIELD =============

def test_arrayfield():
    """Tester ArrayField"""
    # from blog.models import Article
    
    # # Créer avec tags
    # article = Article.objects.create(
    #     titre="Test ArrayField",
    #     contenu="Contenu...",
    #     tags=["Python", "Django", "PostgreSQL"]
    # )
    # 
    # # Filtrer
    # articles_python = Article.objects.filter(tags__contains=["Python"])
    # print(f"Articles avec tag Python : {articles_python.count()}")
    # 
    # # Overlap (au moins un tag en commun)
    # articles_overlap = Article.objects.filter(
    #     tags__overlap=["Django", "API"]
    # )
    # print(f"Articles Django ou API : {articles_overlap.count()}")
    pass


# ============= EXERCICES JSONFIELD =============

def test_jsonfield():
    """Tester JSONField"""
    # from blog.models import Article
    
    # # Créer avec metadata
    # article = Article.objects.create(
    #     titre="Test JSONField",
    #     contenu="Contenu...",
    #     metadata={
    #         "auteur_id": 1,
    #         "categorie": "Tech",
    #         "vues": 150,
    #         "featured": True,
    #         "stats": {
    #             "likes": 10,
    #             "shares": 5
    #         }
    #     }
    # )
    # 
    # # Filtrer par clé JSON
    # tech_articles = Article.objects.filter(metadata__categorie="Tech")
    # print(f"Articles Tech : {tech_articles.count()}")
    # 
    # # Filtrer par valeur numérique
    # populaires = Article.objects.filter(metadata__vues__gte=100)
    # print(f"Articles populaires : {populaires.count()}")
    # 
    # # Filtrer par clé imbriquée
    # liked = Article.objects.filter(metadata__stats__likes__gt=5)
    # print(f"Articles avec >5 likes : {liked.count()}")
    pass


# ============= EXERCICES FULL-TEXT SEARCH =============

def test_fulltext_search():
    """Tester la recherche full-text"""
    # from blog.models import Article
    
    # # Recherche simple
    # resultats = Article.objects.annotate(
    #     search=SearchVector('titre', 'contenu')
    # ).filter(search='django')
    # 
    # print(f"Résultats pour 'django' : {resultats.count()}")
    # 
    # # Recherche avec ranking
    # search_query = SearchQuery('django python')
    # resultats_ranked = Article.objects.annotate(
    #     search=SearchVector('titre', weight='A') + SearchVector('contenu', weight='B'),
    #     rank=SearchRank(SearchVector('titre', 'contenu'), search_query)
    # ).filter(search=search_query).order_by('-rank')
    # 
    # for article in resultats_ranked[:5]:
    #     print(f"{article.titre} - Rank: {article.rank}")
    pass


# ============= EXERCICES INDEXES =============

def voir_indexes():
    """Lister tous les indexes"""
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                tablename,
                indexname,
                indexdef
            FROM pg_indexes
            WHERE schemaname = 'public'
            ORDER BY tablename, indexname;
        """)
        
        indexes = cursor.fetchall()
        print("Indexes dans la base :")
        for idx in indexes:
            print(f"\nTable: {idx[0]}")
            print(f"Index: {idx[1]}")
            print(f"Définition: {idx[2]}")


def analyser_requete():
    """Analyser une requête avec EXPLAIN"""
    # from blog.models import Article
    
    # qs = Article.objects.filter(publie=True).order_by('-date_creation')[:10]
    # 
    # # Voir le SQL
    # print("SQL généré :")
    # print(qs.query)
    # 
    # # EXPLAIN ANALYZE
    # with connection.cursor() as cursor:
    #     sql = str(qs.query)
    #     cursor.execute(f'EXPLAIN ANALYZE {sql}')
    #     for row in cursor.fetchall():
    #         print(row[0])
    pass


# ============= EXERCICES OPTIMISATION =============

def test_performance():
    """Comparer les performances avec/sans optimisation"""
    from django.db import connection, reset_queries
    import time
    
    # from blog.models import Article
    
    # # Sans optimisation
    # reset_queries()
    # start = time.time()
    # articles = Article.objects.all()[:50]
    # for article in articles:
    #     _ = article.auteur.nom
    # temps_sans = time.time() - start
    # nb_queries_sans = len(connection.queries)
    # 
    # # Avec select_related
    # reset_queries()
    # start = time.time()
    # articles = Article.objects.select_related('auteur').all()[:50]
    # for article in articles:
    #     _ = article.auteur.nom
    # temps_avec = time.time() - start
    # nb_queries_avec = len(connection.queries)
    # 
    # print(f"Sans optimisation : {temps_sans:.3f}s, {nb_queries_sans} requêtes")
    # print(f"Avec select_related : {temps_avec:.3f}s, {nb_queries_avec} requêtes")
    # print(f"Gain : {((temps_sans - temps_avec) / temps_sans * 100):.1f}%")
    pass


# ============= EXERCICES MIGRATIONS =============

def migrer_depuis_sqlite():
    """Procédure pour migrer depuis SQLite vers PostgreSQL"""
    instructions = """
    1. Exporter les données de SQLite :
       python manage.py dumpdata > data.json
    
    2. Changer la configuration DATABASES dans settings.py vers PostgreSQL
    
    3. Créer les tables PostgreSQL :
       python manage.py migrate
    
    4. Importer les données :
       python manage.py loaddata data.json
    
    5. Vérifier :
       python manage.py shell
       from blog.models import Article
       Article.objects.count()
    """
    print(instructions)


# ============= EXERCICES BACKUP/RESTORE =============

def backup_restore_commands():
    """Commandes de backup et restore PostgreSQL"""
    commands = """
    === BACKUP ===
    
    # Dump complet
    pg_dump -U djangouser -h localhost blogdb > backup.sql
    
    # Dump compressé (format custom)
    pg_dump -U djangouser -h localhost -Fc blogdb > backup.dump
    
    # Dump seulement les données
    pg_dump -U djangouser -h localhost --data-only blogdb > data.sql
    
    # Dump seulement une table
    pg_dump -U djangouser -h localhost -t blog_article blogdb > articles.sql
    
    === RESTORE ===
    
    # Restore depuis SQL
    psql -U djangouser -h localhost -d blogdb < backup.sql
    
    # Restore depuis format custom
    pg_restore -U djangouser -h localhost -d blogdb backup.dump
    
    # Restore avec nettoyage
    pg_restore -U djangouser -h localhost -d blogdb -c backup.dump
    
    === DOCKER ===
    
    # Backup depuis conteneur Docker
    docker exec -t postgres_container pg_dump -U djangouser blogdb > backup.sql
    
    # Restore vers conteneur Docker
    docker exec -i postgres_container psql -U djangouser -d blogdb < backup.sql
    """
    print(commands)


# ============= STATISTIQUES BDD =============

def statistiques_database():
    """Voir les statistiques de la base de données"""
    with connection.cursor() as cursor:
        # Taille de la BDD
        cursor.execute("""
            SELECT pg_size_pretty(pg_database_size(current_database()));
        """)
        taille_db = cursor.fetchone()[0]
        print(f"Taille de la base : {taille_db}")
        
        # Taille par table
        cursor.execute("""
            SELECT
                schemaname,
                tablename,
                pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
            FROM pg_tables
            WHERE schemaname = 'public'
            ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
        """)
        
        print("\nTaille par table :")
        for row in cursor.fetchall():
            print(f"  {row[1]}: {row[2]}")
        
        # Nombre de connexions actives
        cursor.execute("""
            SELECT count(*) FROM pg_stat_activity;
        """)
        nb_connexions = cursor.fetchone()[0]
        print(f"\nConnexions actives : {nb_connexions}")


# ============= COMMANDES POSTGRESQL UTILES =============

def commandes_psql():
    """Commandes PostgreSQL utiles"""
    commands = """
    === COMMANDES PSQL (ligne de commande) ===
    
    # Se connecter
    psql -U djangouser -d blogdb -h localhost
    
    # Lister les bases de données
    \l
    
    # Se connecter à une base
    \c blogdb
    
    # Lister les tables
    \dt
    
    # Décrire une table
    \d blog_article
    
    # Lister les indexes
    \di
    
    # Lister les utilisateurs
    \du
    
    # Exécuter un fichier SQL
    \i fichier.sql
    
    # Afficher le temps d'exécution
    \timing
    
    # Quitter
    \q
    
    === REQUÊTES SQL UTILES ===
    
    -- Voir la version
    SELECT version();
    
    -- Voir les tables et leur taille
    SELECT schemaname, tablename, pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename))
    FROM pg_tables
    WHERE schemaname = 'public'
    ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
    
    -- Voir les indexes
    SELECT * FROM pg_indexes WHERE schemaname = 'public';
    
    -- Voir les connexions actives
    SELECT * FROM pg_stat_activity;
    
    -- Terminer une connexion
    SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid = <pid>;
    
    -- Vacuum (nettoyer et optimiser)
    VACUUM ANALYZE;
    """
    print(commands)


# ============= EXÉCUTION =============

if __name__ == "__main__":
    print("=" * 60)
    print("Module 22 - Tests PostgreSQL")
    print("=" * 60)
    
    # Décommentez pour tester
    
    # print("\n1. Test connexion PostgreSQL")
    # test_connexion_postgresql()
    
    # print("\n2. Tables")
    # voir_tables()
    
    # print("\n3. Statistiques")
    # statistiques_database()
    
    # print("\n4. Indexes")
    # voir_indexes()
    
    print("\n✅ Module prêt pour vos tests PostgreSQL !")
    print("\n📌 Commandes utiles :")
    print("  - python manage.py shell")
    print("  - psql -U djangouser -d blogdb")
    print("  - pg_dump / pg_restore pour backup")
    print("=" * 60)
