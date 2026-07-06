import java.sql.SQLOutput;

public class pattern2 {
    static void main(String[] args) {
        int n = 5;


        for (int i = 1; i <= n; i += 2) {
            for (int j = 5; j > i; j -= 2) {

                System.out.print(" ");
            }

            for (int k = 1; k <= i; k++) {
                System.out.print("*");

            }
           System.out.println();

        }
    }
    }
