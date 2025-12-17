import java.util.*;

public class ArrayListEx {

    public static void main(String[] args)
    {
        // 4개 이름 입력받아 Array List에 삽입
        ArrayList<String> arr = new ArrayList<String>();
        Scanner scanner = new Scanner(System.in);

        int num = 4;
        while(num --> 0)
        {
            String s = scanner.next();
            arr.add(s);
        }

        // 모든 이름 출력
        for(int i = 0; i < 4; i++)
        {
            String name = arr.get(i);
            System.out.println("name");
        }

        //가장 긴 이름 출력
        int longestIndex = 0;
        for(int i = 0; i < 4; i++)
        {
            String name = arr.get(i);
            if(name.length() > arr.get(longestIndex).length())
            {
                longestIndex = i;
            }
        }

        System.out.println(arr.get(longestIndex));
    }
    
}
