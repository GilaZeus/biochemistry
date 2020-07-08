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



[Back to the index page.](https://kiratsuwa.github.io/biochemistry/)
