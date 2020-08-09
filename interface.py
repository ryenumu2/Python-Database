class DBDB(object):

    def __init__(self,f):
        self._SSDstorage = PersistentStorage(f)
        self._tree = BinaryTree(self._SSDstorage) 
        #PersistentStorage class allocated to attribute 'SSDstorage', which is then stored in the Binary Tree

    def __getitem__(self, key):
        self._assert_not_closed()
        return self._tree.get(key)
    
    def _assert_not_closed(self):
        if self._storage.closed: #f.close() will close an open file, while .closed returns a boolean for whether the file is closed or not
            raise ValueError('Error: Database closed.')
    
    