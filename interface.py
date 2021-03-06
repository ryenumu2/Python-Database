from storage import PersistentStorage
from binary_tree import BinaryTree
class DBDB(object):

    def __init__(self,f):
        self._SSDstorage = PersistentStorage(f)
        self._tree = BinaryTree(self._SSDstorage) 
        #PersistentStorage class allocated to attribute 'SSDstorage', which is then stored in the Binary Tree

    def __getitem__(self, key):
        self._assert_not_closed() 
        return self._tree.get(key) #if file still open, return db[key], or the corresponding value for the key passed in
        #.get() is defined in logical.py
        #if returns False, _SSDstorage is already locked 
    
    def _assert_not_closed(self):
        if self._SSDstorage.closed: #f.close() will close an open file, while .closed returns a boolean for whether the file is closed or not
            raise ValueError('Error: Database closed.')
    
    