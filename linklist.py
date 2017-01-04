#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value, next=0):
        self.data = value
        self.next = next
    
class Linklist(object):
    def __init__(self):
        self.head = 0

    def initialize(self, data):
        self.head = Node(data[0])
        tmp = self.head
        for v in data[1:]:
            node = Node(v)
            tmp.next = node
            tmp = tmp.next

link1 = Linklist()
link1.initialize(range(1,10))
link2 = Linklist()
link2.initialize(range(11,15))

node = link1.head
while True:
    if node.next == 0:
        break
    node = node.next

link1_tail = node
link1_tail.next = link2.head

# now link1 is a combination of link1 and link2
slow_p = fast_p = link1.head
while True:
    fast_p = fast_p.next.next
    slow_p = slow_p.next
    if fast_p == slow_p:
        print 'Fonud shared node'
        break
    if fast_p.next == 0:
        print 'No shared node found'
        break

