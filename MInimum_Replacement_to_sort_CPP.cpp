import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static long minimumReplacement(List<Integer> nums) {
        long ans = 0;

        int max = nums.get(nums.size() - 1);
        for (int i = nums.size() - 2; i >= 0; --i) {
            int ops = (nums.get(i) - 1) / max;
            ans += ops;
            max = nums.get(i) / (ops + 1);
        }

        return ans;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt(); // Read the number of elements in the array

        List<Integer> nums = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            nums.add(scanner.nextInt()); // Read the array elements
        }

        long result = minimumReplacement(nums); // Calculate the result

        System.out.println(result); // Print the result
    }
}
