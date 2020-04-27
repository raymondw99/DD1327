# A list element that stores a value of type T.
class list_element(): 
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list():
    def  __init__(self):
        self.first = None # first element in list
        self.last  = None  # last element in list
        self.size  = 0     # number of elements in list
	
        
    def add_first(self,element):
        "Insert the given element at the befinning of this list."""
        try:
            new = list_element(element)
            if self.first != None:
                new.next = self.first
                self.size += 1
                self.first = new
            else:
                new.next = self.first
                self.size += 1
                self.first = new
                self.last = new
        except:
            return None
         
    def add_last(self,element):
        "Insert the given element at the end of this list."""
        try:
            new = list_element(element)
            if self.last != None:
                self.last.next = new
                self.size += 1
                self.last = new
            else:
                self.last.next = new
                self.size += 1
                self.last = new
                self.first = new
        except:
            return None

        
    def get_first(self):
        """Return the first element of this list."""
        try:
            return self.first.data
        except:
            return None
        
    def get_last(self):
        """Return the last elementof this list."""
        try:
            return self.last.data
        except:
            return None
        
    def get(self,index):
        """Return the element at the specific position in this list."""
        try:
            element = self.first
            for i in range(index-1):
                element = element.next
            return element.data
        except:
            return None

    def remove_first(self):
        """Remove and returns first element from this list."""
        if self.size == 0:
            return None
        elif self.size == 1:
            self.last = None
        elem = self.first
        self.first = self.first.next
        self.size -= 1
        return elem.data

    def clear(self):
        "Remove all elements from this list."""
        self.first = None
        self.last  = None
        self.size  = 0

    def size(self):
        "Return the number of elements in this list."""
        return self.size.data

    def string(self):
        """Return a string representation of this list."""
        """The elements are enclosed in square brackets ("[]")."""
        """Adjacent elements are separated by ","."""
        element = self.first
        if element != None:
            string = str(self.first.data)

            for i in range(self.size-1):
                element = element.next
                string += "," + str(element.data)
            lst = "[" + string + "]"
            return lst
        else:
            return None

    def healthy(self):
        "Checks whether the linked list is intact."""
        if self.size == 0:
            assert self.first == self.last == None
        elif self.size > 0:
            assert self.last.next == None
            
# Unit test
def main():
    T = linked_list()
    T.add_first("Raymond")
    T.add_last("Covid-19")
    T.add_first(1999)
    T.add_last("KTH")
    print(T.string())
    T.healthy()

    assert T.get_first() == 1999
    assert T.get_last() == "KTH"
    assert T.get(2) == "Raymond"
    assert T.get(3) == "Covid-19"
    assert T.size == 4
    T.healthy()

    T.add_last("Wuhan")
    T.add_first("DD1327")
    print(T.string())
    T.healthy()
    
    T.get_first()
    assert T.get_first() ==  "DD1327"
    assert T.get_first() == T.get(1)
    assert T.get_last() ==  "Wuhan"
    assert T.get_last() == T.get(6)
    assert T.size == 6
    T.healthy()

    del_elem = T.remove_first()
    print(T.string())
    assert del_elem != T.get(1)
    assert del_elem != T.get_first()
    assert T.size == 5
    T.healthy()

    T.clear()
    print(T.string())
    assert T.size == 0  
    T.healthy()

    # Issue test case 
    T.add_first("Raymond")
    assert T.remove_first() == "Raymond"
    assert T.size == 0 
    assert T.get_last() == T.get_first() == None
    T.healthy()
 
if __name__ == "__main__":
	main()
