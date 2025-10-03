# Tutorial 02: Core Language Fundamentals

## 🎯 **Learning Objectives**

By the end of this tutorial, you will be able to:
- ✅ Master all LangOne data types and type conversion
- ✅ Use arithmetic, comparison, and logical operators effectively
- ✅ Write conditional statements (if/else) for decision making
- ✅ Implement loops (while, for) for repetition
- ✅ Handle user input and format output
- ✅ Build interactive programs with control flow

**⏱️ Estimated Time**: 45 minutes  
**📋 Prerequisites**: Tutorial 01 (Getting Started)  
**💻 Difficulty**: ⭐⭐☆☆☆ Beginner-Intermediate

---

## 📚 **Introduction: Building Blocks of Programming**

Every powerful program is built from fundamental concepts. In this tutorial, you'll master the core building blocks that make LangOne programs work.

### **What You'll Build**

By the end, you'll create:
- A calculator program
- A number guessing game
- A grade classifier
- An interactive menu system

---

## 🔢 **Part 1: Data Types Deep Dive**

### **Numeric Types**

```l1
# Integers - Whole numbers
let age = 25
let year = 2025
let temperature = -15

# Floating-point - Decimal numbers
let pi = 3.14159
let price = 19.99
let distance = 123.456
```

### **String Type**

```l1
# Strings - Text data
let name = "Alice"
let message = 'Hello, World!'
let multiline = "Line 1
Line 2
Line 3"

# String concatenation
let greeting = "Hello, " + name
print(greeting)  # Output: Hello, Alice

# String repetition
let repeated = "Ha" * 3
print(repeated)  # Output: HaHaHa
```

### **Boolean Type**

```l1
# Booleans - True or False
let is_student = true
let has_license = false
let is_adult = true

# Boolean operations
let can_drive = is_adult and has_license
let can_study = is_student or is_adult
```

### **Type Conversion**

```l1
# Convert to string
let num = 42
let num_str = to_string(num)
print("Number: " + num_str)

# Convert to number
let str_num = "123"
let num_from_str = to_number(str_num)
print(num_from_str + 10)  # Output: 133

# Convert to boolean
let bool_val = to_boolean("true")
print(bool_val)  # Output: true
```

---

### **🔨 Hands-On Exercise 1: Data Types Practice**

```l1
# Create variables of each type and convert between them
# 1. Create an integer age
# 2. Convert it to a string and print "Age: X"
# 3. Create a float price
# 4. Calculate total with 8% tax
# 5. Create a boolean and test it
```

<details>
<summary>💡 Solution</summary>

```l1
# 1. Integer age
let age = 30
print("Age as number: " + to_string(age))

# 2. Convert and print
let age_str = to_string(age)
print("Age: " + age_str)

# 3. Float price
let price = 49.99
print("Price: $" + to_string(price))

# 4. Calculate with tax
let tax_rate = 0.08
let total = price * (1 + tax_rate)
print("Total with tax: $" + to_string(total))

# 5. Boolean test
let is_affordable = total < 100
print("Is affordable: " + to_string(is_affordable))
```
</details>

✅ **Checkpoint**: Can you convert between all data types?

---

## ➕ **Part 2: Operators**

### **Arithmetic Operators**

```l1
let a = 10
let b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a % b)   # Modulus (remainder): 1
print(a ** b)  # Exponentiation: 1000
```

### **Comparison Operators**

```l1
let x = 5
let y = 10

print(x == y)  # Equal to: false
print(x != y)  # Not equal: true
print(x < y)   # Less than: true
print(x > y)   # Greater than: false
print(x <= 5)  # Less than or equal: true
print(y >= 10) # Greater than or equal: true
```

### **Logical Operators**

```l1
let a = true
let b = false

print(a and b)  # AND: false (both must be true)
print(a or b)   # OR: true (at least one true)
print(not a)    # NOT: false (inverts value)

# Complex conditions
let age = 25
let has_id = true
let can_enter = (age >= 21) and has_id
print(can_enter)  # Output: true
```

