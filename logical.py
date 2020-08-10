class LogicalBase(object):

    def get(self,key):
        if not self._SSDstorage.locked: #boolean for whether _storage is locked or not. Run code below if false (not locked).
            portalocker.lock(self._f, portalocker.LOCK_EX)
            self.locked = True
            return True
        else:
            return False