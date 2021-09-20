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
        for t_indx in range(len(tokens)):
            token = tokens[t_indx]
            if(token[0]=="."):
                if(token[1:]=="text"):
                    symtab_append("address:"+str(addressCounter)+"\tname:text\ttype:label\n") #appending to symbol table
                elif(token[1:]=="data"):
                    symtab_append("address:"+str(addressCounter)+"\tname:data\ttype:label\n")
                elif(token[1:]=="word"):
                    symtab_update()
                    value = tokens[t_indx+1]
                    v_bin = "0000000000000000000000000000000"+bin(int(value))[2:]
                    v_bin = v_bin[-32:]
                    mem_mod.update_memory(addressCounter, v_bin[-8:])
                    mem_mod.update_memory(addressCounter+1, v_bin[-16:-8])
                    mem_mod.update_memory(addressCounter+2, v_bin[-24:-16])
                    mem_mod.update_memory(addressCounter+3, v_bin[:-24])
                    addressCounter+=4
                elif(token[1:]=="doubleword"):
                    symtab_update()
                    value = tokens[t_indx+1]
                    v_bin = "000000000000000000000000000000000000000000000000000000000000000"+bin(int(value))[2:]
                    v_bin = v_bin[-64:]
                    mem_mod.update_memory(addressCounter, v_bin[-8:])
                    mem_mod.update_memory(addressCounter+1, v_bin[-16:-8])
                    mem_mod.update_memory(addressCounter+2, v_bin[-24:-16])
                    mem_mod.update_memory(addressCounter+3, v_bin[-32:-24])
                    mem_mod.update_memory(addressCounter+4, v_bin[-40:-32])
                    mem_mod.update_memory(addressCounter+5, v_bin[-48:-40])
                    mem_mod.update_memory(addressCounter+6, v_bin[-56:-48])
                    mem_mod.update_memory(addressCounter+7, v_bin[:-56])
                    addressCounter+=8
                else:
                    print("Unrecognized assembler directive!")

        return addressCounter
