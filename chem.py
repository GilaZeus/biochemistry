import copy

'''Contains main chemistry logic.'''
class NotExistingAtomException(Exception):
    '''Exception for not existing atoms.'''
    
    def __init__(self, proton, electron):
        Exception.__init__(self)
        self.proton = proton
        self.electron = electron


class ProtonNumberException(NotExistingAtomException):
    '''Exception for wrong proton number.'''
    
    def __init__(self, proton, electron):
        NotExistingAtomException.__init__(self, proton, electron)


class ElectronNumberException(NotExistingAtomException):
    '''Exception for wrong electron number.'''
    
    def __init__(self, proton, electron):
        NotExistingAtomException.__init__(self, proton, electron)


class Atom:
    '''Class for atom objects.

    Constructor:
        Needs the proton number (and electron, if it is needed).
        Raises ElectronNumberException, if such an atom with this electron number doesn't exist.
        Raises ProtonNumberException, if such an atom with this proton number doesn't exist.
    
    Accessible methods:
        * get_proton
        * get_electron
        * get_valent
        * get_layer
        * get_max_electrons
        * charge
        * change_charge
        * create electron pair'''
    
    _electron_layers = (2, 8, 8, 18, 18, 32, 32)

    
    def __init__(self, proton, electron = None):
        '''Create an atom.

        Needs the proton number (and electron, if it is needed).
        Raises ElectronNumberException, if such an atom with this electron number doesn't exist.
        Raises ProtonNumberException, if such an atom with this proton number doesn't exist.'''
        try:
            if Atom.__check_proton(proton):
                raise ProtonNumberException(proton, electron)
            if Atom.__check_electron(proton, electron):
               raise ElectronNumberException(proton, electron)
        except NotExistingAtomException:
            self._proton = 0
            self._electron = 0
            raise
        finally:
            self._proton = proton
            
            if electron == None:
                self._electron = proton
            else:
                self._electron = electron

        self.__layer, self.__valence = self.calculate_valence(self._electron)


    def _create_electron_pair(self):
        '''create an electron pair from a H-atom.'''
        self._proton = 0
        self._electron = 2


    @staticmethod
    def __check_proton(proton):
        '''Check if atom with such protons doesn't exist.
        
        returns true in that case.'''
        return (proton < 1 or proton > 118) or isinstance(proton, float)


    @staticmethod
    def __check_electron(proton, electron):
        '''Check if atom with such electrons doesn't exist.
        
        returns true in that case.'''
        if electron == None:
            return False
        return isinstance(electron, float) or electron != 0 and (electron < 0 or electron < proton and \
               Atom.calculate_valence(proton)[1] - proton + electron < 0 or electron > proton \
               and Atom.calculate_valence(proton)[1] + electron - proton > \
                   Atom._electron_layers[Atom.calculate_valence(proton)[0]])


    @staticmethod
    def calculate_valence(electron):
        '''Method for calculating valent electrons and layer.'''
        valent = electron
        layer = 0
        while valent > Atom._electron_layers[layer]:
            valent -= Atom._electron_layers[layer]
            layer += 1
        
        return (layer, valent)
    

    def get_proton(self):
        '''Get the proton number.'''
        return self._proton
    

    def get_electron(self):
        '''Get the electron number.'''
        return self._electron
    

    def get_valent(self):
        '''Get valent electrons.'''
        return self.__valence
    

    def get_layer(self):
        '''Get the number of layers in atom.

        CAUTION: counting starts with 0.'''
        return self.__layer
    

    def get_max_electrons(self):
        '''Get the maximum number of electrons on the most exterior layer.'''

        return Atom._electron_layers[self.__layer]


    def charge(self):
        '''Get the charge.'''
        return self._proton - self._electron
    
    
    def change_charge(self, electron):
        '''Add electrons or remove them.

        Raises ElectronNumberException if it isn't possible.'''
        try:
            if Atom.__check_electron(self._proton, self._electron + electron):
                raise ElectronNumberException(self._proton, self._electron)
        finally:
            self._electron += electron
            self.__valence = Atom.calculate_valence(self._electron)[1]


def atom(symbol):
    '''A factory for atoms. Works with their chemical symbols.'''
    table = {'H' : 1, 'He' : 2,
             'K' : 3, 'Be' : 4, 'B' : 5, 'C' : 6, 'N' : 7, 'O' : 8, 'F' : 9, 'Ne' : 10,
             'Na' : 11, 'Mg' : 12, 'Al' : 13, 'Si' : 14, 'P' : 15, 'S' : 16, 'Cl' : 17, 'Ar' : 18}
    
    if symbol in table:
        return Atom(table[symbol])
    else:
        return Atom(0)


class UnpossibleBoundException(Exception):
    '''Exception for unrealistic chemical bounds.'''
    
    def __init__(self, main_atom, *atoms):
        Exception.__init__(self)
        self.main_atom = main_atom
        self.atoms = atoms


class Bond(Atom):
    '''Class for sharing a pair of electrons.
    
    The central atom in bound must fill the most exterior layer. Double and
    triple bonds are given with linking the same atom twice or thrice.

    Caution: this was tested only for the first three periods.
    
    Constructor:
        * Arguments: main atom in node.
        * Members:
            * atoms: a list of all bonds.
            * _possible_bond: number of possible bonds.
            * _possible_accept: number of empty orbitals.
            * _possible_donate: number of filled orbitals.

    Factories:
        * create_node

    Static fields:
        * __electron_pair: an "Atom" that represents two electrons on orbital.'''

    __electron_pair = Atom(1)
    __electron_pair._create_electron_pair()

    def __init__(self, atom):
        '''Constructor for a bond atom.

        CAUTION: using this constructor is depricated.
                 Look for the factory methods below.'''
        Atom.__init__(self, atom.get_proton(), atom.get_electron())
        self.atoms = []
        pairs_total = self.get_max_electrons() // 2

        if self.get_valent() == 8:
            num_of_pairs = self.get_max_electrons() / 2
            num_of_free = 0
        elif self.get_valent() < pairs_total:
            num_of_pairs = 0
            num_of_free = pairs_total - self.get_valent()
        else:
            num_of_pairs = self.get_valent() % pairs_total
            num_of_free = 0
        for i in range(num_of_pairs):
            self.atoms.append(copy.copy(Bond.__electron_pair))
        for i in range(num_of_free):
            self.atoms.append(None)
        self._possible_bond = pairs_total - len(self.atoms)
        self._possible_accept = self.atoms.count(None)
        self._possible_donate = pairs_total - self._possible_bond - self._possible_accept


    @staticmethod
    def create_covalent(atom, *others):
        '''Create a covalent bond between an atom and its neighbors.'''
        if not isinstance(atom, Bond):
            raise ValueError
        for other in others:
            if not isinstance(atom, Bond):
                raise ValueError
        if len(others) <= atom._possible_bond:
            for other in others:
                atom.atoms.append(other)
                atom._possible_bond -= 1
                if other._possible_bond > 0:
                    other.atoms.append(atom)
                    other._possible_bond -= 1
                else:
                    raise UnpossibleBoundException(other, atom)
        else:
            raise UnpossibleBoundException(atom, others)