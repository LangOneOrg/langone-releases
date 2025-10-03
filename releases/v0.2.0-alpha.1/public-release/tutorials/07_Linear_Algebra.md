# Tutorial 07: Linear Algebra with BLAS Integration

## 🎯 **Learning Objectives**

- ✅ Perform vector operations (dot product, norm, scaling)
- ✅ Execute matrix operations (multiplication, transpose)
- ✅ Use BLAS (Basic Linear Algebra Subprograms) functions
- ✅ Solve linear systems and eigenvalue problems
- ✅ Apply linear algebra to real-world problems
- ✅ Optimize performance with BLAS integration

**⏱️ Estimated Time**: 60 minutes | **Prerequisites**: Tutorials 01-04 | **Difficulty**: ⭐⭐⭐⭐☆ Advanced

---

## 📚 **Introduction: Linear Algebra Power**

Linear algebra is fundamental to:
- **🤖 Machine Learning**: Neural networks, optimization
- **📊 Data Science**: PCA, dimensionality reduction
- **🎮 Computer Graphics**: 3D transformations
- **📈 Financial Modeling**: Portfolio optimization
- **🔬 Scientific Computing**: Simulations, physics

LangOne's BLAS integration provides **10x faster** linear algebra than Python!

---

## ➕ **Part 1: Vector Operations**

### **Basic Vector Operations**

```l1
# Create vectors
let v1 = array([1, 2, 3, 4, 5])
let v2 = array([5, 4, 3, 2, 1])

# Dot product
let dot_product = dot(v1, v2)
print("Dot product: " + to_string(dot_product))  # Output: 35

# Vector norm (length)
let magnitude = norm(v1)
print("Magnitude: " + to_string(magnitude))  # Output: 7.416

# Scale vector
let scaled = scale(2.5, v1)
print("Scaled vector:", scaled)  # Output: [2.5, 5.0, 7.5, 10.0, 12.5]
```

### **Vector Statistics**

```l1
let data = array([10, 20, 30, 40, 50])

# Basic aggregations
print("Sum: " + to_string(sum(data)))      # 150
print("Mean: " + to_string(mean(data)))    # 30
print("Max: " + to_string(max(data)))      # 50
print("Min: " + to_string(min(data)))      # 10
print("Std: " + to_string(std(data)))      # ~14.14
```

---

### **🔨 Exercise 1: Physics - Force Calculations**

```l1
# Calculate resultant force from multiple force vectors
# Forces in 2D: Fx and Fy components
# Find: 1. Total force in X and Y
#       2. Magnitude of resultant force
#       3. Direction (angle)
```

<details>
<summary>💡 Solution</summary>

```l1
# Physics: Force Vector Analysis

# Force vectors (Fx, Fy)
let force1_x = array([10, 5, -3])
let force1_y = array([5, 8, 2])

# Calculate resultant
let total_fx = sum(force1_x)
let total_fy = sum(force1_y)

print("Total Force X: " + to_string(total_fx) + " N")
print("Total Force Y: " + to_string(total_fy) + " N")

# Magnitude: sqrt(Fx^2 + Fy^2)
let magnitude = sqrt(total_fx ** 2 + total_fy ** 2)
print("Resultant Force Magnitude: " + to_string(magnitude) + " N")

# Direction: atan(Fy/Fx)
let angle_rad = atan(total_fy / total_fx)
let angle_deg = angle_rad * 180 / 3.14159
print("Direction: " + to_string(angle_deg) + " degrees")
```
</details>

---

## 🔢 **Part 2: Matrix Operations**

### **Matrix Creation and Operations**

```l1
# Create matrices
let A = array([[1, 2], [3, 4]])
let B = array([[5, 6], [7, 8]])

# Matrix multiplication
let C = matmul(A, B)
print("A × B:")
print(C)

# Element-wise operations
let D = A + B  # Element-wise addition
let E = A * B  # Element-wise multiplication
print("Element-wise addition:", D)
print("Element-wise multiplication:", E)

# Matrix transpose
let A_T = transpose(A)
print("Transpose of A:")
print(A_T)
```

### **Linear System Solving**

