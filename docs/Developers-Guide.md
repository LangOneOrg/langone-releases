# LangOne Developer Guide: Complete Workflow from Program to Execution

## Table of Contents
1. [Overview](#overview)
2. [Architecture Overview](#architecture-overview)
3. [Module-by-Module Breakdown](#module-by-module-breakdown)
4. [Complete Execution Workflow](#complete-execution-workflow)
5. [Code Examples and Flow](#code-examples-and-flow)
6. [Development Guidelines](#development-guidelines)
7. [Troubleshooting Guide](#troubleshooting-guide)

## Overview

This guide provides a comprehensive understanding of how LangOne programs are processed from source code to execution. It's designed for junior developers to understand the complete workflow and each component's role.

## Architecture Overview

```
LangOne Program → Lexer → Parser → AST → Interpreter → Execution
     ↓              ↓        ↓       ↓         ↓
  Source Code   Tokens   Syntax   Tree    Runtime
```

### Key Components:
- **Lexer**: Converts source code into tokens
- **Parser**: Converts tokens into Abstract Syntax Tree (AST)
- **AST**: Tree representation of program structure
- **Interpreter**: Executes the AST directly
- **Environment**: Manages variables and scope

## Module-by-Module Breakdown

### 1. **`src/main.rs` - Entry Point & CLI Interface**

**Purpose**: Command-line interface and program entry point

**Key Components**:
```rust
// Command-line argument parsing
#[derive(Parser)]
#[command(name = "langone")]
#[command(about = "LangOne compiler and interpreter")]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

// Available commands
enum Commands {
    Run { file: PathBuf },      // Execute LangOne program
    Parse { file: PathBuf },    // Parse and show AST
    Tokenize { file: PathBuf }, // Tokenize and show tokens
    Repl,                       // Interactive REPL
}
```

**Responsibilities**:
- Parse command-line arguments
- Read source files
- Route commands to appropriate modules
- Handle file I/O and error reporting

**Workflow**:
1. Parse CLI arguments
2. Read source file (if not REPL)
3. Call appropriate module (lexer, parser, interpreter)
4. Display results or errors

---

### 2. **`src/lexer.rs` - Lexical Analysis**

**Purpose**: Convert source code into a stream of tokens

**Key Components**:
```rust
// Token types
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub enum Token {
    // Literals
    Number(f64),
    String(String),
    Boolean(bool),
    
    // Identifiers
    Identifier(String),
    
    // Keywords
    Let, Const, If, While, For, Return, Function,
    
    // Operators
    Plus, Minus, Multiply, Divide, Modulo,
    Equal, NotEqual, Less, Greater, LessEqual, GreaterEqual,
    And, Or, Not,
    
    // Punctuation
    LeftParen, RightParen, LeftBrace, RightBrace,
    Semicolon, Comma, Dot, Arrow,
    
    // Special
    Newline, Eof, Comment(String), DocComment(String),
}

// Token with position information
#[derive(Debug, Clone)]
pub struct TokenInfo {
    pub token: Token,
    pub line: usize,
    pub column: usize,
}
```

**Responsibilities**:
- Scan source code character by character
- Identify tokens (keywords, identifiers, literals, operators)
- Handle string literals with escape sequences
- Track line and column numbers for error reporting
- Handle comments and whitespace

**Workflow**:
1. Initialize scanner with source code
2. Scan character by character
3. Identify token type based on current character
4. Create `TokenInfo` with token and position
5. Return vector of tokens

**Example**:
```rust
// Input: "let x = 42;"
// Output: [
//   TokenInfo { token: Let, line: 1, column: 1 },
//   TokenInfo { token: Identifier("x"), line: 1, column: 5 },
//   TokenInfo { token: Equal, line: 1, column: 7 },
//   TokenInfo { token: Number(42.0), line: 1, column: 9 },
//   TokenInfo { token: Semicolon, line: 1, column: 11 },
// ]
```

---

### 3. **`src/parser.rs` - Syntax Analysis**

**Purpose**: Convert tokens into Abstract Syntax Tree (AST)

**Key Components**:
```rust
// Parser state
pub struct Parser {
    tokens: Vec<TokenInfo>,
    current: usize,
}

// Main parsing function
pub fn parse(tokens: Vec<TokenInfo>) -> Result<Vec<AstNode>> {
    let mut parser = Parser::new(tokens);
    parser.parse_program()
}
```

**Responsibilities**:
- Parse tokens according to LangOne grammar
- Build AST nodes for each language construct
- Handle operator precedence and associativity
- Report syntax errors with position information
- Manage parsing state and token consumption

**Parsing Methods**:
- `parse_program()`: Entry point, parses entire program
- `parse_statement()`: Parses individual statements
- `parse_expression()`: Parses expressions with precedence
- `parse_primary()`: Parses literals, identifiers, function calls
- `parse_unary()`: Parses unary operators
- `parse_binary()`: Parses binary operators with precedence

**Workflow**:
1. Initialize parser with tokens
2. Parse program as sequence of statements
3. For each statement, determine type and parse accordingly
4. Build AST nodes for each construct
5. Return complete AST

**Example**:
```rust
// Input tokens: [Let, Identifier("x"), Equal, Number(42.0), Semicolon]
// Output AST: AstNode::LetStatement(LetStatement {
//   name: "x",
//   value: Some(Expression::Literal(LiteralExpression::Number(42.0))),
//   type_annotation: None,
// })
```

---

### 4. **`src/ast.rs` - Abstract Syntax Tree**

**Purpose**: Define the structure of parsed programs

**Key Components**:
```rust
// Main AST node type
#[derive(Debug, Clone, PartialEq)]
pub enum AstNode {
    // Statements
    LetStatement(LetStatement),
    ConstStatement(ConstStatement),
    ExpressionStatement(ExpressionStatement),
    BlockStatement(BlockStatement),
    IfStatement(IfStatement),
    WhileStatement(WhileStatement),
    ForStatement(ForStatement),
    ReturnStatement(ReturnStatement),
    FunctionDeclaration(FunctionDeclaration),
    
    // Expressions
    Literal(LiteralExpression),
    Identifier(IdentifierExpression),
    Unary(UnaryExpression),
    Binary(BinaryExpression),
    Assignment(AssignmentExpression),
    Call(CallExpression),
    Grouping(GroupingExpression),
}

// Statement types
#[derive(Debug, Clone, PartialEq)]
pub struct LetStatement {
    pub name: String,
    pub value: Option<Expression>,
    pub type_annotation: Option<TypeAnnotation>,
}

// Expression types
#[derive(Debug, Clone, PartialEq)]
pub enum Expression {
    Literal(LiteralExpression),
    Identifier(IdentifierExpression),
    Unary(UnaryExpression),
    Binary(BinaryExpression),
    Assignment(AssignmentExpression),
    Call(CallExpression),
    Grouping(GroupingExpression),
}
```

**Responsibilities**:
- Define the structure of all language constructs
- Provide type-safe representation of parsed code
- Enable tree traversal for interpretation
- Support serialization for debugging

**Workflow**:
1. Parser creates AST nodes based on grammar rules
2. Each node represents a specific language construct
3. Nodes contain all necessary information for execution
4. Tree structure reflects program hierarchy

---

### 5. **`src/interpreter.rs` - Tree-Walk Interpreter**

**Purpose**: Execute AST directly without compilation

**Key Components**:
```rust
// Runtime values
#[derive(Debug, Clone, PartialEq)]
pub enum Value {
    Number(f64),
    String(String),
    Boolean(bool),
    Function(FunctionValue),
    Nil,
}

// Function representation
#[derive(Debug, Clone, PartialEq)]
pub struct FunctionValue {
    pub name: String,
    pub parameters: Vec<String>,
    pub body: Box<AstNode>,
    pub closure: Option<Rc<RefCell<Environment>>>,
}

// Environment for variable management
#[derive(Debug, Clone)]
pub struct Environment {
    pub values: HashMap<String, Value>,
    pub enclosing: Option<Rc<RefCell<Environment>>>,
}

// Main interpreter
pub struct Interpreter {
    pub environment: Rc<RefCell<Environment>>,
}
```

**Responsibilities**:
- Execute AST nodes directly
- Manage variable environment and scope
- Handle function calls and built-in functions
- Evaluate expressions and return values
- Provide runtime error handling

**Key Methods**:
- `interpret()`: Main entry point for interpretation
- `execute()`: Execute statements
- `evaluate()`: Evaluate expressions
- `call_function()`: Handle function calls
- `execute_block_statement()`: Handle block scoping

**Workflow**:
1. Initialize interpreter with global environment
2. For each AST node, execute according to type
3. Manage variable scope and environment
4. Evaluate expressions and return values
5. Handle function calls and built-in functions

---

### 6. **`src/lib.rs` - Library Interface**

**Purpose**: Public API and module coordination

**Key Components**:
```rust
// Public modules
pub mod lexer;
pub mod parser;
pub mod ast;
pub mod interpreter;
pub mod codegen_simple;

// Public API
pub use interpreter::{Interpreter, Value};

// Main functions
pub fn run(source: &str) -> Result<Value> {
    let tokens = lexer::tokenize(source)?;
    let ast = parser::parse(tokens)?;
    let mut interpreter = Interpreter::new();
    interpreter.interpret(ast)
}

pub fn compile(source: &str) -> Result<String> {
    let tokens = lexer::tokenize(source)?;
    let ast = parser::parse(tokens)?;
    let mut codegen = SimpleCodeGenerator::new();
    codegen.generate(ast)
}
```

**Responsibilities**:
- Expose public API for external use
- Coordinate between modules
- Provide high-level functions for common operations
- Handle error propagation

---

## Complete Execution Workflow

### Step 1: Program Input
```rust
// User runs: cd code && cargo run -- run examples/hello.l1es/hello.l1
// Source code: print("Hello World!");
```

### Step 2: CLI Processing (`main.rs`)
```rust
// 1. Parse command-line arguments
let cli = Cli::parse();
// 2. Read source file
let source = std::fs::read_to_string(file)?;
// 3. Route to appropriate command
match cli.command {
    Commands::Run { file } => run_file(&file)?,
    // ...
}
```

### Step 3: Lexical Analysis (`lexer.rs`)
```rust
// Input: "print(\"Hello World!\");"
// Output: [
//   TokenInfo { token: Identifier("print"), line: 1, column: 1 },
//   TokenInfo { token: LeftParen, line: 1, column: 6 },
//   TokenInfo { token: String("Hello World!"), line: 1, column: 7 },
//   TokenInfo { token: RightParen, line: 1, column: 20 },
//   TokenInfo { token: Semicolon, line: 1, column: 21 },
//   TokenInfo { token: Eof, line: 1, column: 22 },
// ]
```

### Step 4: Syntax Analysis (`parser.rs`)
```rust
// Input: Tokens from lexer
// Output: AST
AstNode::ExpressionStatement(ExpressionStatement {
    expression: Expression::Call(CallExpression {
        callee: Box::new(Expression::Identifier(IdentifierExpression {
            name: "print".to_string(),
        })),
        arguments: vec![Expression::Literal(LiteralExpression::String("Hello World!".to_string()))],
    }),
})
```

### Step 5: Interpretation (`interpreter.rs`)
```rust
// 1. Initialize interpreter
let mut interpreter = Interpreter::new();

// 2. Execute AST
interpreter.interpret(ast)?;

// 3. For ExpressionStatement:
//    - Evaluate the Call expression
//    - Look up "print" function (built-in)
//    - Call function with argument "Hello World!"
//    - Print to stdout
```

### Step 6: Output
```
Hello World!
```

## Code Examples and Flow

### Example 1: Simple Variable Assignment
```rust
// Source: let x = 42;
// 
// Lexer Output:
// [Let, Identifier("x"), Equal, Number(42.0), Semicolon, Eof]
//
// Parser Output:
// AstNode::LetStatement(LetStatement {
//   name: "x",
//   value: Some(Expression::Literal(LiteralExpression::Number(42.0))),
//   type_annotation: None,
// })
//
// Interpreter:
// 1. Execute LetStatement
// 2. Evaluate expression: 42.0
// 3. Define variable "x" in environment with value 42.0
```

### Example 2: Function Call with Expression
```rust
// Source: print(x + 10);
//
// Lexer Output:
// [Identifier("print"), LeftParen, Identifier("x"), Plus, Number(10.0), RightParen, Semicolon, Eof]
//
// Parser Output:
// AstNode::ExpressionStatement(ExpressionStatement {
//   expression: Expression::Call(CallExpression {
//     callee: Box::new(Expression::Identifier(IdentifierExpression { name: "print" })),
//     arguments: vec![Expression::Binary(BinaryExpression {
//       left: Box::new(Expression::Identifier(IdentifierExpression { name: "x" })),
//       operator: Token::Plus,
//       right: Box::new(Expression::Literal(LiteralExpression::Number(10.0))),
//     })],
//   }),
// })
//
// Interpreter:
// 1. Execute ExpressionStatement
// 2. Evaluate Call expression
// 3. Look up "print" function
// 4. Evaluate argument: x + 10
//    - Look up "x" in environment: 42.0
//    - Evaluate: 42.0 + 10.0 = 52.0
// 5. Call print(52.0)
// 6. Output: 52
```

## Development Guidelines

### For Junior Developers

#### 1. **Understanding the Flow**
- Start with `main.rs` to see how everything connects
- Follow the execution path: lexer → parser → interpreter
- Use debug prints to trace execution

#### 2. **Adding New Language Features**
1. **Lexer**: Add new token types in `lexer.rs`
2. **Parser**: Add parsing methods in `parser.rs`
3. **AST**: Add new node types in `ast.rs`
4. **Interpreter**: Add execution logic in `interpreter.rs`

#### 3. **Debugging Tips**
- Use `cargo run -- parse file.l1` to see AST
- Use `cargo run -- tokenize file.l1` to see tokens
- Add debug prints in interpreter methods
- Check environment state with `dbg!(&self.environment)`

#### 4. **Common Patterns**
- **Error Handling**: Use `Result<T>` for fallible operations
- **Position Tracking**: Always include line/column in errors
- **Environment Management**: Use `Rc<RefCell<Environment>>` for shared ownership
- **Expression Evaluation**: Return `Value` enum for all expressions

### Code Quality Guidelines

#### 1. **Error Messages**
```rust
// Good: Specific error with position
Err(Error::new(
    ErrorType::SyntaxError,
    format!("Expected identifier, found '{}'", token),
    line,
    column,
))

// Bad: Generic error
Err(Error::new(ErrorType::SyntaxError, "Parse error", 0, 0))
```

#### 2. **Documentation**
```rust
/// Parses a function declaration from the current token position.
/// 
/// Expected syntax: `function name(params) { body }`
/// 
/// # Returns
/// - `Ok(AstNode::FunctionDeclaration)` on success
/// - `Err(Error)` on syntax error
pub fn parse_function_declaration(&mut self) -> Result<AstNode> {
    // Implementation
}
```

#### 3. **Testing**
```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_simple_assignment() {
        let source = "let x = 42;";
        let tokens = lexer::tokenize(source).unwrap();
        let ast = parser::parse(tokens).unwrap();
        // Test AST structure
    }
}
```

## Language Enhancements (Latest Features)

### Async/Await Support

**Purpose**: Enable asynchronous programming with async functions and await expressions

**Implementation**:
```rust
// Parser: src/parser.rs
Token::Async => self.parse_function_declaration()?,

// AST: src/ast.rs
pub struct FunctionDeclaration {
    pub is_async: bool,  // New field for async functions
    // ... other fields
}

// Interpreter: src/interpreter.rs
fn evaluate_await(&mut self, await_expr: &AwaitExpression) -> Result<Value> {
    let value = self.evaluate(&await_expr.expression)?;
    match value {
        Value::Function(function) if function.is_async => {
            // Simulate async execution
            if let Some(body) = &function.body {
                self.execute(body)
            } else {
                Ok(Value::Null)
            }
        }
        _ => Ok(value),
    }
}
```

**Usage Example**:
```l1
async function fetchData(message: string) -> string {
    return "Async: " + message;
}

let result = await fetchData("Hello from async!");
print(result);
```

### Pattern Matching

**Purpose**: Powerful destructuring and matching with match expressions

**Implementation**:
```rust
// Parser: src/parser.rs
Token::Match => {
    self.advance(); // consume 'match'
    self.consume(&Token::LeftParen)?;
    let expr = self.parse_expression()?.unwrap();
    self.consume(&Token::RightParen)?;
    self.consume(&Token::LeftBrace)?;
    
    let mut arms = Vec::new();
    while !self.check(&Token::RightBrace) && !self.is_at_end() {
        arms.push(self.parse_match_arm()?);
        if self.check(&Token::Comma) {
            self.advance();
        }
    }
    self.consume(&Token::RightBrace)?;
    
    Expression::Match(MatchExpression {
        expression: Box::new(expr),
        arms,
    })
}

// Interpreter: src/interpreter.rs
fn evaluate_match(&mut self, match_expr: &MatchExpression) -> Result<Value> {
    let value = self.evaluate(&match_expr.expression)?;
    for arm in &match_expr.arms {
        if self.pattern_matches(&value, &arm.pattern)? {
            if let Some(guard) = &arm.guard {
                let guard_result = self.evaluate(guard)?;
                if !Interpreter::is_truthy(&guard_result) {
                    continue;
                }
            }
            return self.evaluate(&arm.expression);
        }
    }
    Err(LangOneError::RuntimeError("No matching pattern found".to_string()))
}
```

**Usage Example**:
```l1
let value = 42;
let result = match (value) {
    1 => "One",
    42 => "The Answer to Everything",
    100 => "Century",
    _ => "Unknown number"
};
print(result);
```

### Macro System (Basic)

**Purpose**: Compile-time code generation and metaprogramming

**Implementation**:
```rust
// Parser: src/parser.rs
fn parse_macro_declaration(&mut self) -> Result<AstNode> {
    self.consume(&Token::Macro)?;
    let name = self.parse_identifier()?;
    self.consume(&Token::LeftParen)?;
    let mut parameters = Vec::new();
    while !self.check(&Token::RightParen) && !self.is_at_end() {
        if !parameters.is_empty() {
            self.consume(&Token::Comma)?;
        }
        parameters.push(self.parse_identifier()?);
    }
    self.consume(&Token::RightParen)?;
    self.consume(&Token::LeftBrace)?;
    let _body = self.parse_block_statement()?;
    
    // Placeholder implementation
    Ok(AstNode::LetStatement(LetStatement {
        name: format!("macro_{}", name),
        type_annotation: None,
        value: Expression::Literal(LiteralExpression::String("Macro placeholder".to_string())),
    }))
}
```

**Usage Example**:
```l1
macro debug_print(message) {
    print("DEBUG: " + message);
}
```

### Integration with Existing Features

**Performance Optimizations**:
- All new language features work with constant folding
- Dead code elimination works with async functions
- Variable hoisting works with pattern matching
- Memory management tracks allocations for all features

**Type System Integration**:
- Async functions support full type checking
- Pattern matching works with all value types
- Generic types work with async functions
- Error handling integrates with all features

**Testing Coverage**:
- Comprehensive test suite for all features
- Integration tests for feature combinations
- Performance tests with optimizations
- Edge case testing for robustness

## Troubleshooting Guide

### Common Issues

#### 1. **Parser Hanging**
- **Cause**: Infinite recursion in parsing methods
- **Solution**: Check recursive calls, ensure proper token consumption
- **Debug**: Add debug prints to see which method is called repeatedly

#### 2. **Variable Not Found**
- **Cause**: Variable not defined in current scope
- **Solution**: Check environment management, ensure proper scoping
- **Debug**: Print environment contents with `dbg!(&self.environment)`

#### 3. **Type Mismatch**
- **Cause**: Wrong value type for operation
- **Solution**: Check type checking in interpreter
- **Debug**: Print value types with `dbg!(&value)`

#### 4. **Memory Issues**
- **Cause**: Circular references or improper ownership
- **Solution**: Use `Rc<RefCell<T>>` for shared ownership
- **Debug**: Use `cargo test -- --nocapture` to see debug output

### Debugging Commands

```bash
# Navigate to code directory first
cd code

# See tokens
cargo run -- tokenize examples/hello.l1

# See AST
cargo run -- parse examples/hello.l1

# Run with debug output
RUST_LOG=debug cargo run -- run examples/hello.l1

# Run tests with output
cargo test -- --nocapture
```

### Performance Considerations

#### 1. **Memory Usage**
- AST nodes are stored in `Box<T>` to avoid stack overflow
- Environment uses `Rc<RefCell<T>>` for shared ownership
- Large programs may need garbage collection (future enhancement)

#### 2. **Execution Speed**
- Tree-walk interpreter is slower than compiled code
- Consider JIT compilation for performance-critical code (future enhancement)
- Current implementation prioritizes simplicity over speed

#### 3. **Error Handling**
- All errors include position information
- Errors are propagated up the call stack
- Consider error recovery for better user experience (future enhancement)

---

This guide provides a complete understanding of LangOne's architecture and workflow. Junior developers can use this to understand how each component works and how to contribute to the project effectively.
