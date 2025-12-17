
import java.util.Vector;

class Point{
    private int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public String ToString()
    {
        return "(" + x + "," + y + ")";
    }
}

public class PointVectorEx
{

    public static void main(String[] args)
    {
        Vector<Point> vec = new Vector<Point>();

        vec.add(new Point(1,2));
        vec.add(new Point(2,1));
        vec.add(new Point(3,3));

        vec.remove(1);
    }


}
