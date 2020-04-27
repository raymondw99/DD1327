import math 
  
def mode(vec): 
    """Returning most occuring number 
   of a given array"""
    Map = {}       # Adding to hash 
    count = 0
    val = 0
    for i in vec:            # O(n)
        if i in Map.keys(): 
            Map[i] += 1      # O(1)
        else: 
            Map[i] = 1       # O(1)
  
    for i in Map:            # O(n)
        if (count < Map[i]):  
            count = Map[i]   # O(1)
            val = i          # O(1)
            
    return val
  
# Unit testing 
def main():
  vec1 = [7,7,4,7,6,3,4,2,7,8,9]
  vec2 = [3,4,6,8,3,3,1,9,7,8,5]
  vec3 = [5,5,4,5,3,5,7,9,1,6,6]
  vec4 = [-1,-3,4,8,-1,2,-1,-1,9]
  assert mode(vec1) == 7
  assert mode(vec2) == 3
  assert mode(vec3) == 5 
  assert mode(vec4) == -1

if __name__ == "__main__":
  main()
