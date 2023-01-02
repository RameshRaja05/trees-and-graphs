class AvltreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 1


class Avltree:
    def __init__(self):
        self.root = None

    def heightcalc(self, root):
        if not root:
            return 0
        return root.height

    def balancefactor(self, root):
        if not root:
            return 0
        else:
            return self.heightcalc(root.left)-self.heightcalc(root.right)

    def rightrotate(self, a):
        b = a.left
        c = b.right
        b.right = a
        a.left = c
        a.height = max(self.heightcalc(a.left)-self.heightcalc(a.right))
        b.height = max(self.heightcalc(b.left)-self.heightcalc(b.right))
        return b

    def leftrotate(self, a):
        b = a.right
        c = b.left
        b.left = a
        a.right = c
        a.height = max(self.heightcalc(a.left)-self.heightcalc(a.right))
        b.height = max(self.heightcalc(b.left)-self.heightcalc(b.right))
        return b

    def insert(self, value):
        if not self.root:
            self.root = AvltreeNode(value)
        else:
            return self._insert(self.root, value)

    def _insert(self, currentnode, value):
        if currentnode.value < value:
            if (currentnode.right == None):
                currentnode.right = AvltreeNode(value)
            else:
                return self._insert(currentnode.right, value)
        elif currentnode.value > value:
            if currentnode.left != None:
                currentnode.left = AvltreeNode(value)
            else:
                return self._insert(currentnode.left, value)
        currentnode.height = max(self.heightcalc(
            currentnode.left), self.heightcalc(currentnode.right))
        balance = self.balancefactor(currentnode)
        # ll insertion if value is less than left value this means right rotation
        # Case 1 - left left
        if balance > 1 and value < currentnode.left:
            return self.rightrotate(currentnode)
        #case2-right right
        if balance < -1 and value > currentnode.right.value:
            return self.leftrotate(currentnode)
        # # Case 3 - Left Right
        if balance > 1 and value > currentnode.left.value:
            currentnode.left = self.leftrotate(currentnode)
            return self.rightrotate(currentnode)
         # Case 4 - Right Left
        if balance < -1 and value < currentnode.right.value:
            currentnode.right = self.rightrotate(currentnode)
            return self.leftrotate(currentnode)
        return root
    def preOrder(self, root):
 
        if not root:
            return
 
        print("{0} ".format(root.value), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


myavl=Avltree()
root=None
root=myavl.insert(20)
root=myavl.insert(30)
root=myavl.insert(40)
root=myavl.insert(50)
myavl.preOrder(root)