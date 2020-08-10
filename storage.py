class Storage(object):

    def lock(self,key):
        if not self.locked: #boolean for whether database is locked or not. Run code below if false (not locked).
            portalocker.lock(self._f, portalocker.LOCK_EX)
            self.locked = True
            return True
        else:
            return False