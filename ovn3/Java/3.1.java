
public class Factorial {
    static int factorial(int n) {
        try {
            if (n == 0) {
                return 1;  
            }
            else {
                return n * factorial(n-1);
            }
        } 
        catch(Error e) {
            return 0; 
        }
    }
  
    static Boolean check(int i) {
        if (i == 0 ) {
            return false;
        }
        return true;
 }

    public static void main(String[] args) {
        assert check(factorial(5));
        assert check(factorial(0));
        assert check(factorial(5));
        assert check(factorial(-3)) == false;
        assert check(factorial(-10)) == false;
        assert check(factorial(-8)) == false;  
    }
}
