# Documentation.
## Creating data.
You can create your own displayable reaction chains. Just simply write a python script with an object named 'chain' in it and import it in the program, when the dialogue appears. Use the following classes for that:

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
**`Atom()`** | proton: `int`, electron = `None`: `int` | `bool` | Constructor. Raises `ElectronNumberException` (`ProtonNumberException`), if such an atom with this electron (proton) number doesn't exist.
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
**`get_layer()`** | | `int` | Get the number of layers in atom. CAUTION: counting starts with 0.
**`get_max_electrons()`** | | `int` | Get the maximum number of electrons on the most exterior layer.
**`charge()`** | | `int` | Get the charge.
**`change_charge()`** | electron: `int` | `int` | Add electrons or remove them. Raises ElectronNumberException if it isn't possible.
