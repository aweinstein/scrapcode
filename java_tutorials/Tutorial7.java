class B {
    int x;
    void setIt(int n) 
    {
        x = n;
    }
    
    void increase() 
    {
        x = x + 1;
    }
    
    void triple() 
    {
        x = x * 3;
    }
    
    int returnIt()
    {
        return x;
    }
}


class C extends B 
{
    void triple() 
    {
        x = x + 3;
    }
    
    void quadruple()
    {
        x = x * 4;
    }
}

public class Tutorial7
{
    public static void main(String[] args) 
    {
        B b = new B();
        b.setIt(2);
        b.increase();
        b.triple();
        System.out.println(b.returnIt());
        
        C c =  new C();
        c.setIt(2);
        c.increase();
        c.triple();
        System.out.println(c.returnIt());
    }
}

        
    