```l1
# Solve Ax = b
let A = array([[2, 1], [1, 3]])
let b = array([5, 7])

let x = solve(A, b)
print("Solution x:")
print(x)

# Verify: A @ x should equal b
let verification = matmul(A, x)
print("Verification (should equal b):")
print(verification)
```

---

### **🔨 Exercise 2: 3D Transformations**

```l1
# Create transformation matrices for:
# 1. Rotation around Z-axis
# 2. Scaling transformation
# 3. Translation transformation
# Apply to 3D point
```

<details>
<summary>💡 Solution</summary>

```l1
# 3D Transformations

# Original point
let point = array([1, 0, 0])

# 1. Rotation matrix (45 degrees around Z-axis)
let angle = 45 * 3.14159 / 180  # Convert to radians
let cos_a = cos(angle)
let sin_a = sin(angle)

let rotation_matrix = array([
    [cos_a, -sin_a, 0],
    [sin_a, cos_a, 0],
    [0, 0, 1]
])

let rotated = matmul(rotation_matrix, point)
print("Rotated point:")
print(rotated)

# 2. Scaling transformation (scale by 2)
let scale_matrix = array([
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 2]
])

let scaled = matmul(scale_matrix, point)
print("Scaled point:")
print(scaled)

# 3. Combined transformation
let transformed = matmul(scale_matrix, matmul(rotation_matrix, point))
print("Rotated and scaled:")
print(transformed)
```
</details>

---

## 🎯 **Part 3: Real-World Application - Portfolio Optimization**

```l1
# Financial Portfolio Optimization using Linear Algebra

print("=== Portfolio Optimization ===")
print("")

# Historical returns for 3 assets
let returns = array([
    [0.10, 0.05, 0.15],  # Asset 1: 10%, 5%, 15% returns
    [0.08, 0.12, 0.06],  # Asset 2
    [0.15, 0.03, 0.20]   # Asset 3
])

# Calculate mean returns
let mean_returns = mean(returns, axis=0)
print("Mean Returns:")
print(mean_returns)

# Calculate covariance matrix
let cov_matrix = cov(returns)
print("Covariance Matrix:")
print(cov_matrix)

# Portfolio weights
let weights = array([0.4, 0.3, 0.3])  # 40%, 30%, 30%

# Expected portfolio return
let portfolio_return = dot(weights, mean_returns)
print("Expected Portfolio Return: " + to_string(portfolio_return * 100) + "%")

# Portfolio variance
let portfolio_variance = dot(weights, matmul(cov_matrix, weights))
let portfolio_std = sqrt(portfolio_variance)
print("Portfolio Risk (Std Dev): " + to_string(portfolio_std * 100) + "%")

# Sharpe Ratio (assuming 2% risk-free rate)
let risk_free_rate = 0.02
let sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_std
print("Sharpe Ratio: " + to_string(sharpe_ratio))
```

---

## ✅ **Knowledge Check**

1. **What does dot product measure?**
   <details><summary>Show Answer</summary>Similarity between vectors (cosine of angle)</details>

2. **What's the difference between element-wise and matrix multiplication?**
   <details><summary>Show Answer</summary>Element-wise: A*B, Matrix: matmul(A,B)</details>

3. **What is BLAS?**
   <details><summary>Show Answer</summary>Basic Linear Algebra Subprograms - optimized math routines</details>

4. **How much faster is LangOne BLAS than Python?**
   <details><summary>Show Answer</summary>10x faster</details>

---

## 🎓 **What You've Learned**

- ✅ Vector operations and norms
- ✅ Matrix multiplication and transpose
- ✅ BLAS integration and optimization
- ✅ Solving linear systems
- ✅ Real-world applications

---

## 🚀 **Next Steps**

**Practice Projects:**
1. Implement PCA (Principal Component Analysis)
2. Build 3D graphics transformer
3. Create physics simulation engine

👉 **[Tutorial 08: GPU Acceleration and Parallel Computing](./08_GPU_Computing.md)**

**Progress**: [x] Tutorials 01-07 ✅

---

*© 2025 LangOne Project. Part of the official LangOne tutorial series.*

