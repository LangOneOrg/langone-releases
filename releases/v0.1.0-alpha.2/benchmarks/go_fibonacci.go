package main

import (
    "fmt"
    "time"
)

// Recursive Fibonacci
func fibRecursive(n int) int64 {
    if n <= 0 {
        return 0
    }
    if n == 1 {
        return 1
    }
    return fibRecursive(n-1) + fibRecursive(n-2)
}

// Iterative Fibonacci
func fibIterative(n int) int64 {
    if n <= 0 {
        return 0
    }
    if n == 1 {
        return 1
    }
    
    a, b := int64(0), int64(1)
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}

func main() {
    // Test recursive
    start := time.Now()
    resultRec := fibRecursive(35)
    durationRec := time.Since(start)
    
    // Test iterative
    start = time.Now()
    resultIter := fibIterative(1000)
    durationIter := time.Since(start)
    
    fmt.Println("Go Fibonacci Results:")
    fmt.Printf("Recursive F(35) = %d in %v\n", resultRec, durationRec)
    fmt.Printf("Iterative F(1000) = %d in %v\n", resultIter, durationIter)
}
