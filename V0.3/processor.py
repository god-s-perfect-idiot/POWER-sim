#line is 32bit binary string eg "01111100001001010100001001111000"
def instruction_and(line):	# process "and"
	instruction="And";
	#extracting operands
	op1="R"+str(int(line[6:11],2));
	op2="R"+str(int(line[11:16],2));
	op3="R"+str(int(line[16:21],2));
	rctemp=line[31];
	action=op1+"<- ("+op2+") AND ("+op3+")"
	#print details
	print("Instruction: "+instruction)
	print("Operands: "+op1+","+op2+","+op3)
	print("Action: "+action)
	print("Rc: "+rctemp)

def instruction_nand(line):
	instruction="Nand";
	#extracting operands
	op1="R"+str(int(line[6:11],2));
	op2="R"+str(int(line[11:16],2));
	op3="R"+str(int(line[16:21],2));
	rctemp=line[31];
	action=op1+"<- ("+op2+") NAND ("+op3+")"
	#print details
	print("Instruction: "+instruction)
	print("Operands: "+op1+","+op2+","+op3)
	print("Action: "+action)
	print("Rc: "+rctemp)

def instruction_or(line):
	instruction="Or";
	#extracting operands
	op1="R"+str(int(line[6:11],2));
	op2="R"+str(int(line[11:16],2));
	op3="R"+str(int(line[16:21],2));
	rctemp=line[31];
	action=op1+"<- ("+op2+") OR ("+op3+")"
	#print details
	print("Instruction: "+instruction)
	print("Operands: "+op1+","+op2+","+op3)
	print("Action: "+action)
	print("Rc: "+rctemp)

def instruction_xor(line):
	instruction="Xor";
	#extracting operands
	op1="R"+str(int(line[6:11],2));
	op2="R"+str(int(line[11:16],2));
	op3="R"+str(int(line[16:21],2));
	rctemp=line[31];
	action=op1+"<- ("+op2+") XOR ("+op3+")"
	#print details
	print("Instruction: "+instruction)
	print("Operands: "+op1+","+op2+","+op3)
	print("Action: "+action)
	print("Rc: "+rctemp)


def instruction_add(line):
	instruction="Add";
	#extracting operands
	op1="R"+str(int(line[6:11],2));
	op2="R"+str(int(line[11:16],2));
	op3="R"+str(int(line[16:21],2));
	rctemp=line[31];
	OEtemp=line[21]
	action=op1+"<- ("+op2+") + ("+op3+")"
	#print details
	print("Instruction: "+instruction)
	print("Operands: "+op1+","+op2+","+op3)
	print("Action: "+action)
	print("OE: "+OEtemp)
	print("Rc: "+rctemp)


def instruction_subf(line):
	instruction="subf";
	#extracting operands
	op1="R"+str(int(line[6:11],2));
	op2="R"+str(int(line[11:16],2));
	op3="R"+str(int(line[16:21],2));
	rctemp=line[31];
	OEtemp=line[21]
	action=op1+"<- ("+op2+")` + ("+op3+") + 1  (` denotes 1's complement)"
	#print details
	print("Instruction: "+instruction)
	print("Operands: "+op1+","+op2+","+op3)
	print("Action: "+action)
	print("OE: "+OEtemp)
	print("Rc: "+rctemp)


def parse_xrelatives(line):#handle x,xs,xl etc

	ext_opcode_x=line[21:31]
	ext_opcode_xo=line[22:31]

	#handling X

	if(ext_opcode_x=="0000011100"):
		instruction_and(line)
	elif(ext_opcode_x=="0111011100"):
		instruction_nand(line)
	elif(ext_opcode_x=="0110111100"):
		instruction_or(line)
	elif(ext_opcode_x=="0100111100"):
		instruction_xor(line)


	#handling XO

	if(ext_opcode_xo=="000101000"):
		instruction_subf(line)
	elif(ext_opcode_xo=="100001010"):
		instruction_add(line)


def processline(line):
	PO=line[:6]
	#print(PO+" processline")
	if(PO=="011111"): #Primary opcode == 31?
		parse_xrelatives(line) #handle x,xs,xl etc
