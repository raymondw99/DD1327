def factorial(n):
  try: 
    if n == 0:
      return 1
    else:
      return n * factorial(n-1)
  except:
    return None

# Unit testing 
assert factorial(5)
assert factorial(0)
assert factorial(10)
assert not factorial(-3)
assert not factorial(4.5)
assert not factorial("KTH")
