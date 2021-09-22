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

# Installation Instructions

## Installation

- clone the repo

```
git clone git@github.com:god-s-perfect-idiot/POWER-sim.git
```
- install dependency packages
```
pip install argparse csx_Freeze tk
```
- generate executable package on windows if needed (Optional)

```
python3 generate_windows_exec.py build
```
- Launch modes: 
  - Run /build/gui.exe file for executing POWERSim
  - run gui.py for gui mode

  ```
  python3 launchers/gui.py
  ```
  - run cli.py for cli mode 

  ```
  python3 launchers/cli.py -m [MODE] -i? [input] -o? [output]
  ```
  
 ## Dependencies
 
 - argparse 
 - Tkinter
 - cx_Freeze

# Example Usage

POWERsim has two different launch modes for accessing the application. 
- The GUI mode launches an interactive session where the user can switch between 
assembly and processor modes. The interactive console provides compiled binary
results and the memory devies and symtabs will be viewable as well.

GUI: 

![Capture](https://user-images.githubusercontent.com/33544311/134208538-515e1d31-5ea7-4245-97e7-5fbbce6aa15c.JPG)

- The CLI mode is exclusive to an execution mode and is capable of executing
or assembling instructions. It can also accept an input and output file.

An example use case is as follows: 

![V0 6](https://user-images.githubusercontent.com/33544311/134208458-07c5d05d-cb32-442d-b6ba-b791fbfdedb0.PNG)

# Functionality Documentation

POWERsim has two launch options: A GUI mode and a CLI mode. Both have their own 
different usages and interfaces. 

## CLI Mode:
Launch CLI mode using the following command:
```
cd launchers
python3 cli.py -m [OPERATION MODE] -i [INPUT FILE] -o [OUTPUT FILE]
```
- Here, -m accepts two values. 

The two operation modes are Assembler mode and Processor Mode. 

#### Assembler Mode:
Assembles instructions and returns the binary value of the instruction

#### Processor Mode:
Processes instruction. Assembles first and then executes the instruction. 

- The usage of -i is to provide an input file. 

Any file of the type .s that contains input instructions can be assembled/
processed. 

- The usage of -o is to provide an output file.

The response of the execution is stored there in the output file. 

## GUI Mode:
Launch GUI using the Python script or generated windows exectuable. 
```
# script
cd launchers/
python3 gui.py

#generated exe
python3 generate_windows_exec.py build
# file is in /build
```
GUI Mode has the following sections: 

#### Live console:
Assemble or process the given instruction and print the response in the
console

#### Assemble-Process switch:
Switch between assembly and process modes

#### Symtab/Memory view:
Show the contents of the Symbol Table and the Memory

#### Memory/Symtab switcher:
Button to toggle between either devices

#### Register View:
Display content of the register.

#### Load an external File using the File Menu. 

For detailed per-method documentation, please refer to [documentation.md](https://github.com/god-s-perfect-idiot/POWER-sim/blob/master/documentation.md)

## Supported Instructions: 
POWERsim currently supports a reduced instruction set of POWER ISA compiled 
and titled [nanoPOWERISA](https://github.com/god-s-perfect-idiot/POWER-sim/blob/master/supported_instructions.md). It also, only supports 16 memory bits. This shall be 
expanded upon in future updates. 

# Acknowledgements

We acknowledge contributions from Samar Musthafa, Mathew Joseph Kayyalackakom and 
Adithya Gopakumar during the development of the project. Our guides, Prof. Mohammad
Siyad B and Prof. Basavaraj Talavar also played significant roles during 
the ideation and subsequent development reviews of the project. 

# Contributions

We welcome all types of contributions, either code fixes, new features or doc 
improvements. For commits please follow conventional commits convention. All 
code must pass lint rules before it can be merged into main.
