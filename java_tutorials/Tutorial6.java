
class H {
    int x;
    H(int n) {
        x = n;
    }
}

public class Tutorial6 {
    public static void main(String[] args) {
        int[][] A = {{3, 4, 5}, {77, 50}};
        
        for (int i=0; i<A.length; i++) {
            for (int j=0; j<A[i].length; j++) {
                System.out.print(A[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
        System.out.println();
        
        H[] B;
        B = new H[4];
        
        for (int i=0; i < B.length; i++) {
            B[i] = new H(i);
            System.out.print(new Integer(B[i].x) + " ");
        }
        System.out.println();
    }
}