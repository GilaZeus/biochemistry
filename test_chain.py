from chain import Molecule, Enzyme, Chain
from chem import Bond, atom, Atom

# Einfaches Beispiel: Alcohol-dehydrogenase mit methanol.


# Methanol
CH3 = atom('C')
CH3.create_covalent(atom('H'), atom('H'), atom('H'))
OH = atom('O').create_covalent(atom('H'))
CH3OH = CH3.create_covalent(OH)
methanol = Molecule(CH3OH, 'methanol', 'A very toxic molecule', 'C:\\py\\Resources\\Glucose.png')


# Formaldehyd
CH2 = atom('C').create_covalent(atom('H'), atom('H'))
O = atom('O')
CH2O = CH2.create_covalent(O, O)
formaldehyde = Molecule(CH2O, 'Formaldehyd', 'A very toxic molecule', 'C:\\py\\Resources\\Glucose.png')


# Formate
Ominus = Bond(Atom(8, 9))
O = atom('O')
CHOOminus = atom('C').create_covalent(atom('H'), O, O, Ominus)
formate = Molecule(CHOOminus, 'Formate', '', 'C:\\py\\Resources\\Glucose.png')


# Enzyme
alcoholdehydrogenase = Enzyme('Alcoholdehydrogenase', 'metabolises alcohol', methanol, product=formaldehyde)
enzyme2 = Enzyme('Formaldehyde metabolising', '', formaldehyde, product=formate)


# Chain of reactions
chain = Chain(alcoholdehydrogenase, enzyme2)

for reaction in chain:
    print(reaction.name, 'Educts: ')
    for educt in reaction.educts:
        print(educt.name)
    print('\nProducts: ')
    for product in reaction.products:
        print(product.name)
    print()