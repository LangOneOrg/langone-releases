# LangOne v0.1.0-alpha.1 - Windows x64

## Download

- **langone.exe** - Full LangOne compiler/interpreter (2.3MB)
- **lo.exe** - Short alias for langone.exe (2.3MB)

## Installation

1. Download the executables
2. Add to your PATH or place in a directory you can access from command line
3. Run `langone --help` or `lo --help` to verify installation

## Verification

Verify the integrity of your download using SHA256 checksums:

```bash
# For langone.exe
certutil -hashfile langone.exe SHA256
# Should match: 988ae96b42585511f6b1668298b0d2d78c54d4631716f3b71ca9dc239c610c1b

# For lo.exe  
certutil -hashfile lo.exe SHA256
# Should match: c0020114ecb9c9cce97287c36ed24d2fb516b9073b17630467355c75292b31cc
```

## Quick Start

```bash
# Run a LangOne file
langone run hello.l1
lo run hello.l1

# Start REPL
langone repl
lo repl

# Show help
langone --help
lo --help
```

## Features

- ✅ Mixed numeric type operations (Integer + Float)
- ✅ REPL with syntax highlighting
- ✅ File execution
- ✅ Error handling with detailed messages
- ✅ Standard library functions
- ✅ Pattern matching
- ✅ Control flow (if/else, loops)

## What's New in v0.1.0-alpha.1

- Fixed mixed numeric type operations (Float/Integer arithmetic)
- Added short executable alias `lo.exe`
- Improved error messages and REPL experience
- Enhanced type coercion for better user experience

## System Requirements

- Windows 10/11 (x64)
- No additional dependencies required
