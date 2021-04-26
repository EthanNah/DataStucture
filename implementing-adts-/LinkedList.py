# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Linked List
#
# NAME:         Seongyeon Nah(Ethan)
# ASSIGNMENT:   Technical HW: Implementing ADTs

from Node import Node

class LinkedList(object):
    def __init__(self, list=None):
        self.head = None
        if list is not None:
            for item in list:
                self.add(item)

    def get_head(self):
        # FIXME
        return self.head.data

    def add(self, data):
        # FIXME
        
        New_node= Node(data) #data create  
        New_node.next_node= self.head
        self.head=New_node
       
        
        
        return  

    def search(self, data):
        # FIXME
        head = self.head
        while head != None:
          if head.data == data:
            return True
          head = head.next_node
        return False

    def delete(self, data):
        # FIXME
        head = self.head
        #head change
        if (head is not None):
          if (head.data==data):
            self.head = head.next_node
            head=None
            return
        #key data delete

        while head is not None:
          if head.data==data: 
           break 
          temp=head
          head=head.next_node
           
        
        if (head==None):
           return
        
        temp.next_node=head.next_node
        head = None
    
         

    def print(self):
        n = self.head
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        # FIXME
        head = self.head
        return head == None

    def clear(self):
        # FIXME
        self.head = None
        return

def main():
    l = list(range(1, 5))
    l.reverse()
    ll = LinkedList(l)
    ll.print()
    
    
    print("Search 4: ", ll.search(4))
    print("Search 5: ", ll.search(5))
    print("Delete 1: ", ll.delete(1))
    print("Delete 5: ", ll.delete(5))
    print("Delete 4: ", ll.delete(4))
    ll.print()
    print("Delete 1: ", ll.delete(1))
    
    ll.print()
    
# Don't run main on import
if __name__ == "__main__":
    main()

