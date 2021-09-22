---
title: 'POWERsim: A nanoPOWER ISA Functional Simulator'
tags:
  - Python
  - POWER ISA
  - MicroProcessor
  - Functional Simulator
  - Instruction Set Architecture
authors:
  - name: Samar Musthafa^[co-first author] # note this makes a footnote saying 'co-first author'
    orcid: 0000-0003-2213-8820
    affiliation: 1
  - name: Mathew Joseph Kayyalackakom^[co-first author] # note this makes a footnote saying 'co-first author'
    orcid: 0000-0002-7646-4042
    affiliation: 1
  - name: Adithya Gopakumar^[co-first author] # note this makes a footnote saying 'co-first author'
    orcid: 0000-0001-7395-2481
    affiliation: 1
  - name: Mohammed Siyad B^[project guide]
    affiliation: 2
  - name: Basavaraj Talavar^[project guide]
    affiliation: 3
affiliations:
 - name: B. Tech Final year Student, TKM College of Engineering, Kollam
   index: 1
 - name: Department of Computer Science and Engineering, TKM College of Engineering, Kollam
   index: 2
 - name: Department of Computer Science and Engineering, NITK, Surathkal
   index: 3
date: 21 September 2021
bibliography: paper.bib

---

# Summary

The `Power ISA` is an instruction set architecture (ISA) developed by the 
`OpenPOWER Foundation`, led by `IBM`. It was originally developed by the now 
defunct `Power.org` industry group. Power ISA is an evolution of the PowerPC
ISA, created by the mergers of the core `PowerPC ISA` and the optional `Book E` 
for embedded applications. POWER ISA was made open source by IBM in August 
2019. POWER9 is the latest version of POWER ISA. POWER9 is a family of 
superscalar, multi-threading, symmetric multiprocessors based on the Power 
ISA. Power ISA is a RISC load/store architecture. It has multiple sets of registers.
Instructions have a length of 32 bits, with the exception of the VLE (variable-length
encoding) subset. Most instructions are triadic. Memory operations are strictly  
load/store, but allow for out-of-order execution. Power ISA has been an industry 
standard for Open Coherent Accelerator Processor Interface (OpenCAPI) and Open 
Memory Interface (OMI) architecture-agnostic compute accelerators, or accelerators
in general. With OpenPOWER joining the linux foundation, the need for an open 
source hardware-independent POWER ISA simulator has also come up.

# Statement of need

The main goal of the proposed project is to develop a platform independent,
open source `POWER ISA functional simulator` with minimal hardware requirements
and aims to provide a virtual environment capable of simulating a reduced POWER
ISA and associated operations. The simulator will greatly help in developing 
POWER ISA based solutions by simulating a virtual environment. It also serves 
as a teaching and learning tool for better understanding POWER ISA and how it 
works. The educational aspect of the simulator is very significant as most of 
the open source ISAs have a very powerful simulators associated with it. Such a 
simulator further enables research and advancement in POWER ISA. The proposed 
tool will simulate POWER ISA as well as provide register and memory access.


We aim to build a system to simulate POWER ISA architecture on a software layer
which does not rely on a programmed hardware component. This platform independent
approach aims at providing software to help learn as well as  develop  POWER  ISA
based applications. With the rise in popularity of hardware accelerators in modern
applications, an ISA simulator for the said architecture would create an environment
where the applications can be tested before being deployed to specially designed FPGA
chips or Hardware components for the acceleration. The process consists of two phases,
the Assembler development and the Processor Development. The Assembler converts
instructions to Hex code, handles assembler directives and comments and is a two 
pass assembler. The Processor simulates instruction execution and executes using a
python based processor. We use `Argparse` for CLI and `Tkinter` and `cx_Freeze` for GUI
development. 

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

# References
