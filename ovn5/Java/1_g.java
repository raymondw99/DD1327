public class MaxIncome { 
    // Top down implementation
    // Time Complexity O(2^n)
    private static int _p1(int n, int h[]) {
        if (n <= 0)
            return 0;
        int x = 0;
        for (int i = 0; i<n; i++)
            x = Math.max(x, h[i] + _p1(n-i-1,h) );
        return x; // Maximal revenue
    }
    
    // Bottom up implementation
    // Time Complexity O(n^2)
    private static int _p2(int n,int h[]) { 
        int r[] = new int[n+1]; // Int array with length n 
        r[0] = 0;  
        for (int i = 1; i<=n; i++) { 
            int x = 0; 
            for (int j = 0; j < i; j++) 
                x = Math.max(x,h[j] + r[i-j-1]); 
            r[i] = x; 
        } 
        return r[n]; // Maximal revenue
    }
    
    
    private static int _join(int[] h1, int[] h2, int n, int i) {
        int[] h = new int[h1.length + h2.length];
        System.arraycopy(h1, 0, h, 0,  h1.length);
        System.arraycopy(h2, 0, h, h1.length, h2.length);
        if (i == 1)
            return _p1(n,h);
        else if (i == 2)
            return _p2(n,h);
        return 0 ;
    }
    
    // Adding n-4 zeros to array if n < 4
    private static int _p(int[] h1,int n, int i) {
        int[] h2 = new int [n-4];
        return _join(h1,h2,n,i);
    }
    
    // Initializing array with prices 
    public static int p(int n, int i) {
        int[] h1 = {2,5,6,9};
        int[] h2 = {};
        if (n < 4)
            return _join(h1,h2,n,i);
        return _p(h1,n,i);
    }
    
    /* Unit Testing */
    static void output(int i, int j) {  
        System.out.println("Length Profit");
        for (int n = 0; n < j; n++) {
            System.out.println("  " + String.valueOf(n) 
            + "      " + String.valueOf(p(n,i)));
        }
        System.out.println("");
    }
    
    public static void main(String args[]) {  
        System.out.println("Time Complexity O(2^n)");
        output(1, 10);
        System.out.println("Time Complexity O(n^2)");
        output(2, 10);
    }
}
