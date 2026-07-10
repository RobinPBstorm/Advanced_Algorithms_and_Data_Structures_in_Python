import re

text = "voici mon Hello world"
pattern = r"[a-zA-Z]*[^d\W]\b"

# \w letter, chiffre, _
# \d chiffre
# \s espace, tabulation, retour à la ligne
# \b caractère en fin de mot

# \W tout sauf letter, chiffre, _
# \D tout sauf chiffre
# ...

# {n} nombre de fois
# {n, m} entre n et m fois
# {1, } entre 1 et infini
# (l) groupe de capture (ici la lettre ls) 
# \w(?=a) match les lettres qui son suivi par un a 

# [] liste des éléménts récupérer
# [a-z] toutes les lettres entre a et z
# [^a] tous les caractères sauf a

# * 0 à n
# + 1 à n
# ? 0 ou 1
# . 1 élément

mots = re.findall(pattern, text)
print(mots)

mots = re.search(pattern, text)
print(mots.group())