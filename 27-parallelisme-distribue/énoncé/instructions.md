# Instructions - Parallélisme et Calcul Distribué

Ce module couvre le parallélisme en Python avec threading, multiprocessing et le calcul distribué avec Celery.

## Partie 1 - Threading vs Multiprocessing

### Exercice 1 - Comprendre le GIL

**Le GIL (Global Interpreter Lock)** :

```python
import threading
import time

# Tâche CPU-intensive
def calcul_lourd():
    total = 0
    for i in range(10000000):
        total += i
    return total

# Sans threading
start = time.time()
calcul_lourd()
calcul_lourd()
end = time.time()
print(f"Sans threading : {end - start:.2f}s")

# Avec threading (pas de gain pour CPU-bound !)
def worker():
    calcul_lourd()

start = time.time()
t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(f"Avec threading : {end - start:.2f}s")  # Pas plus rapide !
```

### Exercice 2 - Threading pour I/O-bound

**Threading est bon pour I/O** :

```python
import threading
import time
import requests

urls = [
    'https://www.python.org',
    'https://www.github.com',
    'https://www.stackoverflow.com',
]

# Sans threading
start = time.time()
for url in urls:
    response = requests.get(url)
    print(f"Téléchargé {url}: {len(response.content)} bytes")
end = time.time()
print(f"Sans threading : {end - start:.2f}s")

# Avec threading
def telecharger(url):
    response = requests.get(url)
    print(f"Téléchargé {url}: {len(response.content)} bytes")

start = time.time()
threads = []
for url in urls:
    thread = threading.Thread(target=telecharger, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end = time.time()
print(f"Avec threading : {end - start:.2f}s")  # Plus rapide !
```

## Partie 2 - Multiprocessing

### Exercice 3 - Process simple

**Créez** des processus :

```python
from multiprocessing import Process
import os

def worker(name):
    print(f"Worker {name} dans process {os.getpid()}")

if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = Process(target=worker, args=(f"Process-{i}",))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
```

### Exercice 4 - Pool pour CPU-bound

**Utilisez** multiprocessing.Pool :

```python
from multiprocessing import Pool
import time

def calcul_carre(n):
    return n * n

if __name__ == '__main__':
    # Sans multiprocessing
    start = time.time()
    resultats = [calcul_carre(i) for i in range(10000)]
    print(f"Sans Pool : {time.time() - start:.2f}s")
    
    # Avec multiprocessing
    start = time.time()
    with Pool(processes=4) as pool:
        resultats = pool.map(calcul_carre, range(10000))
    print(f"Avec Pool : {time.time() - start:.2f}s")
```

### Exercice 5 - Communication entre processus

**Utilisez** Queue :

```python
from multiprocessing import Process, Queue

def producteur(queue):
    for i in range(5):
        queue.put(i)
        print(f"Produit : {i}")

def consommateur(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consommé : {item}")

if __name__ == '__main__':
    queue = Queue()
    
    p1 = Process(target=producteur, args=(queue,))
    p2 = Process(target=consommateur, args=(queue,))
    
    p1.start()
    p2.start()
    
    p1.join()
    queue.put(None)  # Signal de fin
    p2.join()
```

### Exercice 6 - Shared memory

**Partagez** des données :

```python
from multiprocessing import Process, Value, Array

def incrementer(compteur, tableau):
    for i in range(100):
        with compteur.get_lock():
            compteur.value += 1
        for j in range(len(tableau)):
            with tableau.get_lock():
                tableau[j] += 1

if __name__ == '__main__':
    compteur = Value('i', 0)  # entier partagé
    tableau = Array('i', [0] * 10)  # tableau partagé
    
    processes = [Process(target=incrementer, args=(compteur, tableau)) for _ in range(4)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    print(f"Compteur final : {compteur.value}")
    print(f"Tableau final : {list(tableau)}")
```

## Partie 3 - concurrent.futures

