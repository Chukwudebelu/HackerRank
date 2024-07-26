#!/bin/python3

import os

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
    
def sortedInsert(llist: DoublyLinkedList, data: int):
    node = DoublyLinkedListNode(data)
    
    if (llist.data > data):  # Insert node at Head
        node.next, llist.prev = llist, node
        return (node)
        
    head = llist
    while (head):
        if (not head.next and head.data <= data):  # Insert node at Tail
            head.next, node.prev = node, head
            return (llist)
            
        if (data <= head.next.data):  # Insert node between Head & Tail nodes
            head.next.prev, node.next = node, head.next
            head.next, node.prev = node, head
            return (llist)
          
        head = head.next # next node
  
    return (llist)


if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
