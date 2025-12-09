# Instructions - Parallélisme et Calcul Distribué

Ce module couvre le parallélisme en Python avec **concurrent.futures** (ThreadPoolExecutor et ProcessPoolExecutor) et le calcul distribué avec **Celery**.

## 📚 Structure du TP

Le TP est divisé en 5 parties avec 14 exercices :

1. **Partie 1** - Threading avec ThreadPoolExecutor (1 exercice)
2. **Partie 2** - Multiprocessing avec ProcessPoolExecutor (2 exercices)
3. **Partie 3** - concurrent.futures avancé (3 exercices)
4. **Partie 4** - Celery et calcul distribué (6 exercices)
5. **Partie 5** - Monitoring et configuration (2 exercices)

## 📁 Fichiers fournis

- **`main.py`** - Exercices 1-6 à compléter (mode hints)
- **`docker-compose.yml`** - Configuration Redis pour Celery
- **`celery_app.py`** - Configuration Celery (prête à l'emploi)
- **`tasks.py`** - Structure pour exercices 8-12 (à compléter)

## 🎯 Objectifs pédagogiques

- Comprendre la différence entre threading (I/O) et multiprocessing (CPU)
- Maîtriser ThreadPoolExecutor et ProcessPoolExecutor
- Utiliser map(), submit() et as_completed()
- Créer des tâches asynchrones avec Celery
- Orchestrer des workflows complexes (chains, groups, chords)
- Implémenter du Map-Reduce distribué
- Monitorer et débugger avec Flower

---

## Partie 1 - Threading avec concurrent.futures

### Exercice 1 - ThreadPoolExecutor pour I/O-bound

**ThreadPoolExecutor est bon pour I/O** (requêtes HTTP, fichiers, etc.) :

```python
from concurrent.futures import ThreadPoolExecutor
import time
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
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            data = response.read()
            print(f"✓ Téléchargé {url}: {len(data)} bytes")
            return len(data)
    except Exception as e:
        print(f"✗ Erreur {url}: {e}")
        return 0

# Sans threading - séquentiel
start = time.time()
for url in urls:
    telecharger(url)
temps_sequentiel = time.time() - start
print(f"Sans threading : {temps_sequentiel:.2f}s")

# Avec ThreadPoolExecutor - parallèle
start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(telecharger, urls))
temps_parallel = time.time() - start
print(f"Avec ThreadPoolExecutor : {temps_parallel:.2f}s")
print(f"Gain: {temps_sequentiel/temps_parallel:.1f}x plus rapide !")
```

## Partie 2 - Multiprocessing avec concurrent.futures

### Exercice 2 - ProcessPoolExecutor simple

**Créez** des processus :

```python
from concurrent.futures import ProcessPoolExecutor
import os

def worker(name):
    print(f"Worker {name} dans process {os.getpid()}")
    return f"Terminé: {name}"

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(worker, f"Process-{i}") for i in range(5)]
        results = [f.result() for f in futures]
```

### Exercice 3 - ProcessPoolExecutor pour CPU-bound

**Utilisez** ProcessPoolExecutor.map :

```python
from concurrent.futures import ProcessPoolExecutor
import time

def calcul_carre(n):
    return n * n

if __name__ == '__main__':
    data = list(range(10000))
    
    # Sans multiprocessing
    start = time.time()
    resultats = [calcul_carre(i) for i in data]
    print(f"Sans ProcessPoolExecutor : {time.time() - start:.2f}s")
    
    # Avec ProcessPoolExecutor
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        resultats = list(executor.map(calcul_carre, data))
    print(f"Avec ProcessPoolExecutor : {time.time() - start:.2f}s")
```

## Partie 3 - concurrent.futures avancé

### Exercice 4 - ThreadPoolExecutor avancé

**Utilisez** ThreadPoolExecutor avec submit :

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

### Exercice 5 - ProcessPoolExecutor avancé

**Utilisez** ProcessPoolExecutor pour calculs lourds :

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

### Exercice 6 - as_completed

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

## Partie 4 - Celery (Calcul Distribué)

### Prérequis : Docker Compose

Ce TP utilise **Docker Compose** pour lancer Redis facilement :

```bash
# Vérifier que Docker est installé
docker --version

# Le fichier docker-compose.yml est déjà fourni
# Il configure Redis sur le port 6379
```

### Exercice 7 - Installation et configuration

**Installez** Celery :

```bash
pip install celery redis
```

**Lancez** Redis avec Docker Compose :

```bash
# Démarrer Redis
docker compose up -d

# Vérifier que Redis fonctionne
docker compose ps

# Voir les logs
docker compose logs redis

# Arrêter Redis
docker compose down
```

**Configuration Celery** :

Le fichier `celery_app.py` est **déjà fourni** avec la configuration suivante :

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

✅ **Ce fichier est prêt à l'emploi, vous n'avez pas besoin de le modifier.**

**🔍 Bonus : Visualiser Redis** (optionnel)

**Option 1 - Interface graphique RedisInsight** :
1. Télécharger **RedisInsight** : https://redis.io/insight/
2. Se connecter à `localhost:6379`
3. Explorer les clés `celery-task-meta-*` (résultats) et `celery` (file d'attente)

**Option 2 - Ligne de commande** :
```bash
# Se connecter à Redis
redis-cli

# Voir toutes les clés
KEYS *

# Voir les résultats de tâches stockés
KEYS celery-task-meta-*

# Voir le contenu d'un résultat (remplacer <task-id> par un ID réel)
GET celery-task-meta-<task-id>

# Quitter
exit
```

### Exercice 8 - Première tâche Celery

Le fichier `tasks.py` est **déjà fourni** avec une structure de base et des commentaires d'aide.

**Objectif** : Créer deux tâches de base dans `tasks.py`

**Syntaxe du décorateur de tâche** :
```python
from celery_app import app
import time

@app.task
def nom_tache(paramètres):
    # Votre code ici
    return résultat
```

**💡 Rappel important** : 
- Une tâche Celery est une fonction Python normale avec `@app.task`
- Elle doit être dans `tasks.py` pour que le worker puisse la trouver
- Le décorateur `@app.task` vient de l'objet `app` créé dans `celery_app.py`

**À faire dans `tasks.py`** :

1. **Importer les modules nécessaires** :
   ```python
   from celery_app import app
   import time
   ```

2. **Créer la tâche `addition(x, y)`** :
   - Décorer avec `@app.task`
   - Retourner simplement `x + y`
   - C'est la tâche la plus simple possible !

3. **Créer la tâche `tache_longue(duree)`** :
   - Décorer avec `@app.task`
   - Utiliser `time.sleep(duree)` pour simuler un traitement long
   - Retourner un message f-string comme `f"Tâche terminée après {duree}s"`

**Lancer le worker** (Terminal 1) :
```bash
celery -A tasks worker --loglevel=info
```

💡 Le worker va charger vos tâches et attendre des jobs. Laissez-le tourner !

**Tester vos tâches** (Terminal 2 - Python interactif) :
```python
from tasks import addition, tache_longue

# Test 1 : Addition simple
result = addition.delay(4, 6)
print(f"ID de la tâche: {result.id}")
print(f"Résultat: {result.get()}")  # Devrait afficher 10

# Test 2 : Tâche longue (vérifiez les logs du worker !)
result = tache_longue.delay(2)
print(f"Tâche lancée: {result.id}")
print(f"Résultat: {result.get()}")  # Attend 2s puis affiche le message
```

**🔍 Vérification** : Dans le terminal du worker, vous devriez voir les logs des tâches exécutées !

### Exercice 9 - Chaînes de tâches

**Objectif** : Enchaîner des tâches où la sortie de l'une devient l'entrée de la suivante

**Concept** : Imaginez un pipeline de traitement : `données -> transformation1 -> transformation2 -> résultat`

**💡 La "signature" avec `.s()`** :
- `.s()` crée une "promesse" d'exécution sans la lancer
- Permet de composer des tâches avant de les exécuter

**Syntaxe complète** :
```python
from celery import chain
from tasks import addition, multiplication

# Exemple : (2 + 3) * 5 = 25
workflow = chain(
    addition.s(2, 3),      # Étape 1: 2 + 3 = 5
    multiplication.s(5)     # Étape 2: 5 * 5 = 25 (reçoit 5 en premier arg)
)

result = workflow.apply_async()
print(result.get())  # Affiche 25
```

**À faire dans `tasks.py`** :
1. **Créer la tâche `multiplication(x, y)`** :
   ```python
   @app.task
   def multiplication(x, y):
       return x * y
   ```

2. **Tester votre chaîne** (dans Python interactif) :
   - Calculer `(4 + 6) * 2`
   - Utiliser `chain()` avec les deux tâches
   - Vérifier que le résultat est 20

**Exemple de test** :
```python
from celery import chain
from tasks import addition, multiplication

# (4 + 6) * 2 = 20
result = chain(
    addition.s(4, 6),
    multiplication.s(2)
).apply_async()

print(f"Résultat: {result.get()}")  # Devrait afficher 20
```

### Exercice 10 - Groupes de tâches

**Objectif** : Exécuter plusieurs tâches en parallèle

**Concept** : Parfait pour traiter plusieurs données indépendamment en même temps.

**Différence avec chain** :
- **Chain** : Exécution **séquentielle** (l'une après l'autre)
- **Group** : Exécution **parallèle** (toutes en même temps)

**Syntaxe complète** :
```python
from celery import group
from tasks import addition

# Exécuter 4 additions en parallèle
job = group([
    addition.s(1, 1),
    addition.s(2, 2),
    addition.s(3, 3),
    addition.s(4, 4)
])

result = job.apply_async()
resultats = result.get()  # [2, 4, 6, 8]
print(f"Résultats: {resultats}")
```

**À faire** :
1. **Créer un groupe** avec 5 ou 6 tâches `addition`
2. **Lancer** avec `.apply_async()`
3. **Récupérer** les résultats (liste ordonnée)
4. **Observer** dans les logs du worker : les tâches s'exécutent en parallèle !

**Test avec timing** :
```python
import time
from celery import group
from tasks import tache_longue

# 3 tâches de 2s chacune
start = time.time()
job = group([tache_longue.s(2) for i in range(3)])
result = job.apply_async()
result.get()
print(f"Temps total: {time.time() - start:.1f}s")  # ~2s au lieu de 6s !
```

🚀 **Si vous avez 12 workers (par défaut), les 3 tâches s'exécutent vraiment en parallèle !**

### Exercice 11 - Map-Reduce avec Celery

**Objectif** : Implémenter un pattern Map-Reduce distribué

**Concept Map-Reduce** (comme Hadoop/Spark) :
- **Map** : Transformer des données en parallèle sur plusieurs workers
- **Reduce** : Combiner tous les résultats en un seul

**Exemple concret** : Calculer la somme des carrés de 1 à 1000
- 📊 Map : Diviser en chunks [1-100], [101-200], etc. et calculer carrés
- 📦 Reduce : Additionner tous les résultats

**💡 Le "chord"** : group + callback finale
```python
from celery import group, chord

# Header = groupe de tâches map
# Callback = tâche reduce qui reçoit tous les résultats
result = chord(header)(callback)
```

**À faire dans `tasks.py`** :

1. **Créer `map_task(data)`** :
   ```python
   @app.task
   def map_task(data):
       """Transforme une portion des données"""
       return [x ** 2 for x in data]  # Calcule les carrés
   ```

2. **Créer `reduce_task(results)`** :
   ```python
   @app.task
   def reduce_task(results):
       """Combine tous les résultats"""
       # results est une LISTE DE LISTES : [[1, 4, 9], [16, 25, 36], ...]
       # Il faut d'abord aplatir puis additionner
       all_values = []
       for chunk_result in results:
           all_values.extend(chunk_result)
       return sum(all_values)
   ```

**Exemple d'utilisation complet** :
```python
from celery import group, chord
from tasks import map_task, reduce_task

# Données : 1 à 1000
data = list(range(1, 1001))

# Découper en chunks de 100
chunks = [data[i:i+100] for i in range(0, len(data), 100)]

# Map-Reduce
header = group(map_task.s(chunk) for chunk in chunks)
callback = reduce_task.s()
result = chord(header)(callback)

print(f"Somme des carrés: {result.get()}")  # 333833500
```

🎯 **Objectif** : Les 10 chunks sont traités en parallèle, puis reduce combine le tout !

### Exercice 12 - Traitement distribué de fichiers (Pipeline)

**Objectif** : Créer un pipeline de traitement de fichier en 3 étapes

**Concept Pipeline** : Chaîner des tâches de traitement de données (comme un pipeline Unix)

**Use case réel** : Lire un fichier → Analyser → Sauvegarder stats

**À faire dans `tasks.py`** :

1. **`lire_fichier(filepath)`** :
   ```python
   @app.task
   def lire_fichier(filepath):
       with open(filepath, 'r') as f:
           return f.read()
   ```

2. **`traiter_texte(texte)`** :
   ```python
   @app.task
   def traiter_texte(texte):
       mots = texte.split()
       return {
           'nombre_mots': len(mots),
           'nombre_lignes': texte.count('\n') + 1,
           'mots_uniques': len(set(mots))
       }
   ```

3. **`sauvegarder_resultats(stats)`** :
   ```python
   @app.task
   def sauvegarder_resultats(stats):
       with open('resultats.txt', 'w') as f:
           for cle, valeur in stats.items():
               f.write(f"{cle}: {valeur}\n")
       return "Statistiques sauvegardées"
   ```

**Utiliser le pipeline** :
```python
from celery import chain
from tasks import lire_fichier, traiter_texte, sauvegarder_resultats

# Créer un fichier de test
with open('test.txt', 'w') as f:
    f.write("Bonjour monde\nCelery est super\nPython est génial")

# Pipeline
pipeline = chain(
    lire_fichier.s('test.txt'),
    traiter_texte.s(),
    sauvegarder_resultats.s()
)

result = pipeline.apply_async()
print(result.get())  # "Statistiques sauvegardées"

# Vérifier le fichier resultats.txt
with open('resultats.txt') as f:
    print(f.read())
```

## Partie 5 - Monitoring et Tests

### Exercice 13 - Flower (monitoring)

**Objectif** : Monitorer vos tâches Celery avec Flower

**Installation** :
```bash
pip install flower
```

**Lancement** :
```bash
celery -A tasks flower
```

**Interface web** : http://localhost:5555

**À explorer dans Flower** :
- 📊 Dashboard : Vue d'ensemble des workers et tâches
- 📈 Graphiques : Débit des tâches en temps réel  
- 📋 Tasks : Liste de toutes les tâches exécutées
- 👷 Workers : Statut et configuration des workers
- 🔍 Détails : Cliquer sur une tâche pour voir arguments, résultat, traceback

**Test** : Lancez quelques tâches et observez-les dans Flower !

### Exercice 14 - Configuration avancée

**Objectif** : Explorer les options de configuration avancées de Celery

**Options utiles à connaître** :

1. **Retry automatique des tâches** :
```python
task_acks_late = True  # Acquitter après exécution
task_reject_on_worker_lost = True  # Réessayer si worker crash
```

2. **Rate limiting** (limiter le débit) :
```python
task_annotations = {
    'tasks.ma_tache': {'rate_limit': '10/m'}  # 10 tâches par minute
}
```

3. **Routes** (diriger vers des queues spécifiques) :
```python
task_routes = {
    'tasks.tache_lourde': {'queue': 'heavy'},
    'tasks.tache_legere': {'queue': 'light'}
}
```

**À faire** : Tester une de ces configurations dans `celery_app.py` et observer le comportement.

## ✅ Checklist de Validation

### Partie 1-3 : concurrent.futures (Exercices 1-6)
- [ ] **Exercice 1** - ThreadPoolExecutor pour I/O-bound avec requêtes HTTP réelles
- [ ] **Exercice 2** - ProcessPoolExecutor simple (création de processus)
- [ ] **Exercice 3** - ProcessPoolExecutor pour CPU-bound (calculs)
- [ ] **Exercice 4** - ThreadPoolExecutor avancé avec submit()
- [ ] **Exercice 5** - ProcessPoolExecutor pour calculs lourds
- [ ] **Exercice 6** - as_completed() pour traiter résultats dès disponibilité

### Partie 4 : Celery (Exercices 7-12)
- [ ] **Exercice 7** - Docker Compose + Redis lancés
- [ ] **Exercice 8** - Première tâche Celery exécutée
- [ ] **Exercice 9** - Chaînes de tâches (chains) fonctionnelles
- [ ] **Exercice 10** - Groupes de tâches parallèles
- [ ] **Exercice 11** - Map-Reduce distribué réalisé
- [ ] **Exercice 12** - Pipeline de traitement de fichiers

### Partie 5 : Monitoring et Configuration (Exercices 13-14)
- [ ] **Exercice 13** - Flower installé et accessible
- [ ] **Exercice 14** - Configuration avancée maîtrisée

### Validation Finale

**Critères de réussite :**

- ✅ Worker Celery démarre sans erreur
- ✅ Les tâches s'exécutent correctement
- ✅ Flower affiche les tâches exécutées (exercice 13)
- ✅ Redis contient les résultats des tâches
- ✅ Performance: gain de 3-4x en parallèle pour les tâches concurrentes

---

**🎉 Félicitations !** Si tous les tests passent, vous maîtrisez le parallélisme et le calcul distribué en Python !

## 🧹 Nettoyage

Après avoir terminé le TP, vous pouvez nettoyer l'environnement :

```bash
# 1. Arrêter le worker Celery (Ctrl+C dans le terminal)
# 2. Arrêter Flower (Ctrl+C dans le terminal)

# 3. Arrêter Redis
docker compose down

# 4. Supprimer aussi les données Redis (optionnel)
docker compose down -v

# 5. Nettoyer les fichiers temporaires Python
rm -rf __pycache__
find . -name "*.pyc" -delete
```

## 📚 Pour Aller Plus Loin

- [Documentation Celery](https://docs.celeryproject.org/)
- [Documentation concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- [Docker Compose Reference](https://docs.docker.com/compose/)
- [Redis Documentation](https://redis.io/docs/)
- [Flower Documentation](https://flower.readthedocs.io/)
