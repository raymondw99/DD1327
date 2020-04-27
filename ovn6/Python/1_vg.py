def p(n):
    """Calculates maximal revenue and its
    associated cuts for scarves of length n"""
    r = list(range(0,n+1)) # Array for revenue
    s = list(range(0,n+1)) # Array for cuts 
    h = [0,2,5,6,9]        # Prices
    r[0] = 0
    lst = []
    if n > 4: # h[n] = 0 for n > 4     
        h.extend([0 for i in range(n-4)])
    for j in range(1,n+1):
        x = 0
        for i in range(1,j+1):
            if x < (h[i] + r[j-i]):
                x = (h[i] + r[j-i])
                s[j] = i
        r[j] = x
    i = n
    lst.append(r[n]) # Maxmimal revenue
    while i > 0:
        lst.append(s[i]) 
        i -= s[i]
    return lst 

def message(n,a,b):
    """Output message"""
    return (" " + str(n) + a +
          str(p(n)[0]) + b + str(p(n)[1:]))

def output(n):
    if n < 4:
        print(message(n,"        ", "      "))
    elif 4 <= n <= 9:
        print(message(n,"        ", "     "))
    elif n > 9:
        print(message(n,"       ", "     "))
        
def main():
    print("Length  Profit  Cuts - [1, 2, 3..., n]")
    for n in range(21):
        output(n)

if __name__ == "__main__":
    main()     
