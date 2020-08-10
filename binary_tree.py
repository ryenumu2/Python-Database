from logic import LogicBase

class BinaryTree(LogicBase):
    def __init__(self, node):
        self._pathTo(node) = None

    def _get(self,node,key):
        while node != None:
            if key < node.key:
                node = self._pathTo(node.left_ref)
            elif node.key < key:
                node = self._pathTo(node.right_ref)
            else:
                return self._pathTo(node.value_ref)
        raise KeyError
