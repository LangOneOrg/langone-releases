# LangOne Development Guide: Rust-Only Interpreter Approach

## Overview

LangOne is implemented in pure Rust with an interpreter-based approach for rapid development and iteration. This guide provides a complete setup for developing LangOne on Windows 11 with Visual Studio Enterprise.

## Development Philosophy

### Why Rust-Only for Initial Development?

- **Simpler Setup**: No need to wrestle with LLVM versions, bindings, or environment configuration
- **Faster Progress**: Focus on syntax, parser, AST, and runtime features instead of low-level codegen
- **Cleaner MVP**: A working interpreter can prove LangOne's concepts quickly
- **Future Flexibility**: LLVM can be added later as a backend for native compilation and optimizations

### Why Interpreter Over Compiler?

- **Rapid Prototyping**: Quick iteration on language features and syntax
- **Easy Debugging**: Step-through execution and runtime inspection
- **Resource Management**: Built-in tracking of RAM/GPU/CPU usage
- **Cross-Platform**: Runs anywhere Rust runs

## Current Status (December 2024)

**🎉 LangOne Interpreter is Fully Functional!**

The core LangOne interpreter is now complete and working. You can write and execute LangOne programs with:

- ✅ **Basic Expressions**: Numbers, strings, booleans
- ✅ **Variables**: `let x = 42;`
- ✅ **Function Calls**: `print("Hello World");`
- ✅ **Arithmetic**: `x + y`, `x * y`, etc.
- ✅ **String Operations**: `"text" + variable`
- ✅ **Comments**: `// This is a comment`
- ✅ **Multiple Statements**: Full programs with multiple lines

### Quick Start

```bash
# Run a simple LangOne program
cargo run -- run examples/hello.l1

# Parse and see the AST
cargo run -- parse examples/hello.l1

# Tokenize and see the tokens
cargo run -- tokenize examples/hello.l1
```

## Development Phases

### Phase 1: Core Language (Rust Interpreter) ✅ COMPLETED
- [x] Lexer and parser
- [x] AST definitions
- [x] Basic interpreter framework
- [x] Expression evaluation
- [x] Variable declarations and assignments
- [x] Function calls and built-in functions
- [x] String concatenation
- [x] Comment parsing
- [x] Error handling and reporting
- [x] CLI interface with run/parse/tokenize commands

### Phase 2: Runtime Features ✅ COMPLETED
- [x] Tree-walk interpreter implementation
- [x] Environment management with proper scoping
- [x] Runtime value system (integers, floats, strings, booleans, functions)
- [x] Built-in functions (print, clock)
- [x] Expression evaluation (arithmetic, comparison, logical operations)
- [x] Memory management for variables and functions
- [x] Debugging support with detailed error messages