### **Operator Precedence**

```l1
# Order: ** → * / % → + - → comparisons → not → and → or
let result = 2 + 3 * 4  # Multiplication first
print(result)  # Output: 14

let result2 = (2 + 3) * 4  # Parentheses override
print(result2)  # Output: 20
```

---

### **🔨 Hands-On Exercise 2: Calculator Program**

```l1
# Build a calculator that:
# 1. Takes two numbers
# 2. Performs all operations
# 3. Displays results nicely
```

<details>
<summary>💡 Solution</summary>

```l1
# Simple Calculator Program

print("=== Simple Calculator ===")
print("")

# Input numbers
let num1 = 15
let num2 = 4

print("Number 1: " + to_string(num1))
print("Number 2: " + to_string(num2))
print("")

# Perform operations
print("Addition: " + to_string(num1) + " + " + to_string(num2) + " = " + to_string(num1 + num2))
print("Subtraction: " + to_string(num1) + " - " + to_string(num2) + " = " + to_string(num1 - num2))
print("Multiplication: " + to_string(num1) + " * " + to_string(num2) + " = " + to_string(num1 * num2))
print("Division: " + to_string(num1) + " / " + to_string(num2) + " = " + to_string(num1 / num2))
print("Modulus: " + to_string(num1) + " % " + to_string(num2) + " = " + to_string(num1 % num2))
print("Power: " + to_string(num1) + " ** " + to_string(num2) + " = " + to_string(num1 ** num2))

# Comparisons
print("")
print("Comparisons:")
print(to_string(num1) + " == " + to_string(num2) + ": " + to_string(num1 == num2))
print(to_string(num1) + " > " + to_string(num2) + ": " + to_string(num1 > num2))
print(to_string(num1) + " < " + to_string(num2) + ": " + to_string(num1 < num2))
```
</details>

---

## 🔀 **Part 3: Conditional Statements**

### **Basic if Statement**

```l1
let age = 20

if (age >= 18) {
    print("You are an adult")
}
```

### **if-else Statement**

```l1
let temperature = 25

if (temperature > 30) {
    print("It's hot!")
} else {
    print("It's comfortable")
}
```

### **if-elif-else Chain**

```l1
let score = 85

if (score >= 90) {
    print("Grade: A")
} else if (score >= 80) {
    print("Grade: B")
} else if (score >= 70) {
    print("Grade: C")
} else if (score >= 60) {
    print("Grade: D")
} else {
    print("Grade: F")
}
```

### **Nested Conditions**

```l1
let age = 25
let has_license = true

if (age >= 18) {
    if (has_license) {
        print("You can drive!")
    } else {
        print("You need a license first")
    }
} else {
    print("You're too young to drive")
}
```

---

### **🔨 Hands-On Exercise 3: Grade Classifier**

```l1
# Create a program that:
# 1. Takes a test score (0-100)
# 2. Classifies it into grades (A, B, C, D, F)
# 3. Provides feedback message
# 4. Checks if the student passed (>= 60)
```

<details>
<summary>💡 Solution</summary>

```l1
# Grade Classification System

print("=== Grade Classifier ===")
print("")

let score = 87
let passing_score = 60

print("Test Score: " + to_string(score))
print("")

# Classify grade
let grade = ""
if (score >= 90) {
    grade = "A"
    print("Excellent work!")
} else if (score >= 80) {
    grade = "B"
    print("Great job!")
} else if (score >= 70) {
    grade = "C"
    print("Good effort!")
} else if (score >= 60) {
    grade = "D"
    print("You passed, but need improvement")
} else {
    grade = "F"
    print("You need to study more")
}

print("Grade: " + grade)
print("")

# Check if passed
if (score >= passing_score) {
    print("Status: PASSED ✓")
    let points_above = score - passing_score
    print("You scored " + to_string(points_above) + " points above passing!")
} else {
    print("Status: FAILED ✗")
    let points_needed = passing_score - score
    print("You need " + to_string(points_needed) + " more points to pass")
}
```
</details>

