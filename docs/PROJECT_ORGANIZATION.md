# LangOne Project Organization

This document explains the new project structure implemented for better maintainability and clarity.

## 📁 Project Structure Overview

```
langone/
├── docs/                    # 📚 All Documentation
├── code/                    # 💻 All Source Code & Development Files
└── .github/                 # 🔧 GitHub Workflows & Templates
```

## 📚 Documentation (`docs/`)

All documentation files are centralized in the `docs/` directory:

- **`README.md`** - Main project documentation
- **`QUICKSTART.md`** - Quick start guide for new users
- **`ALPHA_LAUNCH_CHECKLIST.md`** - Alpha launch preparation checklist
- **`ALPHA_PHASE_SUMMARY.md`** - Alpha phase summary and status
- **`ALPHA_READY.md`** - Alpha readiness assessment
- **`COMPLETED_FEATURES.md`** - List of completed features
- **`IMPLEMENTATION_PLAN.md`** - Detailed implementation roadmap
- **`IMPLEMENTATION_SUMMARY.md`** - Implementation progress summary
- **`NEXT_ACTIONS.md`** - Next steps and action items
- **`PROJECT_ORGANIZATION.md`** - This file
- **`chat.md`** - Development conversation history

## 💻 Source Code (`code/`)

All code and development files are organized in the `code/` directory:

### Core Source Code
- **`src/`** - Rust source code (lexer, parser, interpreter, etc.)
- **`Cargo.toml`** - Rust project configuration
- **`Cargo.lock`** - Dependency lock file

### Testing Structure (`tests/`)
The `tests/` directory contains **ALL** test files, organized by type:

```
tests/
├── unit_tests/           # Rust unit tests (.rs files)
│   ├── await_strict.rs
│   ├── match_bindings.rs
│   ├── match_optimization.rs
│   └── match_trailing_comma.rs
├── integration_tests/    # Comprehensive integration tests (.l1 files)
│   ├── test_advanced_features_comprehensive.l1
│   ├── test_arrays_comprehensive.l1
│   ├── test_data_structures_comprehensive.l1
│   ├── test_error_handling_comprehensive.l1
│   ├── test_language_enhancements_comprehensive.l1
│   ├── test_performance_comprehensive.l1
│   ├── test_type_checking_comprehensive.l1
│   ├── sanity_await_strict.l1
│   ├── sanity_comprehensive.l1
│   ├── sanity_match_bindings.l1
│   ├── sanity_optimizer.l1
│   └── sanity_trailing_comma.l1
├── intp_tests/           # Interpreter-specific tests
├── README.md             # Test organization guide
└── *.l1                  # Individual feature tests
    ├── test_async_await.l1
    ├── test_control_flow_simple.l1
    ├── test_functions_comprehensive.l1
    ├── test_pattern_matching.l1
    ├── test_stdlib.l1
    └── ... (80+ individual test files)
```

### Sample Programs (`samples/`)
**Clean, well-documented example programs** for users (NOT test files):

- **`hello_world.l1`** - Basic "Hello World" program
- **`arithmetic.l1`** - Arithmetic operations demo
- **`control_flow.l1`** - Control flow constructs demo
- **`patterns.l1`** - Pattern matching demo
- **`stdlib_demo.l1`** - Standard library functions demo
- **`README.md`** - Sample programs guide

### Development Examples (`examples/`)
Development examples and experimental code (kept as-is).

### Extensions & Tools
- **`vscode-extension/`** - VS Code extension with syntax highlighting
- **`installers/`** - Package manager configuration files
- **`benchmarks/`** - Performance benchmarks

## 🔍 Key Distinctions

### Tests vs Samples vs Examples

| Directory | Purpose | Content | Audience |
|-----------|---------|---------|----------|
| **`tests/`** | Testing & Validation | Test files (.rs, .l1) | Developers |
| **`samples/`** | User Examples | Clean demo programs | End Users |
| **`examples/`** | Development Examples | Experimental code | Developers |

### Test Organization

- **`unit_tests/`** - Rust unit tests (`.rs` files)
- **`integration_tests/`** - Comprehensive integration tests (`.l1` files)
- **`intp_tests/`** - Interpreter-specific tests
- **Root level** - Individual feature tests (`.l1` files)

## 🚀 Benefits of New Organization

### ✅ Clear Separation
- **Documentation** and **code** are cleanly separated
- **Tests** and **examples** are clearly distinguished
- **User samples** vs **development examples** are separate

### ✅ Better Navigation
- Easy to find documentation in `docs/`
- All code-related files in `code/`
- Organized test structure with clear categories

### ✅ Maintainability
- Logical file grouping
- Clear naming conventions
- Comprehensive README files for each section

### ✅ Alpha Testing Ready
- Clean samples for alpha testers
- Organized test structure for validation
- Clear documentation for setup

## 📋 Migration Summary

### Files Moved to `docs/`
- All `.md` documentation files
- Development conversation history (`chat.md`)

### Files Moved to `code/`
- All source code files (`src/`)
- All test files (consolidated in `tests/`)
- All sample programs (`samples/`)
- All development examples (`examples/`)
- All tooling (`vscode-extension/`, `installers/`)
- Build configuration (`Cargo.toml`, `Cargo.lock`)

### Test Consolidation
- **Rust tests** → `tests/unit_tests/`
- **Comprehensive tests** → `tests/integration_tests/`
- **Individual tests** → `tests/` (root level)
- **Interpreter tests** → `tests/intp_tests/` (kept as-is)

## 🎯 Next Steps

1. **Update all documentation** to reflect new paths
2. **Update CI/CD workflows** to use new structure
3. **Update installation scripts** to reference new paths
4. **Test the new organization** with alpha testers

---

**This organization provides a clean, maintainable structure ready for the LangOne Alpha Launch! 🚀**
