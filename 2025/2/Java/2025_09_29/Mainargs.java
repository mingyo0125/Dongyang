public class Mainargs {
    public static void main(String[] args) {
        double sum = 0.0;
        for(String arg: args)
        {
            // 문자열을 실수(double)타입으로 변환하여 합산
            sum += Double.parseDouble(arg);
        }

        System.out.println("합계: " + sum);
    }
}
