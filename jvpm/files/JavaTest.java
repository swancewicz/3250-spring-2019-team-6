import java.util.Scanner;
public class JavaTest {

   public static void main (String [] args) {
   
      Scanner Reader = new Scanner(System.in);
      
      int a;
      int b;
      int c;
      double d;
      byte e;
      int myInt;
      double myDouble;
      String myString;
      float myFloat;
         
      a = 1 + 2;
      b = 3 / 4;
      c = a + b;
      c = a & b;
      b = c * -1;
      a = c - b;
      c = -a;
      c = a | b;
      c = 16 % 5;
      c = a << 1;
      c = a >> 1;
      c = a ^ b;
      d = c;
      
      myString = Reader.nextLine();
      System.out.println("This is my string: " + myString);
      myInt = Reader.nextInt();
      System.out.println("This is my integer: " + myInt);
      myDouble = Reader.nextDouble();
      System.out.println("This is my double: " + myDouble);
      myFloat = Reader.nextFloat();
      System.out.println("This is my float: " + myFloat);
      System.out.println("Hello World");
            
   }
}