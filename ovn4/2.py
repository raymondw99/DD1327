def sort(array,k):
    n = len(array)
    output = [0] * n             # O(n)
    count = [0] * (k+1)          # O(k)

    for i in range(0, n):        # O(n)
        count[array[i]] += 1

    for i in range(1, k+1):      # O(k)
        count[i] += count[i - 1]

    for i in range(n-1,-1,-1):   # O(n)
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1

    for i in range(0, n):        # O(n)
        array[i] = output[i]

# Unit testing
def main():
    a = [8,4,4,8,1,3,3,2,1,3,5,2,0,1,2,2,3]
    sort(a,8)
    b = [-5,4,5,-5,-5]
    sort(b,5)
    c = [0,0,0]
    sort(c,0)

    assert a == [0,1,1,1,2,2,2,2,3,3,3,3,4,4,5,8,8]
    print(a)
    assert b == [-5,-5,-5,4,5]
    print(b)
    assert c == [0,0,0]
    print(c)

if __name__ == '__main__':
    main() 
