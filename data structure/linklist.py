class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

def create_linklist(li):
    '''''
    尾插法创建链表
    '''''
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

def print_linklist(head):
    '''''
    打印链表
    '''''
    while head:
        print(head.item,end=",")
        head = head.next


def insert(n1, n2, np):
    np.next = n2
    n1.next = np

def delet(n1, np):
    n1.next = np.next


head = create_linklist([1,2,3])
print_linklist(head)
print("\n")
np = Node(10)
insert(head, head.next, np)
print_linklist(head)