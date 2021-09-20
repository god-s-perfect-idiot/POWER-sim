import memory_manage as mem_man

#line is 32bit binary string eg "01111100001001010100001001111000"
def instruction_and(line):	# process "and"
	instruction="And";
	#extracting operands
	opind1=int(line[6:11],2);
	opind2=int(line[11:16],2);
	opind3=int(line[16:21],2);
	rctemp=line[31];
	#action=op1+"<- ("+op2+") AND ("+op3+")"
	#print details
	op1="";
	op2=mem_man.read_register(opind2);
	op3=mem_man.read_register(opind3);
	for i in range(64):
		if(op2[i]=='0' or op3[i]=='0'):
			op1=op1+"0";
		else:
			op1=op1+"1";
	mem_man.update_register(opind1,op1);
	#print("Instruction: "+instruction);
	#print("Operands: "+op1+","+op2+","+op3);
	#print("Action: "+action);
	#print("Rc: "+rctemp);

def instruction_nand(line):
	instruction="Nand";
	#extracting operands
	opind1=int(line[6:11],2);
	opind2=int(line[11:16],2);
	opind3=int(line[16:21],2);
	rctemp=line[31];
	#action=op1+"<- ("+op2+") AND ("+op3+")"
	#print details
	op1="";
	op2=mem_man.read_register(opind2);
	op3=mem_man.read_register(opind3);
	for i in range(64):
		if(op2[i]=='0' or op3[i]=='0'):
			op1=op1+"1";
		else:
			op1=op1+"0";
	mem_man.update_register(opind1,op1);
	#print("Instruction: "+instruction)
	#print("Operands: "+op1+","+op2+","+op3)
	#print("Action: "+action)
	#print("Rc: "+rctemp)

def instruction_or(line):
	instruction="Or";
	#extracting operands
	opind1=int(line[6:11],2);
	opind2=int(line[11:16],2);
	opind3=int(line[16:21],2);
	rctemp=line[31];
	#action=op1+"<- ("+op2+") AND ("+op3+")"
	#print details
	op1="";
	op2=mem_man.read_register(opind2);
	op3=mem_man.read_register(opind3);
	for i in range(64):
		if(op2[i]=='1' or op3[i]=='1'):
			op1=op1+"1";
		else:
			op1=op1+"0";
	mem_man.update_register(opind1,op1);
	#print("Instruction: "+instruction)
	#print("Operands: "+op1+","+op2+","+op3)
	#print("Action: "+action)
	#print("Rc: "+rctemp)

def instruction_xor(line):
	instruction="Xor";
	#extracting operands
	opind1=int(line[6:11],2);
	opind2=int(line[11:16],2);
	opind3=int(line[16:21],2);
	rctemp=line[31];
	#action=op1+"<- ("+op2+") AND ("+op3+")"
	#print details
	op1="";
	op2=mem_man.read_register(opind2);
	op3=mem_man.read_register(opind3);
	for i in range(64):
		if(op2[i]==op3[i]):
			op1=op1+"0";
		else:
			op1=op1+"1";
	mem_man.update_register(opind1,op1);
	#print("Instruction: "+instruction)
	#print("Operands: "+op1+","+op2+","+op3)
	#print("Action: "+action)
	#print("Rc: "+rctemp)


def instruction_add(line):
	instruction="Add";
	opind1=int(line[6:11],2);
	opind2=int(line[11:16],2);
	opind3=int(line[16:21],2);
	rctemp=line[31];
	#action=op1+"<- ("+op2+") AND ("+op3+")"
	#print details
	op1="";
	op2=mem_man.read_register(opind2);
	op3=mem_man.read_register(opind3);
	op1=bin(int(op2,2)+int(op3,2))[2:];
	mem_man.update_register(opind1,op1);
	#print("Instruction: "+instruction)
	#print("Operands: "+op1+","+op2+","+op3)
	#print("Action: "+action)
	#print("OE: "+OEtemp)
	#print("Rc: "+rctemp)


