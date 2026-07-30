# Énoncé : Sudoku Solver (Backtracking)

## Objectif

Implémenter un programme capable de résoudre une grille de Sudoku 9×9 en utilisant l'algorithme de **backtracking** (retour sur trace).

## Rappel des règles du Sudoku

Une grille de Sudoku est un tableau 9×9 divisé en 9 blocs de 3×3. Il faut remplir les cases vides (représentées par `0`) avec des chiffres de `1` à `9` tels que :
- chaque **ligne** contienne les chiffres de 1 à 9 sans répétition ;
- chaque **colonne** contienne les chiffres de 1 à 9 sans répétition ;
- chaque **bloc 3×3** contienne les chiffres de 1 à 9 sans répétition.

## Spécifications fonctionnelles

### 1. Représentation des données
- La grille est représentée par une structure de données au choix (liste de listes, tableau 2D, etc.), de taille 9×9, contenant des entiers de `0` à `9` (`0` = case vide).

### 2. Fonctions à implémenter

| Fonction | Rôle |
|---|---|
| `is_valid(grid, row, col, value)` | Vérifie si `value` peut être placé en `(row, col)` sans violer les règles (ligne, colonne, bloc). |
| `find_empty_cell(grid)` | Retourne les coordonnées de la première case vide trouvée, ou `None` si la grille est complète. |
| `solve(grid)` | Résout la grille en place (ou retourne une nouvelle grille résolue) via backtracking. Retourne `True`/`False` selon que la grille est résolvable. |
| `is_grid_valid(grid)` *(optionnel)* | Vérifie qu'une grille initiale ne contient pas déjà de conflit. |

### 3. Algorithme de backtracking (pseudo-code)

```
fonction solve(grid):
    case = find_empty_cell(grid)
    si case == None:
        retourner True   # grille complète

    (row, col) = case
    pour value de 1 à 9:
        si is_valid(grid, row, col, value):
            grid[row][col] = value
            si solve(grid):
                retourner True
            grid[row][col] = 0   # backtrack

    retourner False   # aucune valeur ne fonctionne
```

## Contraintes techniques
- Langage : au choix (Python recommandé pour la simplicité des tests, mais Java/C++/JS acceptés).
- La fonction `solve` doit modifier la grille **en place** ou retourner une grille résolue clairement identifiable.
- Le programme doit gérer le cas d'une grille **non résolvable** (retourner `False` / lever une exception explicite, selon convention choisie).
- Complexité non contrainte, mais l'algorithme doit terminer en un temps raisonnable (< quelques secondes) sur une grille de difficulté standard.


## Exemple de grille de test

```python
GRID_EASY = [
    [5,3,0, 0,7,0, 0,0,0],
    [6,0,0, 1,9,5, 0,0,0],
    [0,9,8, 0,0,0, 0,6,0],

    [8,0,0, 0,6,0, 0,0,3],
    [4,0,0, 8,0,3, 0,0,1],
    [7,0,0, 0,2,0, 0,0,6],

    [0,6,0, 0,0,0, 2,8,0],
    [0,0,0, 4,1,9, 0,0,5],
    [0,0,0, 0,8,0, 0,7,9]
]
```
