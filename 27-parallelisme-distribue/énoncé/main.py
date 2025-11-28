# Écrivez votre code ici !
# Consultez le fichier instructions.md pour les consignes

import time
import threading
from multiprocessing import Process, Pool, Queue, Value, Array
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# ============= PARTIE 1 : THREADING VS MULTIPROCESSING =============

# Exercice 1 - Comprendre le GIL
def calcul_lourd():
    """Tâche CPU-intensive"""
    total = 0
    for i in range(10000000):
        total += i
    return total


def demo_gil():
    """Démontre que le threading ne parallélise pas le CPU-bound"""
    print("=== Démonstration du GIL ===")
    
    # Sans threading
    start = time.time()
    calcul_lourd()
    calcul_lourd()
    temps_sequentiel = time.time() - start
    print(f"Sans threading : {temps_sequentiel:.2f}s")
    
    # Avec threading (pas plus rapide pour CPU-bound!)
    def worker():
        calcul_lourd()
    
    start = time.time()
    t1 = threading.Thread(target=worker)
    t2 = threading.Thread(target=worker)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    temps_threading = time.time() - start
    print(f"Avec threading : {temps_threading:.2f}s")
    print(f"Gain: {temps_sequentiel/temps_threading:.2f}x (pas d'amélioration)")


# Exercice 2 - Threading pour I/O-bound
def telecharger_simulation(url):
    """Simule un téléchargement (I/O-bound)"""
    time.sleep(1)  # Simule I/O
    return f"Downloaded {url}"


def demo_threading_io():
    """Threading est bon pour I/O-bound"""
    print("\n=== Threading pour I/O ===")
    
    urls = ['url1', 'url2', 'url3', 'url4', 'url5']
    
    # Sans threading
    start = time.time()
    for url in urls:
        telecharger_simulation(url)
    temps_sequentiel = time.time() - start
    print(f"Sans threading : {temps_sequentiel:.2f}s")
    
    # Avec threading
    start = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=telecharger_simulation, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    temps_threading = time.time() - start
    print(f"Avec threading : {temps_threading:.2f}s")
    print(f"Gain: {temps_sequentiel/temps_threading:.1f}x plus rapide")


# ============= PARTIE 2 : MULTIPROCESSING =============

# Exercice 3 - Process simple
def worker_process(name):
    """Worker simple"""
    import os
    print(f"Worker {name} dans process {os.getpid()}")


def demo_process():
    """Démonstration de multiprocessing"""
    print("\n=== Multiprocessing ===")
    
    processes = []
    for i in range(5):
        p = Process(target=worker_process, args=(f"Process-{i}",))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()


# Exercice 4 - Pool pour CPU-bound
def calcul_carre(n):
    """Calcule le carré"""
    return n * n


def demo_pool():
    """Démonstration de Pool"""
    print("\n=== Multiprocessing Pool ===")
    
    data = list(range(10000))
    
    # Sans Pool
    start = time.time()
    resultats = [calcul_carre(i) for i in data]
    temps_sequentiel = time.time() - start
    print(f"Sans Pool : {temps_sequentiel:.4f}s")
    
    # Avec Pool
    start = time.time()
    with Pool(processes=4) as pool:
        resultats = pool.map(calcul_carre, data)
    temps_pool = time.time() - start
    print(f"Avec Pool : {temps_pool:.4f}s")
    print(f"Gain: {temps_sequentiel/temps_pool:.1f}x plus rapide")


# Exercice 5 - Communication avec Queue
def producteur(queue):
    """Producteur de données"""
    for i in range(5):
        queue.put(i)
        print(f"Produit : {i}")
        time.sleep(0.5)


def consommateur(queue):
    """Consommateur de données"""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consommé : {item}")


def demo_queue():
    """Démonstration de Queue"""
    print("\n=== Queue (communication inter-process) ===")
    
    queue = Queue()
    
    p1 = Process(target=producteur, args=(queue,))
    p2 = Process(target=consommateur, args=(queue,))
    
    p1.start()
    p2.start()
    
    p1.join()
    queue.put(None)  # Signal de fin
    p2.join()


# Exercice 6 - Shared memory
def incrementer(compteur, tableau):
    """Incrémente des valeurs partagées"""
    for i in range(100):
        with compteur.get_lock():
            compteur.value += 1
        for j in range(len(tableau)):
            with tableau.get_lock():
                tableau[j] += 1


