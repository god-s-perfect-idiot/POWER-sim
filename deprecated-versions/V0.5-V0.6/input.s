#Data sections holds writable memory declarations
.data
.align 3  #align to 8-byte boundary

#This is where we will load our first value from
first_value:
        #"quad" actually emits 8-byte entities
        .quad 1
second_value:
        .quad 2

#Write the "official procedure descriptor" in its own section
.section ".opd","aw"
.align 3 #align to 8-byte boundary

#procedure description for ._start
.global _start
#Note that the description is named _start,
# and the beginning of the code is labeled ._start
_start:
        .quad ._start, .TOC.@tocbase, 0

#Switch to ".text" section for program code
.text
._start:
        #Use register 7 to load in an address
        #64-bit addresses must be loaded in 16-bit pieces

        #Load in the high-order pieces of the address
        lis 7, first_value@highest
        ori   7, 7, first_value@higher
        #Shift these up to the high-order bits
        rldicr 7, 7, 32, 31
        #Load in the low-order pieces of the address
        oris 7, 7, first_value@h
        ori  7, 7, first_value@l

        #Load in first value to register 4, from the address we just loaded
        ld 4, 0(7)

        #Load in the address of the second value
        lis 7, second_value@highest
        ori 7, 7, second_value@higher
        rldicr 7, 7, 32, 31
        oris 7, 7, second_value@h
        ori 7, 7, second_value@l

        #Load in the second value to register 5, from the address we just loaded
        ld 5, 0(7)

        #Calculate the value and store into register 6
        add 6, 4, 5

        #Exit with the status
        li 0, 1    #system call is in register 0
        mr 3, 6    #Move result into register 3 for the system call

        sc
