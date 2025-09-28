#include <iostream>
#include <chrono>
#include <vector>

// Recursive Fibonacci
long long fib_recursive(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fib_recursive(n - 1) + fib_recursive(n - 2);
}

// Iterative Fibonacci
long long fib_iterative(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    
    long long a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        long long temp = b;
        b = a + b;
        a = temp;
    }
    return b;
}

int main() {
    // Test recursive (smaller number due to exponential complexity)
    auto start = std::chrono::high_resolution_clock::now();
    long long result_rec = fib_recursive(35);
    auto end = std::chrono::high_resolution_clock::now();
    auto duration_rec = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    
    // Test iterative
    start = std::chrono::high_resolution_clock::now();
    long long result_iter = fib_iterative(1000);
    end = std::chrono::high_resolution_clock::now();
    auto duration_iter = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    std::cout << "C++ Fibonacci Results:" << std::endl;
    std::cout << "Recursive F(35) = " << result_rec << " in " << duration_rec.count() << "ms" << std::endl;
    std::cout << "Iterative F(1000) = " << result_iter << " in " << duration_iter.count() << "μs" << std::endl;
    
    return 0;
}
