# Tutorial 01: Getting Started with LangOne

## 🎯 **Learning Objectives**

By the end of this tutorial, you will be able to:
- ✅ Install and set up LangOne on your system
- ✅ Write and run your first LangOne program
- ✅ Understand basic LangOne syntax and structure
- ✅ Use the LangOne REPL (Read-Eval-Print Loop)
- ✅ Debug simple errors and understand error messages

**⏱️ Estimated Time**: 30 minutes  
**📋 Prerequisites**: None - This is where everyone starts!  
**💻 Requirements**: Windows, Linux, or macOS computer

---

## 📚 **Introduction: Welcome to LangOne!**

### **What is LangOne?**

LangOne is a **"Green Code First"** programming language designed for:
- **Maximum Performance**: 10-17x faster than Python
- **Minimal Memory Usage**: 87-88% less memory than traditional languages
- **Energy Efficiency**: 8-16x less energy consumption
- **AI/ML Optimization**: Built for modern computing workloads

### **Why Learn LangOne?**

```
Traditional Programming Languages:
  Python  → Slow but easy to learn
  C/C++   → Fast but complex
  Julia   → Fast for science, steep learning curve
  
LangOne → FAST + EASY + COMPLETE ✨
```

### **What Makes LangOne Special?**

1. **🚀 Performance**: Compiled language with JIT optimization
2. **🌱 Green Computing**: Energy-efficient by design
3. **🎯 Complete Ecosystem**: Everything you need in one language
4. **💡 Developer-Friendly**: Intuitive syntax, easy to learn

---

## 🔧 **Part 1: Installation and Setup**

### **Step 1: Download LangOne**

Visit the official LangOne website or repository:
```
https://github.com/langone/langone
```

Download the appropriate version for your system:
- **Windows**: `langone-windows-x64.exe`
- **Linux**: `langone-linux-x64`
- **macOS**: `langone-macos-x64`

### **Step 2: Install LangOne**

#### **On Windows:**
```powershell
# Option 1: Using PowerShell (Recommended)
# Extract the download and add to PATH
$env:PATH += ";C:\Program Files\LangOne"

# Option 2: Manual Installation
# 1. Extract langone.exe to a folder
# 2. Add that folder to your System PATH
# 3. Restart your terminal
```

#### **On Linux/macOS:**
```bash
# Extract and install
tar -xzf langone-linux-x64.tar.gz
sudo mv langone /usr/local/bin/

# Verify installation
langone --version
```

### **Step 3: Verify Installation**

Open a new terminal/command prompt and type:
```bash
langone --version
```

You should see output like:
```
LangOne v0.6.0-alpha.1
Green Code First Language
```

✅ **Checkpoint**: If you see the version number, you're ready to proceed!

---

## 💻 **Part 2: Your First LangOne Program**

### **The Classic "Hello, World!"**

Let's start with the simplest program. Create a file called `hello.l1`:

```l1
print("Hello, World!")
```

**Run it:**
```bash
langone run hello.l1
```

**Output:**
```
Hello, World!
```

🎉 **Congratulations!** You just ran your first LangOne program!

---

### **Understanding the Code**

Let's break down what happened:

```l1
print("Hello, World!")
│     │              │
│     │              └─ String: Text in quotes
│     └──────────────── String argument
└──────────────────────── Function call
```

**Key Concepts:**
- `print()` is a **function** that displays text
- `"Hello, World!"` is a **string** (text data)
- The parentheses `()` contain the function's arguments
- No semicolons needed at the end of statements!

---

### **🔨 Hands-On Exercise 1: Modify Your Program**

**Task**: Modify your program to print your name.

**Expected Output:**
```
Hello, [Your Name]!
```

<details>
<summary>💡 Click here for the solution</summary>

```l1
print("Hello, Alice!")  # Replace Alice with your name
```
</details>

---

## 🎮 **Part 3: Using the LangOne REPL**

The **REPL** (Read-Eval-Print Loop) lets you experiment with LangOne interactively.

### **Starting the REPL**

```bash
langone repl
```

You'll see a prompt:
```
LangOne v0.6.0-alpha.1
Green Code First Language
>>> 
```

### **Try These Commands:**

```l1
>>> print("Hello from REPL!")
Hello from REPL!

>>> 2 + 2
4

>>> 10 * 5
50

>>> "Lang" + "One"
LangOne
```

### **REPL Tips:**
- Press `Enter` to execute a line
- Type `exit()` or press `Ctrl+D` to quit
- Use Up/Down arrows for command history
- Great for testing small code snippets!

---

### **🔨 Hands-On Exercise 2: REPL Practice**

Try these in the REPL:

