import java.util.*;

public class iteratorEx {
    public static void main(String[] args) {
        Vector<Integer> vec = new Vector<Integer>();
        Iterator<Integer> it = vec.iterator();

        vec.add(100);
        vec.add(200);
        vec.add(1,300);

        // 모든 정수 출력
        while (it.hasNext()) {
            int i =  it.next();
            System.out.println(i);
        }

        // 모든 정수 총합
        int sum = 0;
        while (it.hasNext()) {
            int i =  it.next();
            sum += i;
        }
        System.out.println(sum);
    }
    
}
