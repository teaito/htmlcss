//
#division entière
10 // 3 = 3

%
#modulo
10 % 3 = 1

#variable en minuscules, avec _ pour les espaces ou camelCase

int
#entier

float
#décimaux

"""  phrase avec «  et ‘ """ 
#triples guillemets pour encadrer une phrase sans avoir besoin d’échapper les guillemets et apostrophe et pour écire sur plusieurs lignes (ou 3 apostrophes)

variable += 1
#incrémente une variable de 1

-= et *= et /=
#soustraire, multiplier et diviser une variable par une valeur

>>> a = 5
>>> b = 32
>>> a,b = b,a # permutation
>>> a
32
>>> b
5
>>>

x = y = 3
#affectation à plusieurs variables en 1 fois

type (variable)
#pour obtenir le type d’une variable

print (variable)
#pour afficher

if a > 0 :
    print (« a est positif »)
elif a = 0 :
    print (« a est nul »)
else :
    print(« a est négatif »)
    
True, False
# 1ère lettre en majuscule

and, or, not

a=0
while a<10:
    a+=1
#crtl C pour sortir d'une boucle infinie

chaine = "Bonjour les ZER0S"
for lettre in chaine:
    print(lettre)

in
if lettre in "AEIOUYaeiouy": 
        print(lettre)

break
#pour sortir d'une boucle

continue
#pour revenir directement au début de la boucle

def nomDeFonction (paramètre):
    print("hello")
#pour définir une fonction

def table(nb, max=10):
#valeur par défault pour le paramètre max