---

## 🔁 **Part 4: Loops**

### **While Loop**

```l1
# Basic while loop
let count = 1
while (count <= 5) {
    print("Count: " + to_string(count))
    count = count + 1
}

# Countdown
let countdown = 5
while (countdown > 0) {
    print(to_string(countdown) + "...")
    countdown = countdown - 1
}
print("Blast off! 🚀")
```

### **For Loop**

```l1
# Basic for loop
for i in range(1, 6) {
    print("Number: " + to_string(i))
}

# Loop with step
for i in range(0, 11, 2) {
    print(to_string(i))  # Even numbers: 0, 2, 4, 6, 8, 10
}

# Loop through array
let fruits = ["apple", "banana", "cherry"]
for fruit in fruits {
    print("I like " + fruit)
}
```

### **Loop Control**

```l1
# Break - Exit loop early
for i in range(1, 11) {
    if (i == 5) {
        print("Found 5! Stopping...")
        break
    }
    print(to_string(i))
}

# Continue - Skip to next iteration
for i in range(1, 11) {
    if (i % 2 == 0) {
        continue  # Skip even numbers
    }
    print(to_string(i))  # Only prints odd numbers
}
```

### **Nested Loops**

```l1
# Print multiplication table
for i in range(1, 6) {
    for j in range(1, 6) {
        let product = i * j
        print(to_string(i) + " x " + to_string(j) + " = " + to_string(product))
    }
    print("")  # Blank line between tables
}
```

---

### **🔨 Hands-On Exercise 4: Number Guessing Game**

```l1
# Create a number guessing game:
# 1. Computer picks a number (1-100)
# 2. Player has 7 attempts
# 3. Give "higher" or "lower" hints
# 4. Congratulate on win or show answer
```

<details>
<summary>💡 Solution</summary>

```l1
# Number Guessing Game

print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100")
print("You have 7 attempts to guess it!")
print("")

let secret_number = 42  # In real game, this would be random
let max_attempts = 7
let attempts = 0
let guessed = false

# Simulate guesses (in real program, would use input)
let guesses = [50, 30, 40, 45, 42]  # Player's guesses

for guess in guesses {
    attempts = attempts + 1
    print("Attempt " + to_string(attempts) + ": You guessed " + to_string(guess))
    
    if (guess == secret_number) {
        print("🎉 Congratulations! You guessed it!")
        print("It took you " + to_string(attempts) + " attempts")
        guessed = true
        break
    } else if (guess < secret_number) {
        print("📈 Too low! Try a higher number")
    } else {
        print("📉 Too high! Try a lower number")
    }
    
    let remaining = max_attempts - attempts
    if (remaining > 0) {
        print("Attempts remaining: " + to_string(remaining))
        print("")
    }
    
    if (attempts >= max_attempts) {
        break
    }
}

if (not guessed) {
    print("")
    print("Game Over! 😢")
    print("The number was: " + to_string(secret_number))
}
```
</details>

---

## 💬 **Part 5: Input and Output**

### **Output Formatting**

```l1
# Basic printing
print("Hello, World!")

# Multiple values
let name = "Alice"
let age = 25
print("Name: " + name + ", Age: " + to_string(age))

# Formatted output
let price = 19.99
print("Price: $" + to_string(price))

# Print without newline (using string concatenation)
let message = "Loading"
print(message + "...")
```

### **Input Handling**

```l1
# Reading input (in interactive mode)
let name = input("Enter your name: ")
print("Hello, " + name + "!")

# Reading numbers
let age_str = input("Enter your age: ")
let age = to_number(age_str)
print("Next year you'll be " + to_string(age + 1))

# Input validation
let score_str = input("Enter score (0-100): ")
let score = to_number(score_str)
if (score >= 0 and score <= 100) {
    print("Valid score: " + to_string(score))
} else {
    print("Invalid score! Must be 0-100")
}
```

