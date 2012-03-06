/* Arrays examples */

public class Tutorial5 {
    public static void main(String[] args) {
        int[] my_A;
        my_A = new int[10];
        my_A[3] = 6;
        System.out.print(my_A[3] + "\n");
        System.out.print(my_A.length + "\n");

        for (int i=0; i< my_A.length; i++) {
            System.out.print(my_A[i] + " ");
        }
        System.out.println(" ");
    }
}