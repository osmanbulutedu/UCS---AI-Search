# P2-2(20): Graph4 UCS by using MATRIX.  (Osman Bulut-001530539)



from queue import PriorityQueue

g4matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 8, 0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 2, 0],
            [0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 3, 9, 0, 0, 0, 1, 0, 0, 0]]

def ucs2(graph, source, destination):
    visited = set()
    expanded = []
    q = PriorityQueue()
    q.put((0, [source]))
    children = {}  # this line is special for matrix solution. I needed to pre-definition of a children dictionary
    while q:
        weight, vertex = q.get()
        current = vertex[-1]

        if current not in visited:
            visited.add(current)
            expanded.append(current)

            if current == destination:
                return vertex, expanded  # everthing is almost same with the code in the vertice list one so far except the pre-created empty children dictionary.

        # in this section, determining current node's children is different
        for index, locweight in enumerate(
                graph[current]):  # I'll obtain column number of the corresponding vertices
            if not locweight == 0:  # if the corresponding column number is zero it means there is no edge, if not, that means the number is the local weight.
                child = index  # we are adding each child into the children dictionary one by one
                children.update({child: locweight})

        # now we have children dictionary with node's letters and their corresponding weights. The rest will be same with the code in the vertice list one.
        for i in children:
            if i not in visited:  # we'll check out each child to see whether they were visited before. if not, we'll save their totalweight
                totalweight = weight + children[i]
                q.put((totalweight,
                       vertex + [i]))  # total weight of the corresponding branch. These branches are shown in documentation file.


solution, expanded = ucs2(g4matrix, 11, 6)


#I'm not sure about what format is wanted in the homework. Therefore I'll give both as numbers and characters)
print('The return path is as matrix index numbers ----> ', solution)
print("The expanded vertex list until reaching the destination is as matrix index numbers ---->", expanded)

# I'll need a map between numbers and characters.
maps = ['a','b','c','d','e','f','G','h','p','q','r','s']
pathchc=[]
visitedchc=[]
for i in list(solution):
    pathchc.append(maps[i])
for i in expanded:
    visitedchc.append(maps[i])

print('The return path is as characters ----> ', pathchc)
print("The expanded vertex list until reaching the destination is as characters ---->", visitedchc)