import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);

      System.out.print("Enter first number: ");
      double num1 = scanner.nextDouble();

      System.out.print("Enter second number: ");
      double num2 = scanner.nextDouble();

      System.out.print("Enter the operator (+, -, *, /): ");
      char operator = scanner.next().charAt(0);

      double result = 0.0;

      switch(operator) {
         case '+':
            result = num1 + num2;
            break;

         case '-':
            result = num1 - num2;
            break;

         case '*':
            result = num1 * num2;
            break;

         case '/':
            result = num1 / num2;
            break;

         default:
            System.out.println("Invalid operator!");
            break;
      }

      System.out.println(num1 + " " + operator + " " + num2 + " = " + result);
      scanner.close();
   }
}
