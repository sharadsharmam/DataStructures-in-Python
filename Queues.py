# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:07:21 2019

@author: sharad sharma
"""

class Queue:
    
    def __init__(self, queueLimit):
        self.head = None
        self.tail = None
        self.limit = queueLimit
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def isFull(self):
        if self.isEmpty():
            return False
        currNode = self.head
        count=0
        while(currNode != None):
            count += 1
            currNode = currNode.next
        if count<self.limit:
            return False
        else:
            return True
        
    def enqueue(self, data):
        if self.isFull():
            print("QueueOverFlow")
            return
        tempNode = queueNode(data)
        if self.isEmpty():
            self.tail = tempNode
        else:
            tempNode.next = self.head
            self.head.prev = tempNode 
        self.head = tempNode
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        temp = self.tail.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return temp
    
    def printQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        currNode = self.head
        while(currNode!=None):
            print("<--",currNode.val, end=" ")
            currNode = currNode.next
        print("\n")
    
    def changeLimit(self, newLimit):
        self.limit = newLimit
        
class queueNode:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None








'''
qu = Queue(5)
qu.enqueue(1)
qu.printQueue()
qu.enqueue(2)
qu.printQueue()
qu.enqueue(3)
qu.printQueue()
qu.enqueue(4)
qu.printQueue()
print(qu.dequeue())
qu.printQueue()
qu.enqueue(5)
qu.printQueue()
'''