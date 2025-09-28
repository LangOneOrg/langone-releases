@echo off
echo ========================================
echo LangOne Performance Benchmark Suite
echo ========================================
echo.

echo Building benchmarks...
echo.

REM Build C++
echo Building C++ benchmarks...
g++ -O2 -o cpp_fibonacci cpp_fibonacci.cpp
g++ -O2 -o cpp_hanoi cpp_hanoi.cpp
g++ -O2 -o cpp_dijkstra cpp_dijkstra.cpp

REM Build C#
echo Building C# benchmarks...
csc /optimize+ csharp_fibonacci.cs
csc /optimize+ csharp_hanoi.cs
csc /optimize+ csharp_dijkstra.cs

REM Build Go
echo Building Go benchmarks...
go build -o go_fibonacci fibonacci.go
go build -o go_hanoi hanoi.go
go build -o go_dijkstra dijkstra.go

REM Build Rust
echo Building Rust benchmarks...
rustc -O -o rust_fibonacci fibonacci.rs
rustc -O -o rust_hanoi hanoi.rs
rustc -O -o rust_dijkstra dijkstra.rs

echo.
echo ========================================
echo Running Performance Tests
echo ========================================
echo.

echo 1. FIBONACCI SEQUENCE BENCHMARKS
echo ========================================
echo.

echo Running LangOne Fibonacci...
cd ..\..\code\samples\recursive_algorithms
..\..\..\..\release_package\v0.1.0-alpha.2\windows-x64\lo.exe run fibonacci_fixed.l1
cd ..\..\..\docs\benchmarks

echo.
echo Running C++ Fibonacci...
cpp_fibonacci.exe

echo.
echo Running C# Fibonacci...
csharp_fibonacci.exe

echo.
echo Running Go Fibonacci...
go_fibonacci.exe

echo.
echo Running Rust Fibonacci...
rust_fibonacci.exe

echo.
echo 2. TOWER OF HANOI BENCHMARKS
echo ========================================
echo.

echo Running LangOne Tower of Hanoi...
cd ..\..\code\samples\recursive_algorithms
..\..\..\..\release_package\v0.1.0-alpha.2\windows-x64\lo.exe run tower_of_hanoi.l1
cd ..\..\..\docs\benchmarks

echo.
echo Running C++ Tower of Hanoi...
cpp_hanoi.exe

echo.
echo Running C# Tower of Hanoi...
csharp_hanoi.exe

echo.
echo Running Go Tower of Hanoi...
go_hanoi.exe

echo.
echo Running Rust Tower of Hanoi...
rust_hanoi.exe

echo.
echo 3. DIJKSTRA'S ALGORITHM BENCHMARKS
echo ========================================
echo.

echo Running LangOne Dijkstra...
cd ..\..\code\samples\data_structures
..\..\..\..\release_package\v0.1.0-alpha.2\windows-x64\lo.exe run graph_dijkstra_fixed.l1
cd ..\..\..\docs\benchmarks

echo.
echo Running C++ Dijkstra...
cpp_dijkstra.exe

echo.
echo Running C# Dijkstra...
csharp_dijkstra.exe

echo.
echo Running Go Dijkstra...
go_dijkstra.exe

echo.
echo Running Rust Dijkstra...
rust_dijkstra.exe

echo.
echo ========================================
echo Benchmark Suite Complete
echo ========================================
echo.
echo Results saved to performance_results.txt
echo See PERFORMANCE_COMPARISON_REPORT.md for detailed analysis
echo.

pause
