package Sorting;

public class BubbleSort {

    public static void main(String[] args) {

        int[] n = {56, 78, 23, 65, 2, 1};

        for (int i = 0; i < n.length - 1; i++) {

            for (int j = 0; j < n.length - 1 - i; j++) {

                if (n[j] > n[j + 1]) {

                    int temp = n[j];
                    n[j] = n[j + 1];
                    n[j + 1] = temp;
                }
            }

            for (int num : n) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}