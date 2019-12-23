from Reading import *
SPACE_SIZE = 3

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
