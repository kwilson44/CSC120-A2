import java.util.Scanner;

class GuessingGame {

    static int secretNumber = 4;
    public static void main (String[] args){
        System.out.println("Please guess an integer between 0 and 10.");
        Scanner input = new Scanner (System.in);
        int guess = input.nextInt();

        if (guess == secretNumber ) {
            System.out.println("Yay! Correct :D");
        } else if (guess > 10) {
            System.out.println("That's bigger than 10, incorrect!");

         } else if (guess < 0 ){

            System.out.println("That's bigger than 10, incorrect!")
         } else{
            System.out.print("Sorry, wrong number >:(");
        }

        input.close();
    }
}