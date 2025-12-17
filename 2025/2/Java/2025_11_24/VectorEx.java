import java.util.Vector;

public class VectorEx {
    public static void main(String[] args) {
        Vector<Double> v = new Vector<Double>();

        v.add(1.1);
        v.add(-1.1);

        v.add(1, 2.2);

        System.out.println(v.size());
        System.out.println(v.capacity());

        for(int i = 0; i < v.size(); i++)
        {
            double n = v.get(i);
            System.out.println(n);
        }

        int sum = 0;
        for(int i = 0; i < v.size(); i++)
        {
            double n = v.get(i);
            sum += n;
        }
        System.out.println(sum);
    }
}
