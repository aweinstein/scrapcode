class T2 {
    public int add_one(int n) {
        return n + 1;
    }
}

public class Tutorial4 {
    public static void main(String[] args) {
        T2 x1 = new T2();
        int m = x1.add_one(4);
        System.out.println(m);
   }
}