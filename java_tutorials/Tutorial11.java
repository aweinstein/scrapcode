// http://xahlee.org/java-a-day/super.html
// Java: Extending a Class that has a Constructor; the “super” Keyword

// Here's a example of inheritance of a class that has a constructor.
// Note: constructors are never inherited, only variables and methods are.

class B 
{
    B() 
    {
        System.out.println("BBB");
    }
    
    int triple(int n)
    {
        return 3 * n;
    }
}

class C extends B
{
}


class D
{
    D(int n) 
    {
        System.out.println("D's constructor called");
    }
}

class E extends D
{
    E(int n)
    {
        super(n);
        System.out.println("E's constructor called");
    }
}


public class Tutorial11 
{
    public static void main(String[] args) 
    {
        C c = new C();
        System.out.println(c.triple(4));
        System.out.println();

        D d = new D(4);
        E e = new E(2);
    }
}


       