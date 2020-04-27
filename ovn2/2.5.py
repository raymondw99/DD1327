from random import*

class Node():
    def __init__(self, key, data):
        self.priority = random() # Random priority
        self.key = key           #Ascii index for first letter of word
        self.data = data
        self.left = None
        self.right = None

    def rotate_left(self):
        """If priority of y lower than x"""
        child = self.right
        self.right = child.left
        child.left = self
        self = child
        child = self.left
        return self

    def rotate_right(self):
        """If priority of x lower than y"""
        child = self.left
        self.left = child.right
        child.right = self
        self = child
        child = self.right
        return self

class Treap():
    def __init__(self):
        self.root = None
        self.size = 0
        
    # Worst Case O(log2(n))
    def insert(self, key):
        """Insertion of new element."""
        self.root = self._insert(self.root, ord(key[0]), data=key)
        self.size += 1
        
    # Worst Case O(log2(n))
    def _insert(self, node, key, data):
        """Insertion of new element."""
        if node == None:
            node = Node(key, data)
            return node
        
        if key > node.key:
            node.right = self._insert(node.right, key, data)
            if node.right.priority < node.priority:
                node = node.rotate_left()
                
        elif key < node.key:
            node.left = self._insert(node.left, key, data)
            if node.left.priority < node.priority:
                node = node.rotate_right()
                
        elif key == node.key:
            self.size -= 1
            
        return node

    # Worst Case O(n)
    def string(self):
        """Printing string with all elements arranged alphabetically."""
        if self.root == None:
            return None
        elif self.root != None:
            lst = []
            self._string(self.root,lst)
            print(lst)

    # Worst Case O(n)
    def _string(self,root,lst):
        if root != None:
            self._string(root.left, lst)
            lst.append(str(root.data))
            self._string(root.right,lst)
        elif root == None:
            return None
        return lst
    
    # Worst Case O(1)
    def _size(self):
        """Return size of the treap."""
        if self.root != None:
            return self.size
        else:
            return 0

# Unit testing 
def main():
    T1 = Treap()
    T2 = Treap()
    T1.insert('DD1327')
    assert T1._size() == 1
    T1.insert('Covid-19')
    assert T1._size() == 2
    T1.insert('KTH')
    assert T1._size() == 3
    T1.insert('Raymond')
    assert T1._size() == 4
    T1.insert('Wuhan')
    assert T1._size() == 5
    T1.string()

    T2.insert('Quarantine')
    T2.insert('Quarantine')
    assert T2._size() == 1
    T2.insert('Stockholm')
    T2.insert('Zoom')
    assert T2._size() == 3
    T2.insert('Zoom')
    T2.insert('2020')
    assert T2._size() == 4
    T2.string()

if __name__ == "__main__":  
    main()

