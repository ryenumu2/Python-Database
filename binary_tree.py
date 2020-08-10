from logic import LogicBase

class BinaryTree(LogicBase): #the binary search tree implementation: child nodes to the left are smaller than their parent nodes and child nodes to the right are larger than their parent nodes 
    #def __init__(self, node):
    #    self._pathTo(node) = None

    def _get(self,node,key): #iterate through the binary search tree by comparing the passed in key with the node that the BST is currently on. 
        while node != None:
            if key < node.key:
                node = self._pathTo(node.left_ref) 
            elif node.key < key:
                node = self._pathTo(node.right_ref)
            else:
                return self._pathTo(node.value_ref) 
        raise KeyError

    def _insert(self, node, key, value_ref): #recursively run this function definition to add a new node to the binary search tree
        if node == None:
            newest_node = BinaryNode()
