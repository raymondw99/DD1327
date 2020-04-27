# DD1327 Övning 4
2020-04-24 Kl 8.00

## 2 Linjärtidssortering av små tal

Implementera, dokumentera och testa en algoritm som sorterar heltalen x1, x2, ..., xn. För samtliga tal xi gäller att 0 ≤ xi ≤ k. Din algoritm ska ha värstafallstidskomplexitet O(n+k). För vilka värden på k blir algoritmen linjär? </br>

*En sorteringsalgoritm för heltal med värstafallskomplexiteten O(n+k) är counting sort. Pseudokodsimplementation för algoritmen vore exempelvis:*
```
counting_sort(array,k)
    output = array of same length as input array  # O(n)
    count = array of k+1 zeros                    # O(k)
    n = length of array

    for i from 0 to n do                          # O(n)
        add 1 to count[array[i]] 

    for i from 1 to k+1 do                        # O(k)
        add count[i - 1] to count[i]  

    for i from n-1 down to 0 do                   # O(n)
        output[count[array[i]] - 1] = array[i]
        subtract 1 from count[array[i]]

    for i from o to n do                          # O(n)
        array[i] = output[i]
    return array 

```
*Algoritmen blir linjär, O(n) då k ∈ O(n). Det vill säga, antalet siffror som sorteras inte understiger antalet siffror som förekommer.*
