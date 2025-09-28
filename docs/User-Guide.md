# LangOne User Guide

## How to Build and Run LangOne Programs

This guide explains how end users can build and run LangOne programs on their system.

## Prerequisites

### Required Software
- **Rust 1.70+** - [Download from rustup.rs](https://rustup.rs/)
- **Windows 11** (current development environment)
- **Git** (for cloning the repository)

### Installation Steps

1. **Install Rust**
   ```bash
   # Download and run rustup-init.exe from https://rustup.rs/
   # Or use PowerShell:
   Invoke-WebRequest -Uri "https://win.rustup.rs/x86_64" -OutFile "rustup-init.exe"
   .\rustup-init.exe
   ```

2. **Verify Installation**
   ```bash
   rustc --version
   cargo --version
   ```

## Getting Started

### 1. Clone the Repository
```bash
git clone <repository-url>
cd LangOne
```

### 2. Navigate to Code Directory
```bash
cd code
```

### 3. Build the LangOne Compiler/Interpreter
```bash
cargo build
```

This creates the `langone.exe` executable in `target/debug/` directory.

## Running LangOne Programs

### Method 1: Using Cargo (Recommended)

```bash
# Run a LangOne program
cargo run -- run examples/simple_hello.l1

# Parse and see the AST
cargo run -- parse examples/simple_hello.l1

# Tokenize and see the tokens
cargo run -- tokenize examples/simple_hello.l1

# Interactive REPL
cargo run -- repl
```

### Method 2: Using the Executable Directly

```bash
# Build first
cargo build

# Run using the executable
./target/debug/langone.exe run examples/simple_hello.l1
./target/debug/langone.exe parse examples/simple_hello.l1
./target/debug/langone.exe tokenize examples/simple_hello.l1
./target/debug/langone.exe repl
```

### Method 3: Using Helper Scripts (Windows)

We provide convenient helper scripts for Windows users:

```bash
# Using Batch file
.\run_langone.bat run examples/simple_hello.l1
.\run_langone.bat parse examples/simple_hello.l1
.\run_langone.bat tokenize examples/simple_hello.l1
.\run_langone.bat repl

# Using PowerShell script
.\run_langone.ps1 run examples/simple_hello.l1
.\run_langone.ps1 parse examples/simple_hello.l1
.\run_langone.ps1 tokenize examples/simple_hello.l1
.\run_langone.ps1 repl
```

### Method 4: Install as Global Command (Optional)

```bash
# Install globally
cargo install --path .

# Now you can run from anywhere
langone run my_program.l1
langone parse my_program.l1
langone tokenize my_program.l1
langone repl
```

## Creating Your Own LangOne Programs

### 1. Create a New File
Create a new `.l1` file in the `examples/` directory or anywhere you prefer:

```bash
# Create a new program
notepad my_program.l1
# or
code my_program.l1
```

### 2. Write LangOne Code
```l1
// My First LangOne Program
print("Hello from my program!");

let name = "LangOne Developer";
print("Welcome, " + name);

let x = 10;
let y = 20;
let sum = x + y;
print("10 + 20 = " + sum);
```

### 3. Run Your Program
```bash
cargo run -- run my_program.l1
```

## Available Commands

### `run` - Execute a LangOne Program
```bash
cargo run -- run <file.l1>
```
- Executes the LangOne program
- Shows output and any errors
- Example: `cargo run -- run examples/simple_hello.l1`

### `parse` - Show Abstract Syntax Tree
```bash
cargo run -- parse <file.l1>
```
- Shows the parsed AST structure
- Useful for debugging syntax issues
- Example: `cargo run -- parse examples/simple_hello.l1`

### `tokenize` - Show Tokens
```bash
cargo run -- tokenize <file.l1>
```
- Shows the tokenized representation
- Useful for understanding how the lexer works
- Example: `cargo run -- tokenize examples/simple_hello.l1`

### `repl` - Interactive REPL
```bash
cargo run -- repl
```
- Starts an interactive Read-Eval-Print Loop
- Type LangOne code and see results immediately
- Press Ctrl+C to exit

## Example Programs

### Basic Hello World
```l1
print("Hello, World!");
```

### Variables and Expressions
```l1
let name = "Alice";
let age = 25;
print("Hello, " + name + "! You are " + age + " years old.");
```

### Arithmetic Operations
```l1
let a = 10;
let b = 5;
print("Addition: " + (a + b));
print("Subtraction: " + (a - b));
print("Multiplication: " + (a * b));
print("Division: " + (a / b));
```

### String Concatenation
```l1
let greeting = "Hello";
let name = "World";
let message = greeting + ", " + name + "!";
print(message);
```

## Troubleshooting

### Common Issues

#### 1. "Command not found" or "cargo not found"
**Solution**: Make sure Rust is installed and added to your PATH
```bash
# Check if Rust is installed
rustc --version
cargo --version

# If not installed, install from https://rustup.rs/
```

#### 2. "No such file or directory" when running programs
**Solution**: Make sure you're in the correct directory and the file exists
```bash
# Check current directory
pwd
# Should be: D:\Code\Practice\Others\L1\code

# List files
dir examples
# Should show your .l1 files
```

#### 3. "Parse error" when running programs
**Solution**: Check your LangOne syntax
- Make sure statements end with semicolons: `print("Hello");`
- Use supported syntax only (see Language Features below)
- Check for typos in keywords

#### 4. "Expected identifier" error
**Solution**: This usually means you're using advanced syntax not yet supported
- Stick to basic statements: `print()`, `let`, expressions
- Avoid: `project`, `app`, `function` declarations (not yet implemented)

### Debugging Tips

1. **Use the parse command** to see if your code is syntactically correct:
   ```bash
   cargo run -- parse my_program.l1
   ```

2. **Use the tokenize command** to see how your code is being tokenized:
   ```bash
   cargo run -- tokenize my_program.l1
   ```

3. **Start simple** and build up complexity:
   - Start with `print("Hello");`
   - Add variables: `let x = 42;`
   - Add expressions: `print("Value: " + x);`

## Language Features (Currently Supported)

### ✅ Core Features
- **Print statements**: `print("Hello World");`
- **Variables**: `let x = 42;`
- **Expressions**: `x + y`, `"Hello" + "World"`
- **Data types**: Integers, floats, strings, booleans
- **Arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical**: `&&`, `||`, `!`
- **Comments**: `// This is a comment`

### ✅ Functions & Control Flow
- **Function definitions**: `function add(a: int, b: int) -> int { return a + b; }`
- **Function calls**: `let result = add(5, 3);`
- **Recursive functions**: Full support for recursive calls
- **If/else statements**: `if (x > 0) { print("Positive"); } else { print("Non-positive"); }`
- **While loops**: `while (i < 10) { i = i + 1; }`
- **For loops**: `for (i in 10) { print(i); }`
- **Return statements**: `return value;`

### ✅ Data Structures
- **Arrays**: `let numbers = [1, 2, 3, 4, 5];`
- **Array access**: `let first = numbers[0];`
- **Structs**: `struct Point { x: int, y: int }`
- **Struct instantiation**: `let p = Point { x: 10, y: 20 };`
- **Member access**: `let x = p.x;`

### ✅ Advanced Type System
- **Type annotations**: `let name: string = "Alice";`
- **Function types**: `function add(a: int, b: int) -> int`
- **Generic types**: `function identity<T>(x: T) -> T`
- **Type checking**: Runtime type validation
- **Generic functions**: Full support for type parameters

### ✅ Error Handling
- **Try-catch blocks**: `try { riskyOperation(); } catch (error) { handleError(); }`
- **Throw statements**: `throw "Something went wrong";`
- **Finally blocks**: `try { ... } catch (error) { ... } finally { cleanup(); }`
- **Error propagation**: Errors bubble up through call stack

### ✅ Modules & Classes
- **Module imports**: `import { function1, function2 } from "module";`
- **Module exports**: `export function publicFunction() { ... }`
- **Class definitions**: `class Person { name: string, age: int }`
- **Class inheritance**: `class Student extends Person { ... }`
- **Method definitions**: `method getName() -> string { return this.name; }`

### ✅ Language Enhancements (Latest)
- **Async/Await**: `async function fetchData() -> string { ... }`
- **Await expressions**: `let result = await fetchData();`
- **Pattern matching**: `match (value) { 1 => "One", _ => "Other" }`
- **Macro system**: `macro debug_print(msg) { print("DEBUG: " + msg); }`

### ✅ Performance Features
- **Constant folding**: Compile-time evaluation of constant expressions
- **Dead code elimination**: Removal of unreachable code
- **Variable hoisting**: Optimization of variable declarations
- **Memory management**: Allocation tracking and garbage collection
- **Performance profiling**: Detailed execution statistics

### 🚧 Future Features
- **Pattern guards**: `match (x) { n if n > 0 => "Positive" }`
- **Full macro expansion**: Complete compile-time code generation
- **JIT compilation**: Just-in-time compilation for performance
- **Advanced optimizations**: More sophisticated compiler optimizations

## Performance Notes

- **First run**: May take 10-15 seconds to compile (Rust compilation)
- **Subsequent runs**: Very fast (0.3-0.5 seconds)
- **REPL**: Instant response for simple expressions
- **Large programs**: Currently limited by interpreter performance

## Getting Help

### Documentation
- **Developers Guide**: `docs/Developers-Guide.md` - Complete technical documentation
- **Rust Development Guide**: `docs/Rust-Only-Development-Guide.md` - Development setup
- **This User Guide**: `docs/User-Guide.md` - End-user instructions

### Examples
- Check `examples/` directory for sample programs
- Start with `simple_hello.l1` for basic examples
- Use `intp_tests/` for test cases

### Community
- [Add your community links here]
- [Add your issue tracker here]
- [Add your discussion forum here]

---

**Happy coding with LangOne! 🚀**
