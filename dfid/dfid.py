"""
matrix=[]


def dfidAlgo(matrix,depth,start,goal,n):
    #initialze the stack
    stack = []
    stack.append(start)
    print(stack)
    for i in range(n):
        #print all edges from start
        print(matrix[i][start-1])
        print(matrix[start-1][i])

print("\nplease enter the number of nodes:")
n = int(input())
print("\nplease eneter the graph(matrix):")
#for row i
for i in range(n):
    a = []
    #for column j
    for j in range(n):
        a.append(int(input("please etner the element:")))
        #matrix[][]=input("\nplease enter the weight between nodes"+str(i)+" and "+str(j))
    matrix.append(a)

#print the graph
print(matrix)
startNode= int(input("\nplease enter the start node:"))
endNode = int(input("\nplease enter the end node:"))
depth = int(input("\nplease enter the search depth:"))

dfidAlgo(matrix,depth,startNode,endNode,n)
"""
from colllections import defaultdict
class Graph:
    #constructor
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    #add edges
    def addEdge(self,u,v):
        self.graph[u].append(v)
    #DLS algo
    def DLS(self,src,target,maxDepth):
        if src == target: 
            return True
        if maxDepth<=0:
            return False
        for i in self.graph[src]:
            if(self.DLS(i,target,maxDepth-1)):
                return True
        return False
    #IDDFS
    def IDDFS(self,src,target,maxDepth):
        for i in range(maxDepth):
            print(self.graph)
            if(self.DLS(src,taget,i)):
                return True
        return False
    
noVertice = int(input("Please enter the number of vertices:"))
g = Graph(noVertice)
noEdges = int(input("\n"))
for i in range(1,noEdges-1):
    node_1 = int(input("\nPlease enter 1st node:"))
    node_2 = int(input("\nPlease enter 2nd node:"))
    g.addEdge(node_1,node_2)


target = int(input("\nplease enter your target node:"))
maxDepth = int(input("\nPlease eneter your maxDepth:"))
src = int(input("\nplease enter your source:"))

if g.IDDFS(src, target, maxDepth)==True:
    print("Target is reachable")
else:
    print("Target is not reachable")


#eval parameteres
#completeness
#output
#parameteres
