import java.util.Scanner;
public class atm {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double balance = 1000.0;
        int choice;
        while(true) {
            System.out.println("\n ======= ATM MENU ===");
            System.out.println("1. Check Balance");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
             if(choice == 1){
                System.out.println("Your balance is: " + balance);

             }
             else if(choice == 2){
                System.out.println("Enter the amount for deposit ");
                double deposit = scanner.nextDouble();
                balance = balance + deposit;
                System.out.println("Amount deposited successfully");
             }
             else if(choice == 3){
                System.out.println("Enter the amount to withdraw");
                double withdraw = scanner.nextDouble();
                if (withdraw <= balance){
                    balance = balance - withdraw;
                    System.out.println("Please collect your cash");
                } else{
                    System.out.println("Insufficient balance");
                }
             }
             else if(choice == 4){
                System.out.println("Thanks for using the atm");
                break;
             } else{
                System.out.println("Invalid choice");
             }

        }
        scanner.close();
    }
}