class LogicBase(object): #API for methods such as get and set, ensure storage isn't locked before proceeding

    def get(self,key): 
        if not self._SSDstorage.locked: #if boolean value '.locked' is False (not locked), refresh tree
            self._refresh_binary_tree_ref() 
        return self._get(self._pathTo(self.tree_view_ref), key)
        #only return 
    
    def _refresh_binary_tree_ref(self): #function definition that will refresh the binary tree with updated values on disc
        self._tree_view_ref = self.node_ref_class(address=self._SSDstorage.get_root_address())
    





