class Graph:
    def __init__(self):
        self.numberofNodes=0
        self.adjacencylist={}
    def addvertex(self,node):
        self.adjacencylist[node]=[]
        self.numberofNodes+=1
    def addedge(self,node1,node2):
        self.adjacencylist[node1].append(node2)
        self.adjacencylist[node2].append(node1)
    def showconnection(self):
        for i,j in self.adjacencylist.items():
            print(f"{i}is connected{' '.join(j)}")
mygraph=Graph()
mygraph.addvertex('0')
mygraph.addvertex('1')
mygraph.addvertex('2')
mygraph.addvertex('3')
mygraph.addedge('0','2')
mygraph.addedge('2','1')
mygraph.addedge('2','3')
mygraph.addedge('1','3')
mygraph.showconnection()