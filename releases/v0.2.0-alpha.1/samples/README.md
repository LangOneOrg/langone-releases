# LangOne Sample Programs

This directory contains **clean, well-documented sample programs** demonstrating LangOne's features. These are **NOT test files** - they are example programs designed to show users how to use LangOne effectively.

> **Note**: For test files, see the [`tests/`](../tests/) directory which contains organized unit tests, integration tests, and feature tests.

## 🚀 Quick Start

```bash
# Run any sample
langone run samples/hello_world.l1
langone run samples/arithmetic.l1
langone run samples/control_flow.l1
langone run samples/patterns.l1
langone run samples/stdlib_demo.l1
```

## 📁 Sample Files

### **hello_world.l1**
- **Purpose**: Basic "Hello World" program
- **Features**: Print statements
- **Expected Output**: 
  ```
  Hello, LangOne!
  Welcome to the future of programming!
  ```

### **arithmetic.l1**
- **Purpose**: Demonstrate arithmetic operations
- **Features**: Variables, math operations, precedence
- **Expected Output**: Shows addition, subtraction, multiplication, division, modulo, power, and precedence

### **control_flow.l1**
- **Purpose**: Demonstrate control flow constructs
- **Features**: If/else, while loops, for loops, nested loops
- **Expected Output**: Shows conditional logic and loop patterns

### **patterns.l1**
- **Purpose**: Demonstrate pattern matching
- **Features**: Match expressions, bindings, guards, default cases
- **Expected Output**: Shows different pattern matching scenarios

### **stdlib_demo.l1**
- **Purpose**: Demonstrate all standard library functions
- **Features**: All 41 built-in functions
- **Expected Output**: Comprehensive demo of I/O, math, string, type conversion, array, and utility functions

## 🧪 Testing

### **Run All Samples**
```bash
# Test all samples
for file in samples/*.l1; do
    echo "Running $file..."
    langone run "$file"
    echo "---"
done
```

### **Expected Results**
All samples should run without errors and produce the expected output. If any sample fails:

1. Check the error message
2. Verify LangOne is properly installed
3. Report the issue with the sample name and error details

## 📝 Adding New Samples

When adding new samples:

1. **Create the `.l1` file** in this directory
2. **Add a description** to this README
3. **Test the sample** to ensure it works
4. **Update the list** above

### **Sample Template**
```langone
// Sample Name - Brief Description
// Purpose: What this sample demonstrates
// Features: Key language features used

print("Sample output");
// Add your code here
```

## 🎯 Alpha Testing

These samples are designed for alpha testing:

- **Simple enough** for quick testing
- **Comprehensive** to test all features
- **Well-documented** with expected outputs
- **Error-free** to establish baseline functionality

Use these samples to verify LangOne works correctly on your system!
