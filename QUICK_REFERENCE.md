# LangOne v0.3.0-alpha.1 - Quick Reference Card

## 📥 Download & Install (Copy-Paste Commands)

### Option 1: PowerShell Download

```powershell
# One-line install (run as Administrator)
New-Item -ItemType Directory -Path "C:\LangOne\bin" -Force; Invoke-WebRequest -Uri "https://github.com/LangOneOrg/langone-releases/raw/main/langone.exe" -OutFile "C:\LangOne\bin\langone.exe"; $env:PATH += ";C:\LangOne\bin"; setx PATH "$env:PATH;C:\LangOne\bin" /M
```

### Option 2: Curl Download

```powershell
# One-line install with curl (run as Administrator)
New-Item -ItemType Directory -Path "C:\LangOne\bin" -Force; curl -L "https://github.com/LangOneOrg/langone-releases/raw/main/langone.exe" -o "C:\LangOne\bin\langone.exe"; $env:PATH += ";C:\LangOne\bin"; setx PATH "$env:PATH;C:\LangOne\bin" /M
```

### Verify Installation

```powershell
langone --version
```

---

## 📚 First Steps

### 1. Create Your First Program

```powershell
# Create hello.l1
Set-Content -Path "hello.l1" -Value 'print("Hello, LangOne!")'

# Run it
langone hello.l1
```

### 2. Download Tutorials (Optional)

```powershell
# Download complete package
Invoke-WebRequest -Uri "https://github.com/LangOneOrg/langone-releases/raw/main/LangOne-v0.3.0-alpha.1-windows-x64.zip" -OutFile "LangOne.zip"

# Extract
Expand-Archive -Path "LangOne.zip" -DestinationPath "C:\LangOne" -Force
```

---

## 🎓 Learning Path

1. **Tutorial 1** - Hello World (10 min)
2. **Tutorial 2** - Variables (15 min)
3. **Tutorial 3** - Conditions & Loops (20 min)
4. **Tutorial 4** - Functions (20 min)
5. **Tutorial 5** - AI Features (15 min)
6. **Tutorial 6** - Green Coding (15 min)

**Total:** 90 minutes to become a green coder!

---

## 🔧 Common Commands

```powershell
# Run a program
langone myprogram.l1

# Check version
langone --version

# Get help
langone --help
```

---

## 📍 File Locations

- **Binary:** `C:\LangOne\bin\langone.exe`
- **Tutorials:** `C:\LangOne\Tutorials\`
- **Examples:** `C:\LangOne\examples\`

---

## 🆘 Quick Fixes

### "langone not recognized"
```powershell
setx PATH "$env:PATH;C:\LangOne\bin" /M
# Then restart PowerShell
```

### Check if installed
```powershell
Test-Path C:\LangOne\bin\langone.exe
```

### View PATH
```powershell
$env:PATH -split ';' | Select-String "LangOne"
```

---

## 📖 Documentation

- **README:** See `README.md` for complete guide
- **Installation:** See `INSTALLATION_GUIDE.md` for detailed steps
- **Tutorials:** See `LangOne-v0.3.0-alpha.1/Tutorials/`

---

## 🌐 Links

- **GitHub:** github.com/LangOneOrg/langone-releases
- **Issues:** Report bugs and request features
- **License:** Apache 2.0

---

**Remember:** Replace `LangOneOrg` with actual GitHub username!

---

*Quick Reference for LangOne v0.3.0-alpha.1*

