from tkinter import *
import assembler as asm
import processor as proc

code=""
mode="asm"
view="memory"

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

def update_cout():
    if(code!=""):
        if(mode=="asm"):
            result = asm.parse(code)
        elif(mode=="proc"):
            pass
    consoleList.insert(END, ">> "+code)
    if(code!=""):
        consoleList.insert(END, result)
    consoleList.yview(END)

def read_code():
    global code
    code=e1.get()
    e1.delete(0,END)
    update_cout()

def readmemory():
    memoryList.delete(0,END)
    with open("memory","r") as f:
        content=f.read()
    content = content.split()
    for line in content:
        memoryList.insert(END, line)

def readregisters():
    registerList.delete(0,END)
    with open("memorypad","r") as f:
        content=f.read()
    content = content.split()
    for line in content:
        registerList.insert(END, line)

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

ps = Tk()

ps.title('POWERsim')
ps.geometry("1366x768")

##########################################MENU##############################################

menu = Menu(ps)
ps.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open')
filemenu.add_command(label='Exit')
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
helpmenu.add_command(label='Contact Us')

########################################CONSOLE VIEW########################################

consoleframe = Frame(ps, width=1000, height=650)
consoleframe.pack(side=LEFT, pady=(0,30))

outputframe = Frame(consoleframe, width=1000, height=600)
outputframe.pack(side= TOP)

l2 = Label(outputframe, text="CONSOLE OUTPUT", font="Arial 11 bold")
l2.pack(side=TOP, pady=(0,10))

inputframe = Frame(consoleframe, width=1000)
inputframe.pack(side=BOTTOM, pady=(30,10))

scrollbar = Scrollbar(outputframe)
scrollbar.pack(side=RIGHT, fill= Y)
consoleList = Listbox(outputframe, yscrollcommand = scrollbar.set, height=35, width=130)
consoleList.insert(END, "--------------POWERsim Console V0.6x------------")
consoleList.pack(side=LEFT,padx=(10,10))
clear=Button(outputframe, text="Clear", width=10,command=clear_console)
clear.pack(side=BOTTOM,padx=(10,0))

l1=Label(inputframe , text='>>')
l1.pack(side=LEFT)
e1=Entry(inputframe, width=135)
e1.pack(side=LEFT)
assemble=Button(inputframe, text="Assemble!", width=10, command=read_code)
assemble.pack(side=RIGHT, padx=(20,0))

########################################MEMORY VIEW#####################################


memoryframe = Frame(ps, width=300, height=400)
memoryframe.pack(side=TOP, pady=(28,0))

l4=Label(memoryframe, text='MEMORY VIEW', font="Arial 11 bold")
l4.pack(side=TOP, pady=(0,10))

memscroll = Scrollbar(memoryframe)
memscroll.pack(side=RIGHT, fill=Y)
memoryList = Listbox(memoryframe, yscrollcommand= memscroll.set, height= 17, width=60)

readmemory()
memoryList.pack(side=LEFT)

#######################REGISTER PAD VIEW#################################################

registerframe = Frame(ps, width=300, height=400)
registerframe.pack(side=TOP, pady=(20,0))

l5=Label(registerframe, text='REGISTERS VIEW', font="Arial 11 bold")
l5.pack(side=TOP, pady=(10,10))

regscroll = Scrollbar(registerframe)
regscroll.pack(side=RIGHT, fill=Y)
registerList = Listbox(registerframe, yscrollcommand= regscroll.set, height=11, width=60)

readregisters()
registerList.pack(side=LEFT)

#################################OP MODE#################################################

selectframe = Frame(ps, width=300, height=400)
selectframe.pack(side=TOP, pady=(30,0))

radioframe = Frame(selectframe, width=300, height=400)
radioframe.pack(side=LEFT)

opmod = IntVar()
Radiobutton(radioframe, text='Assemble Only', variable=opmod, value=1, command=mode_change).pack(side=TOP, anchor=W)
Radiobutton(radioframe, text='Process mode', variable=opmod, value=2, command=mode_change).pack(side=TOP, anchor=W)
viewmod = Button(selectframe, text="Symtab View", width=10, command=switchview)
viewmod.pack(side=RIGHT, padx=(100,10))

opmod.set(1)

ps.mainloop()
