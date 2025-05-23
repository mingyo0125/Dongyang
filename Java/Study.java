public class Study
{

    public static void main(String[] args)
    {
        int[] arr = {0,1,2,3,4,5};
        int i = 0;

        try {
            for(i = 0; i < 7; i++)
            {
                System.err.println(arr[i]);
            }
        } catch (Exception e) {
            System.err.println(e);
            System.err.print(i);
            System.err.print("번째 인덱스가 배열의 범위를 벗어났습니다.");
        }

        
    }
}
