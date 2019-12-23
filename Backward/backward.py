SPACE_SIZE = 3

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


def buildGraph(rules):
    graph = {}
    for antecedent, consequent in rules:
        if (consequent not in graph): graph[consequent] = []
        graph[consequent] += [antecedent]
    return(graph)

def printAnswer(depth, result):
    print((depth)*" "*SPACE_SIZE, "DONE", str(result))

def printResult(depth, result, target):
    print((depth)*" "*SPACE_SIZE, "DONE", target, str(result))

def backwards(graph, base, target, depth):
    print(depth*" "*SPACE_SIZE, "DOING", target)
    if (target in base and base[target] == True):
        printResult(depth + 1, True, target)
        return(True)
    if (target not in graph):
        printResult(depth + 1, False, target)
        return(False)
    for rule in graph[target]:
        for element in rule:
            if (backwards(graph, base, element, depth + 1)):
                base[element] = True
            else: break
        else:
            printResult(depth + 1, True, target)
            return(True)
    printResult(depth + 1, False, target)
    return(False)

rules = readRules()
base = readBase()
target = readTarget()

graph = buildGraph(rules)
print("\nGrafo de Inferencia:", graph)

result = backwards(graph, base, target, 0)
print(end="Resposta: ")
printAnswer(0, result)
