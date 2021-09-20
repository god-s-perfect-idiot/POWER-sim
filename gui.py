from tkinter import *
from tkinter.filedialog import askopenfilename
import assembler as asm
import processor as proc
import memory_manage as mem
import first_pass

addressCounter = 3000

mem._init_()

code=""
mode="asm"
view="memory"
membuffer=[]
regbuffer=[]

def mode_change():
    global mode
    c = opmod.get()
    if(c==1):
        mode="asm"
        assemble.config(text="Assemble!")
    elif(c==2):
        mode="proc"
        assemble.config(text="Process!")

def clear_console():
    global code
    consoleList.delete(0,END)
    code=""
    consoleList.insert(END, "-------------------------------POWERsim Console V0.7x----------------------------------")

def readmemory():
    global membuffer
    updates = []
    memoryList.delete(0,END)
    with open("memory","r") as f:
        content=f.read()
    content = content.split()
    for i in range(len(content)):
        if(len(membuffer)>0):
            if(content[i]!=membuffer[i]):
                updates.append(i)
    membuffer = content[:]
    for line in content:
        memoryList.insert(END, line)
    if(len(updates)>0):
        for update in updates:
            memoryList.itemconfig(update, {'bg':'green', 'fg':'white'})
        notimem.config(text=str(len(updates))+" rows changed.")
    else:
        notimem.config(text="")

def readregisters():
    global regbuffer
    updates = []
    registerList.delete(0,END)
    with open("memorypad","r") as f:
        content=f.read()
    content = content.split()
    for i in range(len(content)):
        if(len(regbuffer)>0):
            if(content[i]!=regbuffer[i]):
                updates.append(i)
    regbuffer = content[:]
    for line in content:
        registerList.insert(END, line)
    if(len(updates)>0):
        for update in updates:
            registerList.itemconfig(update, {'bg':'green', 'fg':'white'})
        notireg.config(text=str(len(updates))+" rows changed.")
    else:
        notireg.config(text="")

def readsymtab():
    memoryList.delete(0,END)
    with open("symtab","r") as f:
        content=f.read()
    content = content.split()
    for line in content:
        memoryList.insert(END, line)

def switchview():
    global view
    if(view=="memory"):
        l4.config(text="SYMBOL TABLE VIEW")
        viewmod.config(text="Memory View")
        view = "symtab"
        readsymtab()
    elif(view=="symtab"):
        l4.config(text="MEMORY VIEW")
        viewmod.config(text="Symtab View")
        view = "memory"
        readmemory()

def update_cout():
    if(code!=""):
        if(mode=="asm"):
            result = asm.parse(code)
        elif(mode=="proc"):
            imc=asm.parse(code)
            proc.processline(imc)
            result = imc+ " Assembled!"
    consoleList.insert(END, ">> "+code)
    if(code!=""):
        consoleList.insert(END, result)
    consoleList.yview(END)
    readmemory()
    readregisters()

def read_code():
    global code
    code=e1.get()
    e1.delete(0,END)
    update_cout()

def OpenFile():
    global addressCounter

    name = askopenfilename(filetypes =(("Assembly File", "*.s"),("All Files","*.*")),title = "Choose a file.")
    with open(name) as f:
        mem._init_()
        if(mode == "asm"):
            consoleList.insert(END,"Assembling source at: '"+name+"'")
            lc=1
            for line in f:
                consoleList.insert(END,"->line "+str(lc))
                try:
                    if(line!="\n"):
                        addressCounter = first_pass.par(line, addressCounter)
                        if(line.rstrip()!=""):
                            consoleList.insert(END, str(addressCounter)+": "+line.rstrip())
                        imc=asm.parse(line)
                        if(imc.rstrip()!=""):
                            consoleList.insert(END,"Assembly code:"+imc.strip())
                        else:
                            consoleList.insert(END, "Not(yet) an instruction!")
                except Exception as e:
                    consoleList.insert(END, "Syntax Error at line: "+str(lc)+": "+line+"\n"+str(e))

                    break
                lc+=1
        else:
            consoleList.insert(END,"Processing source at: '"+name+"'")
            lc=1
            for line in f:
                consoleList.insert(END, "->line "+str(lc))
                try:
                    if(line!="\n"):
                        addressCounter = first_pass.par(line, addressCounter)
                        imc=asm.parse(line)
                        proc.processline(imc)
                        if(imc.rstrip()!=""):
                            consoleList.insert(END, line+" assembled binary: "+imc)
                except Exception as e:
                    consoleList.insert(END, "Syntax Error at line: "+str(lc)+": "+line+"\n"+str(e))
                    break
                lc+=1
        readmemory()
        readregisters()


