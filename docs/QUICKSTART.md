# LangOne Quick Start Guide

**Welcome to LangOne!** This guide will get you up and running in under 5 minutes.

## 🚀 Installation (No Rust Required!)

### **Option 1: One-Click Install (Recommended)**

#### **Windows (PowerShell)**
```powershell
# Run as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/langone/langone/main/install.ps1" -OutFile "install.ps1"
.\install.ps1
```

#### **Linux/macOS**
```bash
curl -fsSL https://raw.githubusercontent.com/langone/langone/main/install.sh | bash
```

### **Option 2: Package Managers**

#### **Windows (winget)**
```powershell
winget install LangOne.LangOne
```

#### **macOS (Homebrew)**
```bash
brew install langone
```

#### **Linux (apt)**
```bash
# Add repository (when available)
sudo apt update
sudo apt install langone
```

### **Option 3: Direct Download**

1. Go to [Releases](https://github.com/langone/langone/releases/latest)
2. Download the binary for your platform:
   - **Windows**: `langone-windows-x64.exe`
   - **Linux**: `langone-linux-x64`
   - **macOS**: `langone-macos-x64`
3. Make executable (Linux/macOS): `chmod +x langone`
4. Add to PATH or run from current directory

## ✅ Verify Installation

```bash
langone --version
# Should output: LangOne version 0.1.0
```

## 🎯 Quick Test

### **1. Hello World**
Create a file `hello.l1`:
```langone
print("Hello, LangOne!");
```

Run it:
```bash
langone run hello.l1
# Output: Hello, LangOne!
```

### **2. Interactive REPL**
```bash
langone repl
```

Try these commands:
```langone
langone> 42 + 8
✅ Execution successful (0.23ms)
Result: Integer(50)

langone> let x = 42;
langone> x * 2
✅ Execution successful (0.21ms)
Result: Integer(84)

langone> upper("hello")
✅ Execution successful (0.18ms)
Result: String("HELLO")

langone> exit
```

### **3. Standard Library Functions**
```langone
// Math functions
abs(-15)        // 15
min(10, 20)     // 10
max(10, 20)     // 20
sqrt(25)        // 5.0

// String functions
len("hello")    // 5
upper("hello")  // "HELLO"
lower("WORLD")  // "world"
trim("  test  ") // "test"

// Type functions
to_string(42)   // "42"
to_number("123") // 123
type_of("hello") // "string"
```

## 🎨 VS Code Extension

### **Install Extension**
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "LangOne"
4. Install the LangOne extension

### **Features**
- ✅ **Syntax Highlighting** - Full language support
- ✅ **Error Diagnostics** - Real-time error detection
- ✅ **IntelliSense** - Autocomplete and hover information
- ✅ **Code Snippets** - 15+ useful snippets
- ✅ **Run Commands** - Execute files and selections

### **Usage**
1. Open any `.l1` file
2. Get syntax highlighting automatically
3. See errors as you type
4. Use Ctrl+Space for autocomplete
5. Right-click → "Run LangOne File"

## 📚 Language Features

### **Variables**
```langone
let x = 42;
let name = "LangOne";
let isActive = true;
let numbers = [1, 2, 3];
```

### **Functions**
```langone
function greet(name) -> string {
    return "Hello, " + name + "!";
}

// Async functions
async function fetchData() -> string {
    return "Async data";
}

let result = await fetchData();
```

### **Pattern Matching**
```langone
match (value) {
    42 => "Found the answer!",
    x if x < 10 => "Small number",
    _ => "Other number"
}
```

### **Control Flow**
```langone
// If/else
if (x > 0) {
    print("Positive");
} else {
    print("Not positive");
}

// Loops
for (let i = 0; i < 5; i = i + 1) {
    print("Iteration: " + to_string(i));
}

while (x > 0) {
    x = x - 1;
}
```

### **Macros**
```langone
macro debug(expr) {
    print("Debug: " + to_string(expr));
}

debug(42 + 8); // Prints: Debug: 50
```

## 🔧 Command Reference

```bash
# Run a LangOne file
langone run file.l1

# Start interactive REPL
langone repl

# Parse and show AST
langone parse file.l1

# Show help
langone --help

# Show version
langone --version
```

## 🆘 Troubleshooting

### **Installation Issues**

#### **"command not found" after installation**
- **Windows**: Restart PowerShell/Command Prompt
- **Linux/macOS**: Run `source ~/.bashrc` or `source ~/.zshrc`

#### **Permission denied (Linux/macOS)**
```bash
chmod +x langone
```

#### **Windows execution policy error**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **Runtime Issues**

#### **"Expected Semicolon" error**
Add semicolons at the end of statements:
```langone
let x = 42;  // ← Add semicolon
```

#### **"Undefined variable" error**
Define variables before use:
```langone
let x = 42;  // Define first
print(x);    // Then use
```

### **VS Code Extension Issues**

#### **Syntax highlighting not working**
1. Open a `.l1` file
2. Click on "LangOne" in the bottom-right status bar
3. Select "LangOne" from the language list

#### **Diagnostics not showing**
1. Check that the extension is enabled
2. Restart VS Code
3. Ensure `langone` is in your PATH

## 📖 Next Steps

1. **Explore Examples**: Check out the `/examples` folder
2. **Read Documentation**: Visit [docs/](docs/)
3. **Join Community**: 
   - GitHub Discussions
   - Discord (coming soon)
4. **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## 🎉 You're Ready!

You now have LangOne installed and running! Try creating your first program:

```langone
// my_first_program.l1
function fibonacci(n) -> integer {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

print("Fibonacci sequence:");
for (let i = 0; i < 10; i = i + 1) {
    print(to_string(fibonacci(i)));
}
```

Run it:
```bash
langone run my_first_program.l1
```

**Welcome to LangOne!** 🚀
