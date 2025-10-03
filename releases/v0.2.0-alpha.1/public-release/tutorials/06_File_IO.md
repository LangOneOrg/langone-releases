# Tutorial 06: File I/O and Data Persistence

## 🎯 **Learning Objectives**

By the end of this tutorial, you will be able to:
- ✅ Perform file system operations (create, read, write, delete)
- ✅ Read and write CSV files
- ✅ Handle JSON data for APIs
- ✅ Work with Parquet format for big data
- ✅ Use streaming I/O for large files
- ✅ Build complete data pipelines with file operations

**⏱️ Estimated Time**: 60 minutes  
**📋 Prerequisites**: Tutorials 01-05  
**💻 Difficulty**: ⭐⭐⭐☆☆ Intermediate

---

## 📚 **Introduction: Data Persistence**

Programs need to save and load data. LangOne provides high-performance I/O operations that are **10x faster than Python** with multiple format support.

### **Supported Formats**

- **CSV**: Comma-separated values (spreadsheets)
- **JSON**: JavaScript Object Notation (APIs, config)
- **Parquet**: Columnar storage (big data)
- **Text**: Plain text files
- **Binary**: Custom binary formats

---

## 📁 **Part 1: File Operations**

### **Basic File Operations**

```l1
# Check if file exists
let exists = file_exists("data.csv")
print("File exists: " + to_string(exists))

# Get file size
let size = file_size("data.csv")
print("File size: " + to_string(size) + " bytes")

# List files in directory
let files = list_files("./data")
print("Files:", files)

# Copy file
copy_file("source.txt", "backup.txt")

# Move/rename file
move_file("old_name.txt", "new_name.txt")

# Delete file
delete_file("temp.txt")

# Create directory
create_directory("output")
```

---

## 📄 **Part 2: CSV Operations**

### **Reading CSV**

```l1
# Read CSV file
let df = read_csv("employees.csv")
print("Employee data:")
print(df_head(df, 5))

# CSV with custom delimiter
let df_tsv = read_csv("data.tsv", delimiter="\t")

# Skip header rows
let df_no_header = read_csv("data.csv", skip_rows=1)
```

### **Writing CSV**

```l1
# Create DataFrame
let employee_data = {
    "name": ["Alice", "Bob", "Carol"],
    "age": [25, 30, 28],
    "salary": [50000, 60000, 55000]
}
let df = dataframe(employee_data)

# Write to CSV
write_csv("output.csv", df)
print("Data written to output.csv")

# Custom delimiter
write_csv("output.tsv", df, delimiter="\t")
```

---

### **🔨 Hands-On Exercise 1: CSV Data Pipeline**

```l1
# Create a data processing pipeline:
# 1. Create sample employee data
# 2. Write to CSV file
# 3. Read it back
# 4. Filter high earners (salary > 52000)
# 5. Write filtered data to new CSV
```

<details>
<summary>💡 Solution</summary>

```l1
# CSV Data Pipeline

print("=== CSV Data Pipeline ===")
print("")

# 1. Create sample data
let employees = {
    "employee_id": [101, 102, 103, 104, 105],
    "name": ["Alice Johnson", "Bob Smith", "Carol Davis", "David Brown", "Eve Wilson"],
    "department": ["IT", "HR", "IT", "Finance", "HR"],
    "salary": [50000, 45000, 55000, 65000, 48000],
    "years_employed": [3, 5, 2, 7, 4]
}

let df = dataframe(employees)
print("Step 1: Created employee data")
print(df)
print("")

# 2. Write to CSV
write_csv("employees.csv", df)
print("Step 2: Written to employees.csv")
print("")

# 3. Read back
let loaded_df = read_csv("employees.csv")
print("Step 3: Read from CSV")
print(df_head(loaded_df, 3))
print("")

# 4. Filter high earners
let high_earners = df_filter(loaded_df, "salary", ">", 52000)
print("Step 4: Filtered high earners (salary > 52000)")
print(high_earners)
print("")

# 5. Write filtered data
write_csv("high_earners.csv", high_earners)
print("Step 5: High earners saved to high_earners.csv")
print("")

print("Pipeline complete! ✓")
```
</details>

---

## 🔗 **Part 3: JSON Operations**

### **Reading JSON**

```l1
# Read JSON file
let data = read_json("config.json")
print("Configuration data:")
print(data)

# Access JSON data
print("App name: " + data["app_name"])
print("Version: " + data["version"])
```

### **Writing JSON**

```l1
# Create data structure
let config = {
    "app_name": "LangOne App",
    "version": "1.0.0",
    "settings": {
        "theme": "dark",
        "language": "en"
    },
    "features": ["arrays", "dataframes", "gpu"]
}

# Write to JSON
write_json("config.json", config)
print("Configuration saved")

# Pretty print option
write_json("config_pretty.json", config, pretty=true)
```

---

## 📦 **Part 4: Parquet Format**

### **Working with Parquet**

```l1
# Parquet is optimized for big data

# Write DataFrame to Parquet
let large_df = dataframe({
    "id": arange(0, 1000000),
    "value": arange(0, 1000000) * 1.5,
    "category": ["A", "B", "C"] * 333334
})

write_parquet("large_data.parquet", large_df)
print("Large dataset saved to Parquet")

# Read from Parquet (much faster than CSV)
let loaded_parquet = read_parquet("large_data.parquet")
print("Loaded from Parquet:")
print(df_head(loaded_parquet, 5))

# Performance comparison
print("Parquet is 3-5x faster than CSV for large datasets!")
```

