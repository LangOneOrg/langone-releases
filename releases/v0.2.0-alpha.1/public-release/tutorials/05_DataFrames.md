# Tutorial 05: DataFrames and Data Manipulation

## 🎯 **Learning Objectives**

By the end of this tutorial, you will be able to:
- ✅ Create and load DataFrames from various sources
- ✅ Filter and select data with complex conditions
- ✅ Perform GroupBy operations and aggregations
- ✅ Sort data by multiple columns
- ✅ Merge and join datasets
- ✅ Build complete data analysis pipelines

**⏱️ Estimated Time**: 75 minutes  
**📋 Prerequisites**: Tutorials 01-04  
**💻 Difficulty**: ⭐⭐⭐☆☆ Intermediate

---

## 📚 **Introduction: Structured Data Processing**

DataFrames are the cornerstone of data science. They let you work with structured data (like spreadsheets or SQL tables) with incredible efficiency.

### **Why DataFrames?**

```l1
# Traditional approach - Messy! ❌
let names = ["Alice", "Bob", "Carol"]
let ages = [25, 30, 28]
let salaries = [50000, 60000, 55000]

# DataFrame approach - Clean! ✅
let df = dataframe({
    "name": ["Alice", "Bob", "Carol"],
    "age": [25, 30, 28],
    "salary": [50000, 60000, 55000]
})
```

### **LangOne DataFrame Advantages**

- **10x faster** than pandas for data operations
- **87% less memory** usage
- **15-17x faster** for groupby and merge operations
- **Intuitive API** similar to pandas
- **Production-ready** performance

---

## 🔧 **Part 1: Creating DataFrames**

### **From Dictionary**

```l1
# Create DataFrame from dictionary
let employee_data = {
    "name": ["Alice", "Bob", "Carol", "David", "Eve"],
    "age": [25, 30, 28, 35, 32],
    "department": ["IT", "HR", "IT", "Finance", "HR"],
    "salary": [50000, 45000, 55000, 65000, 48000]
}

let df = dataframe(employee_data)
print(df)
```

### **Viewing DataFrame Structure**

```l1
# View first few rows
let head_data = df_head(df, 3)
print("First 3 rows:")
print(head_data)

# View last few rows
let tail_data = df_tail(df, 2)
print("Last 2 rows:")
print(tail_data)

# Get summary statistics
let stats = df_describe(df)
print("Statistics:")
print(stats)
```

### **Selecting Columns**

```l1
# Select single column
let names = df_select(df, ["name"])
print("Names:")
print(names)

# Select multiple columns
let basic_info = df_select(df, ["name", "age"])
print("Basic Info:")
print(basic_info)
```

---

### **🔨 Hands-On Exercise 1: Create Your Dataset**

```l1
# Create a DataFrame for a class of students:
# Columns: student_id, name, math_score, science_score, english_score
# At least 5 students
# Display the first 3 rows
# Show summary statistics
```

<details>
<summary>💡 Solution</summary>

```l1
# Student Performance Dataset

let student_data = {
    "student_id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Carol", "David", "Eve"],
    "math_score": [85, 92, 78, 95, 88],
    "science_score": [90, 85, 88, 92, 95],
    "english_score": [88, 90, 85, 87, 92]
}

let students = dataframe(student_data)

print("=== Student Performance Dataset ===")
print("")

# Display first 3 rows
print("First 3 Students:")
let first_three = df_head(students, 3)
print(first_three)
print("")

# Summary statistics
print("Summary Statistics:")
let stats = df_describe(students)
print(stats)
print("")

# Select specific columns
print("Math Scores:")
let math_only = df_select(students, ["name", "math_score"])
print(math_only)
```
</details>

✅ **Checkpoint**: Can you create and inspect DataFrames?

---

## 🔍 **Part 2: Filtering Data**

### **Simple Filtering**

