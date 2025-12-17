import java.util.*;

public class HashMapScoreEx{
    public static void main(String[] args) {
        HashMap<String, Integer> javaScore = new HashMap<>();

        javaScore.put("호날두", 90);
        javaScore.put("신지드", 45);

        System.out.println("HashMap의 요소 개수: " + javaScore.size());

        Set<String> keys = javaScore.keySet();

        Iterator<String> it = keys.iterator();

        while(it.hasNext())
        {
            String name = it.next();
            int score = javaScore.get(name);
            System.out.println(name + ":" + score);
        }
    }
}