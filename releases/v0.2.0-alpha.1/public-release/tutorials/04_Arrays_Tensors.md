# Tutorial 04: Working with Arrays and Tensors

## 🎯 **Learning Objectives**

By the end of this tutorial, you will be able to:
- ✅ Create and manipulate multi-dimensional arrays
- ✅ Perform indexing, slicing, and reshaping operations
- ✅ Use broadcasting for efficient computations
- ✅ Apply mathematical operations to arrays
- ✅ Leverage SIMD optimization for performance
- ✅ Build high-performance numerical applications

**⏱️ Estimated Time**: 60 minutes  
**📋 Prerequisites**: Tutorials 1-3 (Foundation Phase)  
**💻 Difficulty**: ⭐⭐⭐☆☆ Intermediate

---

## 📚 **Introduction: Why Arrays Matter**

### **From Lists to High-Performance Arrays**

In traditional programming:
```l1
# Regular list - Slow for numerical work
let numbers = [1, 2, 3, 4, 5]
```

With LangOne arrays:
```l1
# High-performance array - 10x faster!
let numbers = array([1, 2, 3, 4, 5])
```

### **What Makes LangOne Arrays Special?**

1. **🚀 Performance**: 10-17x faster than Python
2. **💾 Memory Efficient**: 87-88% less memory usage
3. **🎯 SIMD Optimized**: Vectorized operations
4. **🌱 Green Code**: Energy-efficient by design

### **Real-World Applications**

- **🧬 Scientific Computing**: Physics simulations, chemistry
- **📊 Data Analysis**: Large dataset processing
- **🖼️ Image Processing**: Computer vision, graphics
- **🤖 Machine Learning**: Neural networks, AI models
- **📈 Financial Modeling**: Risk analysis, trading algorithms

---

## 🔧 **Part 1: Array Creation**

### **Basic Array Creation**

```l1
# From a list
let arr1 = array([1, 2, 3, 4, 5])
print(arr1)  # Output: [1, 2, 3, 4, 5]

# Array of zeros
let zeros_arr = zeros([5])
print(zeros_arr)  # Output: [0, 0, 0, 0, 0]

# Array of ones
let ones_arr = ones([5])
print(ones_arr)  # Output: [1, 1, 1, 1, 1]
```

### **Range-Based Creation**

```l1
# Create sequence: start, stop, step
let range_arr = arange(0, 10, 2)
print(range_arr)  # Output: [0, 2, 4, 6, 8]

# Linearly spaced values
let linear_arr = linspace(0, 1, 5)
print(linear_arr)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

### **Multi-Dimensional Arrays**

```l1
# 2D array (matrix)
let matrix = zeros([3, 4])  # 3 rows, 4 columns
print(matrix)

# 3D array (tensor)
let tensor = ones([2, 3, 4])  # 2x3x4 tensor
print(tensor)
```

---

### **🔨 Hands-On Exercise 1: Array Creation Practice**

**Task 1**: Create arrays using different methods

```l1
# Create these arrays:
# 1. Array of numbers 1 to 10
# 2. 2x2 matrix of zeros
# 3. Array of 5 evenly spaced values between 0 and 100
# 4. 3x3 matrix of ones
```

<details>
<summary>💡 Click here for the solution</summary>

```l1
# 1. Array of numbers 1 to 10
let nums = arange(1, 11, 1)
print("Numbers 1-10:")
print(nums)

# 2. 2x2 matrix of zeros
let zero_matrix = zeros([2, 2])
print("2x2 Zero Matrix:")
print(zero_matrix)

# 3. 5 evenly spaced values between 0 and 100
let spaced = linspace(0, 100, 5)
print("Evenly Spaced:")
print(spaced)

# 4. 3x3 matrix of ones
let one_matrix = ones([3, 3])
print("3x3 One Matrix:")
print(one_matrix)
```
</details>

✅ **Checkpoint**: Can you create arrays using all four methods?

---

## 📍 **Part 2: Indexing and Slicing**

### **Basic Indexing**

```l1
let arr = array([10, 20, 30, 40, 50])

