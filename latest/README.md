# Latest Release

This directory contains the latest LangOne release.

## Current Latest Release: v0.1.0-alpha.1

### Download Links
- **Windows x64**: [langone.exe](../releases/v0.1.0-alpha.1/windows-x64/langone.exe)
- **Short Alias**: [lo.exe](../releases/v0.1.0-alpha.1/windows-x64/lo.exe)

### Documentation
- **Release Notes**: [View Release Notes](../releases/v0.1.0-alpha.1/RELEASE_NOTES.md)
- **Installation Guide**: [Windows Installation Guide](../releases/v0.1.0-alpha.1/windows-x64/README.md)

### Verification
```bash
# Windows
certutil -hashfile langone.exe SHA256
# Expected: 988ae96b42585511f6b1668298b0d2d78c54d4631716f3b71ca9dc239c610c1b

certutil -hashfile lo.exe SHA256
# Expected: c0020114ecb9c9cce97287c36ed24d2fb516b9073b17630467355c75292b31cc
```

## Platform Support

| Platform | Status | Download |
|----------|--------|----------|
| Windows x64 | ✅ Available | [Download](../releases/v0.1.0-alpha.1/windows-x64/) |
| Linux x64 | 🚧 Coming Soon | - |
| macOS x64 | 🚧 Coming Soon | - |

## What's New

- Fixed mixed numeric type operations (Float/Integer arithmetic)
- Added short executable alias (`lo.exe`)
- Enhanced error messages and REPL experience
- Complete documentation and installation guides

For more details, see the [Release Notes](../releases/v0.1.0-alpha.1/RELEASE_NOTES.md).