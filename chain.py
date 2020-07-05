from chem import Bond
from abc import ABCMeta
import os.path
import sys


class TextField(metaclass=ABCMeta):
    '''A simple class for text fields.'''
    def __init__(self, name='', text=''):
        self.text = text
        self.name = name


class Molecule(TextField):
    '''A class for molecules.

    Members:
        - molecule: an atom in molecule, Bond-object
        - text: textfield
        - name: name of the molecule
        - cofactor: boolean, if it is a cofactor.
        - image: path to an image
    
    Method:
        - draw(bond, path): create an image from a Bond-object (NOT COMPLETED)'''
    draw_is_not_completed = True


    def __init__(self, bond, name, text, image, cofactor=False):
        '''Construct a molecule.

        Arguments:
            - bond: a node of a molecule, Bond-object.
            - name: name of a molecule.
            - text: text-field.
            - image: path to an image. If it doesn't exit,
                     program creates a such (NOT COMPLETED).'''
        TextField.__init__(self, name, text)
        if isinstance(bond, Bond):
            self.molecule = bond
        else:
            raise ValueError('The argument is not a Bond-object!')
        
        self.cofactor = cofactor

        if os.path.isfile(image):
            self.image = image
        else:
            Molecule.draw(bond, image)
    

    @staticmethod
    def draw(bond, path):
        '''Draw a molecule from a Bond-object.

        Save it in path.'''
        if Molecule.draw_is_not_completed:
            sys.exit('Draw() is not completed!')


class Enzyme(TextField):
    '''A class for enzymes or reactions (in the program logic they are synonyms).

    Arguments:
            - educts: a list of educts, Molecule-objects.
            - products: a list of products, Molecule-objects.
            - name: name of an enzyme.
            - text: text-field.'''

    def __init__(self, name, text, *educts, **products):
        TextField.__init__(self, name, text)
        if len(educts) == 0 or len(products) == 0:
            raise ValueError('You need at least one educt and one product!')
        
        for educt in educts:
            if not isinstance(educt, Molecule):
                raise ValueError('The educt is not a Molecule-object!')
        self.educts = educts
        
        for product in products.values():
            if not isinstance(product, Molecule):
                raise ValueError('The product is not a Molecule-object!')
        self.products = list(products.values())


class NotAChainException(Exception):
    '''An exception for broken chains.'''
    def __init__(self, enzyme1, enzyme2, not_existing_educt):
        Exception.__init__(self)
        self.enzyme_name1 = enzyme1.name
        self.enzyme_name2 = enzyme2.name
        self.educt = not_existing_educt


class Chain(TextField):
    '''A chain of reactions. Iterator.'''
    
    def __init__(self, *reactions):
        for reaction in reactions:
            if not isinstance(reaction, Enzyme):
                raise ValueError('One of the arguments is not a reaction!')
        
        i = 0
        while i < len(reactions) - 1:
            for educt in reactions[i + 1].educts:
                if (not educt.cofactor) and (not (educt in reactions[i].products)):
                    raise NotAChainException(reactions[i], reactions[i + 1], educt)
            
            i += 1
        
        self.chain = reactions
        self.i = 0
    

    def __iter__(self):
        return self
    

    def __next__(self):
        if self.i == len(self.chain):
            self.i = 0
            raise StopIteration
        self.i += 1
        return self.chain[self.i - 1]