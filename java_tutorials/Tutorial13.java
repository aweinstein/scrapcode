// http://xahlee.org/java-a-day/abstract_class.html
// The “abstract” Keyword in Java

// Abstract classes and abstract methods are like skeletons. It defines a structure, without any implementation. 

// Note that, only abstract classes can have abstract methods. Abstract class does not necessarily require its methods to be all abstract.

// Classes declared with the abstract keyword are solely for the purpose of extension (inheritance) by other classes.

abstract class H 
{
    int x;
    int y; // variables cannot be abstract
    
    H() // constructors cannot be abstract 
    {
        x = 1;
    }
    
    void triple(int n) // a normal method
    {
        x = x * 3;
    }
    
    static int triple2(int n) // a static method in an abstract class is OK
    {
        return 3 * n;
    }
    
    abstract void triple3(); // no definition for abstract method
    
    int returnMe() 
    {
        return x;
    }
}

// H1 extends (inherit) H. Since H is abstract in this example, we also say H1 *implement*
// H
class H1 extends H 
{
    void triple3 () // This *must* be defined
    {
        x = x * 3 + 1;
    }
}


public class Tutorial13 
{
    public static void main(String[] args)
    {
        H1 h1 = new H1();
        h1.triple3();
        System.out.println(h1.returnMe());
    }
}
