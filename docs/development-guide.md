# LangOne Compiler - Development Guide

**Quick Start Guide for LangOne Development**

---

## Prerequisites Installation

### 1. Install Rust
```bash
# Download and run rustup installer
# Visit: https://rustup.rs/
# Or run in PowerShell:
Invoke-WebRequest -Uri "https://win.rustup.rs/x86_64" -OutFile "rustup-init.exe"
.\rustup-init.exe

# Restart your terminal after installation
```

### 2. Install LLVM
```bash
# Option 1: Using Chocolatey (recommended)
# Install Chocolatey first: https://chocolatey.org/install
choco install llvm

# Option 2: Using Scoop
# Install Scoop first: https://scoop.sh/
scoop install llvm

# Option 3: Manual installation
# Download from: https://releases.llvm.org/download.html
# Install LLVM 16.0 or compatible version
```

### 3. Verify Installation
```bash
# Check Rust (should be 1.70+)
rustc --version
cargo --version

# Check LLVM (should be 16.0+)
llvm-config --version

# If LLVM not found, set environment variable
set LLVM_SYS_160_PREFIX=C:\Program Files\LLVM

# Verify project builds
cargo check
```

---

## Building and Running

### Quick Setup
```bash
# Run the setup script
setup.bat

# Or manually check compilation
cargo check
```

### Build Commands
```bash
# Check compilation (fastest)
cargo check

# Build debug version
cargo build

# Build release version
cargo build --release

# Run tests
cargo test

# Clean build artifacts
cargo clean
```

### Running the Compiler
```bash
# Compile a LangOne file
cargo run -- examples/hello.l1

# Compile with specific options
cargo run -- --target wasm examples/hello.l1
cargo run -- --dump-ast examples/hello.l1
cargo run -- --dump-ir examples/hello.l1

# Start interactive REPL
cargo run -- --repl

# See all options
cargo run -- --help
```

---

## Development Workflow

### Daily Development
```bash
# 1. Start development session
git pull origin main
cargo check

# 2. Make changes to code
# Edit files in src/

# 3. Test changes
cargo test
cargo run -- examples/hello.l1

# 4. Format and lint
cargo fmt
cargo clippy

# 5. Commit changes
git add .
git commit -m "feat: implement feature X"
```

### Testing Specific Components
```bash
# Test lexer only
cargo test --lib lexer

# Test parser only
cargo test --lib parser

# Test codegen only
cargo test --lib codegen

# Test with verbose output
RUST_LOG=debug cargo test
```

### Debugging
```bash
# Debug compilation issues
RUST_LOG=debug cargo run -- examples/hello.l1

# Debug specific module
RUST_LOG=debug cargo test --lib lexer

# Check LLVM IR output
cargo run -- --dump-ir examples/hello.l1

# Validate generated IR
cargo run -- --verify examples/hello.l1
```

---

## Project Structure

```
langone/
├── Cargo.toml              # Project configuration
├── setup.bat               # Windows setup script
├── src/                    # Source code
│   ├── lib.rs             # Library entry point
│   ├── main.rs            # CLI application
│   ├── lexer.rs           # Lexical analysis
│   ├── parser.rs          # Syntax parsing
│   ├── ast.rs             # Abstract Syntax Tree
│   ├── codegen.rs         # LLVM code generation
│   └── errors.rs          # Error handling
├── examples/               # Example programs
│   └── hello.l1           # Hello World example
├── Docs/                   # Documentation
│   ├── next-steps.md      # Development roadmap
│   ├── implementation-log.md # Implementation history
│   └── development-guide.md  # This file
└── README.md              # Project overview
```

---

## Common Issues and Solutions

### Issue: "rustc not found"
**Solution:**
```bash
# Install Rust from https://rustup.rs/
# Restart terminal after installation
# Verify: rustc --version
```

### Issue: "LLVM not found"
**Solution:**
```bash
# Install LLVM
choco install llvm

# Or set environment variable
set LLVM_SYS_160_PREFIX=C:\Program Files\LLVM

# Or use bundled LLVM (if available)
cargo build --features llvm16-0
```

### Issue: "Compilation failed"
**Solution:**
```bash
# Clean and rebuild
cargo clean
cargo build

# Update dependencies
cargo update

# Check for errors
cargo check
```

### Issue: "Tests failing"
**Solution:**
```bash
# Run specific test
cargo test test_name

# Run with verbose output
RUST_LOG=debug cargo test

# Check test output
cargo test -- --nocapture
```