def demo_shared_memory():
    """Démonstration de mémoire partagée"""
    print("\n=== Shared Memory ===")
    
    compteur = Value('i', 0)
    tableau = Array('i', [0] * 5)
    
    processes = [Process(target=incrementer, args=(compteur, tableau)) for _ in range(4)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    print(f"Compteur final : {compteur.value}")
    print(f"Tableau final : {list(tableau)}")


# ============= PARTIE 3 : CONCURRENT.FUTURES =============

# Exercice 7 - ThreadPoolExecutor
def tache_io(n):
    """Tâche I/O"""
    time.sleep(0.5)
    return n * n


def demo_threadpoolexecutor():
    """Démonstration de ThreadPoolExecutor"""
    print("\n=== ThreadPoolExecutor ===")
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(tache_io, i) for i in range(10)]
        
        for future in futures:
            print(f"Résultat : {future.result()}")


# Exercice 8 - ProcessPoolExecutor
def calcul_intensif(n):
    """Calcul CPU-intensif"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total


def demo_processpoolexecutor():
    """Démonstration de ProcessPoolExecutor"""
    print("\n=== ProcessPoolExecutor ===")
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        resultats = list(executor.map(calcul_intensif, [1000000] * 8))
        print(f"Résultats : {resultats[:3]}...")


# Exercice 9 - as_completed
def tache_variable(n):
    """Tâche avec durée variable"""
    import random
    duree = random.uniform(0.5, 2)
    time.sleep(duree)
    return n, duree


def demo_as_completed():
    """Traite les résultats dès qu'ils arrivent"""
    print("\n=== as_completed ===")
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(tache_variable, i): i for i in range(5)}
        
        for future in as_completed(futures):
            n, duree = future.result()
            print(f"Tâche {n} terminée en {duree:.2f}s")


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

def benchmark_complet():
    """Benchmark de toutes les approches"""
    print("\n=== Benchmark Complet ===")
    
    def tache_cpu(n):
        return sum(i**2 for i in range(n))
    
    data = [10000] * 20
    
    # Séquentiel
    start = time.time()
    resultats = [tache_cpu(n) for n in data]
    temps_seq = time.time() - start
    print(f"Séquentiel: {temps_seq:.2f}s")
    
    # Threading (pas bon pour CPU)
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        resultats = list(executor.map(tache_cpu, data))
    temps_thread = time.time() - start
    print(f"Threading: {temps_thread:.2f}s (gain: {temps_seq/temps_thread:.2f}x)")
    
    # Multiprocessing (bon pour CPU)
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        resultats = list(executor.map(tache_cpu, data))
    temps_process = time.time() - start
    print(f"Multiprocessing: {temps_process:.2f}s (gain: {temps_seq/temps_process:.2f}x)")


# ============= MAIN =============

if __name__ == "__main__":
    print("=== Tests Parallélisme et Calcul Distribué ===\n")
    
    # ATTENTION : Les tests avec multiprocessing peuvent être lents
    # Commentez ceux que vous ne voulez pas exécuter
    
    # 1. GIL
    demo_gil()
    
    # 2. Threading pour I/O
    demo_threading_io()
    
    # 3. Multiprocessing
    demo_process()
    
    # 4. Pool
    demo_pool()
    
    # 5. ThreadPoolExecutor
    demo_threadpoolexecutor()
    
    # 6. ProcessPoolExecutor
    demo_processpoolexecutor()
    
    # 7. as_completed
    demo_as_completed()
    
    # 8. Map-Reduce
    data = list(range(1000))
    result = map_reduce_simple(data)
    print(f"\nMap-Reduce résultat: {result}")
    
    # 9. Benchmark
    benchmark_complet()
    
    # Exemples Celery
    print("\n=== Code Celery (à créer séparément) ===")
    print(celery_app_code)
    print(celery_tasks_code)
    print(celery_usage_code)
    
    print("\n" + "="*50)
    print("Pour Celery:")
    print("1. pip install celery redis")
    print("2. brew install redis && brew services start redis")
    print("3. Créez celery_app.py et tasks.py")
    print("4. celery -A tasks worker --loglevel=info")
    print("\nConsultez instructions.md pour les exercices détaillés !")
