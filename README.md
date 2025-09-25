# LangOne Programming Language

**AI-native, cloud-ready, quantum-enabled programming language**

## Quick Start

### Download Latest Release

**Windows:**
```powershell
# Download and run
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/LangOneOrg/langone-releases/main/latest/langone-windows-x64.exe" -OutFile "langone.exe"
.\langone.exe --version
```

**Linux:**
```bash
# Download and run
curl -L https://raw.githubusercontent.com/LangOneOrg/langone-releases/main/latest/langone-linux-x64 -o langone
chmod +x langone
./langone --version
```

**macOS:**
```bash
# Download and run
curl -L https://raw.githubusercontent.com/LangOneOrg/langone-releases/main/latest/langone-macos-x64 -o langone
chmod +x langone
./langone --version
```

### Verify Installation

```bash
# Run hello world
langone run samples/hello_world.l1

# Start interactive REPL
langone repl
```

## Alpha Testing

This is an alpha release of LangOne. We're looking for feedback from developers to help shape the language.

### What to Test
- Installation on your platform
- Sample programs in `/samples`
- Interactive REPL
- VS Code extension (coming soon)

### Report Issues
- File issues on GitHub
- Email feedback to team@langone.io

## Documentation

- [Quick Start Guide](latest/QUICKSTART.md)
- [Sample Programs](latest/samples/)
- [Installation Scripts](latest/installers/)

## Releases

- [Latest Release](latest/)
- [All Releases](releases/)

---

**Website**: https://langone.io  
**Email**: team@langone.io