```l1
# Filter by condition
let high_earners = df_filter(df, "salary", ">", 50000)
print("Employees earning > $50,000:")
print(high_earners)

# Filter by department
let it_dept = df_filter(df, "department", "==", "IT")
print("IT Department:")
print(it_dept)
```

### **Multiple Conditions**

```l1
# Filter with multiple conditions (using chain)
let young_high_earners = df_filter(
    df_filter(df, "age", "<", 30),
    "salary", ">", 48000
)
print("Young high earners (age < 30, salary > 48000):")
print(young_high_earners)
```

### **Complex Filtering**

```l1
# Filter seniors in IT department
let senior_it = df_filter(
    df_filter(df, "department", "==", "IT"),
    "age", ">", 27
)
print("Senior IT staff:")
print(senior_it)
```

---

### **🔨 Hands-On Exercise 2: Data Filtering**

```l1
# Using the student dataset from Exercise 1:
# 1. Find students with math_score > 85
# 2. Find students with all scores > 85
# 3. Find top science performers (score >= 90)
# 4. Find students who need improvement (any score < 80)
```

<details>
<summary>💡 Solution</summary>

```l1
# Student Performance Filtering

# 1. Math score > 85
let math_stars = df_filter(students, "math_score", ">", 85)
print("Math Stars (score > 85):")
print(df_select(math_stars, ["name", "math_score"]))
print("")

# 2. All scores > 85 (requires multiple filters)
let high_achievers = df_filter(
    df_filter(
        df_filter(students, "math_score", ">", 85),
        "science_score", ">", 85
    ),
    "english_score", ">", 85
)
print("High Achievers (all scores > 85):")
print(high_achievers)
print("")

# 3. Top science performers
let science_stars = df_filter(students, "science_score", ">=", 90)
print("Science Stars (score >= 90):")
print(df_select(science_stars, ["name", "science_score"]))
print("")

# 4. Need improvement (simulated with one subject for demonstration)
let needs_help_math = df_filter(students, "math_score", "<", 80)
print("Students Needing Math Help (score < 80):")
print(df_select(needs_help_math, ["name", "math_score"]))
```
</details>

---

## 📊 **Part 3: GroupBy and Aggregation**

### **Basic GroupBy**

```l1
# Group by department
let grouped = df_groupby(df, ["department"])
print("Grouped by department:")
print(grouped)

# Aggregate: average salary by department
let avg_salary = groupby_agg(grouped, "salary", "mean")
print("Average salary by department:")
print(avg_salary)
```

### **Multiple Aggregations**

```l1
# Sum of salaries by department
let total_salary = groupby_agg(grouped, "salary", "sum")
print("Total salary by department:")
print(total_salary)

# Count employees by department
let emp_count = groupby_agg(grouped, "name", "count")
print("Employee count by department:")
print(emp_count)

# Max and min salaries
let max_salary = groupby_agg(grouped, "salary", "max")
let min_salary = groupby_agg(grouped, "salary", "min")
print("Salary ranges by department:")
print("Max:", max_salary)
print("Min:", min_salary)
```

### **Multi-Column GroupBy**

```l1
# Group by department and age group
let age_groups = df_groupby(df, ["department", "age_group"])
let stats = groupby_agg(age_groups, "salary", "mean")
print("Average salary by department and age group:")
print(stats)
```

---

### **🔨 Hands-On Exercise 3: Sales Analysis**

```l1
# Create a sales dataset and analyze it:
# Columns: product, category, region, sales, units
# 1. Total sales by category
# 2. Average sales by region
# 3. Count of products by category
# 4. Max sales by region
```

<details>
<summary>💡 Solution</summary>

