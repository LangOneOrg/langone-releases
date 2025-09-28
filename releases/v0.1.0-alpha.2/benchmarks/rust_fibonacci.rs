use std::time::Instant;

// Recursive Fibonacci
fn fib_recursive(n: i32) -> i64 {
    match n {
        n if n <= 0 => 0,
        n if n == 1 => 1,
        _ => fib_recursive(n - 1) + fib_recursive(n - 2),
    }
}

// Iterative Fibonacci
fn fib_iterative(n: i32) -> i64 {
    match n {
        n if n <= 0 => 0,
        n if n == 1 => 1,
        _ => {
            let mut a = 0i64;
            let mut b = 1i64;
            for _ in 2..=n {
                let temp = b;
                b = a + b;
                a = temp;
            }
            b
        }
    }
}

fn main() {
    // Test recursive
    let start = Instant::now();
    let result_rec = fib_recursive(35);
    let duration_rec = start.elapsed();
    
    // Test iterative
    let start = Instant::now();
    let result_iter = fib_iterative(1000);
    let duration_iter = start.elapsed();
    
    println!("Rust Fibonacci Results:");
    println!("Recursive F(35) = {} in {:?}", result_rec, duration_rec);
    println!("Iterative F(1000) = {} in {:?}", result_iter, duration_iter);
}
