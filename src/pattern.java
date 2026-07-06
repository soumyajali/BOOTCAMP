public class pattern {
    public static void main(String[] args) {
        int s = 1;
        for (int i = 0; i < 5; i++) {
            for (int j = 5; j >= 1; j--) {
            if (j == s) {
                    System.out.print("* ");
                } else {
                    System.out.print(j + " ");
                }
            }

            s = s + 1;
            System.out.println();
        }
    }
}