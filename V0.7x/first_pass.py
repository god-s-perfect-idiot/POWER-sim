import asm_dir as directive_handler

def symtab_append(line):
    f=open("symtab","a")
    f.write(line)
    f.close()

def par(line, addressCounter):
    line = line.strip()
    inst=""
	#tokens=line.split()
	#print(tokens[-1])
    if(line==""):
        print("")
    elif(line[-1]==':' and line[0]!="."):
        label=line[0:len(line)-1]
        symtab_append("address:"+str(addressCounter)+"\tname:"+str(label)+"\ttype:label\n") #appending to symbol table
    elif(line[0]=='.'):
        addressCounter = directive_handler.direc(line,addressCounter)
    elif(line[0]=='#'):
        print("")#ignore comment
    else:
        for ch in line:
            if(ch=="#"):
                break
            else:
                inst=inst+ch
        addressCounter+=4;

    return addressCounter
