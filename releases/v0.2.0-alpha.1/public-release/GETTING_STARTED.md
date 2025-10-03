# 🎮 Getting Started

**Write your first LangOne program in under 10 minutes!**

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
```langone
let name = "Alice";
let age = 25;
let isStudent = true;

print("Name: " + name);
print("Age: " + age);
```

### **Numbers and Math**
```langone
let a = 10;
let b = 5;

print("Addition: " + (a + b));        // 15
print("Multiplication: " + (a * b));  // 50
print("Division: " + (a / b));        // 2.0
```

### **Lists (Arrays)**
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
```langone
let score = 85;

if (score >= 90) {
    print("Grade: A");
} else if (score >= 80) {
    print("Grade: B");
} else {
    print("Grade: C");
}
```

### **Loops**
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
```langone
let numbers = [1, 2, 3, 4, 5];

// Find the maximum
let max = max(numbers);           // 5

// Calculate sum
let sum = numbers.sum();          // 15

// Get random number
let random = randomInt(1, 100);   // Random number between 1 and 100
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
- **[Complete Tutorial Series](tutorials/README.md)** - 19.5 hours of structured learning
- **[Sample Programs](samples/README.md)** - Working examples
- **[Performance Optimization](tutorials/13_Performance_Optimization.md)** - Speed up your code

### **Get Help**
- Join community discussions
- Report issues and bugs
- Ask questions

---

**Great job! You're on your way to becoming a LangOne developer! 🌟**
