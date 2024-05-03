using System;

namespace FibonacciCalculator
{
    internal class Program
    {
        // Main method to calculate Fibonacci sequence based on user input.
        static void Main(string[] args)
        {
            int answer;
            do
            {
                try
                {
                    Console.WriteLine("How long should your Fibonacci sequence be?");
                    int length;
                    while (!int.TryParse(Console.ReadLine(), out length) || length < 0)
                    {
                        Console.WriteLine("Invalid input. Please enter a non-negative integer.");
                    }

                    PrintFibonacciSequence(length);
                    
                    // Provide a warning if the sequence is too large for recursive calculation
                    if (length > 36)
                        Console.WriteLine("As you can see, the recursive method is much more performance-intensive for larger sequences.");
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }

                Console.WriteLine("Do you want to calculate another Fibonacci sequence? (Enter 0 for Yes, 1 for No)");
            } while (!int.TryParse(Console.ReadLine(), out answer) || answer != 1);
        }
        
        // Prints the Fibonacci sequence up to the specified length.
        public static void PrintFibonacciSequence(int length)
        {
            Console.WriteLine("Iterative Fibonacci:");
            for (int i = 0; i <= length; i++)
            {
                Console.WriteLine(IterativeFibonacci(i));
            }

            Console.WriteLine("\nRecursive Fibonacci:");
            for (int i = 0; i <= length; i++)
            {
                Console.WriteLine(RecursiveFibonacci(i));
            }
        }

        // Calculates the nth Fibonacci number using an iterative approach.
        public static int IterativeFibonacci(int n)
        {
            if (n <= 0) return 0;
            if (n == 1) return 1;

            int prev = 0;
            int current = 1;
            for (int i = 2; i <= n; i++)
            {
                int temp = current;
                current = prev + current;
                prev = temp;
            }
            return current;
        }

        
        // Calculates the nth Fibonacci number using a recursive approach.
        public static int RecursiveFibonacci(int n)
        {
            if (n <= 0) return 0;
            if (n == 1) return 1;

            return RecursiveFibonacci(n - 1) + RecursiveFibonacci(n - 2);
        }
    }
}