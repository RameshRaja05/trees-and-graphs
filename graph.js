class Graph{
    constructor(){
        this.adjacencylist={};
        this.numofnodes=0
    }
    addvertex(node){
        this.adjacencylist[node]=[]
        this.numofnodes+=1
    }
    addedge(node1,node2){
        this.adjacencylist[node1].push(node2)
        this.adjacencylist[node2].push(node1)
    }
    showconnection(){
        Object.entries(this.adjacencylist).forEach(([element1,element2])=>{
            console.log(`${element1} is connected to ${element2.join(' ')}`)
            
        });
    }
}
mygraph=new Graph()
mygraph.addvertex('0')
mygraph.addvertex('1')
mygraph.addvertex('2')
mygraph.addvertex('3')
mygraph.addedge('0','2')
mygraph.addedge('2','3')
mygraph.addedge('2','1')
mygraph.addedge('1','3')
mygraph.showconnection()
console.log(mygraph)