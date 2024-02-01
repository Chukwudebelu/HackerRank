import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {
    /*
     * Complete the 'miniMaxSum' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */
    public static void miniMaxSum(List<Integer> arr) {
        // Write your code here        
        // Since output can be greater than 'int' (32-bit integer)
        // Use 'long' data type
        long minSum, maxSum, sum_;
        minSum = maxSum = arr.get(0);
        sum_ = 0;
        
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < minSum) { // Smallest integer
                minSum = arr.get(i);
            }
            if (arr.get(i) > maxSum) { // Largest integer
                maxSum = arr.get(i);
            }
            sum_ += arr.get(i);
        }
        
        long num1 = sum_ - maxSum;
        long num2 = sum_ - minSum;
        System.out.print(num1 + " " + num2);
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.miniMaxSum(arr);

        bufferedReader.close();
    }
}
