package Java.operations;

public class ConditionalBool {

    public static void main(String[] args) {

        
        boolean isAlien = false;
        if (isAlien == false) {
            System.out.println("it is not an Alien");
            System.out.println("Herroooo");
        }

        // if (isAlien == false);
        // System.out.println("Its not an Alien")

        int topScore = 80;
        if (topScore > 100) {
            System.out.println("You Got The Highest Score");
        }

        int secondtopScore = 60;
        if (topScore > secondtopScore && topScore < 100) {
            System.out.println("This is greater than the top score and less than 100");
        }


        if ((topScore > secondtopScore) && (topScore < 100)) {
            System.out.println("This is greater than the top score and less than 100");
        }

        if ((topScore > 90) || (secondtopScore <= 90 )) {
            System.out.println("test");
        }

        int newValue = 50;
        if (newValue == 50) {
            System.out.println("Error");
        }

        boolean isCar = false;
        if (isCar = true) {   // this still works cause isCar is a boolean which is weird. // this is wrong
            System.out.println("This is not supposed to happen.");
        }

        if (isCar) {   // this is a shortcut just have the boolean there
            System.out.println("This is not supposed to happen.");
        }

        if (!isCar) {   // this is a shortcut for not, the opposite just have the boolean there
            System.out.println("This is not supposed to happen.");
        }

        isCar = true;
        Boolean wasCar = isCar ? true : false;
//        Boolean wasCar = isCar;
        if (wasCar) {
            System.out.println("wasCar is True");
        }

        int ageOfClient = 20;
        Boolean isEighteenOfOver = (ageOfClient == 20) ? true : false;
        System.out.println(isEighteenOfOver);

        int ageOfClient1 = 20;
        int isEighteenOfOver1 = (ageOfClient1 == 20) ? 20 : 15;
        System.out.println(isEighteenOfOver1);

        // if (isAlien == false);
        // System.out.println("Its not an Alien")
    }
}
