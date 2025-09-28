# Prompt-Updated.md

Updated Cursor AI Prompt for LangOne Project Setup

I am building a new programming language called LangOne. Please help me set up a new Rust project (Cargo package) named langone that will serve as the compiler/interpreter for this language. In addition to the basic compiler structure, LangOne must be optimized for RAM, GPU, and other hardware resources from the very beginning. This means the project should include modules and placeholders dedicated to memory management, GPU resource management, and compile‑time resource analysis, enabling the language to run efficiently on a wide range of devices—from small IoT boards to multi‑GPU servers.

Requirements and Structure

Use Rust for Implementation
Set up a Rust project that uses the inkwell crate for LLVM code generation, along with any other crates needed (e.g., anyhow for error handling or clap for CLI parsing). Ensure Cargo.toml includes inkwell with the appropriate LLVM feature enabled (e.g., llvm16-0 or a suitable version).

Core Compiler Components
Create the following modules/files, each with basic struct or function definitions and // TODO comments for future development:

main.rs – Entry point that parses command‑line arguments (using std::env or clap) and calls the compiler pipeline (lexer → parser → codegen). For now, just demonstrate the flow and print a message or dummy output.

lexer.rs – Define a Token enum and a stub function lex() that returns a list of tokens. Include TODOs for lexical analysis logic.

parser.rs – Define a Parser struct or function and a stub parse() that produces an AST. Include TODOs for parsing logic.

ast.rs – Define simple AST node structs or enums (e.g., for expressions, statements) with derived traits (Debug, Clone). These are placeholders for the abstract syntax tree data structures.

codegen.rs – Initialize an LLVM context and module using inkwell. Provide a placeholder codegen() function that will traverse the AST and generate IR. Include a TODO note for implementing actual code generation.

errors.rs (optional) – Define error types and diagnostic utilities. You may include a basic error struct and an error reporting function with TODOs for richer diagnostics.

Memory and Resource Optimization Module
To ensure that LangOne optimizes RAM, GPU, and other hardware resources from the start, add a new module resource.rs with the following elements:

Memory Pooling and Allocators: Define a MemoryPool struct and associated functions for pooling and reusing memory buffers. Include a TODO to implement arenas or bump allocators that reduce heap fragmentation and manage memory efficiently.

GPU Memory Management: Define a GPUMemoryManager struct with stub methods to allocate, reuse, and release GPU memory buffers. Include TODOs for mixed‑precision control (e.g., FP16 vs. FP32) and for implementing automatic device placement of tensors.

Resource Budgets and Monitoring: Create a ResourceBudget struct or type that represents memory and GPU budgets for a program. Add stub functions to set and enforce these budgets, and placeholders for runtime monitoring that will record real‑time memory and GPU usage statistics.

Compile‑Time Resource Analysis: Include a placeholder function analyze_resources() that the compiler will call to estimate stack and heap usage, and identify potentially expensive allocations. Document that this function will warn developers about high memory or GPU usage at compile time.

Integration Points: In comments, explain how this resource module will integrate with the compiler pipeline—for example, by sharing the budget data with the codegen stage and by exposing an API for the runtime to monitor resource usage.

Wiring Everything Together

Reference all modules using mod statements in main.rs or lib.rs so they compile as one project.

In Cargo.toml, besides inkwell, add any crates that may help with future resource optimization (like profiling for runtime metrics or clap for CLI parsing).

Use // TODO comments liberally to mark where functionality will be filled in later.

Compile‑Ready Scaffold
Ensure that the generated project compiles successfully with cargo build, even though many functions only contain stubs. This gives us a solid scaffold to iterate on as we implement the full compiler, resource management, and other language features.

Please create the project structure and files as described, populating them with the requested placeholders and comments. Once complete, provide the output and ensure that it builds without errors.



# Ultimate Cursor AI Prompt for LangOne Project Setup (with README-Updated.md)

I am building a new programming language called **LangOne**. Please scaffold a complete Rust project (Cargo package) named `langone`. LangOne must be **AI-native, cloud-ready, resource-optimized, and modular from day one.**

