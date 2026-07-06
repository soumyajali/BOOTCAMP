public class balancednum {
    public static void main(String[] args) {

        int num = 248680;
        int temp = num;
        int count = 0;
 
        while (temp > 0) {
            count++;
            temp /= 10;
        }
        if (count % 2 != 0) {
            System.out.println("Unbalanced Number");
            return;
        }

        int half = count / 2;
        int divisor = 1;
        for (int i = 0; i < half; i++) {
            divisor *= 10;
        }
        int left = num / divisor;
        int right = num % divisor;

        int leftEven = 0;
        int rightEven = 0;
        while (left > 0) {
            int digit = left % 10;
            if (digit % 2 == 0)
                leftEven++;
            left /= 10;
        }
        while (right > 0) {
            int digit = right % 10;
            if (digit % 2 == 0)
                rightEven++;
            right /= 10;
        }

        if (leftEven == rightEven && leftEven > 0)
            System.out.println("Balanced Number");
        else
            System.out.println("Unbalanced Number");
    }
}