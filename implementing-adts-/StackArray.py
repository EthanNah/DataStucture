# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: Stack-Array
#
# NAME:         Seongyeon Nah(Ethan)
# ASSIGNMENT:   Technical HW: Implementing ADTs

class StackArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.top = -1

    def peek(self):
        # FIXME

        return self.array[self.top]

    def pop(self):
        # FIXME
        if self.is_empty():
          return None
        else:
          return self.array[self.top]
        return

    def push(self, data=None):
       #해보기
      
      self.top = self.top + 1
      
      self.array.append(data)
      


      return

    def print(self):
        for i in range(self.top, -1, -1):
            print(self.array[i], "=>", end=" ")
        print("NULL")

    def is_empty(self):
        # FIXME
        if len(self.array)==0:
          return True
        else:
          return False
        return

    def is_full(self):
        return self.top == len(self.array) - 1

    def clear(self):
        # FIXME

        if self.is_empty():
          self.array=[]
        return

    def size(self):
        return self.top + 1


def main():
    s = StackArray()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 10):
        s.push(i)
    s.print()
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()

