# jab array ke ander memory ka allocation hota h vo contigous hota h
# LinkedList hume ek option provide kar sakta h kya ki hum runtime p memory allocation kar sakte h
# agar program chal rha hota h toh uss time if we need memory to store data so we can add in memory in runtime


# linkedList = hum normally ek block allocate karate h jisko NODE bola jata h
# then node ke do part hote h
# 1.isme information store hoti h  [ zaruri nhi ki value store karo ek objject bhi store kar sakte h jisme ki mainly sari information hoti h ]
# 2.isme hota h next wali memory ka address
# [i love u dishita]
# Pointer = it is a variable which points to a position / an address
# jaise blaock ke ander do partition h toh hum likhenge ki jaise plhe wale box ko humne Head bol diya jo ki define kar rha h ki humne plhe wale dubbe ki location ki toh hum likhenege ki Head.info  ya fir Head.next .


# SINGLYLINKEDLIST CODE

# in sabka coed jo h vo bahut bda h par dhere dhere samajh me aa rha h toh koi dikkat wali baat nhi h 
# INSERTION AT THE END
# class Node:
#     def __init__(self, info, next=None):
#         self.data = info
#         self.next = next


# class SinglyLinkedList:
#     def __init__(self, head=None):
#         self.head = head

#     def InsertAtEnd(self, value):
#         temp = Node(value)
#         if (self.head != None):
#             t1 = self.head
#             while (t1.next != None):
#                 t1 = t1.next
#             t1.next = temp
#         else:
#             self.head = temp

#     def printLL(self):
#         t1 = self.head
#         while (t1.next != None):
#             print(t1.data)
#             t1 = t1.next
#         print(t1.data)


# obj = SinglyLinkedList()
# obj.InsertAtEnd(10)
# obj.InsertAtEnd(20)
# obj.InsertAtEnd(30)
# obj.printLL()


# INSERTION AT THE BEGINNING

class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def InsertAtEnd(self, value):
        temp = Node(value)
        if (self.head != None):
            t1 = self.head
            while (t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def InsertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
        self.head = temp

    def printLL(self):
        t1 = self.head
        while (t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)


obj = SinglyLinkedList()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.InsertAtBeg(5)
obj.printLL()


# INSERTION IN THE MIDDLE AND TO SERCH AN ELEMENT 
