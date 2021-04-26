# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         Seongyeon Nah(Ethan)
# ASSIGNMENT:   Technical HW: Stacks & Queues

from Queue import Queue

# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty
def count_longest(q):
    
    res=1
    max_res=0

    
    temp=q.deq()
    while not q.is_empty(): 
      temp1=q.deq()
      if(temp==temp1):
        res=res+1
      else:
        if (res>max_res):
          max_res=res
        temp=temp1
        res=1 

    if res >max_res:
      max_res=res     

    
        

    return max_res

def main():
    print("out 2:", count_longest( Queue( [ l for l in "hello" ] ) ))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee"])))
    print("out 4:",count_longest(Queue([ ])))
    


# Don't run main on import
if __name__ == "__main__":
    main()