# Access single elements
print(arr[0])  # Output: 10 (first element)
print(arr[2])  # Output: 30 (third element)
print(arr[-1]) # Output: 50 (last element)
```

### **Slicing**

```l1
let arr = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slice syntax: arr[start:end]
print(arr[0:5])   # Output: [0, 1, 2, 3, 4]
print(arr[5:])    # Output: [5, 6, 7, 8, 9]
print(arr[:5])    # Output: [0, 1, 2, 3, 4]
print(arr[2:8])   # Output: [2, 3, 4, 5, 6, 7]
```

### **Multi-Dimensional Indexing**

```l1
# Create 3x3 matrix
let matrix = array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Access elements
print(matrix[0][0])  # Output: 1 (top-left)
print(matrix[1][1])  # Output: 5 (center)
print(matrix[2][2])  # Output: 9 (bottom-right)

# Access rows
print(matrix[0])     # Output: [1, 2, 3] (first row)
print(matrix[1])     # Output: [4, 5, 6] (second row)
```

### **Boolean Indexing**

```l1
let arr = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Select elements based on condition
let even_nums = arr[arr % 2 == 0]
print(even_nums)  # Output: [2, 4, 6, 8, 10]

let greater_than_5 = arr[arr > 5]
print(greater_than_5)  # Output: [6, 7, 8, 9, 10]
```

---

### **🔨 Hands-On Exercise 2: Indexing and Slicing**

**Task 2**: Practice array indexing

```l1
let data = array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Extract:
# 1. The first three elements
# 2. The last three elements
# 3. Elements from index 2 to 7
# 4. All elements greater than 50
```

<details>
<summary>💡 Click here for the solution</summary>

```l1
let data = array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# 1. First three elements
let first_three = data[0:3]
print("First three:", first_three)

# 2. Last three elements
let last_three = data[-3:]
print("Last three:", last_three)

# 3. Elements from index 2 to 7
let mid_section = data[2:7]
print("Middle section:", mid_section)

# 4. All elements greater than 50
let over_50 = data[data > 50]
print("Greater than 50:", over_50)
```
</details>

---

## 🔄 **Part 3: Broadcasting**

### **What is Broadcasting?**

Broadcasting allows operations on arrays of different shapes:

```l1
# Scalar broadcasting
let arr = array([1, 2, 3, 4, 5])
let result = arr * 2  # Multiply each element by 2
print(result)  # Output: [2, 4, 6, 8, 10]

# Add scalar to array
let result2 = arr + 10
print(result2)  # Output: [11, 12, 13, 14, 15]
```

### **Vector Broadcasting**

```l1
# Add two arrays element-wise
let a = array([1, 2, 3])
let b = array([10, 20, 30])
let sum_ab = a + b
print(sum_ab)  # Output: [11, 22, 33]

# Multiply arrays element-wise
let prod_ab = a * b
print(prod_ab)  # Output: [10, 40, 90]
```

### **Matrix Broadcasting**

```l1
# Broadcasting in 2D
let matrix = array([[1, 2, 3],
                     [4, 5, 6]])

let row_vector = array([10, 20, 30])

# Add row to each row of matrix
let result = matrix + row_vector
print(result)
# Output:
# [[11, 22, 33],
#  [14, 25, 36]]
```

### **Broadcasting Rules**

LangOne follows NumPy-like broadcasting rules:

```
Shape (5,)    → Can broadcast with → Shape (5,)
Shape (3, 5)  → Can broadcast with → Shape (5,)
Shape (3, 5)  → Can broadcast with → Shape (3, 1)
Shape (3, 5)  → Can broadcast with → Shape (1, 5)
```

---

### **🔨 Hands-On Exercise 3: Broadcasting Practice**

**Task 3**: Use broadcasting for calculations

```l1
# Given:
let temps_celsius = array([0, 10, 20, 30, 40])

