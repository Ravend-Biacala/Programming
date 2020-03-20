package Java.string;


public class StriChar {

    public static void main(String[] args) {

        String myString = "This is a string";
        System.out.println(myString);
        myString = myString + "and this is more";
        System.out.println(myString);
        myString = myString + "\u00A0 2019";
        System.out.println(myString);

        String numbersString = "250.55";
        numbersString = numbersString + "49.95";
        System.out.println(numbersString); // was concatinated

        String lastString = "10";
        int myInt = 50;
        lastString = lastString + myInt;
        System.out.println(lastString);

        double doubleNumber = 120.47d;
        lastString = lastString + doubleNumber;
        System.out.println(lastString);

        int test = 10;
        System.out.println(test + "work");
    }
}
