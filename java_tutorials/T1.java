import java.lang.Math;

class T2 {
    public double square (int n) {
        return java.lang.Math.pow(n,2); 
    }
}

class T1 {
    public static void main(String[] arg) {
        T2 x1 = new T2();
        double m = x1.square(3);
        System.out.println(m);
    }
}
