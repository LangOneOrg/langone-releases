# LangOne

**AI‑native, cloud‑ready, quantum‑enabled programming language.**  
Build applications, infrastructure, AI/ML pipelines, and hybrid quantum workloads with one coherent language and toolchain.

> Status: **Pre‑alpha – Day 1**. This repo is the public starting point for the LangOne initiative.

---

## ✨ Vision

LangOne blends the best of .NET, Go, Rust, and Python into a **safe, fast, easy‑to‑learn** language with first‑class support for:

- **Cloud & DevOps**: Infrastructure‑as‑Code (IaC) and CI/CD as native language constructs.
- **AI/ML**: Built‑in model/tensor primitives and deploy‑to‑cloud helpers.
- **Apps**: APIs + UI + packaging targets (web, mobile, desktop) from one project.
- **Quantum**: A small, portable quantum DSL with simulators and cloud backends.
- **Security**: Capabilities, sandboxing, supply‑chain integrity, and observability by default.

Community and adoption are our top priorities. 💙

---

## 🧪 Hello, LangOne

Create a file `hello.l1` and paste the following (also in this repo under `/examples/hello.l1`):

```langone
// Hello World in LangOne
// This is a simple example to test the compiler

project "HelloWorld" {
    version = "1.0.0"
    description = "A simple Hello World program in LangOne"
}

// Simple function definition
function greet(name: string) -> string {
    return "Hello, " + name + "!"
}

// Main execution
let message = greet("LangOne")
print(message)
```

### Running the Example
```bash
# Compile and run the hello world example
cargo run -- examples/hello.l1

# Expected output:
# ✅ Output: Hello, LangOne! 🚀
```

---

## 🗺️ Current Status & Roadmap

### ✅ Completed (Foundation - Phase 1)
- **Tokenizer + Parser + AST**: Complete lexical analysis and syntax parsing
- **LLVM Integration**: Basic code generation with inkwell
- **Error Handling**: Comprehensive error reporting system
- **CLI Interface**: Command-line tool with multiple options
- **Project Structure**: Complete Rust workspace with all modules

### 🔄 In Progress (Runtime - Phase 2)
- **LangOne Virtual Machine (LVM)**: Bytecode interpreter implementation
- **Resource Management**: Memory pooling and GPU resource optimization
- **Security Module**: Source validation and sandboxed execution
- **Standard Library**: Basic language primitives and functions

### 📋 Planned (Advanced Features - Phase 3)
- **AI/ML Integration**: Built-in tensor operations and model wrappers
- **DevOps/IaaC**: Infrastructure as Code and CI/CD pipeline features
- **Quantum Computing**: Quantum circuit compilation and execution
- **Package Manager**: LangOne Package Manager (LPM)
- **LSP Server**: Language Server Protocol for IDE integration
- **Playground**: WASM-based REPL and code playground

### 🚀 Future Vision (Phase 4+)
- **Cross-Platform Deployment**: Web, mobile, desktop targets
- **Cloud Integration**: Native cloud resource provisioning
- **Formal Verification**: Mathematical proof of program correctness
- **Marketplace**: Community package and module ecosystem

---

## 🤝 Contributing

We’re thrilled to build LangOne in the open. Please read **[CONTRIBUTING.md](CONTRIBUTING.md)** to get started:
- Good first issues & labels
- Branching and PR process
- Code style & commit conventions
- Security & reporting issues

> By contributing, you agree that your contributions will be licensed under the project’s license.

---

## 💬 Community

- Discussions: _coming soon_
- Discord/Slack: _coming soon_
- Website: **https://LangOne.io** (placeholder)

---

## 🛡️ Trademark & License

- **Trademark**: “LangOne” is a pending trademark; do not misuse the brand or logos.
- **License**: Planned **Apache‑2.0** for core; enterprise add‑ons may be under a commercial license.

© LangOne Contributors
