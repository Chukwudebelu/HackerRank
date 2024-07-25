#!/bin/python3

import os

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#

def mergeLists(head1: SinglyLinkedListNode, head2: SinglyLinkedListNode) -> SinglyLinkedListNode:
    if (not head1 and not head2):  # Both head1 & head2 are empty linked lists
        return None
    elif (head1 and not head2):  # head2 is empty
        return head1
    elif (not head1 and head2):  # head1 is empty
        return head2
    else:   # head1 & head2 are not empty
        l = []
        
        while (head1):
            l += [head1.data]
            head1 = head1.next
            
        while (head2):
            l += [head2.data]
            head2 = head2.next
        l.sort()

        ll = SinglyLinkedList()
        for i in range(len(l)):
            if (i == 0):    # head node
                head_node_data = l[i]
                ll.insert_node(head_node_data)
            elif (1 <= i <= len(l)-1):   # other nodes
                ll.insert_node(l[i])
        return ll.head
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
