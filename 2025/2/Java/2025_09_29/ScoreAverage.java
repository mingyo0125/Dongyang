public class ScoreAverage {
    public static void main(String[] args) {
        double scores[][] = {
            {3.3, 3.4}, {3.5, 3.6}
        };

        int sum = 0;

        for(int year = 0; year < scores.length; year++)
        {
            for(int term = 0; term < scores[year].length; term++)
            {
                sum += scores[year][term];
            }
        }
        int n = scores.length; //행 개수
        int m = scores[0].length;  //열 개수
        System.out.println("4년 전체 평점 평균은" + sum / (n*m));
    }
}
