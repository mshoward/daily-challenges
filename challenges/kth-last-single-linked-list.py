"""
Write a function kth_to_last_node() that takes an integer kk and the head_node of a singly-linked list, and returns the kkth to last node in the list.
"""

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

def kth_to_last_node(kk, head):
    def list_length(list_node, length):
        if (list_node == None):
            return length
        else:
            return list_length(list_node.next, length + 1)
    # The following solution came to mind as soon as
    # the solution on the website said something about "a stick k nodes wide"
    # using two references means the number of node access requests is the exact
    # same.  Caching strategies affect performance outcomes.
    def iterative_single_pass_solution(kk, head):
        kk_behind = head
        current = head
        for i in range(kk):
            if (current != None):
                current = current.next
            else:
                return None
        print(current.value)
        while(current != None):
            kk_behind = kk_behind.next
            current = current.next
        return kk_behind
    
    #head_length = list_length(head, 0)
    #iter_count = head_length - kk
    #for i in range(iter_count):
    #    head = head.next
    #return head
    return iterative_single_pass_solution(kk, head)


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print(kth_to_last_node(2, a).value)
# returns the node with value "Devil's Food" (the 2nd to last node)


