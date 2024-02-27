import re
import sys


## exo1
pattern1 = r'\+[0-9]{2}\ [0-9]{3}\ [0-9]{2}\ [0-9]{2}\ [0-9]{2}'
p1 = re.compile(pattern1)
pattern2 = r'^-?[1-9][0-9]*$'
p2 = re.compile(pattern2)
pattern3 = r'[1-9][A-Z]{3}[0-9]{3}'
pattern4 = r'[1-9][0-9]{3}[A-Z]{3}'
p3= re.compile(pattern3)
p4 = re.compile(pattern4)
pattern5 = r'[A-Z]:\\'
p5 = re.compile(pattern5)

print(p1.match('') is not None)
print(p1.match('+32 474 33 66 77 ') is not None)
print(p2.match('-13')is not None)
print(p2.match('13')is not None)
print(p2.match('13.5')is not None)
print(p2.match('03')is not None)
print((p3.match('1AAA666') or p4.match('1AAA666')) is not None)
print((p3.match('1666AAA') or p4.match('1666AAA')) is not None)
print((p3.match('AAA1666') or p4.match('AAA1666')) is not None)
print(p5.match('C:\\')is not None)

## exo 2 :
pattern6 = r'\d+'
p6 = re.compile(pattern6)
with open('mon_texte.txt', 'r') as fichier:
    numeros_lignes_nombres = {}
    for numero_ligne, ligne in enumerate(fichier, start=1) :
        nombres = re.findall(r'\d+', ligne)
        if nombres:
            numeros_lignes_nombres['line ' + str(numero_ligne)] = ', '.join(nombres)
    for ligne, nombres in numeros_lignes_nombres.items():
        print(f"{ligne}: {nombres}")
## exo 3 :
##pattern7 = r'^(?P<Protocol>[a-zA-Z]+)://(?P<domain>[a-zA-Z]{3}\.[a-zA-Z]+\.[a-zA-Z]+)/(?P<Path>[a-zA-Z]+/[a-zA-Z]+)'
pattern7 = r'^(?P<Protocol>[a-zA-Z]+)://(?P<domain>[a-zA-Z]+\.[a-zA-Z]+(?:\.[a-zA-Z]+)*)/(?P<Path>[a-zA-Z/]+)'

p7 = re.compile(pattern7)
m= p7.match('http://www.this.is/big/shit/gg/jj')
if m != None :
    print('Protocol =' +m.group('Protocol'))
    print('Domain =' +m.group('domain'))
    print('Path =' +m.group('Path'))
else :
    print('None')
## exo 4 :
def verifier_solution(liste_exp_reg_lignes, liste_exp_reg_colonnes, solution_proposee):
    # Vérifier le nombre de lignes et de colonnes
    nb_lignes = len(liste_exp_reg_lignes)
    nb_colonnes = len(liste_exp_reg_colonnes)
    if nb_lignes != len(solution_proposee) or nb_colonnes != len(solution_proposee[0]):
        return False

    # Vérifier les expressions régulières pour les lignes
    for i in range(nb_lignes):
        if not re.match(liste_exp_reg_lignes[i], solution_proposee[i]):
            return False

    # Transposer la solution proposée pour vérifier les expressions régulières pour les colonnes
    solution_transposee = [''.join(col) for col in zip(*solution_proposee)]
    for j in range(nb_colonnes):
        if not re.match(liste_exp_reg_colonnes[j], solution_transposee[j]):
            return False

    # Si toutes les vérifications passent, la solution est valide
    return True
liste_r_l= [r'[ARBRE](EN|SM)', r'(IS|HAS).*', r'(.)\1[^AEIOU]']
liste_r_c= [r'[BOU](OI|IO)', r'[FLE](SO|OS)', r'.C*(RA|L)']
solution = [
    "BEN",
    "ISC",
    "OOL"
    ]
print(verifier_solution(liste_r_l, liste_r_c,solution))