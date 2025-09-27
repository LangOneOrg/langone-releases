# LangOne v0.1.0-alpha.1 Release Notes

## 🎉 Alpha Release

This is the first alpha release of LangOne, an AI-native, universal programming language designed for modern development workflows.

## ✨ Key Features

### Core Language Features
- **Mixed Numeric Types**: Seamless operations between integers and floats
- **Dynamic Typing**: Flexible type system with automatic type inference
- **Pattern Matching**: Powerful pattern matching for data structures
- **Control Flow**: Complete if/else, loops, and conditional statements

### Developer Experience
- **REPL**: Interactive Read-Eval-Print Loop with syntax highlighting
- **Error Handling**: Detailed error messages with line numbers and suggestions
- **Standard Library**: Built-in functions for common operations
- **Dual Executables**: `langone.exe` and `lo.exe` (short alias)

### Performance
- **Fast Interpreter**: Optimized for rapid development cycles
- **Memory Efficient**: Smart memory management with garbage collection
- **Cross-Platform**: Native Windows, Linux, and macOS support

## 🐛 Bug Fixes

- **Fixed Mixed Type Operations**: Resolved runtime error when mixing integers and floats in arithmetic operations
- **Improved Error Messages**: Better error reporting with specific type information
- **REPL Stability**: Fixed formatting issues in interactive mode

## 🔧 Technical Improvements

- **Type Coercion**: Automatic type conversion for mixed numeric operations
- **Code Formatting**: Applied `cargo fmt` for consistent code style
- **Linting**: Fixed all Clippy warnings and linting issues
- **Build System**: Optimized release builds for better performance

## 📦 Installation

### Windows x64
1. Download `langone.exe` or `lo.exe` from the release assets
2. Verify integrity using provided SHA256 checksums
3. Add to your PATH or run directly from download directory

### Verification
```bash
certutil -hashfile langone.exe SHA256
# Expected: 988ae96b42585511f6b1668298b0d2d78c54d4631716f3b71ca9dc239c610c1b
```

## 🚀 Quick Start

```l1
// Hello World
print("Hello, LangOne!");

// Mixed numeric types now work seamlessly
let price = 19.99;
let quantity = 3;
let total = price * quantity;  // 59.97
print("Total: " + total);

// REPL
langone repl
lo repl
```

## 🔄 What's Next

This alpha release focuses on core language functionality and developer experience. Future releases will include:

- **Beta v0.2.0**: Enhanced standard library, better error recovery
- **RC v0.3.0**: Performance optimizations, advanced features
- **Stable v1.0.0**: Production-ready with full documentation

## 📝 Known Limitations

- Limited standard library functions (expanding in beta)
- No package manager yet (planned for v0.2.0)
- Basic error recovery (improving in future releases)

## 🤝 Contributing

This is an alpha release. We welcome feedback and contributions:

- Report issues on GitHub
- Suggest features and improvements
- Contribute to the codebase

## 📄 License

LangOne is released under the MIT License. See LICENSE file for details.

---

**LangOne Team**  
*Building the future of AI-native programming*
