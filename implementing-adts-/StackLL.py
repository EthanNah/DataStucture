# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Stack-LL
#
# NAME:         Seongyeon Nah(Ethan)
# ASSIGNMENT:   Technical HW: Implementing ADTs

from Node import Node

class StackLL(object):
    def __init__(self, list=None):
        self.top = None
        if list is not None:
            for item in list:
                self.add(item)

    def peek(self):
        # FIXME

        if self.is_empty():
          return None
        else:
          return self.top.data

        return

    def pop(self):
        # FIXME
        if self.is_empty():
          return None
        else:
          popnode=self.top
          self.top=self.top.next_node
          popnode.next_node=None

          return popnode.data

        return

    def push(self, data=None):
        # FIXME

        if self.top==None:
          self.top=Node(data)
        else:
          new_node=Node(data)
          new_node.next_node=self.top
          self.top=new_node

          
        return

    def print(self):
        n = self.top
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        # FIXME
        if self.top==None:
          return True
        else:
          return False  
        

    def clear(self):
        # FIXME
      while self.top != None:
        
        self.top=self.top.next_node
        self.top=None

        return

def main():
    s = StackLL()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 7):
        s.push(i)
    
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())
    while not s.is_empty():
        print(s.pop())

# Don't run main on import
if __name__ == "__main__":
    main()

