# LangOne Public Releases

Welcome to the LangOne public releases directory!

## 📦 Current Release

**Latest Version:** v0.3.0-alpha.1  
**Platform:** Windows 10/11 (64-bit)  
**Release Date:** October 12, 2025

### 📖 Full Documentation

For complete installation instructions, tutorials, and documentation, see:

**👉 [LangOne-v0.3.0-alpha.1/README.md](LangOne-v0.3.0-alpha.1/README.md)**

---

## 🚀 Quick Install (Windows)

> ✅ **No administrator rights required!** These commands set your user PATH.

### Option 1: Download with PowerShell (Recommended)

```powershell
# Create installation directory
New-Item -ItemType Directory -Path "C:\LangOne\bin" -Force

# Download LangOne executable
Invoke-WebRequest -Uri "https://github.com/LangOneOrg/langone-releases/raw/main/LangOne-v0.3.0-alpha.1/bin/langone.exe" `
                  -OutFile "C:\LangOne\bin\langone.exe"

# Add to PATH (for current session)
$env:PATH += ";C:\LangOne\bin"

# Add to PATH permanently (user level - no admin needed, no truncation)
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
[Environment]::SetEnvironmentVariable("Path", "$userPath;C:\LangOne\bin", "User")

# Restart PowerShell and test installation
langone --version
```

### Option 2: Download with Curl

```powershell
# Create installation directory
New-Item -ItemType Directory -Path "C:\LangOne\bin" -Force

# Download LangOne executable
curl.exe -L "https://github.com/LangOneOrg/langone-releases/raw/main/LangOne-v0.3.0-alpha.1/bin/langone.exe" `
     -o "C:\LangOne\bin\langone.exe"

# Add to PATH (for current session)
$env:PATH += ";C:\LangOne\bin"

# Add to PATH permanently (user level - no admin needed, no truncation)
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
[Environment]::SetEnvironmentVariable("Path", "$userPath;C:\LangOne\bin", "User")

# Restart PowerShell and test installation
langone --version
```

---

## 📂 Available Releases

- **[v0.3.0-alpha.1](LangOne-v0.3.0-alpha.1/)** - First public alpha release (October 2025)

---

## 🆘 Need Help?

Visit the full release folder for:
- Complete README
- 6 Beginner Tutorials
- Example Programs
- CHANGELOG
- LICENSE

**Start here:** [LangOne-v0.3.0-alpha.1/README.md](LangOne-v0.3.0-alpha.1/README.md)

---

*Note: Replace `LangOneOrg` with your actual GitHub username when uploading to GitHub.*

