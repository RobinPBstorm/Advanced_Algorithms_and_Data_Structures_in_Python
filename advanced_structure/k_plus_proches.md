## Énoncé : Les K Plus Proches Voisins (Le Radar de Proximité)

### Contexte

Tu développes un petit module pour un système de recommandation. Étant donné une liste de nombres (par exemple des scores, des prix, ou des positions) et une **valeur cible** `x`, tu dois retrouver les `k` nombres de la liste les plus proches de `x`.

### Objectif

L'objectif est de renvoyer les `k` nombres les plus proches de `x`, **triés du plus proche au plus éloigné**. En cas d'égalité de distance entre deux nombres, celui qui a la **plus petite valeur** doit apparaître en premier.

### Consignes de codage

Tu dois écrire une fonction `k_plus_proches(nombres, x, k)` en Python.

* **`nombres`** : Une liste d'entiers (peut contenir des doublons).
* **`x`** : La valeur cible (entier).
* **`k`** : Le nombre de voisins à retourner (entier).
* **Valeur de retour** : Une **liste d'entiers** de taille `k` (ou moins si `len(nombres) < k`), triée selon la règle ci-dessus.

> 💡 **Le piège et l'astuce algorithmique (Pourquoi utiliser `heapq` ?) :**
> Si tu tries l'intégralité de la liste à chaque appel, ta solution sera correcte mais coûteuse en $O(n \log n)$ alors qu'on peut faire mieux quand $k$ est petit devant $n$.
> La stratégie gagnante :
> 1. Pour chaque nombre, calcule une **clé de comparaison** qui combine sa distance à `x` et sa valeur (pour gérer les égalités automatiquement).
> 2. Utilise un **tas** pour ne conserver à tout moment que les `k` meilleurs candidats rencontrés jusqu'ici, en éjectant le pire quand le tas dépasse la taille `k`.
> 3. Attention au sens du tas : `heapq` en Python est un **min-tas**. Réfléchis à quelle valeur tu dois éjecter (et donc comment orienter tes clés) pour ne garder que les `k` plus proches.
> 4. Une fois le tas final obtenu, il faut encore le **trier dans le bon ordre** pour le résultat (le tas garantit que le minimum est accessible en $O(1)$, mais son ordre interne n'est pas trié).

---

### Exemple de comportement attendu

```python
k_plus_proches([1, 5, 8, 3, 10, 6], 7, 3)
# Distances à x=7 : 1->6, 5->2, 8->1, 3->4, 10->3, 6->1
# Les 3 plus proches (distance 1, 1, 2) : 8, 6, 5
# Égalité de distance (1) entre 8 et 6 -> le plus petit (6) passe avant
# Sortie attendue : [6, 8, 5]
```

---

### Prototype de la fonction

```python
import heapq

def k_plus_proches(nombres: list[int], x: int, k: int) -> list[int]:
    """
    Renvoie les k nombres les plus proches de x, triés par proximité croissante.
    En cas d'égalité de distance, le plus petit nombre est prioritaire.

    :param nombres: Liste d'entiers (source)
    :param x: Valeur cible
    :param k: Nombre de voisins à retourner
    :return: Liste triée des k nombres les plus proches (list[int])
    """
    # À toi de jouer
    pass
```

---

### Suite de Tests

```python
print("Démarrage des tests pour le Radar de Proximité...")

# Test 1 : Liste vide
print("Test 1...", k_plus_proches([], 7, 3))
assert k_plus_proches([], 7, 3) == [], "Échec Test 1 : Liste vide -> résultat vide"

# Test 2 : k plus grand que la liste (on doit tout renvoyer, trié par proximité)
print("Test 2...", k_plus_proches([10, 2], 5, 5))
assert k_plus_proches([10, 2], 5, 5) == [2, 10], "Échec Test 2 : distances égales (3 et 5)... "
# Note : distance(2,5)=3, distance(10,5)=5 -> 2 est strictement plus proche, donc [2, 10]

# Test 3 : Exemple de l'énoncé
print("Test 3...", k_plus_proches([1, 5, 8, 3, 10, 6], 7, 3))
assert k_plus_proches([1, 5, 8, 3, 10, 6], 7, 3) == [6, 8, 5], "Échec Test 3 : attendu [6, 8, 5]"

# Test 4 : Gestion stricte des égalités de distance
courses_egalite = [4, 6, 9, 1]
# x = 5 -> distances : 4->1, 6->1, 9->4, 1->4
print("Test 4...", k_plus_proches(courses_egalite, 5, 4))
assert k_plus_proches(courses_egalite, 5, 4) == [4, 6, 1, 9], "Échec Test 4 : égalités mal gérées"

# Test 5 : Doublons dans la liste
print("Test 5...", k_plus_proches([3, 3, 3, 8], 3, 2))
assert k_plus_proches([3, 3, 3, 8], 3, 2) == [3, 3], "Échec Test 5 : les doublons comptent chacun"

# Test 6 : Test de performance (grand volume de données)
import random
random.seed(42)
grande_liste = [random.randint(0, 1_000_000) for _ in range(200_000)]

print("Test 6 (Test de performance)...")
resultat = k_plus_proches(grande_liste, 500_000, 10)
print(f"10 plus proches de 500000 trouvés : {resultat}")
assert len(resultat) == 10, "Échec Test 6 : on doit obtenir exactement 10 résultats"
# Si le code est en O(n log n) via sorted() complet, ça passera quand même ici,
# mais essaie de viser une solution qui reste efficace même pour un k très petit devant n.

print("\nTous les tests sont validés ! Ton radar de proximité fonctionne parfaitement.")
```