### Exercice 7 - ThreadPoolExecutor

**Simplifie** le threading :

```python
from concurrent.futures import ThreadPoolExecutor
import time

def tache(n):
    time.sleep(1)
    return n * n

# Avec ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(tache, i) for i in range(10)]
    
    for future in futures:
        print(future.result())
```

### Exercice 8 - ProcessPoolExecutor

**Simplifie** le multiprocessing :

```python
from concurrent.futures import ProcessPoolExecutor

def calcul_lourd(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as executor:
        resultats = list(executor.map(calcul_lourd, [1000000] * 10))
        print(f"Résultats : {resultats[:3]}...")
```

### Exercice 9 - as_completed

**Traitez** les résultats dès qu'ils arrivent :

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import random

def tache_variable(n):
    duree = random.uniform(1, 3)
    time.sleep(duree)
    return n, duree

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(tache_variable, i): i for i in range(10)}
        
        for future in as_completed(futures):
            n, duree = future.result()
            print(f"Tâche {n} terminée en {duree:.2f}s")
```

## Partie 4 - Celery

### Exercice 10 - Installation et configuration

**Installez** Celery et Redis :

```bash
pip install celery redis
```

**Installez** Redis :

```bash
# Mac
brew install redis
brew services start redis

# Linux
sudo apt install redis-server
sudo systemctl start redis
```

**Créez** `celery_app.py` :

```python
from celery import Celery

app = Celery('tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Europe/Paris',
    enable_utc=True,
)
```

### Exercice 11 - Première tâche Celery

**Créez** `tasks.py` :

```python
from celery_app import app
import time

@app.task
def addition(x, y):
    return x + y

@app.task
def tache_longue(duree):
    time.sleep(duree)
    return f"Tâche terminée après {duree}s"
```

**Lancez** le worker :

```bash
celery -A tasks worker --loglevel=info
```

**Utilisez** les tâches :

```python
from tasks import addition, tache_longue

# Appel asynchrone
result = addition.delay(4, 6)
print(f"ID de la tâche : {result.id}")
print(f"Résultat : {result.get()}")  # Attend le résultat

# Ou sans attendre
result = tache_longue.delay(5)
print(f"Tâche lancée : {result.id}")
# Faire autre chose...
print(f"Résultat : {result.get(timeout=10)}")
```

### Exercice 12 - Tâches avec retry

**Gérez** les échecs :

```python
from celery_app import app
import random

@app.task(bind=True, max_retries=3)
def tache_instable(self, x):
    try:
        if random.random() < 0.7:
            raise Exception("Erreur aléatoire")
        return x * 2
    except Exception as exc:
        raise self.retry(exc=exc, countdown=5)  # Retry après 5s
```

### Exercice 13 - Chaînes de tâches

**Enchaînez** des tâches :

```python
from celery import chain
from tasks import addition

# Chaîne : (4 + 6) + 10 + 5
result = chain(
    addition.s(4, 6),
    addition.s(10),
    addition.s(5)
)()

print(result.get())  # 25
```

### Exercice 14 - Groupes de tâches

**Exécutez** en parallèle :

```python
from celery import group
from tasks import addition

# Groupe de tâches parallèles
job = group([
    addition.s(2, 2),
    addition.s(4, 4),
    addition.s(8, 8)
])

result = job.apply_async()
print(result.get())  # [4, 8, 16]
```

## TP Final - Map-Reduce avec Celery

**Implémentez** Map-Reduce :

```python
# tasks.py
from celery_app import app

@app.task
def map_task(data):
    """Map : Traite une portion des données"""
    return [x ** 2 for x in data]

@app.task
def reduce_task(results):
    """Reduce : Combine les résultats"""
    return sum(results)

# main.py
from celery import group, chord
from tasks import map_task, reduce_task