---

## Development Phases

### Phase 1: Foundation ✅ COMPLETED (Sep 15-22, 2025)
- [x] Basic compiler structure
- [x] Lexer implementation with comprehensive token support
- [x] Parser implementation with recursive descent
- [x] AST definitions with all node types
- [x] LLVM code generation with inkwell integration
- [x] Comprehensive error handling and reporting
- [x] CLI interface with multiple options
- [x] Project structure with all modules
- [x] Tree-walk interpreter implementation
- [x] Pattern matching with identifier bindings and guards
- [x] Async/await with strict validation
- [x] Macro system for compile-time code generation
- [x] Optimizer with constant folding
- [x] Error recovery in parser

### Phase 2: Runtime 🔄 IN PROGRESS (Sep 23 - Oct 15, 2025)
- [ ] REPL implementation
- [ ] Basic standard library functions
- [ ] Memory management and resource optimization
- [ ] Security module implementation
- [ ] LangOne Virtual Machine (LVM) architecture
- [ ] Bytecode interpreter implementation
- [ ] Resource management (GPU, memory pools)

### Phase 3: Language Features 📋 PLANNED (Oct 15 - Dec 15, 2025)
- [ ] Complete type system with inference
- [ ] Advanced function system
- [ ] Module system and imports
- [ ] Concurrency and async/await model - PARTIALLY COMPLETE
- [ ] Control flow constructs - PARTIALLY COMPLETE (match expressions done)

### Phase 4: Advanced Features 🚀 (Future)
- [ ] AI/ML integration with tensor operations
- [ ] DevOps and Infrastructure as Code features
- [ ] Cross-platform compilation targets
- [ ] Quantum computing support
- [ ] Blockchain integration
- [ ] Package manager (LPM)
- [ ] LSP server for IDE integration

---

## Useful Commands

### Development Commands
```bash
# Watch for changes
cargo watch -x check

# Run with specific log level
RUST_LOG=info cargo run -- examples/hello.l1

# Build for specific target
cargo build --target x86_64-pc-windows-msvc

# Check dependencies
cargo outdated

# Security audit
cargo audit
```

### Testing Commands
```bash
# Run all tests
cargo test

# Run specific test
cargo test test_name

# Run tests with output
cargo test -- --nocapture

# Run tests in specific module
cargo test --lib module_name
```

### Debugging Commands
```bash
# Debug with gdb
cargo build
gdb target/debug/langone

# Debug with lldb
cargo build
lldb target/debug/langone

# Profile with perf (Linux)
perf record cargo run -- examples/hello.l1
perf report
```

---

## Next Immediate Steps

### Today (Day 1)
1. **Install Rust and LLVM**
   ```bash
   # Install Rust
   # Visit https://rustup.rs/ and follow instructions
   
   # Install LLVM
   choco install llvm
   ```

2. **Test Compilation**
   ```bash
   cargo check
   cargo build
   cargo test
   ```

3. **Run Example**
   ```bash
   cargo run -- examples/hello.l1
   ```

### This Week (Days 2-7)
1. **Fix Any Issues**
   - Resolve compilation problems
   - Fix LLVM linking issues
   - Ensure all tests pass

2. **Start Runtime Development**
   - Design LVM architecture
   - Implement basic interpreter
   - Add simple instruction set

3. **Create More Examples**
   - Calculator program
   - Data structure examples
   - Function examples

### Next Week (Days 8-14)
1. **Complete Basic Runtime**
   - Finish LVM implementation
   - Add memory management
   - Implement basic standard library

2. **Enhance Language Features**
   - Complete type system
   - Add more control flow
   - Implement functions

---

## Getting Help

### Documentation
- **Rust Book**: https://doc.rust-lang.org/book/
- **LLVM Documentation**: https://llvm.org/docs/
- **Inkwell Crate**: https://docs.rs/inkwell/

### Community
- **Rust Discord**: https://discord.gg/rust-lang
- **LLVM Discord**: https://discord.gg/xS7Z362
- **GitHub Issues**: Create issues for bugs and features

### Debugging Resources
- **Rust Debugging**: https://doc.rust-lang.org/book/appendix-04-useful-development-tools.html
- **LLVM Debugging**: https://llvm.org/docs/ProgrammersManual.html#debugging
- **Cargo Debugging**: https://doc.rust-lang.org/cargo/commands/cargo-test.html

---

**Ready to start development!** 🚀

Follow the steps above to get your development environment set up and start building the future of programming with LangOne.
