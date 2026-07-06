import java.util.Scanner;
public class ATM {
    static void main(String[] args) {
        int actualpin = 9999;
        int bankbalanace = 998;


        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your pin : ");
        int Entered_pin = sc.nextInt();

        if(actualpin != Entered_pin){
            System.out.println("Enter valid PIN");
        }
        else if(actualpin == Entered_pin){
            System.out.print("Enter amount : ");
            int amount = sc.nextInt();


            if (bankbalanace < amount) {
                System.out.println("Insufficient Balance");
            } else if(bankbalanace > amount){
                bankbalanace -= amount;
                System.out.println("Remaining Balance is :" + bankbalanace);
            }

        }
        }
    }



