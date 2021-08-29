class LinkList:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None
    
    class LinkListIterator:
        '''''
        将LinkList改造成可迭代
        '''''
        def __init__(self, node):
            self.node = node
        
        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration
    
    def __init__(self, iterable = None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)
        
    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s
    
    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)
    
    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False
    
    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<" + ",".join(map(str, self)) + ">>"



class HashTable:
    def __init__(self, size = 101): # size为关键字个数
        self.size = size
        self.T = [LinkList() for _ in range(size)]
    
    def h(self, k):
        return k % self.size
    
    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)

    def insert(self, k):
        if self.find(k):
            print("Duplicated Insert!")
        else:    
            i = self.h(k)
            self.T[i].append(k)
    
    def __repr__(self):
        return "<<" + ",".join(map(str, self.T)) + ">>" 

ht = HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(101)
ht.insert(2)
ht.insert(102)
ht.insert(100)
print(ht)
print(ht.find(4))