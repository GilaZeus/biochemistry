from logic.chain import Molecule, Enzyme, Chain
from logic.chem import Bond, atom, Atom
import copy

# Einfaches Beispiel: Alcohol-dehydrogenase mit methanol.


# Methanol
CH3 = atom('C')
CH3.create_covalent(atom('H'), atom('H'), atom('H'))
OH = atom('O').create_covalent(atom('H'))
CH3OH = CH3.create_covalent(OH)
methanol = Molecule(CH3OH, 'METHANOL', 'A very toxic molecule', 'resources\\images\\methanol.png')


# Formaldehyd
CH2 = atom('C').create_covalent(atom('H'), atom('H'))
O = atom('O')
CH2O = CH2.create_covalent(O, O)
formaldehyde = Molecule(CH2O, 'Formaldehyd', 'A very toxic molecule', 'resources\\images\\formaldehyde.png')


# Formate
Ominus = Bond(Atom(8, 9))
O = atom('O')
CHOOminus = atom('C').create_covalent(atom('H'), O, O, Ominus)
formate = Molecule(CHOOminus, 'Formate', '', 'resources\\images\\formate.png')


# Enzyme
alcoholdehydrogenase = Enzyme('Alcoholdehydrogenase AHAHAHAHAAHAHAHAHAHAHA!!!!!!!!', 'metabolises alcohol', methanol, copy.deepcopy(methanol), product=formaldehyde)
enzyme2 = Enzyme('Formaldehyde metabolising', '', formaldehyde, product=formate, product2=copy.deepcopy(formaldehyde))


# Chain of reactions
chain = Chain(alcoholdehydrogenase, enzyme2)