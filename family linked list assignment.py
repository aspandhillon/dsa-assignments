class Node(object):
def __init__(self,val):
self.value=val
self.next=None
self.prev=None

class DoublyLinkedList(object):
def __init__(self):
self.head=None
self.tail=None

def add_node(self, val):
new_node=Node(val)
#if there is no head, set new node as head
if self.head==None:
self.head= new_node
self.tail= new_node
else:
current_node = self.head

#continue traversing until next is none

while current_node.next !=None:
current_node= current_node.next

#if tail, add to end

current_node.next=new_node

#set prev pointer to current node

new_node.prev= current_node

#set new tail to new node

self.tail = new_node

def display(self):

#create empty list

value_list=[]
if self.head != None:
current_node = self.head

#start at head and check if next is not tail

while current_node.next != None:
 #add current node to list and traverse forward
value_list.append(current_node.value)
current_node = current_node.next
value_list.append(current_node.value)
print(value_list)
else:
print("No nodes")
return False

#making family linked list with family names and age

fll = DoublyLinkedList()
fll.add_node("Aspan")
fll.add_node(19)
fll.add_node("Tadbir")
fll.add_node(27)
fll.add_node("Tanvir")
fll.add_node(30)
fll.add_node("Aakanksha")
fll.add_node(19)
fll.display()



