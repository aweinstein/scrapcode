// Using constructors

class C2 
{
    C2(int n) 
    {
        System.out.println("Initializing the class.");
    }
}

class T2 
{
    T2() 
    {
        System.out.println("Empty argument constructor.");
    }
    
    T2(int n)
    {
        System.out.println("Integer argument constructor.");
    }
    
    T2(double x) 
    {
        System.out.println("Float argument constructor.");
    }
}

class Tutorial8
{
    public static void main(String[] args)
    {
        C2 x = new C2(3);
        T2 x1 = new T2();
        T2 x2 = new T2(12);
        T2 x3 = new T2(3.14);
        
    }
}