---

### **🔨 Hands-On Exercise 5: Interactive Menu System**

```l1
# Create a menu system that:
# 1. Shows options to user
# 2. Processes user choice
# 3. Performs action based on choice
# 4. Loops until user exits
```

<details>
<summary>💡 Solution</summary>

```l1
# Interactive Menu System

print("=================================")
print("  Welcome to LangOne Calculator  ")
print("=================================")
print("")

let running = true
let choice = 1  # Simulate user choice

# In a real program, this would be a while loop with input
# while (running) { ... }

# Simulate one menu interaction
print("Menu Options:")
print("1. Add two numbers")
print("2. Subtract two numbers")
print("3. Multiply two numbers")
print("4. Divide two numbers")
print("5. Exit")
print("")

print("Your choice: " + to_string(choice))
print("")

if (choice == 1) {
    let a = 10
    let b = 5
    print("Adding " + to_string(a) + " + " + to_string(b))
    print("Result: " + to_string(a + b))
} else if (choice == 2) {
    let a = 10
    let b = 5
    print("Subtracting " + to_string(a) + " - " + to_string(b))
    print("Result: " + to_string(a - b))
} else if (choice == 3) {
    let a = 10
    let b = 5
    print("Multiplying " + to_string(a) + " * " + to_string(b))
    print("Result: " + to_string(a * b))
} else if (choice == 4) {
    let a = 10
    let b = 5
    if (b != 0) {
        print("Dividing " + to_string(a) + " / " + to_string(b))
        print("Result: " + to_string(a / b))
    } else {
        print("Error: Cannot divide by zero!")
    }
} else if (choice == 5) {
    print("Thank you for using LangOne Calculator!")
    print("Goodbye! 👋")
    running = false
} else {
    print("Invalid choice! Please select 1-5")
}
```
</details>

---

## 🎯 **Part 6: Putting It All Together**

### **Complete Program: Interactive Quiz**

```l1
# Interactive Programming Quiz

print("========================================")
print("      LangOne Programming Quiz")
print("========================================")
print("")

let score = 0
let total_questions = 5

# Question 1
print("Question 1: What is 5 + 3 * 2?")
print("a) 16")
print("b) 11")
print("c) 13")
let answer1 = "b"
if (answer1 == "b") {
    print("✓ Correct!")
    score = score + 1
} else {
    print("✗ Wrong! The answer is b) 11")
}
print("")

# Question 2
print("Question 2: What is the result of 10 % 3?")
print("a) 3")
print("b) 0")
print("c) 1")
let answer2 = "c"
if (answer2 == "c") {
    print("✓ Correct!")
    score = score + 1
} else {
    print("✗ Wrong! The answer is c) 1")
}
print("")

# Question 3
print("Question 3: Is (5 > 3) and (2 < 4) true or false?")
print("a) true")
print("b) false")
let answer3 = "a"
if (answer3 == "a") {
    print("✓ Correct!")
    score = score + 1
} else {
    print("✗ Wrong! The answer is a) true")
}
print("")

# Question 4
print("Question 4: What loop is used for a known number of iterations?")
print("a) while")
print("b) for")
print("c) if")
let answer4 = "b"
if (answer4 == "b") {
    print("✓ Correct!")
    score = score + 1
} else {
    print("✗ Wrong! The answer is b) for")
}
print("")

# Question 5
print("Question 5: What converts a number to a string?")
print("a) to_number()")
print("b) to_string()")
print("c) print()")
let answer5 = "b"
if (answer5 == "b") {
    print("✓ Correct!")
    score = score + 1
} else {
    print("✗ Wrong! The answer is b) to_string()")
}
print("")

# Display results
print("========================================")
print("Quiz Complete!")
print("========================================")
print("Your score: " + to_string(score) + "/" + to_string(total_questions))

let percentage = (score / total_questions) * 100
print("Percentage: " + to_string(percentage) + "%")
print("")

if (percentage >= 90) {
    print("Grade: A - Excellent! 🌟")
} else if (percentage >= 80) {
    print("Grade: B - Great job! 👍")
} else if (percentage >= 70) {
    print("Grade: C - Good effort! ✓")
} else if (percentage >= 60) {
    print("Grade: D - Keep practicing! 📚")
} else {
    print("Grade: F - Review the material! 📖")
}
```

