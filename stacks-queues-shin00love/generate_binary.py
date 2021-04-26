# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         Seongyeon Nah(Ethan)
# ASSIGNMENT:   Technical HW: Stacks & Queues

from Queue import Queue

# generate & return a queue of binary number strings from 1 to N
# front of queue begins @ '1', returns empty Queue otherwise
def generate_binary_numbers(N):
  numbers = Queue([])
  result= Queue([])

  numbers.enq('1')

  

  while result.size()<N:
      
      temp=numbers.front() 
     
      result.enq(temp) 

      numbers.enq(temp+ '0')
      numbers.enq(temp+ '1')

      numbers.deq()
     

  return result

def main():
    #generate_binary_numbers(0).print()
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()


# Don't run main on import
if __name__ == "__main__":
    main()

