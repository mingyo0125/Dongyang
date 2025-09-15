
import java.util.HashMap;

public class Study
{
    public static  int[] solution(String[][] genres, String[] queries)
    {
        HashMap<String, Integer> genreCount = new HashMap<>();
        int[] counts = new int[queries.length];

        for(String[] genre : genres)
        {
            for(String g : genre)
            {
                genreCount.put(g, genreCount.getOrDefault(g, 0) + 1);
            }
            
        }
        
        for(int i = 0; i < queries.length; i++)
        {
            String query = queries[i];
            counts[i] = genreCount.getOrDefault(query, 0);
        }
        return counts;
    }

    public static void main(String[] args)
    {
        String[] dsa = {"SF", "drama", "fantasy","romance"};
        String[][] dsaa = {{"horror", "drama", "SF"},{"horror", "detective", "suspense"},{"SF","fantasy","-"}};
        int[] asd = solution(dsaa, dsa);
        for(int i = 0; i < asd.length; i++)
        {
            System.out.println(asd[i]);
        }
        
    }
}
