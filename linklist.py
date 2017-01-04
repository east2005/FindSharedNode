#!/usr/bin/python
# -*- coding: utf-8 -*-



class findSameNode(Object):
    def __init__(self):
        self.visitor = dict()

    def updateVisitor(node):
        visitor[node.next] += 1 

link1 = linklist()
link2 = linklist()

finder = findSameNode()

for node in link1:
    finder.updateVisitor(node)

for node in link2:
    finder.updateVisitor(node)

if 2 in finder.visitor.values():
    print 'Fonud shared node'
else:
    print 'No shared node found'
