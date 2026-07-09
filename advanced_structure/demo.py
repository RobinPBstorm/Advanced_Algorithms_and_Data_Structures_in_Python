from collections import deque, Counter

list = []
hash = set()
dictionary = {"key": "value"}
tuple = (5,4)

# file (fifo)
queue = deque([])
queue.append(5) # ajoute l'élément à droite
queue.popleft() # retirer le premier (les autres seront décalés)

# pile (lifo)
pile = deque([])
pile.append(4) 
pile.pop()
if pile:
    pile.pop() # Attention si la pile est vide, pop renvoie une erreur

#pile.appendleft(1) # ajoute l'élément à gauche

import heapq
heap = []
heapq.heapify(heap)
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 10)
print(heap)

heapq.heappop(heap)
print(heap)


counter = Counter([11, 11, 4 ,11,0,5])
print(counter.most_common(3))


# string builder
from io import StringIO
chaine = StringIO()
chaine.write("Hello world!")
chaine.write("Hello world!")
chaine.seek(0) # replace le curseur à l'index indiqué
chaine.truncate() # supprime les éléments à partir de curseur ou de l'index indiqué

print(chaine.getvalue())

# jouer avec les matrices
import numpy as np
matrice = np.array([[1,2,3],[4,5,6]])
print(matrice)


# mémoization (aussi nommé bottom-up)
from functools import cache, lru_cache

@cache
@lru_cache(128)
def fibo(n: int) -> int:
    if n <= 1:
        return n
    return fibo(n - 2) + fibo(n - 1)

def fibo2(n: int, cache: dict = dict()) -> int:
    if n <= 1:
        cache[n] = n
        return n
    if n in cache:
        return cache[n]
    cache[n] = fibo2(n - 2, cache) + fibo2(n - 1, cache)
    return cache[n]

print(fibo2(10))

# proposition de François
def fibo3(n):
    if n<=1:
        return (n,0)
    else:
        (a,b) = fibo3(n-1)
        return (a+b,a)

print(fibo3(10))