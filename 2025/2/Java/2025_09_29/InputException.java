import java.util.InputMismatchException;
import  java.util.Scanner;

public class InputException {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sum = 0, n = 0;
        for(int i= 0; i < 3; i++)
        {
            try
            {
                n = scanner.nextInt();
            }
            catch(InputMismatchException ex)
            {
                scanner.next();
                i--;
                continue;
            }
            sum += n;
        }
    }
}
