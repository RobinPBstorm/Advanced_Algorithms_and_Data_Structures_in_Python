# Exercice : Snake asynchrone dans le terminal

## Contexte

Tu vas développer un **Snake** jouable dans le terminal, sans aucune bibliothèque graphique, uniquement avec `curses` (l'affichage) et `asyncio` (la boucle de jeu + la lecture du clavier en simultané).

Le principe : un serpent se déplace en continu sur une grille carrée. Le joueur change sa direction avec les flèches du clavier. S'il mange la nourriture (`0`), il grandit et une nouvelle nourriture apparaît. S'il se mord la queue, c'est game over.

## Prérequis

- Sous Windows : `pip install windows-curses`
- Connaître les bases de `asyncio` (coroutines, `await`, event loop)
- Un terminal suffisamment grand (au moins 20 colonnes x 20 lignes)

## Cahier des charges

Le jeu doit respecter les règles suivantes :

1. **La grille** : un plateau carré de taille `SIZE` (configurable), délimité par une bordure (par exemple avec les caractères `╔ ╗ ╚ ╝ ═ ║`).
2. **Le serpent** : représenté comme une suite de coordonnées `(x, y)`, affiché avec le caractère `X`. Il démarre avec une longueur de 5.
3. **La nourriture** : une position `(x, y)` tirée aléatoirement sur une case libre (pas déjà occupée par le serpent), affichée avec le caractère `0`.
4. **Le déplacement** : le serpent avance automatiquement toutes les 200 ms dans sa direction courante. Quand il sort d'un bord, il réapparaît de l'autre côté (effet "Pac-Man").
5. **Les contrôles** : les flèches du clavier (haut/bas/gauche/droite) changent la direction du serpent, **pendant que le serpent continue de bouger tout seul** — la lecture clavier ne doit jamais bloquer l'affichage.
6. **Manger** : quand la tête du serpent atteint la nourriture, le serpent grandit d'une case et une nouvelle nourriture apparaît ailleurs.
7. **Game over** : quand la tête du serpent touche une autre partie de son propre corps, le jeu s'arrête et affiche `GAME OVER`.
8. **Quitter** : la touche `Echap` doit permettre d'arrêter le programme proprement.

## Étapes suggérées

Tu peux avancer progressivement plutôt que tout écrire d'un coup :

1. **Étape 1 — Affichage statique** : dessine la bordure de la grille avec `curses`, sans logique de jeu.
2. **Étape 2 — Le serpent immobile** : affiche un serpent de 5 cases et une nourriture placée aléatoirement.
3. **Étape 3 — Le mouvement automatique** : fais avancer le serpent tout seul dans une direction fixe, en boucle, avec `asyncio.sleep(0.2)`.
4. **Étape 4 — Les contrôles clavier** : ajoute une deuxième coroutine (ou tâche via `run_in_executor`) qui lit les touches et met à jour la direction, sans bloquer le mouvement automatique.
5. **Étape 5 — Manger et grandir** : détecte la collision avec la nourriture, fais grandir le serpent et régénère la nourriture.
6. **Étape 6 — Game over** : détecte la collision avec soi-même et arrête proprement le jeu.

## Points d'attention

- `curses` peut lever une erreur (`_curses.error: addwstr() returned ERR`) si on écrit dans la toute dernière cellule de la fenêtre (bas-droite) — c'est un comportement normal de la bibliothèque, à anticiper.
- Deux coroutines qui modifient la même variable (`direction`, `snake`, `food`) doivent se coordonner correctement pour éviter les incohérences d'affichage.
- Réfléchis à comment combiner une tâche asynchrone (le mouvement) et une fonction bloquante (`screen.getch()`) sans que l'une empêche l'autre de s'exécuter.

## Bonus (pour aller plus loin)

- Empêcher le serpent de faire un demi-tour direct sur lui-même (ex : aller à droite puis immédiatement à gauche).
- Ajouter un score affiché à l'écran, incrémenté à chaque nourriture mangée.
- Augmenter progressivement la vitesse du serpent au fil de la partie.
- Ajouter des obstacles fixes sur la grille.
- Gérer proprement le redimensionnement du terminal en cours de partie.
- Proposer un écran de fin avec le score final et une option "rejouer".
