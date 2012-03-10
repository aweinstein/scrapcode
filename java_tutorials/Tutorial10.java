// http://xahlee.org/java-a-day/this.html
// “this” Keyword

class CL {
    int x = 1;
    CL me() 
    {
        return this;
    }
}

class OneNumber 
{
    int n;
    void setValue(int n) 
    {
        this.n = n;
    }
}

class B 
{
    int n;
    void setMe(int m) 
    {
        C h = new C();
        h.setValue(this, m);
    }
}

class C
{
    void setValue(B obj, int h) 
    {
        obj.n = h;
    }
}

public class Tutorial10
{
    public static void main(String[] args) 
    {
        CL cl = new CL();
        System.out.println(cl.x);
        System.out.println(cl.me().x);
        System.out.println(cl.me().me().x);

        OneNumber x = new OneNumber();
        x.setValue(3);
        System.out.println(x.n);

        B y = new B();
        y.setMe(4);
        System.out.println(y.n);
    }
}