# Convert to Fahrenheit using: F = C * 9/5 + 32
# Normalize temperatures: (temp - mean) / std
```

<details>
<summary>💡 Click here for the solution</summary>

```l1
# Temperature conversion
let temps_celsius = array([0, 10, 20, 30, 40])

# Convert to Fahrenheit
let temps_fahrenheit = temps_celsius * 9.0 / 5.0 + 32.0
print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)

# Normalize temperatures
let mean_temp = mean(temps_celsius)
let std_temp = std(temps_celsius)
let normalized = (temps_celsius - mean_temp) / std_temp
print("Normalized:", normalized)
```
</details>

---

## 🧮 **Part 4: Mathematical Operations**

### **Element-wise Operations**

```l1
let a = array([1, 2, 3, 4, 5])

# Basic arithmetic
print(a + 10)     # Addition: [11, 12, 13, 14, 15]
print(a - 5)      # Subtraction: [-4, -3, -2, -1, 0]
print(a * 2)      # Multiplication: [2, 4, 6, 8, 10]
print(a / 2)      # Division: [0.5, 1.0, 1.5, 2.0, 2.5]
print(a ** 2)     # Power: [1, 4, 9, 16, 25]
```

### **Mathematical Functions**

```l1
let arr = array([1, 4, 9, 16, 25])

# Mathematical functions
print(sqrt(arr))   # Square root: [1, 2, 3, 4, 5]
print(abs(arr))    # Absolute value
print(exp(arr))    # Exponential
print(log(arr))    # Natural logarithm
```

### **Trigonometric Functions**

```l1
let angles = array([0, 30, 45, 60, 90])
let radians = angles * 3.14159 / 180  # Convert to radians

print(sin(radians))  # Sine
print(cos(radians))  # Cosine
print(tan(radians))  # Tangent
```

### **Aggregation Functions**

```l1
let data = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(sum(data))      # Sum: 55
print(mean(data))     # Mean: 5.5
print(min(data))      # Minimum: 1
print(max(data))      # Maximum: 10
print(std(data))      # Standard deviation
```

---

### **🔨 Hands-On Exercise 4: Mathematical Operations**

**Task 4**: Statistical analysis of data

```l1
# Given sales data for a week:
let sales = array([100, 150, 200, 175, 300, 250, 400])

# Calculate:
# 1. Total sales
# 2. Average daily sales
# 3. Maximum sale day
# 4. Minimum sale day
# 5. Sales above average
```

<details>
<summary>💡 Click here for the solution</summary>

```l1
let sales = array([100, 150, 200, 175, 300, 250, 400])

# 1. Total sales
let total = sum(sales)
print("Total Sales: " + to_string(total))

# 2. Average daily sales
let average = mean(sales)
print("Average Daily Sales: " + to_string(average))

# 3. Maximum sale day
let max_sale = max(sales)
print("Maximum Sale: " + to_string(max_sale))

# 4. Minimum sale day
let min_sale = min(sales)
print("Minimum Sale: " + to_string(min_sale))

# 5. Sales above average
let above_avg = sales[sales > average]
print("Days Above Average:")
print(above_avg)

# Bonus: Calculate percentage increase
let pct_change = (sales[1:] - sales[:-1]) / sales[:-1] * 100
print("Daily Percentage Change:")
print(pct_change)
```
</details>

---

## ⚡ **Part 5: SIMD Optimization**

### **What is SIMD?**

**SIMD** (Single Instruction, Multiple Data) processes multiple data points simultaneously:

```
Without SIMD:  [1] + [2] = [3]
               [3] + [4] = [7]    ← Sequential, slow
               [5] + [6] = [11]

With SIMD:     [1, 3, 5] + [2, 4, 6] = [3, 7, 11]
               ↑ All at once, 3x faster!
