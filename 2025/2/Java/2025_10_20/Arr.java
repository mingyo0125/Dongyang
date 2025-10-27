public class Arr
{
    static  void replaceSpace(char c[])
    {
        for(int i = 0; i < c.length; i++)
        {
            if(c[i] == ' ')
            {
                c[i] = ',';
            }
        }
    }

    static void printArray(char c[])
    {
        for(char ch: c)
        {
            System.out.print(ch);
        }
        System.out.println("");
    }
    public static void main(String[] args) {
        char c[] = {'a',' ','b',' ','c'};
        printArray(c); 
        replaceSpace(c);
        printArray(c);
    }
}