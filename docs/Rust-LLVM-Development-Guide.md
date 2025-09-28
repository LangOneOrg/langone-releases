# LangOne Development Guide: Rust + LLVM Integration

## Overview

LangOne is implemented in Rust with LLVM integration for code generation and optimization. This guide provides a complete setup for developing LangOne on Windows 11 with Visual Studio Enterprise.

## Development Philosophy

### Why Rust for Compiler Development?

- **Memory Safety**: Prevents common bugs (dangling pointers, data races) at compile time
- **Performance**: C/C++-like performance for large-scale compilation
- **Ecosystem**: Excellent crates for parsing, error handling, LLVM integration
- **Maintainability**: Strict compiler ensures clean, maintainable code

### Why LLVM Integration?

- **Battle-tested Backend**: Used by Swift, Rust, Julia, Kotlin Native, Zig
- **Cross-platform**: Generates optimized machine code across architectures
- **Extensibility**: Targets WASM, GPU kernels, quantum simulators
- **Optimizations**: Decades of optimization passes

## Development Phases

### Phase 1: Compiler Frontend (Rust only)
- [x] Build lexer (hand-written)
- [x] Build parser + AST structures
- [ ] Implement semantic checks (types, resources)

### Phase 2: Intermediate Representation (IR)
- [ ] Create LangOne IR (simplified AST → IR)
- [ ] Add basic passes (constant folding, dead-code elimination)

### Phase 3: LLVM Backend Integration
- [x] Use inkwell (safe Rust wrapper around LLVM)
- [ ] Map LangOne IR → LLVM IR → native binary
- [ ] Enable multi-target support (x86, ARM, WASM)

### Phase 4: Runtime + Resource Manager
- [ ] Implement RAM/GPU/CPU managers in Rust
- [ ] Add hooks for observability, sandboxing, quantum stubs

### Phase 5: Developer Tools
- [ ] LSP server for editors (VSCode, Neovim)
- [ ] Package manager (langonepm)
- [ ] WASM REPL (for playground in browsers)

## Environment Setup

### Prerequisites

1. **Rust Toolchain** (via rustup.rs)
   ```bash
   # Install Rust
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   
   # Install additional tools
   cargo install cargo-edit cargo-watch cargo-insta
   ```

2. **LLVM 18.1.0** (Pre-installed)
   - Location: `D:\Program Files\LLVM`
   - Includes: clang, lld, lldb, and all LLVM tools

3. **Visual Studio Enterprise** (for C++ toolchain)
   - Required for LLVM C++ dependencies
   - MSVC compiler toolchain

### Environment Configuration

The project includes `.cargo/config.toml` with proper LLVM configuration:

```toml
[env]
LLVM_SYS_181_PREFIX = "D:\\Program Files\\LLVM"
LLVM_LIB_DIR = "D:\\Program Files\\LLVM\\lib"
LLVM_INCLUDE_DIR = "D:\\Program Files\\LLVM\\include"

[target.x86_64-pc-windows-msvc]
rustflags = ["-C", "link-arg=/LIBPATH:D:\\Program Files\\LLVM\\lib"]
```

### PowerShell Environment Setup

```powershell
# Set LLVM environment variables
$env:LLVM_SYS_181_PREFIX = "D:\Program Files\LLVM"
$env:LLVM_LIB_DIR = "D:\Program Files\LLVM\lib"
$env:LLVM_INCLUDE_DIR = "D:\Program Files\LLVM\include"
$env:PATH += ";D:\Program Files\LLVM\bin"

# Verify installation
clang --version
```

## Project Structure

```
L1/
├── src/
│   ├── ast.rs          # Abstract Syntax Tree definitions
│   ├── codegen.rs      # LLVM code generation
│   ├── errors.rs       # Error handling
│   ├── lexer.rs        # Lexical analysis
│   ├── parser.rs       # Syntax analysis
│   └── lib.rs          # Library entry point
├── examples/
│   └── hello.l1        # Example LangOne programs
├── Docs/
│   └── Rust-LLVM-Development-Guide.md
├── Cargo.toml          # Dependencies and configuration
└── .cargo/
    └── config.toml     # LLVM configuration
```

## Dependencies

### Core Dependencies
- **inkwell**: Safe Rust wrapper for LLVM
- **anyhow/thiserror**: Error handling
- **clap**: CLI argument parsing
- **serde**: Serialization for AST and configuration

