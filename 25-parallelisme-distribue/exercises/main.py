"""
TP 25 - Parallélisme et Calcul Distribué

Ce fichier contient des exercices à compléter sur concurrent.futures.
Suivez les TODO et les syntaxes d'exemple pour implémenter chaque exercice.

Consultez le fichier instructions.md pour les consignes détaillées.
"""

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# ============= PARTIE 1 : THREADING AVEC CONCURRENT.FUTURES =============

# Exercice 1 - ThreadPoolExecutor pour I/O-bound
import urllib.request

urls = [
    'https://www.python.org',
    'https://www.github.com',
    'https://pypi.org',
    'https://docs.python.org',
    'http://example.com'
]

def telecharger(url):
    """Télécharge une URL et retourne la taille"""
    # TODO: Implémenter le téléchargement
    # Syntaxe:
    #   try:
    #       with urllib.request.urlopen(url, timeout=5) as response:
    #           data = response.read()
    #           print(f"✓ Téléchargé {url}: {len(data)} bytes")
    #           return len(data)
    #   except Exception as e:
    #       print(f"✗ Erreur {url}: {e}")
    #       return 0
    pass


def demo_threading_io():
    """ThreadPoolExecutor est bon pour I/O-bound"""
    print("=== Exercice 1 : ThreadPoolExecutor pour I/O ===")
    
    # 1. Sans threading - approche séquentielle
    # TODO: Chronométrer l'exécution séquentielle
    # Syntaxe:
    #   start = time.time()
    #   for url in urls:
    #       telecharger(url)
    #   temps_sequentiel = time.time() - start
    #   print(f"Sans threading : {temps_sequentiel:.2f}s")
    
    # 2. Avec ThreadPoolExecutor
    # TODO: Utiliser ThreadPoolExecutor pour paralléliser
    # Syntaxe:
    #   start = time.time()
    #   with ThreadPoolExecutor(max_workers=5) as executor:
    #       results = list(executor.map(telecharger, urls))
    #   temps_parallel = time.time() - start
    #   print(f"Avec ThreadPoolExecutor : {temps_parallel:.2f}s")
    # 
    # executor.map() applique la fonction à chaque élément de la liste
    # et retourne les résultats dans le même ordre
    
    # TODO: Comparer les temps d'exécution
    #   print(f"Gain: {temps_sequentiel/temps_parallel:.1f}x plus rapide !")
    pass


# ============= PARTIE 2 : MULTIPROCESSING AVEC CONCURRENT.FUTURES =============

# Exercice 2 - ProcessPoolExecutor simple
def worker_process(name):
    """Worker simple"""
    # TODO: Importer os
    # TODO: Afficher le nom du worker et son PID avec os.getpid()
    # TODO: Retourner f"Terminé: {name}"
    pass


def demo_process():
    """Démonstration de ProcessPoolExecutor"""
    print("\n=== Exercice 2 : ProcessPoolExecutor ===")
    
    # TODO: Créer 5 processus avec ProcessPoolExecutor
    # Syntaxe:
    #   with ProcessPoolExecutor(max_workers=5) as executor:
    #       # submit() soumet une tâche et retourne un Future
    #       futures = [executor.submit(fonction, arg) for arg in liste]
    #       # Récupérer les résultats avec .result()
    #       results = [f.result() for f in futures]
    pass


# Exercice 3 - ProcessPoolExecutor pour CPU-bound
def calcul_carre(n):
    """Calcule le carré"""
    # TODO: Retourner n * n
    pass


def demo_pool():
    """Démonstration de ProcessPoolExecutor avec map"""
    print("\n=== Exercice 3 : ProcessPoolExecutor pour CPU-bound ===")
    
    data = list(range(10000))
    
    # 1. Sans ProcessPoolExecutor - approche séquentielle
    # TODO: Chronométrer le calcul séquentiel
    # Syntaxe: resultats = [calcul_carre(i) for i in data]
    
    # 2. Avec ProcessPoolExecutor
    # TODO: Utiliser ProcessPoolExecutor.map() pour paralléliser
    # Syntaxe:
    #   with ProcessPoolExecutor(max_workers=4) as executor:
    #       resultats = list(executor.map(fonction, data))
    # 
    # Note: map() est idéal quand on a une liste de données
    # et qu'on veut appliquer la même fonction à chaque élément
    
    # TODO: Comparer les temps d'exécution
    # Attention: Pour de petits calculs, le overhead du multiprocessing
    # peut être plus grand que le gain de performance!
    pass


