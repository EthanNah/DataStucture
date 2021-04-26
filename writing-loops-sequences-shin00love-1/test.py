def mix(a, b):
  res=""
  if (len(a)==len(b)): 
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



print(mix("1234", "abcdefg"))