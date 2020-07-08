# Documentation.
## Creating data.
You can create your own displayable reaction chains. Just simply write a python script with an object named `chain` in it and import it in the program, when the dialogue appears. Use the following classes for that:

## chem

field | arguments | type | description
----- | --------- | ---- | -----------
**`table`** | | `dict` | A dictionary. Maps element symbols to their proton number.
**`table_inv`** | | `dict` | A reverse function for `table`.
**`atom()`** | symbol: `String` | `Bond` | A factory for atoms. Works with their chemical symbols. Can raise `ValueError` if such an atom does not exist.

### Atom
Simple class for atoms, works like a periodic table.

field | arguments | type | description
----- | --------- | ---- | -----------
**`Atom()`** | proton: `int`, electron = `None`: `int` | `Atom` | Constructor. Raises `ElectronNumberException` (`ProtonNumberException`), if such an atom with this electron (proton) number doesn't exist.
**`_electron_layers`** | | `tuple` | `(2, 8, 8, 18, 18, 32, 32)`, static tuple with number of maximum electrons in layer.
**`_proton`** | | `int` | Proton number
**`_electron`** | | `int` | Electron number
**`__valence`** | | `int` | Number of valent electrons
**`__layer`** | | `int` | Number of electron layers (starts with zero)
**`__check_proton()`** | proton: `int` | `bool` | Static, check if atom with such protons doesn't exist. Return true in that case.
**`__check_electron()`** | proton: `int`, electron: `int` | `bool` | Static, check if atom with such electrons doesn't exist. Return true in that case.
**`calculate_valence()`** | electron: `int` | `tuple` | `(layer, valent)`, static, Method for calculating valent electrons and layer.
**`get_proton()`** | | `int` | Get the proton number.
**`get_electron()`** | | `int` | Get the electron number.
**`get_valent()`** | | `int` | Get the number of valent electrons.
**`get_layer()`** | | `int` | Get the number of layers in atom. **CAUTION**: counting starts with 0.
**`get_max_electrons()`** | | `int` | Get the maximum number of electrons on the most exterior layer.
**`charge()`** | | `int` | Get the charge.
**`change_charge()`** | electron: `int` | `int` | Add electrons or remove them. Raises ElectronNumberException if it isn't possible.

### Bond(Atom)
Class for sharing a pair of electrons. Inherits `Atom`, makes from it a node of the molecule graph. Proves neighbors for the octet rule. Double and triple bonds are given with linking the same atom twice or thrice.
**CAUTION**: this was tested only for the first three periods.

field | arguments | type | description
----- | --------- | ---- | -----------
**`Bond()`** | atom: `Atom` | `Bond` | Constructor. Create a separate molecule graph's node. **CAUTION**: using this constructor is depricated, use factories, if needed.
**`orbitals`** | | `list` | A list with atom's neighbors. Can contain integers: `0` shows an empty orbital, `1` represents a half-filled orbital and `2` means a fully filled orbital.
**`configuration`** | | `tuple` | A tuple with the configuration of the external electron layer.
**`visited`** | | `bool` | Shows, if a node was visited during molecule's traversal.
**`no_repeats()`** | | `list` | Get `orbitals`, but without repeats.
**`change_charge()`** | electron: `int` | | Change charge of an atom, reimplements the super method.
**`possible_covalent()`** | | `int` | Count possible covalent bindings.
**`possible_donations()`** | | `int` | Count pairs for donation.
**`possible_acceptances()`** | | `int` | Count empty orbitals.
**`__create_node()`** | *others: `Bond`, typ = 1: `int` | `Bond` | Create bond between atoms. Raises `ValueError`, if `other` is not a Bond-object, or `ImpossibleBondException`, if atoms cannot be connected.
**`create_covalent()`** | *others: `Bond` | `Bond` | Create covalent bond between atoms. A wrapper for `__create_node()`
**`donate_electrons()`** | *others: `Bond` | `Bond` | Donate electron pairs. A wrapper for `__create_node()`
**`__reset()`** | | | Reset visiting of nodes in a molecule.
**`molecule_charge()`** | | `int` | Calculate the charge of a molecule. A wrapper for `__molecule_charge_body()`
**`__molecule_charge_body()`** | | `int` | Calculate the charge of a molecule.
**`ion()`** | *molecules: `Bond` | `bool` | Check if these molecules build a neutral ion-bond or raise a `ImpossibleIonException`.

## chain
Dependencies:
* `Bond` from `logic.chem`
* `ABCMeta` from `abc`
* `os.path`
* `sys`
* `draw_postscript` from `logic.turtle_helper`

### TextField
An abstract class for text fields.

field | arguments | type | description
----- | --------- | ---- | -----------
**`TextField()`** | name='': `String`, text='': `String` | `String` | Constructor.
**`name`** | | `String` | Name.
**`text`** | | `String` | Text.

### Molecule(TextField)
A molecule object. Inherits TextField

field | arguments | type | description
----- | --------- | ---- | -----------
**`Molecule()`** | bond: `Bond`, name='': `String`, text='': `String`, image: `String`, cofactor=`False`: `bool` | `Molecule` | Constructor. Raises `ValueError`, if bond is not a Bond. Arguments:
 | | | * a molecule's node (Bond)
 | | | * name
 | | | * text
 | | | * image: a path to the image with this molecule. If file does not exist, the program will create such a file.
 | | | * cofactor: boolean, if molecule is a cofactor.
**`name`** | | `String` | Name.
**`text`** | | `String` | Text.
**`draw()`** | bond='': `Bond`, path: `String` | `void` | Draw a molecule from a Bond-object. Save it in path.

### Enzyme(TextField)
A class for enzymes or reactions (in the program logic they are synonyms).

field | arguments | type | description
----- | --------- | ---- | -----------
**`Enzyme()`** | name='': `String`, text: `String`, *educts: `Molecule`, *products: `Molecule` | `Enzyme` | Constructor. Raises `ValueError`, if no educts or products are given or if they are not molecules.


### Chain
A chain of reactions. Iterator.

field | arguments | type | description
----- | --------- | ---- | -----------
**`Chain()`** | *reactions: `Enzyme` | `Chain` | Constructor. Raises `ValueError`, if reactions are not instances of `Enzyme`. Raises  `NotAChainException`.

## turtle_helper
Methods for drawing. Dependencies:
* `turtle`
* `Bond`, `table_inv` from `logic.chem` 
* `subprocess`
* `os`
* `numpy`
* `Image` from `PIL`
* `gswin64c.exe` from `C:\Program Files\gs\gs9.52\bin`

field | arguments | type | description
----- | --------- | ---- | -----------
**`draw_single()`** | position: `Vec2D`, direction: `int` | `Vec2D` | Draw a single line between atoms. Return the endposition.
**`draw_mult()`** | position: `Vec2D`, direction: `int`, multiplicity = 1: `int` | `Vec2D` | 'Draw multiple lines between two atoms. Return the endposition.
**`draw_body()`** | molecule: `Bond`, direction: `int`, position: `Vec2D` | `Vec2D` | Body of the recursive draw function.
**`crop()`** | png_image_name: `String` | `void` | Crop a png-image.
**`draw_postscript()`** | molecule: `Bond`, path: `String` | `void` | draw a molecule and save it as png.


[Back to the index page.](https://kiratsuwa.github.io/biochemistry/)
