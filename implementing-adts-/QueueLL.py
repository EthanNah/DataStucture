# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: Queue-LL
#
# NAME:         Seongyeon Nah(Ethan)
# ASSIGNMENT:   Technical HW: Implementing ADTs

from Node import Node

class QueueLL(object):
    def __init__(self, list=None):
        self.front = None
        self.tail = None
        if list is not None:
            for item in list:
                self.enq(item)

    def get_front(self):
        # FIXME
        


        return self.front.data

    def get_tail(self):
        # FIXME
        return self.tail.data

    def deq(self):
        # FIXME
        if self.front == None:
          return None
        else:
          deq_node=self.front
          self.front= self.front.next_node
          deq_node.next_node=None
        
        return deq_node.data

    def enq(self, data=None):
        # FIXME
        if self.tail == None:
          self.front=Node(data)
          self.tail=self.front 
        else:
          self.tail.next_node =Node(data)
          self.tail=self.tail.next_node          


        return

    def print(self):
        n = self.front
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        # FIXME
        if self.front == None:
          return True
        else:
          return False
        

    def clear(self):
        # FIXME

        while self.front != None:
          head = self.front
          self.front=self.front.next_node
          head.next_node=None
        return


def main():
    s = QueueLL()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 7):
        s.enq(i)
    s.print()
    #print("Peek:", s.peek())
    print("Deq: ", s.deq())
    s.print()
    
    print("Is empty?", s.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()

