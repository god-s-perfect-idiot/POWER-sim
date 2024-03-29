
## Detailed Documentation:

### 1. asm_dir.py

- dependencies:	memory_manage.py
- globals: direc_list(stores assembler directives to be processed)
- action: assembler directive handler

#### functions:
```
a) symtab_update: 
	- inputs - none
	- outputs - none
	- action - updates a word's or doubleword's symbol table entry, whose definition was in the previous line.

b) symtab_append:
	- inputs - line(directive to be written)
	- outputs - none
	- action - appends an assembler directive to symbol table, whose definition is in the current line.

c) direc:
	- inputs - line(current instruction), addressCounter(current address counter value)
	- outputs - addressCounter(updated address counter value)
	- action - reads the line, checks for assembler directives. If found, updates the symtab accordingly.
```
### 2. assembler.py

- dependencies: re
- globals: none
- actions: instuction parser



### 3. first_pass.py

- dependencies: asm_dir.py
- globals: none
- action: handles pass 1 of the assembler

#### functions: 
```
a) symtab_append:
	- inputs - line(directive to be written)
	- outputs - none
	- action - appends an assembler directive to symbol table, whose definition is in the current line.

b) par:
	- inputs - line(current instruction), addressCounter(current address counter value)
	- outputs - addressCounter(updated address counter value)
	- action - checks if line has assembler directives, comments or labels and updates the symtab accordingly and calls 
		 assembler directive processor as asm_dir.direc().
```
### 4. gui.py
- dependencies: tkinter, assembler.py, processor.py, memory_manage.py
- globals: code(current console command), asm(current software operating mode), view(to switch between memory view and symtab)
	 ps(window), menu(top menu), consoleframe(stores console details like input, output, buttons, etc), memoryframe(stores
	 memory view details for symtab, memory display), registerframe(stores register details), selectframe(for mode change)  
- action: generates and handles gui of software.

#### functions: 
```
a) mode_change:
	- inputs - mode(global)
	- outputs - mode(global)
	- action - switches between assembler and processor mode

b) clear_console:
	- inputs - code(global)
	- outputs - code(global)
	- action - clears console output

c) update_cout:
	- inputs - code(global)
	- outputs - none
	- action - checks code, assembles or processes it and updates the console

d) read_code:
	- inputs - code(global)
	- outputs - code(global)
	- action - reads console input and updates code with it

e) readmemory: 
	- inputs - none
	- outputs - none
	- action - reads memory file and displays it in memoryList

f) readregisters:
	- inputs - none
	- outputs - none
	- action - reads mempad file and displays it in registerList

g) readsymtab:
	- inputs - none
	- outputs - none
	- action - reads symtab file and displays it in memoryList

h) switchview:
	- inputs - view(global)
	- outputs - view(global)
	- action - changes between memory view and symtab view in memoryList

e) __main__:
	- inputs: globals
	- outputs: globals
	- action: creates and organizes UI components
	
```
### 5) main.py

- dependencies: argparse, assembler.py, processor.py, memory_manage.py, firstpass
- globals: addressCounter(stores address counter values)
- action: handles CLI action of software

#### functions:
```
a) run:
	- inputs - args, addressCounter(global)
	- outputs - addressCounter(global)
	- action - checks current mode and handles the actions of instruction accordingly

b) main:
	- inputs - none
	- outputs - none
	- action - assigns cli arguments

c) __main__:
	- inputs - none
	- outputs - none
	- action - calls main
```

### 6) memory_manage.py

- dependencies: none
- globals : f(memory reader), g(mempad reader)
- action: handles memory management

#### functions: 
```
a) symtab_flush:
	- inputs - none
	- outputs - none
	- action - clears symtab

b) memw_unfold:
	- inputs - f(global)
	- outputs - f(global)
	- action - opens memory in write mode

c) regw_unfold:
	- inputs - g(global)
	- outputs - g(global)
	- action - opens memorypad in write mode	

d) memr_unfold:
	- inputs - f(global)
	- outputs - f(global)
	- action - opens memory in read mode

e) regr_unfold:
	- inputs - g(global)
	- outputs - g(global)
	- action - opens memorypad in read mode

f) mem_fold:
	- inputs - f(global)
	- outputs - f(global)
	- action - closes memory

g) reg_fold:
	- inputs - g(global)
	- outputs - g(global)
	- action - closes memorypad

h) init_memory:
	- inputs - none
	- outputs - none
	- action - initialise 2^16 8 bit locations as 00000000

i) init_mempad:
	- inputs - none
	- outputs - none
	- action - initialise 32 32 bit registers as 00000000000000000000000000000000

j) update_memory:
	- inputs - loc(update address), datum(update data)
	- outputs - none
	- action - writes datum to loc

i) update_register:
	- inputs - indx(register index), datum(register data)
	- outputs - none
	- action - writes datum to indx-th register

j) _init_:
	- inputs - none
	- outputs - none
	- action - flushes symtab, mempad and memory, initialises memory and mempad
```

### 7) processor.py

- dependencies: none
- globals: none
- action: processes instruction

#### funtcions: several

### 8) input.s
IBM's original sample code for POWERPC

### 9) simple.s
A simpler sample code we made for testing

### 10) memory
displays memory status

### 11) mempad
displays memorypad status

### 12) symtab
displays symbol table status

### 13) setup_Windows.py

	Build executable for Windows. supply the command: 'python setup_Windows.py build' in a CMD terminal. 
