import java.util.Arrays;

public class negPos {
   public static void sort(int[] vec) {
      // Sorts a given array of numbers
      // Positive precedent over negative
      int count = 0;
      for (int i = 0; i <= vec.length-1; i++) {  // O(n)
	 // Invariant: Every negative element is inserted at
	 // beginning of the array and removed in its original index
	 if (vec[i] < 0) {           // Incremeneting count if negative number 
            // Invariant: Index of negative element swapped with pivot element
            int elem = vec[i];              
	    vec[i] = vec[count];                 // O(1)
	    vec[count] = elem; 			 // O(1)
	    count++;  				 // O(1)
	 }
      }
   }
	
   // Unit testing
   public static void main(String[] args) {
      int[] vec1 = {-8,4,2,1,-9,9,-3,4};
      int[] vec2 = {1,-5,-3,1,2,0,-1,2,-2,2,-3};
      int[] vec3 = {-8,-4,-4,-8,1,3,3,2};
      sort(vec1);
      System.out.println(Arrays.toString(vec1));
      sort(vec2);
      System.out.println(Arrays.toString(vec2));
      sort(vec3);
      System.out.println(Arrays.toString(vec3));
   }
}
