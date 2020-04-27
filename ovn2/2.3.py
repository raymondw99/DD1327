class Node(): 
    def __init__(self,data):
        self.data  = data
        self.left  = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 1

    # Worst Case O(log2(N))
    def insert(self,data):
        """Insertion of new element."""
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    # Worst Case O(log2(N))
    def _insert(self,data,root):
        if data > root.data:
            if root.right == None:
                root.right = Node(data)
                self.size += 1
            else:
                self._insert(data,root.right)
        elif data < root.data:
            if root.left == None:
                root.left = Node(data)
                self.size += 1
            else:
                self._insert(data, root.left)
        elif data == root.data:
            print("Preexisting element")

    # Worst Case O(N)
    def string(self):
        """Printing string with all element arranged alphabetically."""
        if self.root == None:
            return None
        elif self.root != None:
            lst = []
            self._string(self.root,lst)
            print(lst)


    # Worst Case O(N)
    def _string(self,root,lst):
        if root != None:
            self._string(root.left, lst)
            lst.append(str(root.data))
            self._string(root.right,lst)
        elif root == None:
            return None
        return lst
  
    # Worst Case O(1)
    def size(self):
        """Returning number of elements in tree."""
        return self.size
                        	
#Unit testing
def main():
    tree = BinarySearchTree()
    tree.insert("Raymond")
    tree.insert("Wuhan")
    tree.string()
    print(tree.size)
    
    tree.insert("KTH")
    tree.insert("1999")
    tree.string()

    print(tree.size)

    tree.insert("Covid-19")
    tree.string()
    print(tree.size)

if __name__ == '__main__':
    main()
