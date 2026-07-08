public class Sumofeven{
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};

        int sum = 0;

        for (int i = 1; i < arr.length; i += 2) {
            sum += arr[i];
        }

        System.out.println("Sum of elements at even positions = " + sum);
    }
}