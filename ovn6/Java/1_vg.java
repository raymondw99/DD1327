import java.util.Arrays;
import java.util.*; 

public class MaxIncome {
    private static int[][] p(int n,int[] h) {
        int[] r = new int[n+1];  // Array for revenue
        int[] c = new int[n+1];  // Array for cuts
        
        r[0] = 0;
        int x = 0;
        for (int j = 1; j <= n; j++) {
            x = 0;
            for (int i = 0; i < j; i++) {
                if (x < h[i] + r[j - i - 1]) {
                    x = h[i] + r[j - i - 1];
                    c[j] = i + 1;
                }
            }
            r[j] = x; // Maximal revenue
        }
        
       // Initialize Int array with revenue and cuts 
        int[][] rc = new int[2][n + 1];
        for (int i = 0; i < n + 1; i++) {
            rc[0][i] = r[i];
            rc[1][i] = c[i];
        }
        return rc; 
    }
    
    private static int[] _join(int[] h1, int[] h2, int n) {
        int[] h = new int[h1.length + h2.length];
        System.arraycopy(h1, 0, h, 0,  h1.length);
        System.arraycopy(h2, 0, h, h1.length, h2.length);
        return h;
    }
    
    // Adding n-4 zeros to array if n < 4
    private static int[] _f(int[] h1,int n) {
        int[] h2 = new int [n-4];
        return _join(h1,h2,n);
    }
    
    // Output message 
    static void message(int[] h1, int[] h2, int n, int[] h) {
        int[][] revCuts = p(n,h);
        int rev = revCuts[0][n];
        int[] cuts = revCuts[1];
        Integer lst[] = {};
        
        List<Integer>x = new ArrayList<Integer>(Arrays.asList(lst));
        
        System.out.println("Length: " + String.valueOf(n));
        while (n > 0) {
            x.add(cuts[n]);
            n -= cuts[n];
        }
        lst = x.toArray(lst);
        System.out.println("Profit: " + String.valueOf(rev));
        System.out.println("Cuts:   " + Arrays.toString(lst));
        System.out.println("----------------");
    }
    
    /* Unit Testing */
    public static void main(String[] args) {
        int n = 10; 
        
        // Initializing array with prices 
        int[] h1 = {2,5,6,9};
        int[] h2 = {};
        for (int i = 0; i < n; i++) {
            if (i < 4)
                message(h1,h2,i,_join(h1,h2,i));
            else
                message(h1,h2,i,_f(h1,i));
        }
    }
}  
