# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Seongyeon Nah(Ethan)
# ASSIGNMENT:   Technical HW: Stacks & Queues

from Stack import Stack

# Returns True if the braces match,
# & False otherwise
def matcher(str):

  """  
 brackets=['[]','()','{}']   

 while any(x in str for x in brackets):
   for y in brackets:
     str=str.replace(y,'')

 return not str    

"""
  def comp(a,b):
    if a=="[" and b=="]":
      return True
    if a=="{" and b=="}":
      return True
    if a=="(" and b==")":
      return True  
    return False 

  s = Stack([])

  for l in str:
    if l =="{" or l=="[" or l=="(":
      s.push(l)
    elif  l =="}" or l=="]" or l==")":
      if s.is_empty():
        return False

      te=s.pop()

      if not comp(te,l):
        return False  

  if not s.is_empty():
    return False

  return True

  


 #brackets 제외하고 다 날려버리기
    #s.print
    
    
# return True

def main():
    print("matcher: ", matcher("[(Pretty)Ruth lee]"))

# Don't run main on import
if __name__ == "__main__":
    main()

