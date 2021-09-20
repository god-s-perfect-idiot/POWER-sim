#! /usr/bin/env python3
import argparse
import assembler as asm
import processor as prcs

def run(args):
    filename = args.input # these match the "dest": dest="input"
    output_filename = args.output # from dest="output"
    r_mode = args.mode
    if(r_mode=="asm"):
        if(filename==None):
            run=True
            print("\n-------------------------POWER Sim V0.1 Assembler Console----------------------\n")
            while(run):
                line=input(">>>")
                if(line not in ["quit()","q()","exit","quit"]):
                    try:
                        imc=asm.parse(line)
                        print(imc)
                    except:
                        print("Error thrown")
                else:
                    run=False
        else:
            if(output_filename==None):
                with open(filename, "r") as f:
                    lc=1
                    #line=f.readline()[:-1]
                    #while(line!=""):
                    for line in f:
                        print("\n->line "+str(lc)+"\n")
                        try:
                            imc=asm.parse(line)
                            print(asm.inst)
                            print(imc)
                        except:
                            print("Syntax Error at line: "+str(lc))
                            break
                        #line=f.readline()[:-1]
                        lc+=1
            else:
                with open(filename,"r") as f:
                    lc=1
                    fw=open(output_filename,"w")
                    #line=f.readline()[:-1]
                    #while(line!=""):
                    for line in f:
                        print("\n->line "+str(lc)+"\n")
                        try:
                            imc=asm.parse(line)
                            fw.write(imc)
                        except:
                            print("Syntax Error at line: "+str(lc))
                            break
                        #line=f.readline()[:-1]
                        lc+=1
    elif(r_mode=="proc"):
        if(filename==None):
            run=True
            print("\n-------------------------POWER Sim V0.1 Processor Console----------------------\n")
            while(run):
                line=input(">>>")
                if(line not in ["quit()","q()","exit","quit"]):
                    try:
                        imc=asm.parse(line)
                        prcs.processline(imc)
                    except:
                        print("Error thrown")
                else:
                    run=False


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
