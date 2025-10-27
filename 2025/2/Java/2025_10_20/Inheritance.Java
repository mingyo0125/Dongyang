public class Inheritance
{
    class Point
    {
        private int x,y;

        public void Set(int x, int y)
        {
            this.x = x;
            this.y = y;
        }

        public void ShowPoint()
        {
            System.out.println("x: " + x + " y: " + y);
        }
    }

    class ColorPoint extends Point
    {
        private String _color;

        public void SetColor(String st)
        {
            _color = st;
        }

        public void ShowColorPoint()
        {
            this.ShowPoint();
            System.out.println(_color);
        }
    }
    
    public static void main(String[] args) {
        
    }
}