# Tutorial 03: Functions and Program Organization

## 🎯 **Learning Objectives**

By the end of this tutorial, you will be able to:
- ✅ Define and call functions with proper syntax
- ✅ Use parameters and arguments effectively
- ✅ Return values from functions
- ✅ Understand variable scope (local vs global)
- ✅ Organize code into modular, reusable components
- ✅ Apply best practices for function design

**⏱️ Estimated Time**: 45 minutes  
**📋 Prerequisites**: Tutorials 01-02  
**💻 Difficulty**: ⭐⭐☆☆☆ Beginner-Intermediate

---

## 📚 **Introduction: Code Reusability**

Functions are the building blocks of organized, maintainable code. Instead of repeating the same code, write it once and reuse it everywhere!

### **Why Functions Matter**

```l1
# Without functions - Repetitive ❌
print("Welcome, Alice!")
print("Your age: 25")
print("Status: Active")
print("---")

print("Welcome, Bob!")
print("Your age: 30")
print("Status: Active")
print("---")

# With functions - Reusable ✅
function display_user(name, age) {
    print("Welcome, " + name + "!")
    print("Your age: " + to_string(age))
    print("Status: Active")
    print("---")
}

display_user("Alice", 25)
display_user("Bob", 30)
```

---

## 🔧 **Part 1: Function Basics**

### **Defining Functions**

```l1
# Basic function
function greet() {
    print("Hello, World!")
}

# Call the function
greet()  # Output: Hello, World!
```

### **Functions with Parameters**

```l1
# Function with one parameter
function greet_person(name) {
    print("Hello, " + name + "!")
}

greet_person("Alice")  # Output: Hello, Alice!
greet_person("Bob")    # Output: Hello, Bob!

# Function with multiple parameters
function introduce(name, age, city) {
    print("My name is " + name)
    print("I am " + to_string(age) + " years old")
    print("I live in " + city)
}

introduce("Alice", 25, "New York")
```

### **Return Values**

```l1
# Function that returns a value
function add(a, b) {
    return a + b
}

let result = add(5, 3)
print("Result: " + to_string(result))  # Output: Result: 8

# Function with conditional return
function get_grade(score) {
    if (score >= 90) {
        return "A"
    } else if (score >= 80) {
        return "B"
    } else if (score >= 70) {
        return "C"
    } else if (score >= 60) {
        return "D"
    } else {
        return "F"
    }
}

let my_grade = get_grade(85)
print("Grade: " + my_grade)  # Output: Grade: B
```

---

### **🔨 Hands-On Exercise 1: Temperature Converter**

```l1
# Create functions to:
# 1. Convert Celsius to Fahrenheit
# 2. Convert Fahrenheit to Celsius
# 3. Convert Celsius to Kelvin
# Test each function
```

<details>
<summary>💡 Solution</summary>

```l1
# Temperature Conversion Functions

function celsius_to_fahrenheit(celsius) {
    return celsius * 9.0 / 5.0 + 32.0
}

function fahrenheit_to_celsius(fahrenheit) {
    return (fahrenheit - 32.0) * 5.0 / 9.0
}

function celsius_to_kelvin(celsius) {
    return celsius + 273.15
}

# Test the functions
print("=== Temperature Conversions ===")
print("")

let temp_c = 25
print(to_string(temp_c) + "°C = " + to_string(celsius_to_fahrenheit(temp_c)) + "°F")

let temp_f = 77
print(to_string(temp_f) + "°F = " + to_string(fahrenheit_to_celsius(temp_f)) + "°C")

let temp_c2 = 0
print(to_string(temp_c2) + "°C = " + to_string(celsius_to_kelvin(temp_c2)) + "K")
```
</details>

---

## 🔄 **Part 2: Advanced Function Concepts**

### **Multiple Return Values (Using Arrays)**

```l1
# Return multiple values
function get_statistics(numbers) {
    let total = sum(numbers)
    let average = mean(numbers)
    let maximum = max(numbers)
    let minimum = min(numbers)
    return [total, average, maximum, minimum]
}

let data = [10, 20, 30, 40, 50]
let stats = get_statistics(data)
print("Total: " + to_string(stats[0]))
print("Average: " + to_string(stats[1]))
print("Max: " + to_string(stats[2]))
print("Min: " + to_string(stats[3]))
```

### **Recursive Functions**

```l1
# Factorial using recursion
function factorial(n) {
    if (n <= 1) {
        return 1
    }
    return n * factorial(n - 1)
}

print("5! = " + to_string(factorial(5)))  # Output: 120

# Fibonacci using recursion
function fibonacci(n) {
    if (n <= 1) {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2)
}

print("Fibonacci(10) = " + to_string(fibonacci(10)))  # Output: 55
```

### **Helper Functions**

