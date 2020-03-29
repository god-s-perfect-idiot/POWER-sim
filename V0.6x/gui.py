def readmemory():
    with open("memory","r") as f:
        content=f.read()
    return content

def readregisters():
    with open("memorypad","r") as f:
        content=f.read()
    return content

from tkinter import *

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
consoleList = Listbox(outputframe, yscrollcommand = scrollbar.set, height=35, width=150)

for line in range(100):
    consoleList.insert(END, "This is console ouput line"+str(line))

consoleList.pack(side=LEFT)

l1=Label(inputframe , text='>>')
l1.pack(side=LEFT)
e1=Entry(inputframe, width=135)
e1.pack(side=LEFT)
assemble=Button(inputframe, text="Assemble!", width=10)
assemble.pack(side=RIGHT, padx=(20,0))

########################################MEMORY VIEW#####################################

content=readmemory().split()

memoryframe = Frame(ps, width=300, height=400)
memoryframe.pack(side=TOP, pady=(28,0))

l4=Label(memoryframe, text='MEMORY VIEW', font="Arial 11 bold")
l4.pack(side=TOP, pady=(0,10))

memscroll = Scrollbar(memoryframe)
memscroll.pack(side=RIGHT, fill=Y)
memoryList = Listbox(memoryframe, yscrollcommand= memscroll.set, height= 17, width=60)

for line in content:
    memoryList.insert(END, line)

memoryList.pack(side=LEFT)

#######################REGISTER PAD VIEW#################################################

regcontent = readregisters().split()

registerframe = Frame(ps, width=300, height=400)
registerframe.pack(side=TOP, pady=(20,0))

l5=Label(registerframe, text='REGISTERS VIEW', font="Arial 11 bold")
l5.pack(side=TOP, pady=(10,10))

regscroll = Scrollbar(registerframe)
regscroll.pack(side=RIGHT, fill=Y)
registerList = Listbox(registerframe, yscrollcommand= regscroll.set, height=11, width=60)

for line in regcontent:
    registerList.insert(END, line)

registerList.pack(side=LEFT)

#################################OP MODE#################################################

selectframe = Frame(ps, width=300, height=400)
selectframe.pack(side=TOP, pady=(30,0))

opmod = IntVar()
Radiobutton(selectframe, text='Assemble Only', variable=opmod, value=1).pack(side=TOP, anchor=W)
Radiobutton(selectframe, text='Process mode', variable=opmod, value=2).pack(side=TOP, anchor=W)


ps.mainloop()