---

## 🌊 **Part 5: Streaming I/O**

### **Large File Processing**

```l1
# For files too large to fit in memory

# Create streaming configuration
let stream_config = {
    "chunk_size": 10000,  # Process 10,000 rows at a time
    "compression": "gzip",
    "buffer_size": 8192
}

# Stream large CSV
let stream = streaming_read("huge_file.csv", stream_config)

# Process in chunks
let total_rows = 0
while (stream.has_next()) {
    let chunk = stream.next_chunk()
    total_rows = total_rows + len(chunk)
    
    # Process chunk
    let filtered_chunk = df_filter(chunk, "value", ">", 100)
    streaming_write("output.csv", filtered_chunk, append=true)
}

print("Processed " + to_string(total_rows) + " rows")
```

---

### **🔨 Hands-On Exercise 2: Multi-Format Data Pipeline**

```l1
# Build a pipeline that:
# 1. Reads from CSV
# 2. Processes the data
# 3. Saves to JSON (for API)
# 4. Saves to Parquet (for analysis)
# 5. Creates summary report in CSV
```

<details>
<summary>💡 Solution</summary>

```l1
# Multi-Format Data Pipeline

print("=== Multi-Format Data Pipeline ===")
print("")

# 1. Read from CSV
print("Step 1: Reading source data...")
let source_data = read_csv("sales_data.csv")
print("Loaded " + to_string(len(source_data)) + " records")
print("")

# 2. Process the data
print("Step 2: Processing data...")

# Calculate total sales
let by_product = df_groupby(source_data, ["product"])
let total_sales = groupby_agg(by_product, "revenue", "sum")
let avg_sales = groupby_agg(by_product, "revenue", "mean")
let unit_count = groupby_agg(by_product, "quantity", "sum")

# Create processed DataFrame
let processed = df_merge(
    df_merge(total_sales, avg_sales, "product", "inner"),
    unit_count,
    "product",
    "inner"
)
print("Processed data ready")
print("")

# 3. Save to JSON (for API)
print("Step 3: Saving to JSON for API...")
write_json("sales_summary.json", processed, pretty=true)
print("✓ Saved to sales_summary.json")
print("")

# 4. Save to Parquet (for analysis)
print("Step 4: Saving to Parquet for analysis...")
write_parquet("sales_data.parquet", source_data)
print("✓ Saved to sales_data.parquet")
print("")

# 5. Create summary report
print("Step 5: Creating summary report...")
let summary = {
    "total_records": [len(source_data)],
    "total_revenue": [sum(source_data["revenue"])],
    "average_sale": [mean(source_data["revenue"])],
    "top_product": [get_top_product(total_sales)]
}
let summary_df = dataframe(summary)
write_csv("summary_report.csv", summary_df)
print("✓ Summary report saved")
print("")

print("Pipeline complete! All formats generated ✓")
```
</details>

---

## 🎯 **Part 6: Complete Example - Log Analyzer**

```l1
# Log File Analyzer

print("=== Log File Analyzer ===")
print("")

# Sample log data
let log_data = {
    "timestamp": ["2025-01-01 10:00:00", "2025-01-01 10:05:00", "2025-01-01 10:10:00"],
    "level": ["INFO", "ERROR", "WARNING"],
    "message": ["Application started", "Database connection failed", "High memory usage"],
    "module": ["app", "database", "memory"]
}

let logs = dataframe(log_data)

# Analyze logs
print("Total logs: " + to_string(len(logs)))
print("")

# Group by log level
let by_level = df_groupby(logs, ["level"])
let level_counts = groupby_agg(by_level, "message", "count")
print("Logs by Level:")
print(level_counts)
print("")

# Find errors
let errors = df_filter(logs, "level", "==", "ERROR")
print("Error Logs:")
print(errors)
print("")

# Save error report
write_csv("error_report.csv", errors)
write_json("errors.json", errors)
print("Error reports saved ✓")
```

---

## ✅ **Knowledge Check**

1. **What function reads a CSV file?**
   <details><summary>Show Answer</summary>`read_csv(filename)`</details>

2. **How do you check if a file exists?**
   <details><summary>Show Answer</summary>`file_exists(filename)`</details>

3. **What format is best for large datasets?**
   <details><summary>Show Answer</summary>Parquet (3-5x faster than CSV)</details>

4. **How do you write JSON with formatting?**
   <details><summary>Show Answer</summary>`write_json(filename, data, pretty=true)`</details>

---

## 🎓 **What You've Learned**

- ✅ File system operations
- ✅ CSV read/write operations
- ✅ JSON data handling
- ✅ Parquet for big data
- ✅ Streaming I/O for large files
- ✅ Complete data pipelines

---

## 🚀 **Next Steps**

👉 **[Tutorial 07: Linear Algebra with BLAS Integration](./07_Linear_Algebra.md)**

**Progress Tracker:**
- [x] Tutorials 01-06 ✅
- [ ] Tutorial 07: Linear Algebra

---

*© 2025 LangOne Project. Part of the official LangOne tutorial series.*

