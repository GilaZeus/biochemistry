from logic.chain import Molecule, Enzyme, Chain
from logic.chem import Bond, atom, Atom

# С
C = atom('C')
C = Molecule(C, 'PLACEHOLDER', 'PLACEHOLDER', 'resources\\images\\placeholder.png')

# Enzyme
enzyme = Enzyme('placeholder', 'placeholder', C, product=C)

# Chain of reactions
chain = Chain(enzyme)