---

## Project Setup

- Rust implementation.
- Cargo dependencies:
  - `inkwell` (LLVM codegen).
  - `anyhow` / `thiserror` (errors).
  - `clap` (CLI).
  - `serde` (serialization).
  - `tokio` (async).
  - `opentelemetry` + `tracing` (observability).
- Dev dependencies:
  - `insta` (snapshot testing).
  - `assert_matches`, `assert_cmd` (testing).
- MIT or Apache-2.0 LICENSE.
- Git initialized.

---

## Examples

### Hello World
```bash
cargo run -- examples/HelloWorld.l1
```

Expected Output:
```
✅ Output: Hello, World from LangOne! 🚀
```

### examples/math.l1
```l1
project "MathDemo" { version="0.1.0" }
task main() { print(2 + 3 * 4) }
```

---

## Snapshot Test
**tests/hello_snapshot.rs**
```rust
use assert_cmd::Command;
use insta::assert_snapshot;

#[test]
fn hello_world_output_matches_snapshot() {
    let mut cmd = Command::cargo_bin("langone").unwrap();
    cmd.arg("examples/HelloWorld.l1");
    let output = cmd.assert().success().to_string();
    assert_snapshot!("hello_world_output", output);
}
```

---

## Golden Tests
**tests/golden_tests.rs**
```rust
use assert_cmd::Command;
use std::fs;

#[test]
fn golden_file_examples() {
    let examples = ["examples/HelloWorld.l1", "examples/math.l1"];
    for file in examples {
        let expected_path = format!("{}.out", file);
        let expected = fs::read_to_string(&expected_path).unwrap_or_default();
        let mut cmd = Command::cargo_bin("langone").unwrap();
        cmd.arg(file);
        let output = cmd.assert().success().to_string();
        assert_eq!(output.trim(), expected.trim(), "Mismatch for {}", file);
    }
}
```

---

## LSP Scaffolding
**langone-lsp/src/main.rs**
```rust
fn main() {
    println!("LangOne LSP server stub — integrate with VSCode/Neovim later.");
}
```

---

## Playground (WASM REPL)
**langone-playground/src/lib.rs**
```rust
#[wasm_bindgen]
pub fn run_code(code: &str) -> String {
    format!("Executed LangOne code: {}", code)
}
```

---

## Package Manager Stub
**langonepm/src/main.rs**
```rust
fn main() {
    println!("LangOnePM — future package manager stub.");
}
```

---

## Security Module
**src/security.rs**
```rust
pub fn validate_source(input: &str) -> bool {
    !input.contains("unsafe") // placeholder
}
pub fn sandbox_execute(code: &str) {
    println!("Sandboxed execution: {}", code);
}
```

---

## Quantum Module Stub
**src/quantum.rs**
```rust
pub fn run_quantum_demo() {
    println!("Quantum stub: running H gate on qubit 0...");
}
```

---

## Blockchain Module Stub
**src/blockchain.rs**
```rust
pub fn record_transaction(data: &str) {
    println!("Blockchain stub: recording transaction {}", data);
}
```

---

## CI/CD Pipeline
**.github/workflows/ci.yml**
```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions-rs/toolchain@v1
        with: { toolchain: stable, override: true }
      - run: cargo build --verbose
      - run: cargo test --verbose
```

---

## Dockerfile
```dockerfile
FROM rust:1.79-slim
WORKDIR /app
COPY . .
RUN cargo build --release
CMD ["./target/release/langone", "examples/HelloWorld.l1"]
```

---

## Deliverable

A **full Cargo workspace** with:

- Compiler modules.
- Resource optimization + security + observability.
- Examples (`HelloWorld.l1`, `math.l1`).
- Snapshot & golden-file tests.
- Package manager subcrate.
- LSP server subcrate.
- Playground (WASM REPL).
- Quantum & blockchain stubs.
- Dockerfile + CI/CD pipeline.

Should **compile, run HelloWorld, pass tests, build Docker image, and validate snapshots**.
