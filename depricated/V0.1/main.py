#! /usr/bin/env python3
import argparse
import assembler as asm

def run(args):
    filename = args.input # these match the "dest": dest="input"
    output_filename = args.output # from dest="output"
    if(filename==None):
        run=True
        print("\n-------------------------POWER Sim V0.1 Console----------------------\n")
        while(run):
            line=input(">>>")
            if(line not in ["quit()","q()","exit","quit"]):
                try:
                    asm.parse(line)
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
                        asm.parse(line)
                    except:
                        print("Syntax Error at line: "+str(lc))
                        break
                    #line=f.readline()[:-1]
                    lc+=1

def main():
    parser=argparse.ArgumentParser(description="Assemble Our Custom ISA.")
    parser.add_argument("-in",help="Input file" ,dest="input", type=str)
    parser.add_argument("-out",help="Output file" ,dest="output", type=str)
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__=="__main__":
	main()
