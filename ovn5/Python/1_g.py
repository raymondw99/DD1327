# Time complexity O(2^n) 
def p1(n):
  """Top down implementation"""
  """Calculates maximal revenue for 
     scarves of length n"""
  h = [0,2,5,6,9] # Prices
  x = 0 
  try:
    if n > 4:       # h[n] = 0 for n > 4
      h.extend([0 for i in range(n-4)])
    elif n == 0:
      return 0
    elif n < 0:
      return None
    for i in range(1,n+1): # if n > 0  
      x = max(x,h[i] + p1(n-i))
    return x # Maximal revenue
  except:
    return None

# Time complexity O(n^2) 
def p2(n):
  """Bottom up implementation"""
  """Calculates maximal revenue for 
     scarves of length n"""
  h = [0,2,5,6,9] # Prices 
  try:
    r = list(range(0,n+1)) # Array of length n 
    if n > 4:       # h[n] = 0 for n > 4
      h.extend([0 for i in range(n-4)])
    for i in range(1,n+1):
      x = 0
      for j in range(1,i+1):
        x = max(x,h[j] + r[i-j])
      r[i] = x
    return r[n] # Maxmimal revenue
  except:
    return None

# Unit testing
def output(p):
  print("Length Profit")
  for n in range(10):
    print("  " + str(n) + "      " + str(p(n)))
  print("")
  
def main():
    print("Time complexity O(2^n)")
    output(p1)
    print("Time complexity O(n^2)")
    output(p2)
    assert p1(3.2) == None
    assert p2(-4.5) == None
    
if __name__ == "__main__":
    main()
 
