# NAME:         FIXME
# ASSIGNMENT:   FIXME

# Example
def hello_world():
    return "Hello!"

# 1
def squared_sum(array):
  res=0

  if array: 
    for k in array:
      res=res+ pow(k,2)

  return res

# 2 len(a)
def mix(a, b):

  res=""
  if(len(a)==len(b)): 
      for k in range(len(a)):
        res+=a[k]+b[k]   
  elif (len(a)>len(b)):
      for k in range(len(b)):  
          res+=a[k]+b[k] 
      res+=a[len(b):]  
  else:
        for k in range(len(a)):  
          res+=a[k]+b[k] 
        res+=b[len(a):]   

  return res

def main():
    print("squared sum: ", squared_sum([-3, 4]))
    print("mix:         ", mix("1234", "abcd") == "1a2b3c4d")
     
main()