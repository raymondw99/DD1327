import java.util.Arrays;

public class CountingSort {
    public static void sort(int[] array, int k) {
        int n = array.length;
        int[] output = new int[n];            // O(n)
        int[] count  = new int[k+1];          // O(k)
    
        for (int i = 0; i < n; i++) {      // O(n)
            count[array[i]] += 1;
        }
        
        for (int i = 1; i < k+1; i++) {       // O(k)
            count[i] += count[i-1];
        }
        
        for (int i = n-1; i > -1; i-= 1) {   // O(n)
            output[count[array[i]] - 1] = array[i];
            count[array[i]] -= 1;
        }
        
        for (int i = 0; i <= n-1; i++) {    // O(n)
            array[i] = output[i];
        }
    }
	
   // Unit testing
    public static void main(String[] args) {
        int[] a = {8,4,4,8,1,3,3,2,1,3,5,2,0,1,2,2,3};
        sort(a,8);
        int[] b = {5,4,5,5,5};
        sort(b,5);
        int[] c = {0,0,0};
        sort(c,0);
        
        int[] aSorted = {0,1,1,1,2,2,2,2,3,3,3,3,4,4,5,8,8};
        int[] bSorted = {4,5,5,5,5};
        int[] cSorted = {0,0,0};
        
        assert a == aSorted;
        System.out.println(Arrays.toString(a));
        assert b == aSorted;
        System.out.println(Arrays.toString(b));
        assert c == cSorted;
        System.out.println(Arrays.toString(c));
   }
}

