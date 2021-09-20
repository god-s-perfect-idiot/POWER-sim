#Data sections holds writable memory declarations
.data

#This is where we will load our first value from
first_value:
        #"quad" actually emits 8-byte entities
        .word 2234
second_value:
        .doubleword 2

.text
_start:

        ld 16, 3000(0)
        std 16, 3012(0)
        lwz 6, 3000(0)

        andi 4, 16, 4000
        xori 5, 16, 6200

        lis 7, first_value@highest
        ori   7, 7, first_value@higher
        #Shift these up to the high-order bits
        rldicr 7, 7, 32, 31
        #Load in the low-order pieces of the address
        oris 7, 7, first_value@h
        ori  7, 7, first_value@l

        #Load in first value to register 4, from the address we just loaded
        ld 4, 0(7)
        ba 3004

        #Load in the address of the second value
        lis 7, second_value@highest
        ori 7, 7, second_value@higher
        rldicr 7, 7, 32, 31
        oris 7, 7, second_value@h
        ori 7, 7, second_value@l

there:
        #Load in the second value to register 5, from the address we just loaded
        ld 5, 0(7)

        #Calculate the value and store into register 6
        add 6, 4, 5

        #Exit with the status
        li 0, 1    #system call is in register 0
        mr 3, 6    #Move result into register 3 for the system call

        sc
