# ⚡ LangOne Alpha Quickstart Guide

**Get coding with LangOne Alpha in 5 minutes!**

---

## 🚀 Step 1: Download & Install

### Windows
```powershell
# Download the alpha release
Invoke-WebRequest -Uri "https://github.com/LangOneOrg/langone-releases/raw/main/v0.3.0-alpha.1/binaries/windows-x64/langone.exe" -OutFile "langone.exe"

# Test installation
.\langone.exe --version
```

### macOS
```bash
# Download the alpha release
curl -L https://github.com/LangOneOrg/langone-releases/raw/main/v0.3.0-alpha.1/binaries/macos-x64/langone -o langone

# Make executable and test
chmod +x langone
./langone --version
```

### Linux
```bash
# Download the alpha release
curl -L https://github.com/LangOneOrg/langone-releases/raw/main/v0.3.0-alpha.1/binaries/linux-x64/langone -o langone

# Make executable and test
chmod +x langone
./langone --version
```

---

## 🎯 Step 2: Your First Program

Create a file called `hello.l1`:

```langone
// Hello World in LangOne Alpha
println("Hello, LangOne Alpha! 🚀");

// Variables and types
let name = "Alpha Tester";
let version = "0.3.0-alpha.1";
let is_alpha = true;

println("Name:", name, "Version:", version, "Alpha:", is_alpha);
```

Run it:
```bash
langone run hello.l1
```

**Expected Output:**
```
Hello, LangOne Alpha! 🚀
Name: Alpha Tester Version: 0.3.0-alpha.1 Alpha: true
```

---

## 🧠 Step 3: Enable Developer Intelligence (Optional)

```bash
# Enable telemetry for personalized experience
langone config --enable-telemetry

# Configure privacy settings
langone config --telemetry-level anonymous
langone config --telemetry-retention 30d

# View current settings
langone config --show-telemetry-settings
```

---

## 🎮 Step 4: Interactive REPL

Start the interactive REPL:
```bash
langone repl
```

Try these commands:
```langone
// Basic arithmetic
let result = 2 + 3 * 4;
println("Result:", result);

// Arrays
let numbers = [1, 2, 3, 4, 5];
let doubled = array::map(numbers, |x| x * 2);
println("Doubled:", doubled);

// Functions
let add = fn(a: i32, b: i32) -> i32 { a + b };
println("Sum:", add(10, 20));
```

---

## 🤖 Step 5: AI-Native Features (Alpha)

Try the new AI integration:
```langone
// Load an AI model (requires internet)
let model = ai::load_model("gpt-4");
let response = model.generate("Write a simple sorting algorithm");

// Quantum primitives (experimental)
let qubit = quantum::create_qubit();
let result = quantum::measure(qubit);
println("Quantum result:", result);
```

---

## 📚 Step 6: Explore Examples

Run the provided examples:
```bash
# CLI Application
langone run examples/cli_app.l1

# Web API
langone run examples/web_api.l1

# AI Agent
langone run examples/ai_agent_example.l1
```

---

## 🧪 Step 7: Alpha Testing

### Report Issues
- **Critical Bugs**: [GitHub Issues](https://github.com/LangOneOrg/langone/issues)
- **Feature Requests**: [GitHub Discussions](https://github.com/LangOneOrg/langone/discussions)
- **Community Feedback**: [Feedback Portal](./community-feedback.md)

### Test Focus Areas
1. **Basic Functionality**: Variables, functions, control flow
2. **AI Features**: Model integration, quantum primitives
3. **Performance**: Memory usage, compilation speed
4. **Error Handling**: Error messages, debugging
5. **Developer Intelligence**: Telemetry, learning features

---

## 🔧 Common Alpha Issues

### Issue: "Command not found"
**Solution**: Make sure `langone` is in your PATH or use full path

### Issue: "Permission denied" (Linux/macOS)
**Solution**: Make the binary executable: `chmod +x langone`

### Issue: "Windows Defender blocked"
**Solution**: Allow the file in Windows Security or add exclusion

### Issue: "AI model connection failed"
**Solution**: Check internet connection or use `--offline-mode`

---

## 📞 Getting Help

- **Documentation**: [LangOne Docs](https://docs.langone.io)
- **Community**: [GitHub Discussions](https://github.com/LangOneOrg/langone/discussions)
- **Issues**: [GitHub Issues](https://github.com/LangOneOrg/langone/issues)
- **Discord**: [LangOne Discord](https://discord.gg/langone)

---

## 🎉 Next Steps

1. **Explore Tutorials**: Check out the [tutorials](./tutorials/) directory
2. **Read Documentation**: Learn about [Developer Intelligence](./developer-intelligence.md)
3. **Join Community**: Participate in [community discussions](https://github.com/LangOneOrg/langone/discussions)
4. **Provide Feedback**: Help improve LangOne through [alpha feedback](./community-feedback.md)

---

**Welcome to LangOne Alpha! 🚀**

*Remember: This is an alpha release. Expect bugs and missing features. Your feedback helps make LangOne better!*