# Exercice 4 - ThreadPoolExecutor avancé
def tache_io(n):
    """Tâche I/O"""
    # TODO: Simuler une opération I/O avec time.sleep(0.5)
    # TODO: Retourner n * n
    pass


def demo_threadpoolexecutor_avance():
    """Démonstration avancée de ThreadPoolExecutor"""
    print("\n=== Exercice 4 : ThreadPoolExecutor avancé ===")
    
    # TODO: Utiliser submit() pour soumettre 10 tâches
    # Syntaxe:
    #   with ThreadPoolExecutor(max_workers=5) as executor:
    #       # submit() retourne un Future pour chaque tâche
    #       futures = [executor.submit(tache_io, i) for i in range(10)]
    #       
    #       # Récupérer les résultats avec .result()
    #       for i, future in enumerate(futures):
    #           resultat = future.result()  # Bloque jusqu'à ce que la tâche soit terminée
    #           print(f"Résultat {i} : {resultat}")
    pass


# Exercice 5 - ProcessPoolExecutor avancé
def calcul_intensif(n):
    """Calcul CPU-intensif"""
    # TODO: Calculer la somme des carrés de 0 à n
    # Syntaxe: total = 0
    #          for i in range(n):
    #              total += i ** 2
    # TODO: Retourner le total
    pass


def demo_processpoolexecutor_avance():
    """Démonstration avancée de ProcessPoolExecutor"""
    print("\n=== Exercice 5 : ProcessPoolExecutor avancé ===")
    
    # TODO: Utiliser ProcessPoolExecutor.map() pour exécuter
    # calcul_intensif sur 8 valeurs de 1000000
    # Syntaxe:
    #   with ProcessPoolExecutor(max_workers=4) as executor:
    #       # map() exécute la fonction sur chaque élément de la liste
    #       resultats = list(executor.map(calcul_intensif, [1000000] * 8))
    #       print(f"Résultats : {resultats[:3]}...")
    # 
    # Note: Ici, 4 workers vont se partager 8 tâches
    pass


# Exercice 6 - as_completed
def tache_variable(n):
    """Tâche avec durée variable"""
    # TODO: Importer random
    # TODO: Générer une durée aléatoire entre 0.5 et 2 secondes
    # Syntaxe: duree = random.uniform(0.5, 2)
    # TODO: Attendre cette durée avec time.sleep(duree)
    # TODO: Retourner (n, duree)
    pass


def demo_as_completed():
    """Traite les résultats dès qu'ils arrivent"""
    print("\n=== Exercice 6 : as_completed ===")
    
    # TODO: Utiliser as_completed pour traiter les résultats dès qu'ils sont prêts
    # Syntaxe:
    #   with ProcessPoolExecutor(max_workers=4) as executor:
    #       # Créer un dictionnaire {Future: valeur}
    #       futures = {executor.submit(tache_variable, i): i for i in range(5)}
    #       
    #       # as_completed() retourne les futures dès qu'elles sont terminées
    #       for future in as_completed(futures):
    #           n, duree = future.result()
    #           print(f"Tâche {n} terminée en {duree:.2f}s")
    # 
    # Note: Contrairement à map(), as_completed() ne préserve pas l'ordre
    # mais permet de traiter les résultats dès qu'ils arrivent
    pass


# ============= PARTIE 4 : CELERY (EXEMPLES) =============

# NOTE: Ces exemples nécessitent Celery et Redis installés
# pip install celery redis

celery_app_code = """
# celery_app.py
from celery import Celery

app = Celery('tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
)
"""

celery_tasks_code = """
# tasks.py
from celery_app import app
import time

@app.task
def addition(x, y):
    return x + y

@app.task
def tache_longue(duree):
    time.sleep(duree)
    return f"Tâche terminée après {duree}s"

@app.task(bind=True, max_retries=3)
def tache_instable(self, x):
    import random
    try:
        if random.random() < 0.7:
            raise Exception("Erreur aléatoire")
        return x * 2
    except Exception as exc:
        raise self.retry(exc=exc, countdown=5)
"""