def instruction_subf(line):
	instruction="subf";
	#extracting operands
	opind1=int(line[6:11],2);
	opind2=int(line[11:16],2);
	opind3=int(line[16:21],2);
	rctemp=line[31];
	#action=op1+"<- ("+op2+") AND ("+op3+")"
	#print details
	op1="";
	temp="";
	op2=mem_man.read_register(opind2);
	op3=mem_man.read_register(opind3);
	for i in range(64):
		if(op2[i]=="0"):
			temp=temp+"1";
		else:
			temp=temp+"0";
	op2=temp;
	op1=bin(int(op2,2)+int(op3,2)+int("1",2))[2:];
	mem_man.update_register(opind1,op1);
	#print("Instruction: "+instruction)
	#print("Operands: "+op1+","+op2+","+op3)
	#print("Action: "+action)
	#print("OE: "+OEtemp)
	#print("Rc: "+rctemp)

def instruction_sld(line):
	instruction="sld";
	#extracting operands
	opind1=int(line[6:11],2);
	opind2=int(line[11:16],2);
	opind3=int(line[16:21],2);
	rctemp=line[31];

	op1=mem_man.read_register(opind1);
	op3=mem_man.read_register(opind3);
	n=int(op3[-7:],2);
	op2=op1[n:];
	for i in range(n):
		op2=op2+"0";
	mem_man.update_register(opind2,op2)

def instruction_srd(line):
	instruction="srd";
	#extracting operands
	opind1=int(line[6:11],2);
	opind2=int(line[11:16],2);
	opind3=int(line[16:21],2);
	rctemp=line[31];

	op1=mem_man.read_register(opind1);
	op3=mem_man.read_register(opind3);
	n=int(op3[-7:],2);
	op2="";
	for i in range(n):
		op2=op2+"0";
	op2=op2+op1[:-n]
	mem_man.update_register(opind2,op2)
def instruction_srad(line):
	instruction="srad";
	#extracting operands
	opind1=int(line[6:11],2);
	opind2=int(line[11:16],2);
	opind3=int(line[16:21],2);
	rctemp=line[31];

	op1=mem_man.read_register(opind1);
	op3=mem_man.read_register(opind3);
	n=int(op3[-7:],2);
	op2="";
	filler=op1[0]
	for i in range(n):
		op2=op2+filler;
	op2=op2+op1[:-n]
	mem_man.update_register(opind2,op2)

def instruction_extsw(line):
	instruction="srad";
	#extracting operands
	opind1=int(line[6:11],2);
	opind2=int(line[11:16],2);
	rctemp=line[31];
	op1=mem_man.read_register(opind1);
	filler=op1[32];
	op2="";
	for i in range(32):
		op2=op2+filler;
	op2=op2+op1[32:]
	mem_man.update_register(opind2,op2)


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
	elif(ext_opcode_x=="0000011011"): #27
		instruction_sld(line)
	elif(ext_opcode_x=="1000011011"): #539
		instruction_srd(line)
	elif(ext_opcode_x=="1100011010"): #794
		instruction_srad(line)
	elif(ext_opcode_x=="1111011010"): #986
		instruction_extsw(line)


	#handling XO

	if(ext_opcode_xo=="000101000"):
		instruction_subf(line)
	elif(ext_opcode_xo=="100001010"):
		instruction_add(line)

def ld(line):
	rt = int(line[6:11],2)
	ra = int(line[11:16],2)
	ds = int(line[16:30],2)
	t1 = int(mem_man.read_register(ra),2)
	disp = ds*4
	ea = int(disp) + int(t1)
	datum1 = mem_man.read_memory(ea)
	datum2 = mem_man.read_memory(ea+1)
	datum3 = mem_man.read_memory(ea+2)
	datum4 = mem_man.read_memory(ea+3)
	datum5 = mem_man.read_memory(ea+4)
	datum6 = mem_man.read_memory(ea+5)
	datum7 = mem_man.read_memory(ea+6)
	datum8 = mem_man.read_memory(ea+7)
	data = datum8+datum7+datum6+datum5+datum4+datum3+datum2+datum1
	mem_man.update_register(rt, data)

