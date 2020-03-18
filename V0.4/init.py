f = open("memory","w")
g = open("memorypad","w")

#Currently memory adresses are 16 bit

def init_memory():
    for i in range (2**16):
        f.write(str(i)+": "+"00000000\n")

def init_mempad():
    for i in range(32):
        g.write("R"+str(i)+": 00000000000000000000000000000000\n")

def _init_():
    global f,g
    init_memory()
    init_mempad()
    f.close()
    g.close()
