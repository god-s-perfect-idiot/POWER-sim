import re

def getregnum(regname):
	if(regname[0]=="r"):
		regnum=(regname[1:])
		regnumbin="{0:05b}".format(int(regnum))
	else:
		regnumbin="{0:05b}".format(int(regname))
	return regnumbin

def parse(line):
	line=line.strip()
	line=line.lower()
	xformlist31=["and","extsw","nand","or","xor","sld","srd","srad"]	#instructions in X-form that has 31 as Primary Opcode
	xformlist63=[]	#instructions in X-form that has 63 as Primary Opcode
	xoformlist=["add","subf"]
	x3optype1=["and","extsw","nand","or","xor","sld","srd","srad"]	#instruction in X-form with 3 register operands
	x2optype1=["extsw"] #x-form instructions with 2 register operands
	xo3op=["add","subf"] #xo-form instructions with 3 register operands
	ucbranchlist=["b","ba","bl","bla"]
	cbranchlist=["bc","bca","bcl","bcla"]
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
	if(inst in xformlist31):
		hexword=hexword+"011111"
		if(no_of_operands==3):
			if(inst in x3optype1):
				r1=getregnum(tokens[1])
				r2=getregnum(tokens[2])
				r3=getregnum(tokens[3])
				hexword=hexword+r1+r2+r3
			hexword=hexword+"{0:010b}".format(xo_dictionary[inst])
		if(no_of_operands==2):
			if(inst in x2optype1):
				r1=getregnum(tokens[1])
				r2=getregnum(tokens[2])
				r3="00000"
				hexword=hexword+r1+r2+r3
			hexword=hexword+"{0:010b}".format(xo_dictionary[inst])
		if(tokens[0][-1]=="."):		#To check if Rc bit is to be set or not
			hexword=hexword+"1"
		else:
			hexword=hexword+"0"
	elif(inst in xoformlist):
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
	elif(inst == "ld"):
		hexword += bin(58)[2:]
		rt = "00000"+bin(int(tokens[1]))[2:]
		rt = rt[-5:]
		arg2 = tokens[2].split("(")
		ds = "000000000000000"+bin(int(arg2[0])//4)[2:]
		ds = ds[-14:]
		ra = "00000"+bin(int(arg2[1][:-1]))[2:]
		ra = ra[-5:]
		hexword += rt+ra+ds+"00"
	elif(inst == "std"):
		hexword += bin(62)[2:]
		rs = "00000"+bin(int(tokens[1]))[2:]
		rs = rs[-5:]
		arg2 = tokens[2].split("(")
		ds = "000000000000000"+bin(int(arg2[0])//4)[2:]
		ds = ds[-14:]
		ra = "00000"+bin(int(arg2[1][:-1]))[2:]
		ra = ra[-5:]
		hexword += rs+ra+ds+"00"
	elif(inst == "lwz"):
		hexword += bin(32)[2:]
		rt = "00000"+bin(int(tokens[1]))[2:]
		rt = rt[-5:]
		arg2 = tokens[2].split("(")
		ds = "000000000000000"+bin(int(arg2[0]))[2:]
		ds = ds[-16:]
		ra = "00000"+bin(int(arg2[1][:-1]))[2:]
		ra = ra[-5:]
		hexword += rt+ra+ds
	elif(inst == "stw"):
		hexword += bin(36)[2:]
		rs = "00000"+bin(int(tokens[1]))[2:]
		rs = rs[-5:]
		arg2 = tokens[2].split("(")
		ds = "000000000000000"+bin(int(arg2[0]))[2:]
		ds = ds[-16:]
		ra = "00000"+bin(int(arg2[1][:-1]))[2:]
		ra = ra[-5:]
		hexword += rs+ra+ds
	elif(inst == "lhz"):
		hexword += bin(40)[2:]
		rt = "00000"+bin(int(tokens[1]))[2:]
		rt = rt[-5:]
		arg2 = tokens[2].split("(")
		ds = "000000000000000"+bin(int(arg2[0]))[2:]
		ds = ds[-16:]
		ra = "00000"+bin(int(arg2[1][:-1]))[2:]
		ra = ra[-5:]
		hexword += rt+ra+ds
	elif(inst == "sth"):
		hexword += bin(44)[2:]
		rs = "00000"+bin(int(tokens[1]))[2:]
		rs = rs[-5:]
		arg2 = tokens[2].split("(")
		ds = "000000000000000"+bin(int(arg2[0]))[2:]
		ds = ds[-16:]
		ra = "00000"+bin(int(arg2[1][:-1]))[2:]
		ra = ra[-5:]
		hexword += rs+ra+ds
	elif(inst == "lbz"):
		hexword += bin(34)[2:]
		rt = "00000"+bin(int(tokens[1]))[2:]
		rt = rt[-5:]
		arg2 = tokens[2].split("(")
		ds = "000000000000000"+bin(int(arg2[0]))[2:]
		ds = ds[-16:]
		ra = "00000"+bin(int(arg2[1][:-1]))[2:]
		ra = ra[-5:]
		hexword += rt+ra+ds
	elif(inst == "stb"):
		hexword += bin(38)[2:]
		rs = "00000"+bin(int(tokens[1]))[2:]
		rs = rs[-5:]
		arg2 = tokens[2].split("(")
		ds = "000000000000000"+bin(int(arg2[0]))[2:]
		ds = ds[-16:]
		ra = "00000"+bin(int(arg2[1][:-1]))[2:]
		ra = ra[-5:]
		hexword += rs+ra+ds
	elif(inst in ucbranchlist):
		op = "000000"+bin(18)[2:]
		op = op[-6:]
		ll = "000000000000000000000000"+bin(int(tokens[1]))[2:]
		ll = ll[-24:]
		hexword = op+ll
		if(inst == "b"):
			hexword+="00"
		elif(inst == "ba"):
			hexword+="10"
		elif(inst == "bl"):
			hexword+="01"
		elif(inst == "bla"):
			hexword+="11"
	elif(inst in cbranchlist):
		op = "000000"+bin(16)[2:]
		op = op[-6:]
		bo = "00000"+bin(int(tokens[1]))[2:]
		bo = bo[-5:]
		bi = "00000"+bin(int(tokens[2]))[2:]
		bi = bi[-5:]
		ll = "00000000000000"+bin(int(tokens[3]))[2:]
		ll = ll[-14:]
		hexword = op+bo+bi+ll
		if(inst == "bc"):
			hexword+="00"
		elif(inst == "bca"):
			hexword+="10"
		elif(inst == "bcl"):
			hexword+="01"
		elif(inst == "bcla"):
			hexword+="11"
	elif(inst == "andi"):
		op = "000000"+bin(28)[2:]
		op = op[-6:]
		hexword += op
		ra = "00000"+bin(int(tokens[1]))[2:]
		ra = ra[-5:]
		rs = "00000"+bin(int(tokens[2]))[2:]
		rs = rs[-5:]
		ui = "0000000000000000"+bin(int(tokens[3]))[2:]
		ui = ui[-16:]
		hexword += rs+ra+ui
	elif(inst == "xori"):
		op = "000000"+bin(26)[2:]
		op = op[-6:]
		hexword += op
		ra = "00000"+bin(int(tokens[1]))[2:]
		ra = ra[-5:]
		rs = "00000"+bin(int(tokens[2]))[2:]
		rs = rs[-5:]
		ui = "0000000000000000"+bin(int(tokens[3]))[2:]
		ui = ui[-16:]
		hexword += rs+ra+ui

	return hexword
