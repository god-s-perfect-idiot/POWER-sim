import memory_manage as mem_mod
direc_list = ["text", "data", "word", "doubleword"]

def symtab_update():
    with open("symtab", "r") as f:
        content = f.readlines()
    mem_mod.symtab_flush()
    with open("symtab", "w") as f:
        for i in range(len(content)-1):
            f.write(content[i])
        f.write(content[len(content)-1][:-6]+"data\n")


def symtab_append(line):
    f=open("symtab","a")
    f.write(line)
    f.close()

def direc(line, addressCounter):

    tokens=line.split()
    if(len(tokens)>0):
        for token in tokens:
            if(token[1:]=="text"):
                symtab_append("address:"+str(addressCounter)+"\tname:text\ttype:label\n") #appending to symbol table
                addressCounter+=4
            elif(token[1:]=="data"):
                symtab_append("address:"+str(addressCounter)+"\tname:data\ttype:label\n")
                addressCounter+=4
            elif(token[1:]=="word"):
                symtab_update()
                addressCounter+=4
            elif(token[1:]=="doubleword"):
                symtab_update()
                addressCounter+=8
            else:
                print("Unrecognized assembler directive!")

        return addressCounter
