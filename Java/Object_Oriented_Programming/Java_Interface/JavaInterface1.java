import java.util.*;

interface AdvancedArithmetic
{
    int divisor_sum(int n);
}

// Write your code here
class MyCalculator implements AdvancedArithmetic
{
    public int divisor_sum(int n)
    {
        // Sum of all the divisors or factors of the number n
        int factor_sum = 0;
        for (int j = 1; j <= (n/2); j++)
        {
            if (n % j == 0) 
            {
                factor_sum += j;
            }
        }
    return factor_sum + n;
    }
}

class Solution 
{
    public static void main(String[] args)
    {
        MyCalculator my_calculator = new MyCalculator();
        System.out.print("I implemented: ");
        ImplementedInterfaceNames(my_calculator);
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.print(my_calculator.divisor_sum(n) + "\n");
        sc.close(); // Close Scanner Object
    }
    /*
    *  ImplementedInterfaceNames method takes an object and
    *  prints the name of the interfaces it implemented
    */
    static void ImplementedInterfaceNames(Object o)
    {
        Class[] theInterfaces = o.getClass().getInterfaces();
        for (int i = 0; i < theInterfaces.length; i++)
        {
            String interfaceName = theInterfaces[i].getName();
            System.out.println(interfaceName);
        }
    }
}
