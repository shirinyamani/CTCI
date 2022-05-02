class linkedlist:
    def __init__(self,val):
        self.val = val
        self.next = None

    def addnode(self, val):
        if self.next is None:
            self.next = linkedlist(val)
        else:
            self.next.addnode(val)
