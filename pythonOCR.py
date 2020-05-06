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
    return True
#pour définir une fonction

def table(nb, max=10):
#valeur par défault pour le paramètre max

def nomFonction ():
    """ aide pour cette fonction """
#docstring visible en tapant help(nomFonction)

variable = lambda x, y: x + y
print (variable(2,3))
#affiche 5
#lambda est une fonction sur une seule ligne

import math
math.sqrt(16)
#affiche 4
#importation de module et appel d'une fonction

help("math.sqrt")
#pour avoir la description de cette fonction

import math as mathematiques
mathematiques.sqrt(25)
#changement de l'espace de nom

from math import sqrt
sqrt(16)
#affiche 4

from math import *
#pour importer toutes les fonctions de ce module
#attention aux noms des fonctions avec vos propres fonctions

#début de module mettre une docstring aussi

if __name__ == "__main__":
    table(4)
#à mettre dans un module, permet de faire des tests des fonctions du module qui ne fonctionnent pas quand il est importé mais seulement quand elles sont appelées quand on lance directement le module
    
#un module contient des fonctions et des class, un package contient des modules ou d'autres packages
    
from package.sousPackage import module
#nommage comme une variable (minuscule puis CamelCase)
    
from package.fonctions import table
table(5) # Appel de la fonction table

# Ou ...
import package.fonctions
package.fonctions.table(5)  # Appel de la fonction table

try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
#pour gérer les exceptions et éviter au programme de planter
except type_de_l_exception as exception_retournee:
    print("Voici l'erreur :", exception_retournee)
else:
    print("dans le cas où il n'y a pas d'erreur")
finally:
    # Instruction(s) exécutée(s) qu'il y ait eu des erreurs ou non
    pass
    #permet de faire un bloc try vide

assert variable
assert variable == valeur
#si la variable ou le test vaut True rien ne se passe, si elle vaut False, une exception AssertionError est levée
try:
    x = 2
    assert x==3
except AssertionError:
    print ("x 'nest pas égal à 3")

raise TypeDeLException("message à afficher")