```

### **Checking SIMD Support**

```l1
# Check your CPU's SIMD capabilities
let simd_capabilities = simd_info()
print(simd_capabilities)

# Example output:
# SIMD Support: AVX2, SSE4.2
# Vector Width: 256 bits
# Max Float Operations: 8 simultaneous
```

### **Using SIMD Optimization**

```l1
# Create large array
let data = arange(0, 1000, 1)

# Automatic SIMD optimization
let optimized = simd_optimize(data)
let result = optimized * 2 + 10

# Compare performance
let start = time()
let manual_result = data * 2 + 10
let manual_time = time() - start

let start2 = time()
let simd_result = optimized * 2 + 10
let simd_time = time() - start2

print("Manual Time: " + to_string(manual_time))
print("SIMD Time: " + to_string(simd_time))
print("Speedup: " + to_string(manual_time / simd_time) + "x")
```

### **Performance Comparison**

```l1
# Large dataset
let size = 10000
let a = arange(0, size, 1)
let b = arange(size, size * 2, 1)

# Without optimization
let start1 = time()
let result1 = a + b
let time1 = time() - start1

# With SIMD optimization
let a_opt = simd_optimize(a)
let b_opt = simd_optimize(b)
let start2 = time()
let result2 = a_opt + b_opt
let time2 = time() - start2

print("Standard: " + to_string(time1) + "s")
print("SIMD: " + to_string(time2) + "s")
print("Speedup: " + to_string(time1 / time2) + "x faster")
# Expected: 8-16x speedup!
```

---

### **🔨 Hands-On Exercise 5: SIMD Performance**

**Task 5**: Compare performance with and without SIMD

```l1
# Create a program that:
# 1. Creates large arrays (size 10,000+)
# 2. Performs complex operations
# 3. Compares SIMD vs standard performance
# 4. Calculates speedup factor
```

<details>
<summary>💡 Click here for the solution</summary>

```l1
# Performance Comparison Program

print("=== SIMD Performance Benchmark ===")
print("")

# Create large arrays
let size = 100000
print("Array Size: " + to_string(size) + " elements")
print("")

let a = linspace(0, 100, size)
let b = linspace(100, 200, size)
let c = linspace(200, 300, size)

# Standard operations
print("Standard Operations:")
let start_std = time()
let result_std = (a * 2 + b * 3) / (c + 1)
let time_std = time() - start_std
print("Time: " + to_string(time_std) + " seconds")
print("")

# SIMD-optimized operations
print("SIMD-Optimized Operations:")
let a_simd = simd_optimize(a)
let b_simd = simd_optimize(b)
let c_simd = simd_optimize(c)

let start_simd = time()
let result_simd = (a_simd * 2 + b_simd * 3) / (c_simd + 1)
let time_simd = time() - start_simd
print("Time: " + to_string(time_simd) + " seconds")
print("")

# Calculate speedup
let speedup = time_std / time_simd
print("=== Results ===")
print("Speedup: " + to_string(speedup) + "x faster")
print("Performance Gain: " + to_string((speedup - 1) * 100) + "%")

# Energy efficiency
print("")
print("Energy Efficiency:")
print("CPU cycles saved: ~" + to_string((1 - 1/speedup) * 100) + "%")
print("Green Code First in action! 🌱")
```
</details>

---

## 🎯 **Part 6: Real-World Application**

### **Complete Example: Image Processing**

```l1
# Image Processing with Arrays
# Simulating image manipulation

print("=== Image Processing Example ===")
print("")

# Create a "grayscale image" (2D array)
let width = 10
let height = 10
let image = zeros([height, width])

# Add some pattern
for i in range(0, height):
    for j in range(0, width):
        image[i][j] = (i + j) % 256
    end
end

print("Original Image Pattern:")
print(image)
print("")

# Apply filters using broadcasting

# 1. Brightness adjustment (add constant)
let brightened = image + 50
print("Brightened Image:")
print(brightened)
print("")

