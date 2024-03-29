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
date: 22 September 2021
bibliography: paper.bib

---

# Summary

The `Power ISA`[@manual] is an instruction set architecture (ISA) developed by the 
`OpenPOWER Foundation`, led by `IBM`. An `Instruction Set Architecture`[@isa] is essentially
an abstract model or documentation that defines the instructions, data types, features,
hardware support, etc for a particular hardware device capable of exeucting it. 
The relevance of an ISA as a whole is that understanding one aids research and
development in assembly level applications on a specific hardware board. POWER10 or 
POWER ISA v3.1 is the latest version of POWER ISA. Power ISA is a RISC load/store 
architecture. It has multiple sets of registers. Instructions have a length of 32  
bits, with the exception of the VLE (variable-length encoding) subset. Most instructions 
are triadic(Two sources and one destination). Memory operations are strictly load/store, 
but allow for out-of-order execution. With OpenPOWER joining the linux foundation, the 
need for an open source hardware-independent POWER ISA simulator has also come up. POWER
ISA was made open source by IBM in August 2019. The currently existing solution for the
given problem depends on an actual hardware target board or a ghdl simulator that 
is relatively more tedious to set up and get into. As can be inferred, the proposed
software would be a `hardware simulation project` mainly focusing on providing a 
software that helps develop micrprocessor assembly code for testing POWER ISA 
programs and developing applications following its open-sourcing. 

# Statement of need

The main goal of the proposed project is to develop a platform independent,
open source `POWER ISA functional simulator` with minimal hardware requirements
and aims to provide a sanbox for executing a reduced POWER ISA instruction set. 
The applications of proposed simulator would include the ability to test and 
develop POWER ISA based assembly code. Apart from the mentioned use-case of
testing and developing assembly code, the software is also capable of  being used
as a teaching and learning tool for better understanding POWER ISA and how it 
works. Simply put, the target audience comprises of research personnel looking to
test the ISA and learn it as well as developers aiming to test their assembly code. 
The niche nature of the ISA as well as the lack of a hassle-free open source simulator
work in favor of the project. The educational aspect of the simulator is very significant as most of 
the open source ISAs have a very powerful simulators associated with it. Such a 
software further enables research and advancement of POWER ISA based applications. 
The proposed tool will simulate POWER ISA as well as provide register and memory access.


We aim to build a system to simulate POWER ISA architecture completely independent of
the installed system's hardware. Essentially, everything including the memory devices
will be simulated file objects that are used to serve this purpose. There are currently 
two other widely accepted software that simulates POWER ISA; Microwatt[@microwatt] and Power10 Functional
Simulator[@power10fs]. MicroWatt is an open source tool capable of executing POWER ISA assembly code. 
But, this software is written in VHDL and relies on a hardware board or a GHDL simulator 
to execute the code. Simply put, setting the tool up is tedious. Another alternative is 
Power10 Functional Simulator developed by IBM. The proposed software would be superioer
due to the closed-source nature of Power10 Functional Simulator. Our platform independent 
approach aims at providing software to help learn as well as develop POWER ISA based 
applications. With the rise in popularity of hardware accelerators in modern applications,
an ISA simulator for the said architecture would create an environment where the applications
can be tested before being deployed to specially designed FPGA chips or Hardware components
for their intended purpose. This means that researchers and developers can both test and 
debug their assembly code before running it on actual hardware board. The process consists 
of two phases, the Assembler development and the Processor Development. The Assembler 
converts instructions to Hex code, handles assembler directives and comments and is a two 
pass assembler. The Processor simulates instruction execution and executes using a
python[@pythonlibs] based processor. We use `Argparse`[@cpython] for CLI and `Tkinter`[@cpython] and `cx_Freeze`[@cx_Freeze] for GUI
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

An example assembly code can be found in the file `/simple.s`

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

# References
