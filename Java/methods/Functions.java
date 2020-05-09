// package com.company;

// public class Main {

//     public static void main(String[] args) { // main is already a method
//     calculateScore();

//     }

//     public static void calculateScore() { // void means we're returning nothing
//         boolean gameOver = true;
//         int score = 800;
//         int levelCompleted = 5;
//         int bonus = 100;

//         if (gameOver) {
//             int finalScore = score + (levelCompleted * bonus);
//             finalScore += 100;
//             System.out.println(" Your final score " + finalScore);
//         }

//     }
// }

package Java.methods;

public class Functions {

    public static void main(String[] args) { // main is already a method
    calculateScore(true, 800, 5, 100);

    }

    public static void calculateScore(boolean gameOver, int score, int levelCompleted, int bonus) { // void means we're returning nothing
        if (gameOver) {
            int finalScore = score + (levelCompleted * bonus);
            finalScore += 100;
            System.out.println(" Your final score " + finalScore);
        }

    }
}

// package com.company;

// public class Main {

//     public static void main(String[] args) { // main is already a method
//         calculateScore(true, 800, 5, 100);
//         calculateScore(true, 1000, 8, 200);

//     }

//     public static void calculateScore(boolean gameOver, int score, int levelCompleted, int bonus) { // void means we're returning nothing
//         if (gameOver) {
//             int finalScore = score + (levelCompleted * bonus);
//             finalScore += 100;
//             System.out.println(" Your final score " + finalScore);
//         }

//     }
// }
