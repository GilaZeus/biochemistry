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


    @staticmethod
    def __check_proton(proton):
        '''Check if atom with such protons doesn't exist.
        
        Return true in that case.'''
        return (proton < 1 or proton > 118) or isinstance(proton, float)


    @staticmethod
    def __check_electron(proton, electron):
        '''Check if atom with such electrons doesn't exist.
        
        Return true in that case.'''
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
    global table

    if symbol in table:
        return Bond(Atom(table[symbol]))
    else:
        raise ValueError


table = {'H' : 1, 'He' : 2,
             'K' : 3, 'Be' : 4, 'B' : 5, 'C' : 6, 'N' : 7, 'O' : 8, 'F' : 9, 'Ne' : 10,
             'Na' : 11, 'Mg' : 12, 'Al' : 13, 'Si' : 14, 'P' : 15, 'S' : 16, 'Cl' : 17, 'Ar' : 18}

table_inv = {v: k for k, v in table.items()}


class ImpossibleBondException(Exception):
    '''Exception for unrealistic chemical bounds.'''
    
    def __init__(self, main_atom, *atoms):
        Exception.__init__(self)
        self.main_atom = main_atom
        self.atoms = atoms


class ImpossibleIonException(ImpossibleBondException):
    '''Exception for not neutral ion bonds.'''
    
    def __init__(self, *atoms):
        ImpossibleBondException.__init__(None, *atoms)


class Bond(Atom):
    '''Class for sharing a pair of electrons.
    
    The central atom in bound must fill the most exterior layer. Double and
    triple bonds are given with linking the same atom twice or thrice.

    Caution: this was tested only for the first three periods.
    
    Constructor:
        * Arguments: main atom in node.
        * Members:
            * orbitals: a list of all bindings. The index number is important
                        and represents different orbitals! 
            * configuration: configuration of an atom befor bindings.
            * visited: helps to prevent infinite recursions in graph.'''


    def __init__(self, atom):
        '''Constructor for a bond atom.

        CAUTION: using this constructor is depricated.
                 Look for the factory methods below.'''
        Atom.__init__(self, atom.get_proton(), atom.get_electron())
        self.orbitals = [0 for i in range(self.get_max_electrons() // 2)]
        self.visited = False
        i = 0
        electrons_total = self.get_valent()
        while i < electrons_total:
            self.orbitals[i] += 1
            i += 1
            if i >= len(self.orbitals):
                i = 0
                electrons_total -= len(self.orbitals)
        self.configuration = tuple(self.orbitals)


    def no_repeats(self):
        '''Get list of neighbors without repetition.'''
        return  list(dict.fromkeys(self.orbitals)) 


    def change_charge(self, electron):
        '''Change charge of an atom.'''
        super().change_charge(electron)
        result = Bond(self)
        self.orbitals = result.orbitals
        self.configuration = result.configuration


    def possible_covalent(self):
        '''Count possible covalent bindings.'''
        return self.orbitals.count(1)
    

    def possible_donations(self):
        '''Count pairs for donation.'''
        return self.orbitals.count(2)
    

    def possible_acceptances(self):
        '''Count empty orbitals.'''
        return self.orbitals.count(0)
    

    def __create_node(self, *others, typ=1):
        '''Create bond between atoms.'''
        for other in others:
            if not isinstance(other, Bond):
                raise ValueError
            if typ == 1:
                self_max = self.possible_covalent()
                other_max = other.possible_covalent()
                other_typ = 1
            elif typ == 2:
                self_max = self.possible_donations()
                other_max = other.possible_acceptances()
                other_typ = 0
            else:
                raise ValueError

            if self_max > 0 and other_max > 0:
                self.orbitals[self.orbitals.index(typ)] = other
                other.orbitals[other.orbitals.index(other_typ)] = self
            else:
                raise ImpossibleBondException(self, *others)
        
        return self


    def create_covalent(self, *others):
        '''Create covalent bond between atoms.'''
        return self.__create_node(*others, typ=1)
    

    def donate_electrons(self, *others):
        '''Donate electron pairs.'''
        return self.__create_node(*others, typ=2)


    def __reset(self):
        '''Reset visiting of nodes in a molecule.'''
        self.visited = False
        for at in self.orbitals:
            if isinstance(at, Bond) and at.visited:
                at.__reset()


    def molecule_charge(self):
        '''Calculate the charge of a molecule.'''
        result = self.__molecule_charge_body()
        self.__reset()
        return result


    def __molecule_charge_body(self):
        '''Calculate the charge of a molecule.'''
        result = self.charge()
        self.visited = True
        for at in self.orbitals:
            if isinstance(at, Bond) and not at.visited:
                result += at.__molecule_charge_body()
        return result


    @staticmethod
    def ion(*molecules):
        '''Check if this molecules build a neutral ion-bond.'''
        result = 0
        for molecule in molecules:
            result += molecule.molecule_charge()
        
        if result == 0:
            return True
        else:
            raise ImpossibleIonException(*molecules)