---

## ✅ **Knowledge Check**

Test your understanding:

1. **What are the four basic data types in LangOne?**
   <details><summary>Show Answer</summary>Integer, Float, String, Boolean</details>

2. **What operator checks if two values are equal?**
   <details><summary>Show Answer</summary>`==` (double equals)</details>

3. **What's the difference between `and` and `or`?**
   <details><summary>Show Answer</summary>`and` requires both conditions true, `or` requires at least one true</details>

4. **When would you use a while loop vs a for loop?**
   <details><summary>Show Answer</summary>While: unknown iterations, For: known iterations</details>

5. **What does the modulus operator (%) do?**
   <details><summary>Show Answer</summary>Returns the remainder after division</details>

6. **How do you convert a string to a number?**
   <details><summary>Show Answer</summary>`to_number(string_value)`</details>

---

## 🎓 **What You've Learned**

Congratulations! You now know:

- ✅ All LangOne data types and conversions
- ✅ Arithmetic, comparison, and logical operators
- ✅ Conditional statements (if/else/elif)
- ✅ Loop structures (while, for)
- ✅ Input/output operations
- ✅ Building interactive programs

---

## 🚀 **Next Steps**

### **Practice Projects:**

1. **Temperature Converter**
   - Convert between Celsius, Fahrenheit, Kelvin
   - Validate input ranges
   - Format output nicely

2. **Simple ATM System**
   - Check balance
   - Deposit money
   - Withdraw money (with validation)
   - Show transaction history

3. **Pattern Printer**
   - Print various patterns (triangles, pyramids, diamonds)
   - Use nested loops
   - Allow user to specify size

### **What's Next:**
👉 **[Tutorial 03: Functions and Program Organization](./03_Functions_Organization.md)**

In the next tutorial, you'll learn:
- Creating reusable functions
- Parameters and return values
- Variable scope
- Code organization best practices
- Building modular programs

---

## 💡 **Best Practices**

### **1. Clear Variable Names**
```l1
# ❌ Bad
let x = 25
let y = true

# ✅ Good
let age = 25
let is_student = true
```

### **2. Consistent Formatting**
```l1
# ✅ Good formatting
if (condition) {
    do_something()
}

# Consistent indentation
# Clear spacing
# Readable code
```

### **3. Input Validation**
```l1
# Always validate user input
let age_str = input("Enter age: ")
let age = to_number(age_str)

if (age > 0 and age < 120) {
    # Valid age
} else {
    print("Invalid age!")
}
```

---

## 📚 **Additional Resources**

- 📖 **Data Types Reference**: [docs.langone.dev/types](https://docs.langone.dev/types)
- 📖 **Control Flow Guide**: [docs.langone.dev/control-flow](https://docs.langone.dev/control-flow)
- 💻 **Practice Exercises**: [github.com/langone/exercises](https://github.com/langone/exercises)
- 🎥 **Video Tutorial**: [youtube.com/langone/fundamentals](https://youtube.com/langone/fundamentals)

---

## 🎉 **Congratulations!**

You've mastered the core fundamentals of LangOne programming!

**Progress Tracker:**
- [x] Tutorial 01: Getting Started ✅
- [x] Tutorial 02: Core Fundamentals ✅
- [ ] Tutorial 03: Functions and Organization
- [ ] Tutorial 04: Arrays and Tensors

👉 **Ready to level up?** [Continue to Tutorial 03](./03_Functions_Organization.md)

---

*© 2025 LangOne Project. Part of the official LangOne tutorial series.*

