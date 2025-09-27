# LangOne Releases

**Official release repository for LangOne - AI-native, universal programming language**

## 🚀 Latest Release

### v0.1.0-alpha.1 (Alpha Release)
**Status**: Available for testing  
**Release Date**: September 27, 2025

#### Download Links
- **Windows x64**: [Download langone.exe](releases/v0.1.0-alpha.1/windows-x64/langone.exe) (2.3MB)
- **Short Alias**: [Download lo.exe](releases/v0.1.0-alpha.1/windows-x64/lo.exe) (2.3MB)

#### Documentation
- **Release Notes**: [View Release Notes](releases/v0.1.0-alpha.1/RELEASE_NOTES.md)
- **Installation Guide**: [Windows Installation](releases/v0.1.0-alpha.1/windows-x64/README.md)

## 📁 Repository Structure

```
langone-releases/
├── latest/                    # Symlinks to latest release
├── releases/                  # All versioned releases
│   └── v0.1.0-alpha.1/       # Current alpha release
│       ├── RELEASE_NOTES.md   # Comprehensive release notes
│       └── windows-x64/       # Windows binaries and docs
│           ├── langone.exe    # Main executable
│           ├── lo.exe         # Short alias
│           ├── *.sha256       # Checksums for verification
│           └── README.md      # Platform-specific docs
└── README.md                  # This file
```

## 🔐 Verification

Verify your download integrity using SHA256 checksums:

```bash
# Windows
certutil -hashfile langone.exe SHA256
# Expected: 988ae96b42585511f6b1668298b0d2d78c54d4631716f3b71ca9dc239c610c1b

certutil -hashfile lo.exe SHA256
# Expected: c0020114ecb9c9cce97287c36ed24d2fb516b9073b17630467355c75292b31cc
```

## 🚀 Quick Start

1. **Download** the appropriate binary for your platform
2. **Verify** the checksum matches the expected value
3. **Run** `langone --help` or `lo --help` to see available commands
4. **Start coding** with the REPL: `langone repl` or `lo repl`

## 📋 What's New in v0.1.0-alpha.1

- ✅ **Fixed mixed numeric type operations** (Float/Integer arithmetic)
- ✅ **Dual executables** (`langone.exe` and `lo.exe` for convenience)
- ✅ **Enhanced error messages** with detailed type information
- ✅ **Improved REPL experience** with better formatting
- ✅ **Complete documentation** and installation guides

## 🔄 Release Process

This repository follows a structured release process:

1. **Alpha releases** (`v0.x.x-alpha.x`) - Early testing and feedback
2. **Beta releases** (`v0.x.x-beta.x`) - Feature-complete, testing phase
3. **Release candidates** (`v0.x.x-rc.x`) - Final testing before stable
4. **Stable releases** (`v1.x.x`) - Production-ready releases

## 📞 Support & Feedback

- **Issues**: Report bugs and request features on the main [LangOne repository](https://github.com/LangOneOrg/langone)
- **Discussions**: Join community discussions
- **Documentation**: Visit [langone.io](https://langone.io) for comprehensive guides

## 📄 License

LangOne is released under the MIT License. See [LICENSE](LICENSE) file for details.

---

**LangOne Team**  
*Building the future of AI-native programming*

**Website**: https://langone.io  
**Email**: team@langone.io