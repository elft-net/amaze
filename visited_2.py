class BSTNode:
    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

        if not self.val:
            return False

        if self.val == val:
            return True

        if val < self.val:
            if self.left:
                return self.left.exists(val)
            return False

        if self.right:
            return self.right.exists(val)
        return False

    def postorder(self, visited):
        visited = []
        if self.left:
            self.left.postorder(visited)

        if self.right:
            self.right.postorder(visited)

        if self.val:
            visited.append(self.val)

        return visited

    def inorder(self, visited):
        if self.left:
            self.left.inorder(visited)
        if self.val:    
            visited.append(self.val)
        if self.right:
            self.right.inorder(visited)
        return visited



    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

