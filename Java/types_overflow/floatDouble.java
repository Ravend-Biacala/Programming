package Java.types_overflow;

public class floatDouble {

    public static void main(String[] args) {

        float myMinFloatValue = Float.MIN_VALUE;
        float myMaxFloatValue = Float.MAX_VALUE;
        System.out.println("Float minimum value = " + myMinFloatValue);
        System.out.println("Float maximum value = " + myMaxFloatValue);

        double myMinDoubleValue = Float.MIN_VALUE;
        double myMaxDoubleValue = Float.MAX_VALUE;
        System.out.println("Double minimum value = " + myMinDoubleValue);
        System.out.println("Double maximum value = " + myMaxDoubleValue);

        int myInt = 5 / 3;
        System.out.println(myInt);
        float myFloat = 5f / 3f;
        System.out.println(myFloat);
        double myDouble = 5 / 3;
        System.out.println(myDouble);

    }
}
