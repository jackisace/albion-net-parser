

pos = 0
prepSt = ""

def prepString(st):
    global prepSt
    prepSt += st
    prepSt += "    "


def showVar(st, sizePos):
    global pos
    if pos+sizePos > len(st):
        return
    prepString(st[pos:pos+sizePos])
    pos += sizePos

files = ["stillOnHorse.txt","stillOffHorse.txt",  "movingOnHorse.txt", "movingOffHorse.txt"]

for file in files:

    #print("\n\n" + file + "\n")
    print()

    with open(file) as f:

        
        raw = f.readlines()
    
    
    mid = round(len(raw) / 2)
    step = 5
    numLines = 50
    raw = raw[mid+step : mid+numLines+step]


    for line in raw:
        if line[0] == '5':
            packet = "OUT"
            #continue
        else:
            packet = "IN"
            continue
        
        prepSt += file + "  \t"


        showVar(line, 8)
        showVar(line, 8)
        showVar(line, 8)
        showVar(line, 8)
        showVar(line, 8)
        showVar(line, 8)
        showVar(line, 4)
        showVar(line, 4)
        showVar(line, 4)
        showVar(line, 4)
        showVar(line, 4)
        showVar(line, 4)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 4)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)

        

        



        
        print(prepSt)
        prepSt = ""
        pos = 0
        