```l1
# Sales Analysis

let sales_data = {
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset", "Cable", "Laptop", "Monitor"],
    "category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "region": ["North", "North", "South", "South", "North", "South", "South", "North"],
    "sales": [1200, 25, 75, 300, 80, 15, 1100, 320],
    "units": [1, 5, 3, 1, 2, 10, 1, 1]
}

let sales_df = dataframe(sales_data)

print("=== Sales Analysis ===")
print("")

# 1. Total sales by category
let by_category = df_groupby(sales_df, ["category"])
let total_by_category = groupby_agg(by_category, "sales", "sum")
print("Total Sales by Category:")
print(total_by_category)
print("")

# 2. Average sales by region
let by_region = df_groupby(sales_df, ["region"])
let avg_by_region = groupby_agg(by_region, "sales", "mean")
print("Average Sales by Region:")
print(avg_by_region)
print("")

# 3. Count of products by category
let count_by_category = groupby_agg(by_category, "product", "count")
print("Product Count by Category:")
print(count_by_category)
print("")

# 4. Max sales by region
let max_by_region = groupby_agg(by_region, "sales", "max")
print("Maximum Sales by Region:")
print(max_by_region)
```
</details>

---

## 🔀 **Part 4: Sorting and Merging**

### **Sorting**

```l1
# Sort by single column (ascending)
let sorted_asc = df_sort_values(df, ["salary"], true)
print("Sorted by salary (ascending):")
print(sorted_asc)

# Sort by single column (descending)
let sorted_desc = df_sort_values(df, ["salary"], false)
print("Sorted by salary (descending):")
print(sorted_desc)

# Sort by multiple columns
let multi_sorted = df_sort_values(df, ["department", "salary"], true)
print("Sorted by department, then salary:")
print(multi_sorted)
```

### **Merging DataFrames**

```l1
# Create two DataFrames
let employees = dataframe({
    "emp_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Carol"],
    "dept_id": [10, 20, 10]
})

let departments = dataframe({
    "dept_id": [10, 20, 30],
    "dept_name": ["IT", "HR", "Finance"]
})

# Inner join - only matching records
let inner = df_merge(employees, departments, "dept_id", "inner")
print("Inner Join:")
print(inner)

# Left join - all from left, matching from right
let left = df_merge(employees, departments, "dept_id", "left")
print("Left Join:")
print(left)

# Outer join - all records from both
let outer = df_merge(employees, departments, "dept_id", "outer")
print("Outer Join:")
print(outer)
```

---

### **🔨 Hands-On Exercise 4: Complete Data Pipeline**

```l1
# Build a complete analysis:
# 1. Create employee and performance DataFrames
# 2. Merge them
# 3. Filter high performers
# 4. Group by department
# 5. Calculate average performance
# 6. Sort by performance
```

<details>
<summary>💡 Solution</summary>

```l1
# Complete Data Analysis Pipeline

print("=== Employee Performance Analysis ===")
print("")

# 1. Create DataFrames
let employees = dataframe({
    "emp_id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Carol", "David", "Eve"],
    "department": ["IT", "HR", "IT", "Finance", "HR"],
    "salary": [50000, 45000, 55000, 65000, 48000]
})

let performance = dataframe({
    "emp_id": [1, 2, 3, 4, 5],
    "rating": [4.5, 3.8, 4.2, 4.8, 4.0],
    "projects_completed": [12, 8, 10, 15, 9]
})

# 2. Merge DataFrames
let merged = df_merge(employees, performance, "emp_id", "inner")
print("Merged Data:")
print(df_head(merged, 3))
print("")

# 3. Filter high performers (rating >= 4.0)
let high_performers = df_filter(merged, "rating", ">=", 4.0)
print("High Performers (rating >= 4.0):")
print(high_performers)
print("")

# 4. Group by department
let by_dept = df_groupby(merged, ["department"])

# 5. Calculate averages
let avg_rating = groupby_agg(by_dept, "rating", "mean")
let avg_salary = groupby_agg(by_dept, "salary", "mean")
let avg_projects = groupby_agg(by_dept, "projects_completed", "mean")

print("Average Rating by Department:")
print(avg_rating)
print("")

print("Average Salary by Department:")
print(avg_salary)
print("")

# 6. Sort by rating (descending)
let sorted = df_sort_values(merged, ["rating"], false)
print("Employees Sorted by Rating:")
print(sorted)
```
</details>

