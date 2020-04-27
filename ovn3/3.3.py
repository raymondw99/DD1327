def sort(vec):
  """Sorts a given array of numbers"""
  """Positive precedent over negative"""
  try:
    count = 0 # index of pivot element
    for i in range(len(vec)): #O(N)
    	# // Invariant: Every negative element is inserted at
    	#    beginning of the array and removed in its original index
        if vec[i] < 0:
	    # // Invariant: Every negative element is placed before pivot 
            temp = vec[i]         # O(1)
            vec[i] = vec[count]   # O(1)
            vec[count] = temp     # O(1)
            count += 1
  except:
    return None
            
# Unit testing
def main():
  vec1 = [-8,4,2,1,-9,9,-3,4]
  vec2 = [1,-5,-3,1,2,0,-1,2,-2,2,-3]
  vec3 = [-8,-4,-4,-8,1,3,3,2]
  vec4 = [2,-4,-3,"apple"]
  sort(vec1)
  print(vec1)
  sort(vec2)
  print(vec2)
  sort(vec3)
  print(vec3)
  assert sort(vec4) == None

if __name__ == '__main__':
    main()
          