```l1
# Break complex tasks into smaller functions

function is_even(n) {
    return n % 2 == 0
}

function count_evens(numbers) {
    let count = 0
    for num in numbers {
        if (is_even(num)) {
            count = count + 1
        }
    }
    return count
}

let data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let even_count = count_evens(data)
print("Even numbers: " + to_string(even_count))  # Output: 5
```

---

### **🔨 Hands-On Exercise 2: String Utilities**

```l1
# Create a string utilities library:
# 1. Function to reverse a string
# 2. Function to count vowels
# 3. Function to check if palindrome
# 4. Function to capitalize words
```

<details>
<summary>💡 Solution</summary>

```l1
# String Utilities Library

function reverse_string(text) {
    let reversed = ""
    let length = len(text)
    for i in range(length - 1, -1, -1) {
        reversed = reversed + text[i]
    }
    return reversed
}

function count_vowels(text) {
    let vowels = "aeiouAEIOU"
    let count = 0
    for char in text {
        if (vowels.contains(char)) {
            count = count + 1
        }
    }
    return count
}

function is_palindrome(text) {
    let cleaned = text.lower().replace(" ", "")
    return cleaned == reverse_string(cleaned)
}

function capitalize_words(text) {
    let words = text.split(" ")
    let result = []
    for word in words {
        if (len(word) > 0) {
            let first = word[0].upper()
            let rest = word[1:]
            result.append(first + rest)
        }
    }
    return " ".join(result)
}

# Test the functions
print("=== String Utilities Test ===")
print("")

let test_str = "hello"
print("Original: " + test_str)
print("Reversed: " + reverse_string(test_str))
print("Vowels: " + to_string(count_vowels(test_str)))
print("")

let palindrome_test = "racecar"
print(palindrome_test + " is palindrome: " + to_string(is_palindrome(palindrome_test)))

let text = "hello world"
print("Original: " + text)
print("Capitalized: " + capitalize_words(text))
```
</details>

---

## 🌍 **Part 3: Variable Scope**

### **Local Scope**

```l1
function calculate() {
    let x = 10  # Local variable
    let y = 20  # Local variable
    return x + y
}

let result = calculate()
print(result)  # Output: 30
# print(x)  # Error: x is not defined outside function
```

### **Global Scope**

```l1
let global_var = 100  # Global variable

function use_global() {
    print("Global variable: " + to_string(global_var))
}

use_global()  # Output: Global variable: 100

function modify_local() {
    let global_var = 200  # This is a NEW local variable
    print("Local variable: " + to_string(global_var))
}

modify_local()  # Output: Local variable: 200
print("Global variable: " + to_string(global_var))  # Output: Global variable: 100
```

### **Best Practice: Avoid Global Variables**

```l1
# ❌ Bad: Using global variables
let counter = 0

function increment() {
    counter = counter + 1
}

# ✅ Good: Using parameters and return values
function increment(counter) {
    return counter + 1
}

let counter = 0
counter = increment(counter)
```

---

### **🔨 Hands-On Exercise 3: Mathematical Functions Library**

```l1
# Create a math library with:
# 1. Function to check if number is prime
# 2. Function to find GCD of two numbers
# 3. Function to calculate power without **
# 4. Function to find all factors
```

<details>
<summary>💡 Solution</summary>

```l1
# Mathematical Functions Library

function is_prime(n) {
    if (n < 2) {
        return false
    }
    for i in range(2, n) {
        if (n % i == 0) {
            return false
        }
    }
    return true
}

function gcd(a, b) {
    while (b != 0) {
        let temp = b
        b = a % b
        a = temp
    }
    return a
}

function power(base, exponent) {
    let result = 1
    for i in range(0, exponent) {
        result = result * base
    }
    return result
}

function find_factors(n) {
    let factors = []
    for i in range(1, n + 1) {
        if (n % i == 0) {
            factors.append(i)
        }
    }
    return factors
}

# Test the functions
print("=== Math Library Test ===")
print("")

print("Is 17 prime? " + to_string(is_prime(17)))
print("Is 18 prime? " + to_string(is_prime(18)))
print("")

print("GCD(48, 18) = " + to_string(gcd(48, 18)))
print("")

print("2^10 = " + to_string(power(2, 10)))
print("")

print("Factors of 24:")
let factors = find_factors(24)
for factor in factors {
    print("  " + to_string(factor))
}
```
</details>

---

## 📦 **Part 4: Code Organization**

### **Grouping Related Functions**

```l1
# User Management Module

function create_user(name, email, age) {
    return {
        "name": name,
        "email": email,
        "age": age,
        "active": true
    }
}

function display_user(user) {
    print("Name: " + user["name"])
    print("Email: " + user["email"])
    print("Age: " + to_string(user["age"]))
    print("Status: " + ("Active" if user["active"] else "Inactive"))
}

function deactivate_user(user) {
    user["active"] = false
    return user
}

# Usage
let user1 = create_user("Alice", "alice@example.com", 25)
display_user(user1)
```