celery_usage_code = """
# Utilisation
from tasks import addition, tache_longue

# Appel asynchrone
result = addition.delay(4, 6)
print(f"ID: {result.id}")
print(f"Résultat: {result.get()}")

# Chaînes de tâches
from celery import chain
result = chain(
    addition.s(4, 6),
    addition.s(10),
    addition.s(5)
)()
print(result.get())  # 25

# Groupes parallèles
from celery import group
job = group([
    addition.s(2, 2),
    addition.s(4, 4),
    addition.s(8, 8)
])
result = job.apply_async()
print(result.get())  # [4, 8, 16]
"""

# ============= TP FINAL : MAP-REDUCE =============

def map_function(data):
    """Map : Traite une portion des données"""
    return [x ** 2 for x in data]


def reduce_function(results):
    """Reduce : Combine les résultats"""
    return sum(results)


def map_reduce_simple(data, chunk_size=100):
    """Map-Reduce avec multiprocessing"""
    print("\n=== Map-Reduce Simple ===")
    
    # Découper les données en chunks
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    # Map : Traiter chaque chunk en parallèle
    with ProcessPoolExecutor(max_workers=4) as executor:
        map_results = list(executor.map(map_function, chunks))
    
    # Reduce : Combiner les résultats
    final_result = reduce_function([item for sublist in map_results for item in sublist])
    
    return final_result


# ============= BENCHMARK COMPLET =============

def tache_cpu_benchmark(n):
    """Tâche CPU pour le benchmark"""
    return sum(i**2 for i in range(n))


def benchmark_complet():
    """Benchmark de toutes les approches"""
    print("\n=== Benchmark Complet ===")
    
    data = [10000] * 20
    
    # Séquentiel
    start = time.time()
    resultats = [tache_cpu_benchmark(n) for n in data]
    temps_seq = time.time() - start
    print(f"Séquentiel: {temps_seq:.2f}s")
    
    # Threading (pas bon pour CPU)
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        resultats = list(executor.map(tache_cpu_benchmark, data))
    temps_thread = time.time() - start
    print(f"Threading: {temps_thread:.2f}s (gain: {temps_seq/temps_thread:.2f}x)")
    
    # Multiprocessing (bon pour CPU)
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        resultats = list(executor.map(tache_cpu_benchmark, data))
    temps_process = time.time() - start
    print(f"Multiprocessing: {temps_process:.2f}s (gain: {temps_seq/temps_process:.2f}x)")


# ============= MAIN =============

if __name__ == "__main__":
    print("=== Tests Parallélisme et Calcul Distribué ===\n")
    
    # ATTENTION : Les tests avec multiprocessing peuvent être lents
    # Décommentez les exercices au fur et à mesure que vous les complétez
    
    # Exercices concurrent.futures (à compléter)
    # demo_threading_io()          # Exercice 1
    # demo_process()               # Exercice 2
    # demo_pool()                  # Exercice 3
    # demo_threadpoolexecutor_avance()  # Exercice 4
    # demo_processpoolexecutor_avance() # Exercice 5
    # demo_as_completed()          # Exercice 6
    
    # Exemples avancés (décommentez après avoir complété les exercices de base)
    # data = list(range(1000))
    # result = map_reduce_simple(data)
    # print(f"\nMap-Reduce résultat: {result}")
    
    # benchmark_complet()
    
    # Exemples Celery
    print("\n=== Code Celery (à créer séparément) ===")
    print(celery_app_code)
    print(celery_tasks_code)
    print(celery_usage_code)
    
    print("\n" + "="*50)
    print("Pour Celery:")
    print("1. pip install celery redis")
    print("2. docker compose up -d  # Lancer Redis")
    print("3. Créez celery_app.py et tasks.py")
    print("4. celery -A tasks worker --loglevel=info")
    print("\nAlternative: brew install redis && brew services start redis")
    print("\nConsultez instructions.md pour les exercices détaillés !")
