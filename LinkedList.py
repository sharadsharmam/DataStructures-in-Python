# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 06:38:21 2019

@author: sharad sharma
"""


class LinkedList:
    
    def __init__(self):
        self.head = None

    def add(self,data):
        if self.head == None:
            temp = LinkedListNode(data)
            self.head = temp
        else:
            currNode = self.head
            while(currNode.next != None):
                currNode = currNode.next
            temp = LinkedListNode(data)
            currNode.next = temp
            
    def addAtIndex(self,index,data):
        if self.head == None and index==0:
            temp = LinkedListNode(data)
            self.head = temp
        elif self.head == None and index>0:
            print("IndexOutOfBound")
            print("Task Unsuccesful")
        else:
            currNode, i = self.head, 0
            while(i<index-1):
                if currNode.next == None:
                    print("IndexOutOfBound")
                    print("Task Unsuccesful")
                    return
                else:
                    currNode = currNode.next
                    i += 1
            temp = LinkedListNode(data)
            temp.next = currNode.next
            currNode.next = temp
    
    def addFirst(self,data):
        temp = LinkedListNode(data)
        if self.head != None:
            temp.next = self.head
        self.head = temp
        
            
    
    def printLinkedList(self):
        currNode = self.head
        if(currNode == None):
            print('None')
        else:
            while(currNode!=None):
                print(currNode.val, '-->',end=' ')
                currNode = currNode.next
            print('None')

    def clear(self):
        self.head = None
    
    def contains(self, data):
        if self.head==None:
            print("LinkedList is empty")
            return False
        currNode = self.head
        while(currNode != None):
            if currNode.val == data:
                return True
            currNode=currNode.next
        return False
    
    def removeAtIndex(self, index):
        if self.head==None:
            print("LinkedList is empty")
            return
        elif index == 0:
            temp = self.head.val
            self.head = self.head.next
            return temp
        else:
            currNode, i = self.head, 0
            while(i<index-1):
                if currNode.next == None:
                    print("IndexOutOfBound")
                    return
                currNode = currNode.next
                i += 1
            if currNode.next == None:
                print("IndexOutOfBound")
                return
            temp = currNode.next.val
            currNode.next = currNode.next.next
            return temp
        
    def indexOf(self, data):
        if self.head == None:
            return -1
        currNode, i = self.head, 0
        while(currNode != None):
            if currNode.val == data:
                return i
            currNode = currNode.next
            i += 1
            
    def set(self, index, data):
        if self.isEmpty():
            print("LinkedList is Empty")
        currNode, i = self.head, 0
        while(i<index):
            if currNode.next == None:
                print("IndexOutOfBound")
                return
            currNode = currNode.next
            i += 1
        currNode.val = data
        
    def size(self):
        if self.isEmpty():
            return 0
        currNode, i = self.head, 1
        while(currNode.next!=None):
            currNode = currNode.next
            i += 1
        return i
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
class LinkedListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None

















'''
ll1 = LinkedList()
ll1.add(93)
ll1.add(44)
ll1.add(65)
ll1.add(28)
ll1.add(35)
ll1.add(82)
ll1.add(13)
ll1.add(24)
ll1.addAtIndex(5,77)
ll1.addFirst(27)
ll1.printLinkedList()
print(ll1.removeAtIndex(2))
ll1.printLinkedList()
print(ll1.contains(48))
print(ll1.indexOf(13))
ll1.set(4, 101)
print(ll1.size())
ll1.printLinkedList()
ll1.clear()
ll1.printLinkedList()
'''