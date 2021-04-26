# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Seongyeon Nah(Ethan)
# ASSIGNMENT:   Technical HW: Stacks & Queues

from Queue import Queue
from Stack import Stack


# Return a new queue in reverse order
# Hint: can use a stack to help
def reverse(i): 
  
  q_new=Queue([]) 
  s_new=Stack([]) 
   
  while not i.is_empty(): 
   s_new.push(i.deq())  
   
  while not s_new.is_empty():
    q_new.enq(s_new.pop()) 
  
  return q_new

def main():
    q = Queue(list(range(1, 5)))
    q.print()
    print("reverse: ", end="")
    reverse(q).print()

# Don't run main on import
if __name__ == "__main__":
    main()