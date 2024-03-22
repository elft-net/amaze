class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None

class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        nn = RBNode(val)
        nn.parent = None
        nn.red = True
        nn.left = self.nil
        nn.right = self.nil

        self.parent = None
        current = self.root

        while current != self.nil:
            self.parent = current
            if nn.val < current.val:
                current = current.left
            else:
                current = current.right

        nn.parent = self.parent
        if self.parent == None:
            self.root = nn
        elif nn.val < self.parent.val:
            self.parent.left = nn
        else:
            self.parent.right = nn
        
