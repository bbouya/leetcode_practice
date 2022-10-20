"""
Lists
acces a chaque element: [index]
list definie par list : [begin:end]

completer les different print avec la sortie souhaiter
"""

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
print() #afficher ==> ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
print() # afficher la taille de list : 6   utiliser la fonction len pour savoir la taille du list ex: len([1,2,0]) = 3
print() # afficher ==> Mercury
print() # afficher le type de planets[0] : <class 'str'>  pour savoir le type de variable utiliser la fonction type ---> type('2') = str
print() # afficher ==> Mars
print() # afficher ==> ['Mercury']
print() #afficher le type de ['Mercury', 'Venus'] ==> <class 'list'>
print() #afficher ==> ['Mercury', 'Venus']
print() # afficher ==> ['Venus', 'Earth']
print() #afficher ==> ['Earth', 'Mars', 'Jupiter', 'Saturn']
print() #afficher ==> ['Mercury', 'Venus', 'Earth']
print() # afficher ===> ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn\']


"""
List slice with steps
List slice with step: [start:end:step]
exemple : a = ['1','2','3','4','6']
pour afficher  ['1','3','6'] ===> a[::2] 
explanation -----0--0+2--0+2+2------
-----------------0---2----4----------


"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print() #afficher ==> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print() #afficher ==> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print() #afficher ==> ['a', 'c', 'e', 'g', 'i']
print() #afficher ==> ['b', 'd', 'f', 'h', 'j']
print() #afficher ==> ['c', 'e', 'g']
print() #afficher ==> ['b', 'e', 'h']


#Change a List 
#Exemple 1 : changer 'abc' par 'qqrq' : 
x = ['abc', 'def', 'ghi', 'jkl']
#pour la changer x[0] = 'qqrq'
x[0] = 'qqrq'
print(x) # ['qqrq', 'def', 'ghi', 'jkl']
# pour changer une list par une autre list exe:
x[1:3] = ['xyz', 'dod']
print(x) # ['qqrq', 'xyz', 'dod', 'jkl']

# Exercices afficher ==> x = ['qqrq', 'bla', 'jkl']
print()
# Exercices afficher ==> x = ['qqrq', 'elp', 'free', 'jkl']
print()
