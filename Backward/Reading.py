def getAtom(atom):
    atom = atom.strip(' ')
    if (atom[0] != '!'): 
        return(atom)
    return('!' + atom[1:].strip(' '))

def readRules():
    print(input())
    rules = []
    while (True):
        line = input()
        if (line == "END"): 
            break
        print(line)
        antecedent, consequent = line.split("ENTAO")
        rules += [[[getAtom(s) for s in antecedent.split('AND')], getAtom(consequent)]]
    return(rules)

def readBase():
    print(input())
    base = {}
    while (True):
        line = input()
        if (line == "END"): 
            break
        print(line)
        for symbol in line.split(','):
            base[getAtom(symbol)] = True
    return(base)

def readTarget():
    print(input())
    target = ""
    while (True):
        line = input()
        if (line == "END"): 
            break
        print(line)
        target = line
    return(target)
