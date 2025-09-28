using System;
using System.Diagnostics;

class Program {
    // Recursive Fibonacci
    static long FibRecursive(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        return FibRecursive(n - 1) + FibRecursive(n - 2);
    }
    
    // Iterative Fibonacci
    static long FibIterative(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        
        long a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            long temp = b;
            b = a + b;
            a = temp;
        }
        return b;
    }
    
    static void Main() {
        // Test recursive
        var stopwatch = Stopwatch.StartNew();
        long resultRec = FibRecursive(35);
        stopwatch.Stop();
        
        // Test iterative
        stopwatch.Restart();
        long resultIter = FibIterative(1000);
        stopwatch.Stop();
        var iterTime = stopwatch.Elapsed.TotalMicroseconds;
        
        Console.WriteLine("C# (.NET) Fibonacci Results:");
        Console.WriteLine($"Recursive F(35) = {resultRec} in {stopwatch.ElapsedMilliseconds}ms");
        Console.WriteLine($"Iterative F(1000) = {resultIter} in {iterTime:F3}μs");
    }
}
