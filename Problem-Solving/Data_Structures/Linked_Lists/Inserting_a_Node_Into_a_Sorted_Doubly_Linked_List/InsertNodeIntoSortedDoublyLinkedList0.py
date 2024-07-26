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

def sortedInsert(llist: DoublyLinkedListNode, data: int) -> DoublyLinkedListNode:
    length = 0
    curr = llist
    
    while (curr):    # Determine size of the Doubly Linked List
        length += 1
        curr = curr.next
    
    if (length == 0 or not llist):    # Empty Doubly Linked List: NULL <- _ -> NULL
        llist = DoublyLinkedListNode(data)
        return llist
    elif (length == 1 or (llist.prev is None and llist.next is None)):    # Single Element Doubly Linked List: NULL <- x -> NULL
        new_node = DoublyLinkedListNode(data)
        
        if (llist.data < data):    # Attach at tail
            llist.next = new_node
            new_node.prev = llist
            return (llist)    # old head stays the same
        elif (llist.data > data):    # Attach before head
            new_node.next = llist
            llist.prev = new_node
            return (new_node)     # new head
    else:    # Binary Doubly Linked List and others: NULL <- x -><- y -> NULL
        curr2 = llist
        new_node = DoublyLinkedListNode(data)
        
        if (curr2.data >= data):    # Attach before head
            new_node.next = llist
            llist.prev = new_node
            return (new_node)
                
        while (curr2 and curr2.next):
            if (curr2.data <= data <= curr2.next.data):    # Attach between head and tail
                old_node = curr2.next    # Store chain of nodes before inserting new node
                curr2.next = new_node
                new_node.prev = curr2
                new_node.next = old_node
                old_node.prev = curr2
                return (llist)
            curr2 = curr2.next
            
        if (curr2.data <= data):    # Attach at tail
            curr2.next = new_node
            new_node.prev = curr2
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
