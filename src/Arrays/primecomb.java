package Arrays;
public class primecomb {

    static void isPrime(int n, int m) {
        int s = n + m;

        boolean prime = true;

        if (s < 2) {
            prime = false;
        } else {
            for (int i = 2; i <= Math.sqrt(s); i++) {
                if (s % i == 0) {
                    prime = false;
                    break;
                }
            }
        }

        if (prime) {
            System.out.println("(" + n + ", " + m + ")");
        } else {
            System.out.println(Math.min(n, m));
        }
    }

    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4};
        int[] b = {2, 3, 5, 1};

        for (int i : a) {
            for (int j : b) {
                isPrime(i, j);
            }
        }
    }
}