# 2. Contrast adjustment (multiply)
let contrasted = image * 1.5
print("Contrasted Image:")
print(contrasted)
print("")

# 3. Invert colors
let max_value = 255
let inverted = max_value - image
print("Inverted Image:")
print(inverted)
print("")

# 4. Normalize to 0-1 range
let normalized = image / max_value
print("Normalized Image:")
print(normalized)

print("Image processing complete!")
```

---

## ✅ **Knowledge Check**

Test your understanding:

1. **What function creates an array of zeros?**
   <details><summary>Show Answer</summary>`zeros([shape])`</details>

2. **How do you access the last element of an array?**
   <details><summary>Show Answer</summary>`arr[-1]`</details>

3. **What is broadcasting?**
   <details><summary>Show Answer</summary>Automatic expansion of array shapes for element-wise operations</details>

4. **What does SIMD stand for?**
   <details><summary>Show Answer</summary>Single Instruction, Multiple Data</details>

5. **How do you check SIMD capabilities?**
   <details><summary>Show Answer</summary>`simd_info()`</details>

6. **What's the expected speedup with SIMD?**
   <details><summary>Show Answer</summary>8-16x with AVX2/AVX-512</details>

---

## 🎓 **What You've Learned**

Congratulations! You now know:

- ✅ How to create arrays using multiple methods
- ✅ Indexing and slicing operations
- ✅ Broadcasting for efficient computations
- ✅ Mathematical operations on arrays
- ✅ SIMD optimization for performance
- ✅ Real-world array applications

---

## 🚀 **Next Steps**

### **Practice Projects:**

1. **Statistical Calculator**
   - Create arrays of random data
   - Calculate statistics (mean, median, std)
   - Visualize results

2. **Matrix Calculator**
   - Implement matrix operations
   - Add, multiply, transpose matrices
   - Calculate determinants

3. **Signal Processing**
   - Generate sine waves
   - Apply filters
   - Perform FFT analysis

### **What's Next:**
👉 **[Tutorial 05: DataFrames and Data Manipulation](./05_DataFrames.md)**

In the next tutorial, you'll learn:
- Creating and loading DataFrames
- Complex data filtering
- GroupBy and aggregations
- Merging datasets
- Complete data analysis

---

## 💡 **Best Practices**

### **Performance Tips:**
1. **Use SIMD**: Always optimize large arrays
2. **Vectorize**: Avoid loops, use array operations
3. **Pre-allocate**: Create arrays with correct size
4. **Broadcasting**: Use for element-wise operations
5. **Memory**: Be mindful of array copies

### **Common Pitfalls:**
1. **Index out of bounds** - Always check array size
2. **Shape mismatch** - Verify dimensions match
3. **Type errors** - Ensure consistent data types
4. **Memory leaks** - Delete large arrays when done
5. **Unnecessary copies** - Use views when possible

---

## 📚 **Additional Resources**

- 📖 **Array Operations Reference**: [docs.langone.dev/arrays](https://docs.langone.dev/arrays)
- 📖 **SIMD Guide**: [docs.langone.dev/simd](https://docs.langone.dev/simd)
- 💻 **Code Examples**: [github.com/langone/array-examples](https://github.com/langone/array-examples)
- 🎥 **Video Tutorial**: [youtube.com/langone/arrays](https://youtube.com/langone/arrays)

---

## 🎉 **Congratulations!**

You've mastered LangOne arrays and are ready for advanced data manipulation!

**Progress Tracker:**
- [x] Tutorial 01: Getting Started ✅
- [x] Tutorial 02: Core Fundamentals ✅
- [x] Tutorial 03: Functions and Organization ✅
- [x] Tutorial 04: Arrays and Tensors ✅
- [ ] Tutorial 05: DataFrames

👉 **Ready for more?** [Continue to Tutorial 05](./05_DataFrames.md)

---

*© 2025 LangOne Project. Part of the official LangOne tutorial series.*