### Development Dependencies
- **criterion**: Benchmarking
- **proptest**: Property-based testing
- **mockall**: Mock testing

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
# Compile and run a LangOne program
cargo run -- examples/hello.l1

# Generate LLVM IR
cargo run -- --emit-ir examples/hello.l1

# Generate assembly
cargo run -- --emit-asm examples/hello.l1
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

## Code Generation Pipeline

### 1. Lexical Analysis
```rust
// Tokenize source code
let tokens = lex(source)?;
```

### 2. Parsing
```rust
// Parse tokens into AST
let mut parser = Parser::new(tokens);
let ast = parser.parse()?;
```

### 3. Code Generation
```rust
// Generate LLVM IR
let mut codegen = CodeGenerator::new()?;
codegen.codegen(&ast)?;

// Emit IR
let ir = codegen.emit_ir_to_string();
```

### 4. Compilation
```rust
// Generate object file
codegen.emit_object_file("output.o")?;

// Generate assembly
codegen.emit_assembly_file("output.s")?;
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
    }
}
```

### Generated LLVM IR
```llvm
; ModuleID = 'langone_module'
source_filename = "langone_module"

define void @main() {
entry:
  %0 = call i32 @printf(i8* getelementptr inbounds ([30 x i8], [30 x i8]* @.str, i32 0, i32 0))
  ret void
}

@.str = private unnamed_addr constant [30 x i8] c"Hello, World from LangOne! 🚀\00"
```

## Advanced Features

### Multi-target Compilation
```rust
// Target different architectures
let target_machine = target.create_target_machine(
    &target.create_target_data(),
    "x86_64-pc-windows-msvc",  // Windows x64
    "",                         // CPU features
    OptimizationLevel::Default,
    RelocMode::Default,
    CodeModel::Default,
)?;
```

### Optimization Passes
```rust
// Apply LLVM optimizations
codegen.optimize(OptimizationLevel::Aggressive)?;
```

### Custom LLVM Passes
```rust
// Add custom optimization passes
// TODO: Implement LangOne-specific optimizations
```

## Testing Strategy

### Unit Tests
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_lexer() {
        let tokens = lex("let x = 42;").unwrap();
        assert_eq!(tokens.len(), 5);
    }

    #[test]
    fn test_parser() {
        let ast = parse_source("let x = 42;").unwrap();
        assert!(!ast.is_empty());
    }

    #[test]
    fn test_codegen() {
        let mut codegen = CodeGenerator::new().unwrap();
        let result = codegen.codegen_literal(&LiteralExpression::Integer(42));
        assert!(result.is_ok());
    }
}
```

### Integration Tests
```rust
#[test]
fn test_full_compilation() {
    let source = r#"
        project "Test" {
            version = "1.0.0"
        }
    "#;
    
    let result = compile(source);
    assert!(result.is_ok());
}
```

## Performance Considerations

### Memory Management
- Use `Box<T>` for large AST nodes
- Implement `Drop` for LLVM resources
- Use `Rc<T>` for shared references

### Compilation Speed
- Parallel parsing with `rayon`
- Incremental compilation
- Caching for repeated operations

### Runtime Performance
- LLVM optimizations
- JIT compilation for REPL
- Native code generation

## Debugging

### LLVM IR Inspection
```rust
// Print LLVM IR to console
println!("{}", codegen.emit_ir_to_string());

// Save IR to file
codegen.emit_ir_to_file("debug.ll")?;
```

### LLVM Verification
```rust
// Verify LLVM module
let is_valid = codegen.verify()?;
assert!(is_valid, "Invalid LLVM module generated");
```

### Debug Symbols
```rust
// Enable debug information
let builder = context.create_builder();
builder.set_current_debug_location(debug_location);
```

## Future Enhancements

### Quantum Computing Support
- Qubit type system
- Quantum circuit generation
- Quantum optimization passes

### AI/ML Integration
- Tensor operations
- Model compilation
- GPU acceleration

### WebAssembly Target
- WASM code generation
- Browser-based REPL
- Cross-platform deployment

## Resources

- [Rust Book](https://doc.rust-lang.org/book/)
- [LLVM Documentation](https://llvm.org/docs/)
- [Inkwell Crate](https://docs.rs/inkwell/)
- [LangOne Repository](https://github.com/langone/langone)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

Apache-2.0 - See LICENSE file for details.
