global f,g
import time

def symtab_flush():
    f = open("symtab","w")
    f.close()

def memw_unfold():
    global f
    f = open("memory","w")

def regw_unfold():
    global g
    g = open("memorypad","w")

def memr_unfold():
    global f
    f = open("memory","r")

def regr_unfold():
    global g
    g = open("memorypad","r")

def mem_fold():
    global f
    f.close()

def reg_fold():
    global g
    g.close()

#Currently memory adresses are 16 bit

def init_memory():
    for i in range ((2**16)-1):
        f.write(str(i)+": "+"00000000\n")
    f.write(str(2**16-1)+": "+"00000000")

def init_mempad():
    for i in range(31):
        g.write("R"+str(i)+": 0000000000000000000000000000000000000000000000000000000000000000\n")
    g.write("R"+str(31)+": 0000000000000000000000000000000000000000000000000000000000000000")

def update_memory(loc, datum):
    if(loc<0 or loc> 65535):
        raise ValueError

    memr_unfold()

    mem_buffer=f.read().split("\n")
    pre_buffer=""
    buffer=str(loc)+": "+str(datum)
    post_buffer=""

    datum = "00000000"+datum
    datum = datum[-8:]

    mem_fold()

    for lc in range(loc):
        pre_buffer += mem_buffer[lc]+str("\n")

    for lc in range(loc+1,len(mem_buffer)):
        post_buffer += mem_buffer[lc]+str("\n")

    pre_buffer = pre_buffer.strip()
    post_buffer = post_buffer.strip()

    memw_unfold()

    f.write(pre_buffer+"\n"+buffer+"\n"+post_buffer)

    mem_fold()


def update_register(indx, datum):

    if(indx<0 or indx> 32):
        raise ValueError

    datum = "0000000000000000000000000000000000000000000000000000000000000000"+datum
    datum = datum[-64:]

    regr_unfold()

    reg_buffer=g.read().split("\n")
    pre_buffer=""
    buffer="R"+str(indx)+": "+str(datum)
    post_buffer=""

    reg_fold()

    for lc in range(indx):
        pre_buffer += reg_buffer[lc]+str("\n")

    for lc in range(indx+1,len(reg_buffer)):
        post_buffer += reg_buffer[lc]+str("\n")

    pre_buffer = pre_buffer.strip()
    post_buffer = post_buffer.strip()

    regw_unfold()

    g.write(pre_buffer+"\n"+buffer+"\n"+post_buffer)

    reg_fold()

def read_memory(loc):

    if(loc<0 or loc> 65535):
        raise ValueError

    memr_unfold()
    mem_buffer=f.read().split("\n")
    datum = mem_buffer[loc][-8:]
    mem_fold()

    return datum

def read_register(loc):

    if(loc<0 or loc> 32):
        raise ValueError

    regr_unfold()
    reg_buffer=g.read().split("\n")
    datum = reg_buffer[loc][-64:]
    mem_fold()

    return datum

def _init_():
    symtab_flush()
    memw_unfold()
    regw_unfold()
    init_memory()
    init_mempad()
    mem_fold()
    reg_fold()

#update_memory(3002,"0000001")