ps = Tk()
ps.state("zoomed")
ps.configure(background="white")
ps.title('POWERsim')
ps.geometry("1366x768")

##########################################MENU##############################################

menu = Menu(ps)
ps.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command=OpenFile)
filemenu.add_command(label='Exit', command=lambda:exit())
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
helpmenu.add_command(label='Contact Us')

########################################CONSOLE VIEW########################################

consoleframe = Frame(ps, width=1000, height=650, bg="white")
consoleframe.pack(side=LEFT, pady=(0,30))

outputframe = Frame(consoleframe, width=1000, height=600, bg="white")
outputframe.pack(side= TOP)

l2 = Label(outputframe, text="CONSOLE OUTPUT", font="Helvetica 10 bold", bg="white")
l2.pack(side=TOP, pady=(20,20))

inputframe = Frame(consoleframe, width=1000, bg="white")
inputframe.pack(side=BOTTOM, pady=(50,10))

scrollbar = Scrollbar(outputframe, bg="white")
scrollbar.pack(side=RIGHT, fill= Y)
consoleList = Listbox(outputframe, yscrollcommand = scrollbar.set, height=31, width=130 , bg="white")
consoleList.insert(END, "-------------------------------POWERsim Console V0.7x----------------------------------")
consoleList.pack(side=LEFT,padx=(10,10))
clear=Button(outputframe, text="Clear", font="Helvetica 9", width=10,command=clear_console, bg="white")
clear.pack(side=BOTTOM,padx=(10,0))

l1=Label(inputframe , text='>>', font="Helvetica 9", bg="white")
l1.pack(side=LEFT)
e1=Entry(inputframe, width=135, bg="white")
e1.pack(side=LEFT)
assemble=Button(inputframe, text="Assemble!", font="Helvetica 9", width=10, command=read_code, bg="white")
assemble.pack(side=RIGHT, padx=(20,0))

########################################MEMORY VIEW#####################################


memoryframe = Frame(ps, width=300, height=400, bg="white")
memoryframe.pack(side=TOP, pady=(28,0))

l4=Label(memoryframe, text='MEMORY VIEW', font="Helvetica 10 bold", bg="white", anchor=W)
l4.pack(side=TOP, fill='both')

notimem = Label(memoryframe, text="", font="Helvetica 9", bg="white", anchor=E)
notimem.pack(side=TOP, pady=(0,10), fill='both')

memscroll = Scrollbar(memoryframe, bg="white")
memscroll.pack(side=RIGHT, fill=Y)
memoryList = Listbox(memoryframe, yscrollcommand= memscroll.set, height= 15, width=60, bg="white")

readmemory()
memoryList.pack(side=LEFT)

#######################REGISTER PAD VIEW#################################################

registerframe = Frame(ps, width=300, height=400, bg="white")
registerframe.pack(side=TOP, pady=(20,0))

l5=Label(registerframe, text='REGISTERS VIEW', font="Helvetica 10 bold", bg="white", anchor=W)
l5.pack(side=TOP, pady=(10,0), fill='both')

notireg=Label(registerframe, text='', font="Helvetica 9", bg="white", anchor=E)
notireg.pack(side=TOP, pady=(0,10), fill='both')

regscroll = Scrollbar(registerframe)
regscroll.pack(side=RIGHT, fill=Y)
registerList = Listbox(registerframe, yscrollcommand= regscroll.set, height=11, width=60, bg="white")

readregisters()
registerList.pack(side=LEFT)

#################################OP MODE#################################################

selectframe = Frame(ps, width=300, height=400, bg="white")
selectframe.pack(side=TOP, pady=(30,0))

radioframe = Frame(selectframe, width=300, height=400, bg="white")
radioframe.pack(side=LEFT)

opmod = IntVar()
Radiobutton(radioframe, text='Assemble Only', font="Helvetica 9", variable=opmod, value=1, command=mode_change, bg="white").pack(side=TOP, anchor=W)
Radiobutton(radioframe, text='Process mode', font="Helvetica 9", variable=opmod, value=2, command=mode_change, bg="white").pack(side=TOP, anchor=W)
viewmod = Button(selectframe, text="Symtab View", font="Helvetica 9", width=10, command=switchview , bg="white")
viewmod.pack(side=RIGHT, padx=(100,10))

opmod.set(1)

ps.mainloop()