def map_reduce(data, chunk_size=100):
    """
    Map-Reduce distribué
    1. Découpe les données en chunks
    2. Map chaque chunk en parallèle
    3. Reduce tous les résultats
    """
    # Découper les données
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    # Map-Reduce avec chord
    callback = reduce_task.s()
    header = group(map_task.s(chunk) for chunk in chunks)
    result = chord(header)(callback)
    
    return result.get()

if __name__ == '__main__':
    data = list(range(1000))
    resultat = map_reduce(data)
    print(f"Somme des carrés : {resultat}")
```

### TP - Traitement distribué de fichiers

**Créez** un pipeline de traitement :

```python
# tasks.py
from celery_app import app
import time

@app.task
def lire_fichier(filepath):
    """Étape 1 : Lire le fichier"""
    with open(filepath) as f:
        return f.read()

@app.task
def traiter_texte(texte):
    """Étape 2 : Traiter le texte"""
    mots = texte.split()
    return {
        'nombre_mots': len(mots),
        'nombre_lignes': texte.count('\n'),
        'mots_uniques': len(set(mots))
    }

@app.task
def sauvegarder_resultats(stats):
    """Étape 3 : Sauvegarder les statistiques"""
    with open('resultats.txt', 'w') as f:
        for key, value in stats.items():
            f.write(f"{key}: {value}\n")
    return "Sauvegardé"

# Pipeline complet
from celery import chain

pipeline = chain(
    lire_fichier.s('document.txt'),
    traiter_texte.s(),
    sauvegarder_resultats.s()
)

result = pipeline.apply_async()
print(result.get())
```

### TP - Calcul distribué parallèle

**Calculez** des nombres premiers en parallèle :

```python
from celery import group
from celery_app import app

@app.task
def trouver_premiers_chunk(start, end):
    """Trouve les nombres premiers dans une plage"""
    def est_premier(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return [n for n in range(start, end) if est_premier(n)]

def trouver_premiers_distribue(max_n, chunk_size=10000):
    """Trouve tous les premiers jusqu'à max_n en distribué"""
    # Créer les tâches
    chunks = []
    for start in range(2, max_n, chunk_size):
        end = min(start + chunk_size, max_n)
        chunks.append(trouver_premiers_chunk.s(start, end))
    
    # Exécuter en parallèle
    job = group(chunks)
    result = job.apply_async()
    
    # Collecter tous les résultats
    all_primes = []
    for chunk_result in result.get():
        all_primes.extend(chunk_result)
    
    return sorted(all_primes)

if __name__ == '__main__':
    premiers = trouver_premiers_distribue(100000)
    print(f"Trouvé {len(premiers)} nombres premiers")
    print(f"Premiers 10 : {premiers[:10]}")
```

## Partie 5 - Monitoring et déploiement

### Exercice 15 - Flower (monitoring)

**Installez** Flower :

```bash
pip install flower
```

**Lancez** :

```bash
celery -A tasks flower
```

Accédez à http://localhost:5555

### Exercice 16 - Configuration avancée

**Configurez** Celery :

```python
# celery_config.py
broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

timezone = 'Europe/Paris'
enable_utc = True

# Retry
task_acks_late = True
task_reject_on_worker_lost = True

# Rate limiting
task_annotations = {
    'tasks.api_call': {'rate_limit': '10/m'}
}

# Routes
task_routes = {
    'tasks.heavy_task': {'queue': 'heavy'},
    'tasks.light_task': {'queue': 'light'},
}
```

## Checklist de validation

- ✅ GIL compris (threading vs multiprocessing)
- ✅ Threading utilisé pour I/O-bound
- ✅ Multiprocessing utilisé pour CPU-bound
- ✅ Pool et Queue maîtrisés
- ✅ concurrent.futures utilisé
- ✅ Celery installé et configuré
- ✅ Tâches asynchrones créées
- ✅ Retry et error handling implémentés
- ✅ Chaînes et groupes de tâches utilisés
- ✅ **TP : Map-Reduce avec Celery réalisé**
- ✅ Flower pour monitoring configuré
