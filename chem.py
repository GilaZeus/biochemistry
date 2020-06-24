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


class Atom():
    '''Class for atom objects.

    Constructor:
        Needs the proton number (and electron, if it is needed).
        Raises ElectronNumberException, if such an atom with this electron number doesn't exist.
        Raises ProtonNumberException, if such an atom with this proton number doesn't exist.
    
    Accessible methods:
        * get_proton_number
        * get_electron_number
        * get_valent
        * get_layer
        * get_max_electrons
        * charge
        * change_charge'''
    
    __electron_layers = (2, 8, 8, 18, 18, 32, 32)
    
    def __init__(self, proton, electron = 0):
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
            self.__proton = 0
            self.__electron = 0
            raise
        finally:
            self.__proton = proton
            
            if electron == 0:
                self.__electron = proton
            else:
                self.__electron = electron

        self.__layer, self.__valence = self.calculate_valence(self.__electron)
    

    @staticmethod
    def __check_proton(proton):
        '''Check if atom with such protons doesn't exist.
        
        returns true in that case.'''
        return (proton < 1 or proton > 118) or isinstance(proton, float)


    @staticmethod
    def __check_electron(proton, electron):
        '''Check if atom with such electrons doesn't exist.
        
        returns true in that case.'''
        return isinstance(electron, float) or electron != 0 and (electron < 0 or electron < proton and \
               Atom.calculate_valence(proton)[1] - proton + electron < 0 or electron > proton \
               and Atom.calculate_valence(proton)[1] + electron - proton > \
                   Atom.__electron_layers[Atom.calculate_valence(proton)[0]])


    @staticmethod
    def calculate_valence(electron):
        '''Method for calculating valent electrons and layer.'''
        valent = electron
        layer = 0
        while valent > Atom.__electron_layers[layer]:
            valent -= Atom.__electron_layers[layer]
            layer += 1
        
        return (layer, valent)
    

    def get_proton_number(self):
        '''Get the proton number.'''
        return self.__proton
    

    def get_electron_number(self):
        '''Get the electron number.'''
        return self.__proton
    

    def get_valent(self):
        '''Get valent electrons.'''
        return self.__valence
    

    def get_layer(self):
        '''Get the number of layers in atom.

        CAUTION: counting starts with 0.'''
        return self.__layer
    

    def get_max_electrons(self):
        '''Get the maximum number of electrons on the most exterior layer.'''

        return Atom.__electron_layers[self.__layer]


    def charge(self):
        '''Get the charge.'''
        return self.__proton - self.__electron
    
    
    def change_charge(self, electron):
        '''Add electrons or remove them.

        Raises ElectronNumberException if it isn't possible.'''
        try:
            if Atom.__check_electron(self.__proton, self.__electron + electron):
                raise ElectronNumberException(self.__proton, self.__electron)
        finally:
            self.__electron += electron
            self.__valence = Atom.calculate_valence(self.__electron)[1]


class UnpossibleBoundException(Exception):
    '''Exception for unrealistic chemical bounds.'''
    
    def __init__(self, main_atom, *atoms):
        Exception.__init__(self)
        self.main_atom = main_atom
        self.atoms = atoms


class BoundAtom():
    '''Class for sharing a pair of electrons.
    
    The central atom in bound must fill the most exterior layer. Double, triple,
    qudriple bounds are given with linking the same atom twice, thrice and so on.
    
    Constructor:
        * Arguments: main atom, his bound atoms.
        * Raises UnpossibleBoundException, if the last electron layer is not filled.
    
    Methods:
        * is_filled
        * atoms_no_duplicates'''
    
    def __init__(self, main_atom, *atoms):
        '''A simple chemical binding.'''
        self.main_atom = main_atom
        if not BoundAtom.is_filled(main_atom, len(atoms)):
            self.atoms = None
            raise UnpossibleBoundException(main_atom, atoms)
        else:
            self.atoms = atoms
    

    @staticmethod
    def is_filled(atom, num_of_bindings):
        '''Check if atom has filled the last electron layer.'''
        return atom.get_valent() + num_of_bindings == atom.get_max_electrons()


    def atoms_no_duplicates(self):
        '''Return the list of atoms without giving the same atom twice.'''
        return list((dict.fromkeys(self.atoms)))


class Molecule():
    '''Collection of bound atoms.'''

    def __init__(self, *boundAtoms):
        pass