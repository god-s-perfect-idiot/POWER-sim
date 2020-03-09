import re
def getregnum(regname):
	regnum=(regname[1:])
	regnumbin="{0:05b}".format(int(regnum))
	return regnumbin

def parse(line):

	xformlist=["and","extsw","nand","or","xor","sld","srd","srad"]	#instructions in X-form
	x3optype1=["and","extsw","nand","or","xor","sld","srd","srad"]	#instruction in X-form with 3 register operands
	xo_dictionary={"and":28,"extsw":986,"nand":476,"or":444,"xor":316,"sld":27,"srd":539,"srad":794}	#extended opcode dictionary
	tokens=[]
	tokens=re.split(r"[, ] *",line)
	inst=(re.split(r"[o.]%",tokens[0])[0]).lower()
	no_of_operands=len(tokens)-1
	hexword="";
	#print(tokens,inst)

	if(inst in xformlist):
		hexword=hexword+"011111"
		if(no_of_operands==3):
			if(inst in x3optype1):
				r1=getregnum(tokens[1])
				r2=getregnum(tokens[2])
				r3=getregnum(tokens[3])
				hexword=hexword+r1+r2+r3
			hexword=hexword+"{0:010b}".format(xo_dictionary[inst])
	if(tokens[0][-1]=="."):
		hexword=hexword+"1"
	else:
		hexword=hexword+"0"
	return hexword
