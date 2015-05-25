import java.io.PrintStream;
import java.lang.reflect.Array;

public class givemeflag
{
  public static void main(String[] paramArrayOfString)
  {
    if (paramArrayOfString.length != 1) {
      System.out.println("You are not worthy of receiving the flag.");
    }
    else
    {
      int[] arrayOfInt2 = { 4329, 4347, 4301, 4339, 4351, 4301, 4344, 4339, 4324, 4339, 4301, 4351, 4339, 4321, 4326, 4343, 4320, 4335 };
      int[] arrayOfInt1 = new int[paramArrayOfString[0].length()];
      for (int i = 0; i < Array.getLength(arrayOfInt2); i++) {
        arrayOfInt1[i] = paramArrayOfString[0].charAt(i);
        if (((arrayOfInt1[i] ^ 0x1092) != arrayOfInt2[i]) || (paramArrayOfString[0].length() != Array.getLength(arrayOfInt2))) {
          System.out.println("You are wrong.");
          System.exit(0);
        }
      }
      System.out.println("Flag: " + paramArrayOfString[0]);
    }
  }
}