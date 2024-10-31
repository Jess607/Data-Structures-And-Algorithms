class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

    
class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while temp is not None:
            if new_node.value>temp.value:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right

            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left

            if new_node.value==temp.value:
                return False
            


bs=BinarySearchTree()
bs.insert(2)
bs.insert(1)
bs.insert(2)
bs.insert(70)
bs.insert(5)
print(bs.root.right.left.value)

