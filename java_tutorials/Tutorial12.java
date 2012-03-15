// http://xahlee.org/java-a-day/access_specifiers.html
// Java's Access Specifiers

class P 
{
    int x = 7;
    // private int x = 7; // This produce a compiler error
}

class Q 
{
    public int x;
    // private Q(int n) // It doesn't compile
    Q(int n)
    {
        x = n;
        System.out.println("I'm born int!");
    }
    
    private Q(double n)
    {
        System.out.println("I'm born double!");
    }
}

public class Tutorial12 
{
    public static void main(String[] args)
    {
        P p = new P();
        System.out.println(p.x);

        Q q = new Q(3);
        System.out.println(q.x);
        // Q q2 = new Q(1.1); // Error, the constructoru for double is private
    }
}
