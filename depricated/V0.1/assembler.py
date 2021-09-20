def parse(line):

    tokens=line.split()

    indx=0
    for token in tokens:
        if(token[0]=="#"):
            if(token[1:]=="data"):
                print("data section declaration")
            elif(token[1:]=="text"):
                print("code section declaration")
            print("comment: ", end=" ")
            for i in range(indx,len(tokens)):
                print(tokens[i], end=" ")
            print("\n")
            break
        elif(token[0]=="."):
            print("Assembler directive: "+token[1:])
        else:
            print("NA: "+str(token))

        indx+=1