### **Main Program Structure**

```l1
# Good program organization

# 1. Define all functions first
function calculate_total(price, tax_rate) {
    return price * (1 + tax_rate)
}

function format_currency(amount) {
    return "$" + to_string(amount)
}

function display_receipt(items, tax_rate) {
    let subtotal = 0
    for item in items {
        subtotal = subtotal + item["price"]
    }
    
    let total = calculate_total(subtotal, tax_rate)
    
    print("=== Receipt ===")
    for item in items {
        print(item["name"] + ": " + format_currency(item["price"]))
    }
    print("Subtotal: " + format_currency(subtotal))
    print("Tax: " + format_currency(total - subtotal))
    print("Total: " + format_currency(total))
}

# 2. Main program logic
let shopping_cart = [
    {"name": "Book", "price": 15.99},
    {"name": "Pen", "price": 2.50},
    {"name": "Notebook", "price": 5.99}
]

let tax_rate = 0.08
display_receipt(shopping_cart, tax_rate)
```

---

## 🎯 **Part 5: Complete Example - Contact Manager**

```l1
# Contact Manager System

# Data structure for contacts
let contacts = []

# Function to add a contact
function add_contact(name, phone, email) {
    let contact = {
        "id": len(contacts) + 1,
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    return contact
}

# Function to find contact by name
function find_contact(name) {
    for contact in contacts {
        if (contact["name"] == name) {
            return contact
        }
    }
    return null
}

# Function to display all contacts
function display_all_contacts() {
    if (len(contacts) == 0) {
        print("No contacts found")
        return
    }
    
    print("=== All Contacts ===")
    for contact in contacts {
        display_contact(contact)
        print("---")
    }
}

# Function to display single contact
function display_contact(contact) {
    print("ID: " + to_string(contact["id"]))
    print("Name: " + contact["name"])
    print("Phone: " + contact["phone"])
    print("Email: " + contact["email"])
}

# Function to delete contact
function delete_contact(name) {
    let new_contacts = []
    let found = false
    
    for contact in contacts {
        if (contact["name"] != name) {
            new_contacts.append(contact)
        } else {
            found = true
        }
    }
    
    contacts = new_contacts
    return found
}

# Main program
print("=== Contact Manager ===")
print("")

# Add contacts
add_contact("Alice Johnson", "555-0101", "alice@example.com")
add_contact("Bob Smith", "555-0102", "bob@example.com")
add_contact("Carol Davis", "555-0103", "carol@example.com")

# Display all
display_all_contacts()
print("")

# Find specific contact
print("=== Finding 'Bob Smith' ===")
let found_contact = find_contact("Bob Smith")
if (found_contact != null) {
    display_contact(found_contact)
}
print("")

# Delete contact
print("=== Deleting 'Bob Smith' ===")
let deleted = delete_contact("Bob Smith")
if (deleted) {
    print("Contact deleted successfully")
}
print("")

# Display remaining
display_all_contacts()
```

---

## ✅ **Knowledge Check**

1. **What keyword is used to define a function?**
   <details><summary>Show Answer</summary>`function`</details>

2. **How do you return a value from a function?**
   <details><summary>Show Answer</summary>Use the `return` keyword</details>

3. **What is the scope of a variable declared inside a function?**
   <details><summary>Show Answer</summary>Local - only accessible within the function</details>

4. **Can a function call itself?**
   <details><summary>Show Answer</summary>Yes - this is called recursion</details>

5. **What's the difference between parameters and arguments?**
   <details><summary>Show Answer</summary>Parameters are in function definition, arguments are values passed when calling</details>

---

## 🎓 **What You've Learned**

- ✅ Defining and calling functions
- ✅ Using parameters and return values
- ✅ Understanding variable scope
- ✅ Creating recursive functions
- ✅ Organizing code with functions
- ✅ Building complete modular programs

---

## 🚀 **Next Steps**

**Practice Projects:**
1. Build a calculator with functions for each operation
2. Create a text-based adventure game
3. Implement a simple banking system

👉 **[Tutorial 04: Working with Arrays and Tensors](./04_Arrays_Tensors.md)**

---

## 💡 **Best Practices**

1. **Single Responsibility**: Each function should do one thing well
2. **Descriptive Names**: Function names should describe what they do
3. **Avoid Side Effects**: Functions should not modify global variables
4. **Document Complex Logic**: Add comments for non-obvious code
5. **Keep Functions Short**: Aim for 10-20 lines per function

---

**Progress Tracker:**
- [x] Tutorial 01: Getting Started ✅
- [x] Tutorial 02: Core Fundamentals ✅
- [x] Tutorial 03: Functions and Organization ✅
- [x] Tutorial 04: Arrays and Tensors ✅

👉 **[Continue to Tutorial 04](./04_Arrays_Tensors.md)**

---

*© 2025 LangOne Project. Part of the official LangOne tutorial series.*

