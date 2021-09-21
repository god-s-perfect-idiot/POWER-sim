<h1 align='center'>POWERSIM</h1>

<p align='center'>An open-source cross platform nanoPOWER ISA functional simulator.</p>

### Launch Modes:

- CLI Mode:
run:
`launchers/cli.py -m operation mode -i input file -o output file`
input and output files are optional

- GUI Mode:
Compile the script:
`generate_windows_exec.py`
run the command:
```
python3 generate_windows_exec.py build
```
or Run `gui.py`

### Dependencies:
- Argparse (CLI framework for Python)
- cx_Freeze (executable generation)
- Tkiner (GUI Development)

### Documentation
- Please check out [documentation.md](https://github.com/god-s-perfect-idiot/POWER-sim/blob/master/documentation.md)
