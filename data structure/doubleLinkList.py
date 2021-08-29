class Node:
    def __init__(self, item = None):
        self.item = item
        self.next = None
        self.prior = None

def createDoubleLinkList(li):
    '''''
    头插法创建双向链表
    '''''
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        head.prior = node
        node.next = head
        head = node
    return head

def print_DLL(head):
    '''''
    打印双向链表
    '''''
    while head:
        print(head.item, end=",")
        head = head.next

def insert(n1, np):
    np.next = n1.next
    n1.next.prior = np
    n1.next = np
    np.prior = n1

def delet(n1, p):
    n1.next = p.next
    p.next.prior = n1

    


head = createDoubleLinkList([1,2,3,4])
print_DLL(head)
print("\n")
print(head.next.prior.item)
