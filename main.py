#! /usr/bin/env python3
import argparse
import assembler as asm
import processor as prcs
import memory_manage as mem_mod
import first_pass
import time

addressCounter = 3000

def run(args):
    global addressCounter

    filename = args.input # these match the "dest": dest="input"
    output_filename = args.output # from dest="output"
    r_mode = args.mode

    mem_mod._init_()

    if(r_mode=="asm"):
        if(filename==None):
            run=True
            print("\n-------------------------POWER Sim V0.7x Assembler Console----------------------\n")
            while(run):
                line=input(">>>")
                if(line not in ["quit()","q()","exit","quit"]):
                    try:
                        addressCounter = first_pass.par(line, addressCounter)
                        imc=asm.parse(line)
                        print(str(addressCounter)+"\t"+line.rstrip())
                        print(imc.strip())
                    except:
                        print("Error thrown")
                else:
                    run=False

        else:
            if(output_filename==None):
                with open(filename, "r") as f:
                    lc=1
                    for line in f:
                        print("->line "+str(lc))
                        try:
                            if(line!="\n"):
                                addressCounter = first_pass.par(line, addressCounter)
                                imc=asm.parse(line)
                                if(line.rstrip()!=""):
                                    print(str(addressCounter)+"\t"+line.rstrip())
                                if(imc.rstrip()!=""):
                                    print(imc.strip())
                        except Exception as e:
                            print("Syntax Error at line: "+str(lc)+": "+line+"\n"+str(e))
                            break
                        lc+=1
            else:
                with open(filename,"r") as f:
                    lc=1
                    fw=open(output_filename,"w")
                    for line in f:
                        print("->line "+str(lc))
                        try:
                            if(line!="\n"):
                                addressCounter = first_pass.par(line, addressCounter)
                                imc=asm.parse(line)
                                fw.write(imc)
                        except:
                            print("Syntax Error at line: "+str(lc))
                            break
                        lc+=1
    elif(r_mode=="proc"):
        if(filename==None):
            run=True
            print("\n-------------------------POWER Sim V0.7x Processor Console----------------------\n")
            while(run):
                line=input(">>>")
                if(line not in ["quit()","q()","exit","quit"]):
                    try:
                        addressCounter = first_pass.par(line, addressCounter)
                        imc=asm.parse(line)
                        prcs.processline(imc)
                    except:
                        print("Error thrown")
                else:
                    run=False

        else:
            if(output_filename==None):
                with open(filename, "r") as f:
                    lc=1
                    for line in f:
                        print("->line "+str(lc))
                        try:
                            if(line!="\n"):
                                addressCounter = first_pass.par(line, addressCounter)
                                imc=asm.parse(line)
                                prcs.processline(imc)
                        except Exception as e:
                            print("Syntax Error at line: "+str(lc)+": "+str(line)+"\n"+str(e))
                            break
                        lc+=1
            else:
                with open(filename,"r") as f:
                    lc=1
                    fw=open(output_filename,"w")
                    for line in f:
                        print("->line "+str(lc))
                        try:
                            if(line!="\n"):
                                addressCounter = first_pass.par(line, addressCounter)
                                imc=asm.parse(line)
                                fw.write(imc)
                                prcs.processline(imc)
                        except:
                            print("Syntax Error at line: "+str(lc))
                            break
                        lc+=1

def main():
    parser=argparse.ArgumentParser(description="POWERsim V0.15. Simulates reduced POWER ISA.\nModes:\n\n\t-m\toperation mode\n\t-i\tinput file\n\t-o\toutput file\n")
    parser.add_argument("-i","--input",help="Input file" ,dest="input", type=str)
    parser.add_argument("-o","--output",help="Output file" ,dest="output", type=str)
    parser.add_argument("-m","--mode",required=True,help="POWERsim operational mode",dest="mode",type=str)
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__=="__main__":
	main()
