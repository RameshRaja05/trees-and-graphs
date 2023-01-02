class Node{
    constructor(value){
        this.value=value
        this.rightchild=null
        this.leftchild=null
        this.parent=null
    }
}
class bst{
    constructor(){
        this.root=null
    }
    insert(value){
        if(!this.root){
            this.root=new Node(value)
        }
        else{
            this._insert(value,this.root)
        }
    }
    _insert(value,currentnode){
        if(value<currentnode.value){
            if(currentnode.leftchild==null){
                currentnode.leftchild=new Node(value)
                currentnode.leftchild.parent=currentnode
            }
            else{
                this._insert(value,currentnode.leftchild)
            }
        }
        else if(value>currentnode.value){
            if(currentnode.rightchild===null){
                currentnode.rightchild=new Node(value)
                currentnode.rightchild.parent=currentnode
            }
            else{
                this._insert(value,currentnode.rightchild)
            }
        }
    }
    search(value){
        if(this.root!=null){
            
            return this._search(value,this.root)
        }
        else{
            return false
        }
    }
    _search(value,currentnode){
        if(value==currentnode.value){
            return currentnode
        }
        else if(value>currentnode.value &&currentnode.rightchild!=null){
            return this._search(value,currentnode.rightchild)
        }
        else if(value<currentnode.value && currentnode.leftchild!=null){
            return this._search(value,currentnode.leftchild)
        }
        return false
    }
    delete_value(value){
        return this.delete_node(this.search(value))
    }
    delete_node(node){
        if (node==null){
            return undefined
        }
        else{
            let node_parent=node.parent
            let node_children=this.numofnodes(node)
            if(node_children===0){
                if(node_parent!=null){
                    if(node_parent.leftchild==node){
                        node_parent.leftchild=null
                    }
                    else{
                        node_parent.rightchild=null
                    }
                }
                else{
                    this.root=null
                }
            }
            else if(node_children===1){
                let child=node
                if(node.leftchild!=null){
                    child=node.leftchild
                }
                else{
                    child=node.rightchild
                }
            
            if(node_parent!=null){
                if(node===node_parent.leftchild){
                    node_parent.leftchild=child
                }
                else{
                    node_parent.rightchild=child
                }
            }
            else{
                this.root=child
            }
        }
        else if(node_children===2){
            let sucessor=this.min_value(node)
            node.value=sucessor.value
            this.delete_node(sucessor)
        }
        }
    }
    
    min_value(node){
        let currentnode=node
        while(currentnode.leftchild!=null){
            currentnode=currentnode.leftchild
        }
        return currentnode
    }
    numofnodes(node){
        let numofchild=0
        if(node.leftchild!=null){
            numofchild+=1

        }
        if(node.rightchild!=null){
            numofchild+=1
        }
        return numofchild
    }
    parentprint(){
        let currentnode=this.root
        while(currentnode.leftchild!=null){
            console.log(currentnode.parent)
            currentnode=currentnode.leftchild
        }
    }
}
function traverse(node) {
    const tree = { value: node.value };
    tree.left = node.leftchild === null ? null : traverse(node.leftchild);
    tree.right = node.rightchild === null ? null : traverse(node.rightchild);
    return tree;
  }
  


mybst=new bst()
mybst.insert(30)
mybst.insert(15)
mybst.insert(20)
mybst.insert(35)
mybst.insert(32)
mybst.insert(40)
console.log(JSON.stringify(traverse(mybst.root)))
mybst.delete_value(15)


