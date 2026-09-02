# Calculator

Two versions of the same calculator, written in Python.

- `calculator.py` — command-line version. Supports addition, subtraction,
  multiplication, division, exponentiation, and square root, with basic
  error handling (divide-by-zero, negative square roots, bad input).
- `calculator_gui.py` — desktop GUI version built with `tkinter` (part of
  the Python standard library, no extra install needed on most systems).
  Supports +, -, *, /, parentheses, decimals, backspace, and clear.
  Keyboard: Enter = `=`, Backspace = `⌫`.

## Usage

```bash
python3 calculator.py       # CLI version
python3 calculator_gui.py   # GUI version
```

CLI: follow the on-screen menu to pick an operation and enter numbers.
GUI: click buttons or type on your keyboard, then press Enter or `=`.

> Note: on some minimal Linux installs, tkinter isn't bundled with Python
> and needs `sudo apt-get install python3-tk` first. Windows and macOS
> installers normally include it already.

## Tests

```bash
python3 -m unittest test_calculator.py -v
```
