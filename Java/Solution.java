
import java.util.*;

public class Solution
{
    public int[][] solution(int[] arr)
    {
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < arr.length; i++)
        {
            List<Integer> list = new ArrayList<>();
            int num = arr[i];

            while (num > 0)
            {
                int digit = num % 10;
                list.add(digit);
                num /= 10;
            }

            int sum = list.stream().mapToInt(Integer::intValue).sum();
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }

        int[][] answer = new int[map.size()][2];
        int idx = 0;

        for (Map.Entry<Integer, Integer> entry : map.entrySet())
        {
            answer[idx][0] = entry.getKey();
            answer[idx][1] = entry.getValue();
            idx++;
        }

        Arrays.sort(answer, (a, b) -> Integer.compare(a[0], b[0]));
        return answer;
    }
    public static void main(String[] args)
    {
        
    }
    
}
