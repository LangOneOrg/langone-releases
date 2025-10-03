# 🎮 Basic Usage

**Write your first LangOne program in minutes!**

This guide will teach you the basics of LangOne programming. No prior experience needed!

---

## 🚀 **Your First Program**

### **Step 1: Create a File**
Create a new file called `hello.l1`:

```langone
// Hello World in LangOne
print("Hello, LangOne! 🚀");
```

### **Step 2: Run Your Program**
```bash
langone run hello.l1
```

**Output:**
```
Hello, LangOne! 🚀
```

**🎉 Congratulations!** You've written your first LangOne program!

---

## 💡 **Basic Concepts**

### **Variables**
Store information in variables:

```langone
let name = "Alice";
let age = 25;
let isStudent = true;

print("Name: " + name);
print("Age: " + age);
print("Student: " + isStudent);
```

### **Numbers and Math**
LangOne handles numbers automatically:

```langone
let a = 10;
let b = 5;

print("Addition: " + (a + b));        // 15
print("Subtraction: " + (a - b));     // 5
print("Multiplication: " + (a * b));  // 50
print("Division: " + (a / b));        // 2.0
```

### **Lists (Arrays)**
Store multiple values:

```langone
let fruits = ["apple", "banana", "orange"];

print("First fruit: " + fruits[0]);  // apple
print("All fruits: " + fruits);      // [apple, banana, orange]

// Add to list
fruits.push("grape");
print("Updated: " + fruits);          // [apple, banana, orange, grape]
```

---

## 🔄 **Control Flow**

### **If Statements**
Make decisions:

```langone
let score = 85;

if (score >= 90) {
    print("Grade: A");
} else if (score >= 80) {
    print("Grade: B");
} else if (score >= 70) {
    print("Grade: C");
} else {
    print("Grade: F");
}
```

### **Loops**
Repeat actions:

```langone
// Count from 1 to 5
for (i in 5) {
    print("Count: " + i);
}

// Loop through a list
let colors = ["red", "green", "blue"];
for (color in colors) {
    print("Color: " + color);
}
```

---

## 🔧 **Functions**

### **Create Your Own Functions**
```langone
function greet(name: string) -> string {
    return "Hello, " + name + "!";
}

let message = greet("Alice");
print(message);  // Hello, Alice!
```

### **Built-in Functions**
LangOne comes with many useful functions:

```langone
let numbers = [1, 2, 3, 4, 5];

// Find the maximum
let max = max(numbers);           // 5

// Find the minimum
let min = min(numbers);           // 1

// Calculate sum
let sum = numbers.sum();          // 15

// Get random number
let random = randomInt(1, 100);   // Random number between 1 and 100
```

---

## 📊 **Working with Data**

### **Simple Data Processing**
```langone
let scores = [85, 92, 78, 96, 88];

// Calculate average
let sum = 0;
for (score in scores) {
    sum = sum + score;
}
let average = sum / scores.length;
print("Average score: " + average);

// Find highest score
let highest = max(scores);
print("Highest score: " + highest);
```

### **String Operations**
```langone
let text = "Hello, World!";

print("Length: " + text.length);           // 13
print("Uppercase: " + text.toUpperCase()); // HELLO, WORLD!
print("Lowercase: " + text.toLowerCase()); // hello, world!
print("Substring: " + text.substring(0, 5)); // Hello
```

---

## 🎯 **Interactive Mode (REPL)**

### **Start Interactive Mode**
```bash
langone repl
```

### **Try These Commands**
```langone
> let name = "LangOne"
> print("Hello, " + name + "!")
Hello, LangOne!

> let numbers = [1, 2, 3, 4, 5]
> let doubled = numbers.map(function(x: int) -> int { return x * 2; })
> print(doubled)
[2, 4, 6, 8, 10]

> exit
```

---

## 🏆 **Your First Project**

### **Simple Calculator**
Create `calculator.l1`:

```langone
function add(a: int, b: int) -> int {
    return a + b;
}

function multiply(a: int, b: int) -> int {
    return a * b;
}

// Test the calculator
let result1 = add(5, 3);
let result2 = multiply(4, 6);

print("5 + 3 = " + result1);    // 8
print("4 * 6 = " + result2);     // 24
```

Run it:
```bash
langone run calculator.l1
```

---

## 🎊 **You're Ready!**

You've learned the basics of LangOne! Here's what you can do now:

### **Practice More**
- Try modifying the examples above
- Create your own simple programs
- Experiment with the interactive mode

### **Learn Advanced Features**
- [🚀 Next Steps](next-steps.md) - Explore advanced features
- [📖 Complete Documentation](index.md) - Comprehensive guides
- [🎓 Tutorial Series](../public-release/tutorials/README.md) - 15 comprehensive tutorials

### **Get Help**
- [💬 Community Discussions](https://github.com/langone-project/langone/discussions)
- [🐛 Report Issues](https://github.com/langone-project/langone/issues)

---

**Great job! You're on your way to becoming a LangOne developer! 🌟**
