package Java.types_overflow;

public class Main {

    public static void main(String[] args) {

        int myValue = 10000;

        int myMinIntValue = Integer.MIN_VALUE;
        int myMaxIntValue = Integer.MAX_VALUE;
        System.out.println("Integer Minimum = " + myMinIntValue);
        System.out.println("Integer Maximum = " + myMaxIntValue);
        System.out.println("Busted Max value = " + (myMaxIntValue + 1));
        System.out.println("Busted Min value = " + (myMinIntValue - 1));
        int underTest = 2_147_483_647;
        System.out.println(underTest);
        System.out.println(myValue);


        byte myMinByteValue = Byte.MIN_VALUE;
        byte myMaxByteValue = Byte.MAX_VALUE;
        System.out.println("Byte M in value = " + (myMinByteValue));
        System.out.println(myMaxByteValue);

        short myMinShortValue = Short.MIN_VALUE;
        short myMaxShortValue = Short.MAX_VALUE;
        System.out.println("Short Min value = " + (myMinShortValue));
        System.out.println("Short Min value = " + (myMaxShortValue));

        long myLongValue = 100L;
        System.out.println(myLongValue);
        long myMinLongValue = Long.MIN_VALUE;
        long myMaxLongValue = Long.MAX_VALUE;
        System.out.println("Long Min value = " + (myMinLongValue));
        System.out.println("Long Min value = " + (myMaxLongValue));
        long bitLongLiteralValue = 2_147_483_647_234L;
        System.out.println(bitLongLiteralValue);

        int myTotal = (myMinIntValue /2);
        byte myNewByteValue = (byte)(myMinByteValue / 2);

        short myNewShortValue = (short) (myMinShortValue /2);
        System.out.println(myTotal + myNewByteValue + myNewShortValue);

    }
}
