import java.util.*;

public class PasswordChecker {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter password: ");
        String password = sc.nextLine();

        boolean hasUpper = false, hasLower = false, hasDigit = false, hasSpecial = false;

        for (char ch : password.toCharArray()) {
            if (Character.isUpperCase(ch)) hasUpper = true;
            else if (Character.isLowerCase(ch)) hasLower = true;
            else if (Character.isDigit(ch)) hasDigit = true;
            else hasSpecial = true;
        }

        int score = 0;
        if (password.length() >= 8) score++;
        if (hasUpper) score++;
        if (hasLower) score++;
        if (hasDigit) score++;
        if (hasSpecial) score++;

        System.out.println("\n---- Password Strength ----");

        if (score <= 2) {
            System.out.println("Weak Password ❌");
        } else if (score == 3 || score == 4) {
            System.out.println("Moderate Password ⚠️");
        } else {
            System.out.println("Strong Password ✅");
        }

        sc.close();
    }
}