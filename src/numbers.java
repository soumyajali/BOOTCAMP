import java.util.*;
public class numbers {
    static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int max = 0;
        int min = 0;
        for (int i = 1; i <= 3; i++) {
            int n = sc.nextInt();
            if(max < n)
            {
                max = n;
            } else if (min < n) {
                min = n;
            }
        }
        System.out.println(max);
        System.out.println(min);


    }
}
