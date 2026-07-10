## Énoncé : Le Planificateur de tâches

### Contexte

On dispose d'une liste `tasks` (des lettres représentant des tâches CPU, par
exemple ['A', 'A', 'B', 'B', ...]) et d'un entier `n` : le délai minimum de
refroidissement entre deux exécutions de la MÊME tâche.

À chaque unité de temps, le CPU peut :
  - exécuter une tâche disponible (pas en cooldown), ou
  - rester "idle" (ne rien faire) si aucune tâche n'est disponible.

### Exemple

tasks = ["A","A","A","B","B","B"], n = 2 → 8 (ex: A B _ A B _ A B)
tasks = ["A","A","A","B","B","B"], n = 0 → 6
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2 → 16


### Objectif

Écrire une fonction qui calcule le temps total minimum pour exécuter toutes les tâches.

### Prototype de la fonction

```python
def min_temp_tache(tasks: list[str], n: int) -> int:
    """
    Calcule le temps minimum pour exécuter toutes les tâches en respectant
    le délai de refroidissement n entre deux occurrences d'une même tâche.

    Args:
        tasks: liste de tâches (ex: ["A", "A", "B"])
        n: délai minimum (en unités de temps) entre deux exécutions
           d'une même tâche

    Returns:
        Le nombre d'unités de temps minimum nécessaires (int).
    """
    # Votre code ici
    pass
```

### Tests
```python
print("Démarrage des tests pour le Planificateur de tâches...")

# Test 1 : Liste de tâches vide
print("Test 1...", min_temp_tache([], 3))
assert min_temp_tache([], 3) == 0, "Échec Test 1"

# Test 2: Une seule tâche
print("Test 2...", min_temp_tache(["A"], 3))
assert min_temp_tache(["A"], 5) == 1, "Échec Test 2"

# Test 3 : Tâches identiques
print("Test 3...", min_temp_tache(["A", "A", "A"], 2))
assert min_temp_tache(["A", "A", "A"], 2) == 7, "Échec Test 3"

# Test 4 : Tâches distinctes alternées
print("Test 4...", min_temp_tache(["A", "B", "A", "B", "A", "B"], 1))
assert min_temp_tache(["A", "B", "A", "B", "A", "B"], 1) == 6, "Échec Test 4"

# Test 5 : Exemple classique avec temps d'attente
print("Test 5...", min_temp_tache(["A", "A", "A", "B", "B", "B"], 2))
assert min_temp_tache(["A", "A", "A", "B", "B", "B"], 2) == 8, "Échec Test 5"

# Test 6 : Taches sans cooldown
print("Test 6...", min_temp_tache(["A", "A", "A", "B", "B", "B"], 0))
assert min_temp_tache(["A", "A", "A", "B", "B", "B"], 0) == 6, "Échec Test 6"

print("\nTous les tests du Planificateur de tâches ont passé avec succès !")
```