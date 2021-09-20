import re
from asm_dir import direc

global addressCounter
addressCounter=3000;
symtab={}


def scan(line):
	#tokens=line.split()
	#print(tokens[-1])
	global addressCounter;
	if(line[-1]==':' and line[0]!="."):
		label=line[0:len(line)-1]
		symtab[addressCounter]=label
		addressCounter+=4
	elif(line[0]=='.'):
		direc(line)

def getregnum(regname):
	regnum=(regname[1:])
	regnumbin="{0:05b}".format(int(regnum))
	return regnumbin

def parse(line):

    scan(line)
    xformlist31=["and","extsw","nand","or","xor","sld","srd","srad"]	#instructions in X-form that has 31 as Primary Opcode
    xformlist63=[]	#instructions in X-form that has 63 as Primary Opcode
    xoformlist=["add","subf"]
    x3optype1=["and","extsw","nand","or","xor","sld","srd","srad"]	#instruction in X-form with 3 register operands
    xo3op=["add","subf"] #xo-form instructions with 3 register operands
    xo_dictionary={"and":28,"extsw":986,"nand":476,"or":444,"xor":316,"sld":27,"srd":539,"srad":794,"add":266,"subf":40}	#extended opcode dictionary

    tokens=[];
    tokens=re.split(r"[, ] *",line)
    inst=tokens[0]
    if(inst[-2:]=="o."):
        inst=inst[:-2]
    elif(inst[-1:]=="o" or inst[-1:]=="."):
        inst=inst[:-1]
    no_of_operands=len(tokens)-1
    hexword="";
    #print(tokens,inst)

    if(inst in xformlist31):
        hexword=hexword+"011111"
        if(no_of_operands==3):
            if(inst in x3optype1):
                r1=getregnum(tokens[1])
                r2=getregnum(tokens[2])
                r3=getregnum(tokens[3])
                hexword=hexword+r1+r2+r3
            hexword=hexword+"{0:010b}".format(xo_dictionary[inst])


    if(inst in xoformlist):
        hexword=hexword+"011111"
        if(no_of_operands==3):
            r1=getregnum(tokens[1])
            r2=getregnum(tokens[2])
            r3=getregnum(tokens[3])
            hexword=hexword+r1+r2+r3
        if(tokens[0][-1]=="o" or (tokens[0][-2]=="o" and tokens[0][-1]==".")): #To check if OE bit is to be set or not
            hexword=hexword+"1"
        else:
            hexword=hexword+"0"
            hexword=hexword+"{0:09b}".format(xo_dictionary[inst])




    if(tokens[0][-1]=="."):		#To check if Rc bit is to be set or not
        hexword=hexword+"1"
    else:
        hexword=hexword+"0"
    return hexword