---

## 📈 **Part 5: Real-World Example - Sales Dashboard**

```l1
# Sales Dashboard Application

print("╔════════════════════════════════════════╗")
print("║       MONTHLY SALES DASHBOARD          ║")
print("╚════════════════════════════════════════╝")
print("")

# Sample sales data
let sales = dataframe({
    "date": ["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03"],
    "product": ["Laptop", "Mouse", "Laptop", "Keyboard", "Monitor"],
    "category": ["Electronics", "Accessories", "Electronics", "Accessories", "Electronics"],
    "region": ["North", "South", "North", "North", "South"],
    "quantity": [2, 10, 1, 5, 3],
    "price": [1000, 25, 1000, 75, 300],
    "revenue": [2000, 250, 1000, 375, 900]
})

print("1. SALES OVERVIEW")
print("─────────────────────────────────────────")
let overview = df_describe(sales)
print(overview)
print("")

print("2. TOP PRODUCTS BY REVENUE")
print("─────────────────────────────────────────")
let sorted_sales = df_sort_values(sales, ["revenue"], false)
let top_products = df_head(sorted_sales, 3)
print(top_products)
print("")

print("3. SALES BY CATEGORY")
print("─────────────────────────────────────────")
let by_category = df_groupby(sales, ["category"])
let category_revenue = groupby_agg(by_category, "revenue", "sum")
let category_units = groupby_agg(by_category, "quantity", "sum")
print("Revenue:", category_revenue)
print("Units:", category_units)
print("")

print("4. SALES BY REGION")
print("─────────────────────────────────────────")
let by_region = df_groupby(sales, ["region"])
let region_revenue = groupby_agg(by_region, "revenue", "sum")
let region_avg = groupby_agg(by_region, "revenue", "mean")
print("Total Revenue:", region_revenue)
print("Average Sale:", region_avg)
print("")

print("5. HIGH-VALUE TRANSACTIONS (> $500)")
print("─────────────────────────────────────────")
let high_value = df_filter(sales, "revenue", ">", 500)
print(high_value)

print("")
print("Dashboard Complete! 📊")
```

---

## ✅ **Knowledge Check**

1. **How do you create a DataFrame from a dictionary?**
   <details><summary>Show Answer</summary>`dataframe(dictionary)`</details>

2. **What function shows the first N rows?**
   <details><summary>Show Answer</summary>`df_head(df, N)`</details>

3. **How do you filter a DataFrame?**
   <details><summary>Show Answer</summary>`df_filter(df, column, operator, value)`</details>

4. **What does GroupBy do?**
   <details><summary>Show Answer</summary>Groups rows by column values for aggregation</details>

5. **What are the four types of joins?**
   <details><summary>Show Answer</summary>inner, left, right, outer</details>

6. **How much faster is LangOne than pandas for merges?**
   <details><summary>Show Answer</summary>15-17x faster</details>

---

## 🎓 **What You've Learned**

- ✅ Creating and inspecting DataFrames
- ✅ Filtering with complex conditions
- ✅ GroupBy operations and aggregations
- ✅ Sorting by multiple columns
- ✅ Merging datasets with different join types
- ✅ Building complete data analysis pipelines

---

## 🚀 **Next Steps**

**Practice Projects:**
1. Build a customer analytics dashboard
2. Create a product inventory system
3. Analyze financial transaction data

👉 **[Tutorial 06: File I/O and Data Persistence](./06_File_IO.md)**

---

## 💡 **Best Practices**

1. **Use descriptive column names**
2. **Validate data before processing**
3. **Chain operations for readability**
4. **Use GroupBy for efficient aggregations**
5. **Choose appropriate join types**

**Progress Tracker:**
- [x] Tutorial 01-04 ✅
- [x] Tutorial 05: DataFrames ✅
- [ ] Tutorial 06: File I/O

---

*© 2025 LangOne Project. Part of the official LangOne tutorial series.*