### Phase 3: Language Features ✅ PARTIALLY COMPLETED
- [x] Variables and constants (let statements)
- [x] Basic function calls
- [x] String operations and concatenation
- [x] Comments (single-line // comments)
- [ ] Function definitions with parameters
- [ ] Control flow (if/while/for statements)
- [ ] Data structures (arrays, structs, enums)
- [ ] Pattern matching

### Phase 4: Advanced Features
- [ ] Async/await support
- [ ] Concurrency primitives
- [ ] Quantum computing stubs
- [ ] AI/ML integration hooks
- [ ] Resource optimization

### Phase 5: Developer Tools
- [ ] REPL (Read-Eval-Print Loop)
- [ ] LSP server for editors
- [ ] Package manager
- [ ] Web playground

### Phase 6: Future LLVM Backend (Optional)
- [ ] Native code generation
- [ ] Performance optimizations
- [ ] GPU kernel compilation
- [ ] WebAssembly target

## Project Structure

```
L1/
├── src/
│   ├── ast.rs              # Abstract Syntax Tree definitions
│   ├── interpreter.rs      # Tree-walk interpreter
│   ├── vm.rs              # Bytecode virtual machine (future)
│   ├── runtime.rs         # Runtime environment and resource management
│   ├── errors.rs          # Error handling
│   ├── lexer.rs           # Lexical analysis
│   ├── parser.rs          # Syntax analysis
│   └── lib.rs             # Library entry point
├── examples/
│   └── hello.l1           # Example LangOne programs
├── tests/
│   └── integration/       # Integration tests
├── Docs/
│   └── Rust-Only-Development-Guide.md
├── Cargo.toml             # Dependencies and configuration
└── README.md
```

## Dependencies

### Core Dependencies
- **anyhow/thiserror**: Error handling
- **clap**: CLI argument parsing
- **serde**: Serialization for AST and configuration
- **log/env_logger**: Logging
- **regex**: String processing
- **chrono**: Time handling

### Development Dependencies
- **criterion**: Benchmarking
- **proptest**: Property-based testing
- **mockall**: Mock testing

## Interpreter Architecture

### Tree-Walk Interpreter
```rust
pub struct Interpreter {
    environment: Environment,
    globals: HashMap<String, Value>,
    locals: Vec<HashMap<String, Value>>,
}

impl Interpreter {
    pub fn interpret(&mut self, statements: &[AstNode]) -> Result<Value> {
        for statement in statements {
            self.execute(statement)?;
        }
        Ok(Value::Null)
    }
}
```

### Value System
```rust
#[derive(Debug, Clone, PartialEq)]
pub enum Value {
    Integer(i64),
    Float(f64),
    String(String),
    Boolean(bool),
    Function(FunctionValue),
    Array(Vec<Value>),
    Object(HashMap<String, Value>),
    Null,
}
```

### Environment Management
```rust
pub struct Environment {
    values: HashMap<String, Value>,
    enclosing: Option<Box<Environment>>,
}

impl Environment {
    pub fn define(&mut self, name: String, value: Value) {
        self.values.insert(name, value);
    }
    
    pub fn get(&self, name: &str) -> Result<Value> {
        if let Some(value) = self.values.get(name) {
            Ok(value.clone())
        } else if let Some(ref enclosing) = self.enclosing {
            enclosing.get(name)
        } else {
            Err(LangOneError::UndefinedVariable(name.to_string()))
        }
    }
}
```

## Development Workflow

### 1. Building the Project
```bash
# Check compilation
cargo check

# Build in debug mode
cargo build

# Build in release mode
cargo build --release

# Run tests
cargo test

# Run benchmarks
cargo bench
```

### 2. Running Examples
```bash
# Run a LangOne program
cargo run -- run examples/hello.l1

# Start REPL
cargo run -- repl

# Parse and show AST
cargo run -- parse examples/hello.l1

# Tokenize and show tokens
cargo run -- tokenize examples/hello.l1
```

### 3. Development Tools
```bash
# Watch for changes and rebuild
cargo watch -x check

# Format code
cargo fmt

# Lint code
cargo clippy

# Update dependencies
cargo update
```

## Example: Hello World

### Input (hello.l1)
```l1
project "HelloWorld" {
    version = "1.0.0"
}

app "HelloWorld" {
    main() {
        print("Hello, World from LangOne! 🚀")
        
        let x = 42
        let y = 8
        let result = x + y
        
        print("42 + 8 = " + result)
    }
}
```

### Interpreter Output
```
Hello, World from LangOne! 🚀
42 + 8 = 50
```

## Resource Management

### Memory Tracking
```rust
pub struct ResourceManager {
    memory_usage: usize,
    max_memory: usize,
    allocations: Vec<Allocation>,
}

impl ResourceManager {
    pub fn allocate(&mut self, size: usize) -> Result<AllocationId> {
        if self.memory_usage + size > self.max_memory {
            return Err(LangOneError::OutOfMemory);
        }
        // Track allocation
        Ok(allocation_id)
    }
}
```

### GPU Resource Tracking
```rust
pub struct GPUManager {
    available_memory: usize,
    active_kernels: Vec<Kernel>,
    compute_units: usize,
}
```

## Testing Strategy

### Unit Tests
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_interpreter_arithmetic() {
        let mut interpreter = Interpreter::new();
        let result = interpreter.evaluate("2 + 3 * 4");
        assert_eq!(result, Value::Integer(14));
    }

    #[test]
    fn test_variable_assignment() {
        let mut interpreter = Interpreter::new();
        interpreter.execute("let x = 42");
        let value = interpreter.get_variable("x");
        assert_eq!(value, Value::Integer(42));
    }
}
```

### Integration Tests
```rust
#[test]
fn test_hello_world_program() {
    let source = include_str!("../examples/hello.l1");
    let mut interpreter = Interpreter::new();
    let result = interpreter.run(source);
    assert!(result.is_ok());
}
```

## Performance Considerations

### Interpreter Optimizations
- **Value Caching**: Cache frequently used values
- **Function Lookup**: Optimize function resolution
- **Memory Pool**: Reuse memory allocations
- **JIT Hints**: Prepare for future JIT compilation

### Profiling
```rust
// Use criterion for benchmarking
use criterion::{criterion_group, criterion_main, Criterion};

fn benchmark_arithmetic(c: &mut Criterion) {
    c.bench_function("arithmetic", |b| {
        b.iter(|| interpreter.evaluate("2 + 3 * 4"))
    });
}
```

## Future LLVM Integration

When ready to add LLVM backend:

1. **Keep Interpreter**: Maintain interpreter for development and debugging
2. **Add Compiler**: Create LLVM-based compiler as alternative backend
3. **Unified Interface**: Both interpreter and compiler use same AST
4. **Performance Comparison**: Benchmark interpreter vs compiled code

## Resources

- [Rust Book](https://doc.rust-lang.org/book/)
- [Crafting Interpreters](https://craftinginterpreters.com/)
- [LangOne Repository](https://github.com/langone/langone)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

Apache-2.0 - See LICENSE file for details.
