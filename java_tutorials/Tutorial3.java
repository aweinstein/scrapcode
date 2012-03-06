public class Tutorial3 {
    public static void main(String[] args) {
        String s1 = "some str";
        StringBuffer s2 = new StringBuffer(9);
        s2.replace(0, 0, s1);
        System.out.println(s2.toString());
    }
}