# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:19:35 2019

@author: sharad sharma
"""

class llStack:
    def __init__(self,stackLimit):
        self.head = None
        self.limit = stackLimit
        
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def isFull(self):
        currNode = self.head
        count=0
        while currNode!=None:
            count += 1
            currNode = currNode.next
        if count<self.limit:
            return False
        else:
            return True
        
    def printStack(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        currNode = self.head
        while(currNode != None):
            print( "<--", currNode.val, end=' ')
            currNode = currNode.next
        print("Bottom")
    
    def changeLimit(self, newlimit):
        self.limit = newlimit
    
    def push(self, data):
        if self.isFull():
            print("StackOverFlow")
            return
        tempNode = StackNode(data)
        if ~self.isEmpty():
            tempNode.next = self.head
        self.head = tempNode
    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        temp = self.head.val
        self.head = self.head.next
        return temp
    
    def peek(self):
        if self.isEmpty():
            return
        return self.head.val
    
    def contains(self,data):
        if self.isEmpty():
            return False
        currNode = self.head
        while currNode!=None:
            if currNode.val == data:
                return True
            currNode = currNode.next
        return False

            
class StackNode:
    def __init__(self, data):
        self.val = data
        self.next = None
        
        
        
'''        
st = llStack(5)
st.push(17)
st.printStack()
st.push(10)
st.printStack()
st.push(21)
st.printStack()
st.push(43)
st.printStack()
st.push(24)
st.printStack()
st.push(39)
st.changeLimit(10)
st.push(67)
st.printStack()
st.push(9)
st.printStack()
st.push(24)
st.printStack()
st.push(14)
st.printStack()
st.push(36)
st.printStack()
print(st.isFull())
st.push(44)
st.printStack()
st.pop()
st.printStack()
'''