import java.util.Map.Entry; 
import java.util.Map; 
import java.util.HashMap; 

public class Mode { 
    static int mode(int vec[]) { 
        // Returning most occuring number 
        // of a given array
        Map<Integer, Integer> hash = 
               new HashMap<Integer, Integer>(); 
        int count = 0;
        int val = 0; 
          
        for (int i: vec)  {               // O(n)
            if (hash.containsKey(i)) { 
                int rec = hash.get(i);   
                rec++; 
                hash.put(i, rec);         // O(1)
            } 
            else { 
                hash.put(i, 1);           // O(1)
            } 
        } 
          
        for (Entry<Integer, Integer> i : hash.entrySet()) {  // O(n)
            if (count < i.getValue()) { 
                val = i.getKey();            // O(1)
                count = i.getValue();        // O(1)
            } 
        }
        return val; 
    } 
      
    // Unit testing
    public static void main(String[] args) { 
        int[] vec1 = {7,7,4,7,6,3,4,2,7,8,9};
        int[] vec2 = {3,4,6,8,3,3,1,9,7,8,5};
        int[] vec3 = {5,5,4,5,3,5,7,9,1,6,6};
        int[] vec4 = {-1,-3,4,8,-1,2,-1,-1,9};
        assert mode(vec1) == 7;
        assert mode(vec2) == 3;
        assert mode(vec3) == 5;
        assert mode(vec4) == -1;
    } 
} 
  
