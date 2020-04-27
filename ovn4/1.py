import time

def pow(n):
    """Return 2**n, where n is a nonnegative integer."""
    if n == 0:              # T(0) = 1
        return 1                 
    x = pow(n//2)           # T(n) = 1+T(n/2)
    if n%2 == 0:
        return x*x
    return 2*x*x

def sum1(a):
    """Return the sum of the elements in the list a."""
    n = len(a)
    if n == 0:                                # T(0) = 1
        return 0
    if n == 1:                                # T(1) = 1
        return a[0]
    return sum1(a[:n//2]) + sum1(a[n//2:])    # T(n) = 2 + 2T(n/2)

def sum2(a):
    """Return the sum of the elements in the list a."""
    return _sum(a, 0, len(a)-1)      # T(n) =  1 + 2T(n/2)

def _sum(a, i, j):
    """Return the sum of the elements from a[i] to a[j]."""
    if i > j:                        # T(n) = 0 
        return 0
    if i == j:                       # T(n) = 1
        return a[i]
    mid = (i+j)//2
    return _sum(a, i, mid) + _sum(a, mid+1, j)

def elapsedtime(n,a,i):
    start = time.time()
    if i == 0:
        pow(n)
    elif i == 2:
        sum1(a)
    elif i == 3:
        sum2(a)      
    print(n, time.time() - start) # elapsed time

def lst(n):
    return list(range(1,n+1))


def powtime():
    elapsedtime(10, [], 0)
    elapsedtime(100, [], 0)
    elapsedtime(1000, [], 0)
    elapsedtime(10000, [], 0)
    elapsedtime(100000, [], 0)
    elapsedtime(1000000, [], 0)	

def sumtime(i):
    print("")
    elapsedtime(10, lst(10), i)
    elapsedtime(100, lst(100), i)
    elapsedtime(1000, lst(1000), i)
    elapsedtime(10000, lst(10000), i)
    elapsedtime(100000, lst(100000), i)
    elapsedtime(1000000, lst(1000000), i)

def main():
    powtime()
    sumtime(1)
    sumtime(2)

if __name__ == '__main__':
    main() 