1. Calculate: `15 + 27`
2. Calculate: `100 / 4`
3. Concatenate: `"Hello " + "LangOne"`
4. Print: `print("I'm learning LangOne!")`

✅ **Checkpoint**: Can you get all four to work?

---

## 📝 **Part 4: Basic Syntax and Structure**

### **Comments**

Comments help explain your code (they're ignored by the compiler):

```l1
# This is a single-line comment

# Comments can explain what code does
print("This code runs")  # Inline comment

# TODO: Add more features later
```

**Best Practice:** Use comments to explain *why*, not *what*.

### **Variables**

Variables store data that can change:

```l1
# Creating variables
let name = "Alice"
let age = 25
let pi = 3.14159
let is_student = true

# Using variables
print(name)        # Output: Alice
print(age)         # Output: 25
```

**Variable Rules:**
- Start with a letter or underscore
- Can contain letters, numbers, underscores
- Case-sensitive (`name` ≠ `Name`)
- Use descriptive names (`age` is better than `a`)

### **Basic Data Types**

```l1
# Numbers
let integer = 42           # Whole numbers
let float_num = 3.14       # Decimal numbers

# Strings
let text = "Hello"         # Text in quotes
let message = 'World'      # Single quotes work too

# Booleans
let is_true = true         # True/false values
let is_false = false

# Print type information
print(integer)    # Output: 42
print(text)       # Output: Hello
```

---

### **🔨 Hands-On Exercise 3: Variables Practice**

Create a file `my_info.l1` with your personal information:

```l1
# Store your information
let name = "Your Name"
let age = 0              # Your age
let city = "Your City"
let favorite_language = "LangOne"

# Print it out
print("Name: " + name)
print("Age: " + to_string(age))
print("City: " + city)
print("Favorite Language: " + favorite_language)
```

**Note**: `to_string()` converts numbers to text for printing.

<details>
<summary>💡 Click here for a complete example</summary>

```l1
# My Information
let name = "Alice Johnson"
let age = 25
let city = "San Francisco"
let favorite_language = "LangOne"

# Display information
print("Name: " + name)
print("Age: " + to_string(age))
print("City: " + city)
print("Favorite Language: " + favorite_language)
print("I'm learning LangOne!")
```

**Output:**
```
Name: Alice Johnson
Age: 25
City: San Francisco
Favorite Language: LangOne
I'm learning LangOne!
```
</details>

---

## 🐛 **Part 5: Understanding Error Messages**

Errors are normal! Let's learn to read them.

### **Common Beginner Errors**

#### **Error 1: Syntax Error**
```l1
print("Hello World"
```

**Error Message:**
```
Error: Expected ')' at line 1
print("Hello World"
                   ^
```

**Fix:** Add the closing parenthesis
```l1
print("Hello World")
```

#### **Error 2: Undefined Variable**
```l1
print(unknown_variable)
```

**Error Message:**
```
Error: Undefined variable 'unknown_variable' at line 1
```

**Fix:** Define the variable first
```l1
let unknown_variable = "Now it exists!"
print(unknown_variable)
```

#### **Error 3: Type Mismatch**
```l1
let result = "Hello" + 5
```

**Error Message:**
```
Error: Cannot add String and Integer at line 1
```

**Fix:** Convert the number to a string
```l1
let result = "Hello" + to_string(5)
print(result)  # Output: Hello5
```

### **Debugging Tips**

1. **Read the error message carefully** - It tells you what's wrong
2. **Check the line number** - Where the error occurred
3. **Look at the context** - Lines before and after
4. **Start simple** - Comment out code to isolate the problem
5. **Use print statements** - Debug by printing variable values

---

### **🔨 Hands-On Exercise 4: Fix the Bugs**

This program has three errors. Can you find and fix them?

```l1
# Bug-filled program
let name = "Alex
print(name)

let age = 30
print("I am " + age + " years old")

print(unknown
```

<details>
<summary>💡 Click here for the solution</summary>

```l1
# Fixed program
let name = "Alex"        # Added closing quote
print(name)

let age = 30
print("I am " + to_string(age) + " years old")  # Converted age to string

print("unknown")         # Added quotes and closing parenthesis
```
</details>

---

## 🎯 **Part 6: Your First Complete Program**

Let's combine everything you've learned into a complete program!

### **Program: Personal Greeting**

Create a file called `greeting.l1`:

```l1
# Personal Greeting Program
# Tutorial 01 - Final Project

# User information
let name = "Alice"
let age = 25
let city = "San Francisco"

# Display greeting
print("=" * 40)  # Print a line of equals signs
print("Welcome to LangOne!")
print("=" * 40)
print("")

# Display user info
print("Hello, " + name + "!")
print("You are " + to_string(age) + " years old.")
print("You live in " + city + ".")
print("")

# Display a fun fact
print("Fun Fact:")
print("LangOne is 10-17x faster than Python!")
print("You made a great choice learning it!")
print("")

# Closing message
print("Happy coding with LangOne! 🚀")
```

**Run it:**
```bash
langone run greeting.l1
```

**Expected Output:**
```
========================================
Welcome to LangOne!
========================================

Hello, Alice!
You are 25 years old.
You live in San Francisco.

Fun Fact:
LangOne is 10-17x faster than Python!
You made a great choice learning it!

Happy coding with LangOne! 🚀
```

---

### **🔨 Final Exercise: Customize Your Greeting**

**Task**: Modify the greeting program to:
1. Use your own information
2. Add your favorite hobby
3. Add an interesting fact about yourself
4. Make it personal and creative!

**Challenge**: Can you add an ascii art banner at the top?

---

## ✅ **Knowledge Check**

Test your understanding:

1. **What command runs a LangOne file?**
   <details><summary>Show Answer</summary>`langone run filename.l1`</details>

2. **How do you start the LangOne REPL?**
   <details><summary>Show Answer</summary>`langone repl`</details>

3. **What's wrong with this code?**
   ```l1
   print("Hello World"
   ```
   <details><summary>Show Answer</summary>Missing closing parenthesis</details>

4. **How do you convert a number to a string?**
   <details><summary>Show Answer</summary>`to_string(number)`</details>

5. **What symbol starts a comment?**
   <details><summary>Show Answer</summary>`#`</details>

---

## 🎓 **What You've Learned**

Congratulations! You now know:

- ✅ How to install and set up LangOne
- ✅ How to write and run LangOne programs
- ✅ Basic syntax (comments, variables, data types)
- ✅ How to use the REPL for experimentation
- ✅ How to read and fix common errors
- ✅ How to create a complete program

---

## 🚀 **Next Steps**

You're ready to move forward!

### **What's Next:**
👉 **[Tutorial 02: Core Language Fundamentals](./02_Core_Fundamentals.md)**

In the next tutorial, you'll learn:
- Control flow (if statements, loops)
- More advanced data types
- String manipulation
- Mathematical operations
- Input/output operations

### **Practice Suggestions:**

Before moving on, try these exercises:

1. **Calculator**: Create a simple calculator program
   ```l1
   let a = 10
   let b = 5
   print("Addition: " + to_string(a + b))
   print("Subtraction: " + to_string(a - b))
   # Add more operations
   ```

2. **Mad Libs**: Create a fun mad libs game
   ```l1
   let noun = "cat"
   let verb = "jumps"
   let adjective = "quick"
   print("The " + adjective + " " + noun + " " + verb + "!")
   ```

3. **ASCII Art**: Create an ASCII art program
   ```l1
   print("   /\\_/\\  ")
   print("  ( o.o ) ")
   print("   > ^ <  ")
   print("  /|   |\\")
   ```

---

## 💡 **Common Pitfalls and Solutions**

### **Pitfall 1: Forgetting to Convert Types**
```l1
# ❌ Wrong
print("Age: " + 25)

# ✅ Correct
print("Age: " + to_string(25))
```

### **Pitfall 2: Missing Quotes**
```l1
# ❌ Wrong
print(Hello World)

# ✅ Correct
print("Hello World")
```

### **Pitfall 3: Typos in Variable Names**
```l1
# ❌ Wrong
let userName = "Alice"
print(username)  # Lowercase 'n'

# ✅ Correct
let userName = "Alice"
print(userName)  # Matching case
```

---

## 📚 **Additional Resources**

- 📖 **Official Documentation**: [docs.langone.dev](https://docs.langone.dev)
- 💬 **Community Forum**: [community.langone.dev](https://community.langone.dev)
- 🎥 **Video Tutorials**: [youtube.com/langone](https://youtube.com/langone)
- 💻 **Code Examples**: [github.com/langone/examples](https://github.com/langone/examples)

---

## 🎉 **Congratulations!**

You've completed your first LangOne tutorial! You're now ready to explore more advanced concepts.

**Keep practicing, and remember**: Every expert programmer started exactly where you are now.

**Happy coding!** 🚀

---

**Progress Tracker:**
- [x] Tutorial 01: Getting Started ✅
- [ ] Tutorial 02: Core Fundamentals
- [ ] Tutorial 03: Functions and Organization

👉 **Ready for the next challenge?** [Continue to Tutorial 02](./02_Core_Fundamentals.md)

---

*© 2025 LangOne Project. Part of the official LangOne tutorial series.*

