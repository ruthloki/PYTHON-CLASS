#linked list
#1.stored in memory
#2. fast access by index
#3. Myst traverse step by step
#4.flexivle size

#BASIC STRUCTURE
#data and structure of the next node


# {10|next}->[20|next]->[30|next]

#step by step logic
#create a class node
#store reference to next node

# class Node:
#     def __init__(self,data):
#         self.data=data #value
#         self.next=None

# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n1.next=n2
# n2.next=n3
# print(n1.data)
# print(n1.next.data)



#create Linkedlist class
#create head fointer
#head stores first node



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    
    def insert_begin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    
    def insert_end(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newNode

    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



li = LinkedList()

li.insert_begin(10)
li.insert_begin(5)
li.insert_begin(20)
li.insert_begin(30)

li.display()


# for i in range(5):
#     print("hellow")

# previous->newnode->nex t10,20,30,40,50


# 10->20->30->40->50

# 10-.20->30->new->40->50
# pos=2
# pos=4

# 2
# for i in range(2):
#     n1.next=n2.data
