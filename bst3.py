class Node:
    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None
        self.parent = None


class Binaryst:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root==None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, currentnode):
        if (value < currentnode.value):
            if (currentnode.leftchild == None):
                currentnode.leftchild = Node(value)
                currentnode.leftchild.parent = currentnode
            else:
                self._insert(value, currentnode.leftchild)
        elif (value > currentnode.value):
            if (currentnode.rightchild == None):
                currentnode.rightchild = Node(value)
                currentnode.rightchild.parent = currentnode
            else:
                self._insert(value, currentnode.rightchild)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, currentnode):
        if currentnode.value == value:
            return True
        elif currentnode.value>value and currentnode.leftchild!=None:
            return self._search(value, currentnode.leftchild)
        elif currentnode.value<value and currentnode.rightchild!=None:
            return self._search(value, currentnode.rightchild)
        return False

    def delete_value(self, value):
        if (self.root is None):
            return None
        else:
            return self.delete_node(self.find(value))

    def delete_node(self, currentnode):
        def min_value(n):
            current = n
            while (current.leftchild is None):
                current = current.leftchild
            return current

        def numofchildren(n):
            noofchild = 0
            if n.leftchild != None:
                noofchild += 1
            if n.rightchild != None:
                noofchild += 1
            return noofchild
        node_parent = currentnode.parent
        noofchild = numofchildren(currentnode)
        if noofchild == 0:
            if node_parent != None:
                if currentnode == node_parent.leftchild:
                    node_parent.leftchild = None
                else:
                    node_parent.rightchild = None
            else:
                self.root
        elif noofchild == 1:
            if currentnode.leftchild != None:
                child = currentnode.leftchild
            else:
                child = currentnode.rightchild
            if node_parent != None:
                if currentnode == node_parent.leftchild:
                    node_parent.leftchild = child
                else:
                    node_parent.rightchild = child
        elif noofchild == 2:
            sucessor = min_value(currentnode)
            currentnode.value = sucessor.value
            self.delete_node(sucessor)

    def find(self, value):
        if (self.root != None):
            return self._find(value, self.root)
        else:
            return False

    def _find(self, value, currentnode):
        if (currentnode.value == value):
            return currentnode
        elif (currentnode.value > value and currentnode.leftchild!=None):
            return self._find(value, currentnode.leftchild)
        elif (currentnode.value < value and currentnode.rightchild!=None):
            return self._find(value, currentnode.rightchild)


mybst = Binaryst()
mybst.insert(30)
mybst.insert(20)
mybst.insert(35)
mybst.insert(25)
mybst.insert(40)
print(mybst.search(40))
mybst.delete_value(40)
print(mybst.search(40))