def std(line):
	rs = int(line[6:11],2)
	ra = int(line[11:16],2)
	ds = int(line[16:30],2)
	t1 = int(mem_man.read_register(ra),2)
	disp = ds*4
	ea = disp + t1
	data = mem_man.read_register(rs)
	mem_man.update_memory(ea, data[-8:])
	mem_man.update_memory(ea+1, data[-16:-8])
	mem_man.update_memory(ea+2, data[-24:-16])
	mem_man.update_memory(ea+3, data[-32:-24])
	mem_man.update_memory(ea+4, data[-40:-32])
	mem_man.update_memory(ea+5, data[-48:-40])
	mem_man.update_memory(ea+6, data[-56:-48])
	mem_man.update_memory(ea+7, data[-64:-56])

def lwz(line):
	rt = int(line[6:11],2)
	ra = int(line[11:16],2)
	ds = int(line[16:32],2)
	t1 = int(mem_man.read_register(ra),2)
	ea = ds + t1
	datum1 = mem_man.read_memory(ea)
	datum2 = mem_man.read_memory(ea+1)
	datum3 = mem_man.read_memory(ea+2)
	datum4 = mem_man.read_memory(ea+3)
	data = datum4+datum3+datum2+datum1
	mem_man.update_register(rt, data)

def stw(line):
	rs = int(line[6:11],2)
	ra = int(line[11:16],2)
	ds = int(line[16:30],2)
	t1 = int(mem_man.read_register(ra),2)
	ea = ds + t1
	data = mem_man.read_register(rs)
	mem_man.update_memory(ea, data[-8:])
	mem_man.update_memory(ea+1, data[-16:-8])
	mem_man.update_memory(ea+2, data[-24:-16])
	mem_man.update_memory(ea+3, data[-32:-24])

def lhz(line):
	rt = int(line[6:11],2)
	ra = int(line[11:16],2)
	ds = int(line[16:32],2)
	t1 = int(mem_man.read_register(ra),2)
	ea = ds + t1
	datum1 = mem_man.read_memory(ea)
	datum2 = mem_man.read_memory(ea+1)
	data = datum2+datum1
	mem_man.update_register(rt, data)

def sth(line):
	rs = int(line[6:11],2)
	ra = int(line[11:16],2)
	ds = int(line[16:30],2)
	t1 = int(mem_man.read_register(ra),2)
	ea = ds + t1
	data = mem_man.read_register(rs)
	mem_man.update_memory(ea, data[-8:])
	mem_man.update_memory(ea+1, data[-16:-8])

def lbz(line):
	rt = int(line[6:11],2)
	ra = int(line[11:16],2)
	ds = int(line[16:32],2)
	t1 = int(mem_man.read_register(ra),2)
	ea = ds + t1
	data = mem_man.read_memory(ea)
	mem_man.update_register(rt, data)

def stb(line):
	rs = int(line[6:11],2)
	ra = int(line[11:16],2)
	ds = int(line[16:30],2)
	t1 = int(mem_man.read_register(ra),2)
	ea = ds + t1
	data = mem_man.read_register(rs)
	mem_man.update_memory(ea, data[-8:])

def andi(line):
	rs = int(line[6:11],2)
	ra = int(line[11:16],2)
	ui = int(line[16:32],2)
	t1 = int(mem_man.read_register(rs)[-16:],2)
	t2 = str(t1 & ui)
	mem_man.update_register(ra, t2)

def xori(line):
	rs = int(line[6:11],2)
	ra = int(line[11:16],2)
	ui = int(line[16:32],2)
	t1 = int(mem_man.read_register(rs)[-16:],2)
	t2 = str(t1 ^ ui)
	mem_man.update_register(ra, t2)

def processline(line):
	PO=line[:6]
	#print(PO+" processline")
	if(PO == "011111"): #Primary opcode == 31?
		parse_xrelatives(line) #handle x,xs,xl etc
	elif(PO == "111010"): #58 load double word
		ld(line)
	elif(PO == "111110"):
		std(line)
	elif(PO == "100000"):
		lwz(line)
	elif(PO == "100100"):
		stw(line)
	elif(PO == "101000"):
		lhz(line)
	elif(PO == "101100"):
		sth(line)
	elif(PO == "100010"):
		lbz(line)
	elif(PO == "100110"):
		stb(line)
	elif(PO == "011100"):
		andi(line)
	elif(PO == "011010"):
		xori(line)
