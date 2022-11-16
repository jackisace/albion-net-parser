

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

files = ["stillOnHorse.txt","stillOffHorse.txt",  "movingOnHorse.txt", "movingOffHorse.txt", "allOnMyOwn.txt"]

for file in files:

    #print("\n\n" + file + "\n")
    print()
    print()

    with open(file) as f:

        
        raw = f.readlines()
    
    
    mid = round(len(raw) / 2)
    step = 30
    numLines = 10
    lineCount = 0
    raw = raw[mid+step:]


    for line in raw:
        if line[0] == '5':
            packet = "OUT"
            continue
        else:
            packet = "IN"
            #continue
            
        lineCount += 1
        if lineCount > numLines:
            break
        
        prepSt += file + "  \t"


        #pos = 24
        #showVar(line, 16)
        #showVar(line, 8)
        showVar(line, 4)
        showVar(line, 4)
        showVar(line, 4)
        showVar(line, 4)
        showVar(line, 4)
        showVar(line, 4)
        #showVar(line, 16)
        #showVar(line, 16)
        showVar(line, 4)
        showVar(line, 4)
        showVar(line, 16)
        showVar(line, 16)
        showVar(line, 4)
        showVar(line, 4)
        #showVar(line, 16)
        #showVar(line, 16)
        #showVar(line, 4)
        #showVar(line, 4)
        #showVar(line, 16)
        #showVar(line, 16)
        #showVar(line, 4)
        #showVar(line, 4)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 4)
        #showVar(line, 4)
        #showVar(line, 4)
        #showVar(line, 4)
        #showVar(line, 4)
        #showVar(line, 4)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 4)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 4)
        #showVar(line, 4)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)
        #showVar(line, 8)

        

        



        
        print(prepSt)
        prepSt = ""
        pos = 0
        
