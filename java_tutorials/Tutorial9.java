// The static keyword
// http://xahlee.org/java-a-day/instance_vs_class_members.html

class T2 
{
    int x = 0; // instance variable
    static int y = 0; // class variable
    
    void setX(int n) 
    {
        x = n;
    }
    
    void setY(int n)
    {
        y = n;
    }
    
    int getX()
    {
        return x;
    }
    
    int getY() 
    {
        return y;
    }
}

class T3 
{
    static int triple(int n) 
    {
        return 3 * n;
    }
}


class Tutorial9 
{
    public static void main(String[] args) 
    {
        T2 x1 = new T2();
        T2 x2 = new T2();
        
        x1.setX(9);
        x2.setX(10);
        
        // each x1 and x2 has separate copies of x
        System.out.println(x1.getX());
        System.out.println(x2.getX());
        
        System.out.println(T2.y);
        T2.y = 7; // This compiles only because y is a class instance
        System.out.println(T2.y);
        
        x1.setY(T2.y + 1);
        System.out.println(x1.getY());
        System.out.println(x2.getY());
        
        System.out.println(T3.triple(4));
        
    }
}
