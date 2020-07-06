import os
import shutil

def open_chain(path):
    '''Help to import and open a chain.'''
    shutil.copyfile(path, 'chain_to_import.py')