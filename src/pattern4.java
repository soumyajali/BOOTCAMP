public class pattern4 {
    public static void main(String[] args) {
        int n = 4;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= 3 * i - 2; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
