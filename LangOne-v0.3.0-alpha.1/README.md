# LangOne — The AI-Native Green Programming Language for Everyone

**Version:** 0.3.0-alpha.1  
**Platform:** Windows 10/11 (64-bit)  
**Release Date:** October 12, 2025

## What is LangOne?

LangOne is a new kind of programming language — intelligent, eco-friendly, and designed for people of all backgrounds to learn coding easily.

You don't need prior experience. Just download, run, and start learning!

---

## 🚀 Quick Install

📋 **For complete installation instructions, see:** [**Installation Guide**](../README.md#-quick-install-windows)

### Quick Command (PowerShell)

```powershell
# Create directory and download LangOne
New-Item -ItemType Directory -Path "C:\LangOne\bin" -Force
Invoke-WebRequest -Uri "https://github.com/LangOneOrg/langone-releases/raw/main/LangOne-v0.3.0-alpha.1/bin/langone.exe" `
                  -OutFile "C:\LangOne\bin\langone.exe"

# Add to PATH and test
$env:PATH += ";C:\LangOne\bin"
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
[Environment]::SetEnvironmentVariable("Path", "$userPath;C:\LangOne\bin", "User")
langone --version
```

> **Note:** No admin rights required! This sets your user PATH.

---

## ✅ Verify Installation

After installation, verify everything works:

```powershell
# Check version
langone --version

# Expected output: LangOne v0.3.0-alpha.1
```

---

## 🎯 Your First Program

### Option A: From Scratch

1. Create a file called `hello.l1`
2. Add this code:
   ```langone
   print("Hello, LangOne!")
   ```
3. Run it:
   ```powershell
   langone hello.l1
   ```

### Option B: Use Included Example

If you have the full release package:

```powershell
cd C:\LangOne\examples
langone hello.l1
```

Expected Output:
```
Hello, LangOne!
Welcome to the future of programming!
```

---

## 📖 Learning Path

Follow these tutorials in order:

1. **01_Hello_World.l1** (10 min) - Your first program
2. **02_Variables_and_Types.l1** (15 min) - Storing data
3. **03_Conditions_and_Loops.l1** (20 min) - Making decisions
4. **04_Functions_and_Modules.l1** (20 min) - Organizing code
5. **05_AI_Code_Assist.l1** (15 min) - AI-powered coding
6. **06_Green_Code_Principles.l1** (15 min) - Sustainable programming

**Total learning time:** ~90 minutes from zero to green coder!

📖 See [Tutorials/index.md](Tutorials/index.md) for detailed tutorial guide.

---

## 📦 What's Included in Full Package

When you download the complete release:

- **bin/langone.exe** - The LangOne compiler and interpreter
- **Tutorials/** - 6 beginner-friendly lessons
- **examples/** - Sample programs to try
- **README.md** - This file
- **LICENSE.txt** - Legal information
- **CHANGELOG.md** - What's new in this version

---

## 🔋 System Requirements

- **Operating System:** Windows 10 or Windows 11 (64-bit)
- **Disk Space:** At least 100 MB free
- **Memory:** 2 GB RAM minimum (4 GB recommended)
- **Internet:** Required for initial download

---

## 🆘 Troubleshooting

### ⚠️ "WARNING: The data being saved is truncated to 1024 characters"

**This is critical!** The old `setx` method truncated your PATH and may have broken other programs.

**Solution - Restore and Fix:**

```powershell
# Check your current user PATH
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
$userPath

# If it looks wrong/truncated, you may need to restore it from system restore
# or manually re-add missing paths

# To add LangOne correctly (no truncation):
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($userPath -notlike "*C:\LangOne\bin*") {
    [Environment]::SetEnvironmentVariable("Path", "$userPath;C:\LangOne\bin", "User")
    Write-Host "✅ LangOne added to PATH successfully (no truncation!)"
}

# Restart PowerShell to see the changes
```

> **Why this happened:** `setx PATH "$env:PATH"` has a 1024 char limit. The new method uses .NET APIs with no limit.

---

### "langone is not recognized as a command"

**Solution:** PATH not set correctly. Try:

```powershell
# Check if LangOne exists
Test-Path C:\LangOne\bin\langone.exe

# If true, add to PATH again:
$env:PATH += ";C:\LangOne\bin"
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
[Environment]::SetEnvironmentVariable("Path", "$userPath;C:\LangOne\bin", "User")

# Then restart PowerShell
```

### Download fails with Invoke-WebRequest

**Solution 1:** Try curl instead (Option 2 in the [Installation Guide](../README.md))  
**Solution 2:** Download manually from GitHub  
**Solution 3:** Check your internet connection  

### Permission denied when creating directory

**Solution:** Choose a different location where you have write permissions, or run PowerShell normally (admin rights not required for C:\LangOne\bin)

### "Unsupported 16-Bit Application" or "not a valid application for this OS platform"

**This means the downloaded file is corrupted or not a proper Windows executable.**

**Solution - Re-download and verify:**

```powershell
# Step 1: Check if the file exists and its size
Get-ChildItem "C:\LangOne\bin\langone.exe" | Select-Object Name, Length, LastWriteTime

# Step 2: Check file type (should show PE32+ executable)
Get-ItemProperty "C:\LangOne\bin\langone.exe" | Select-Object Name, Length

# Step 3: Delete corrupted file
Remove-Item "C:\LangOne\bin\langone.exe" -Force

# Step 4: Re-download with verification
Invoke-WebRequest -Uri "https://github.com/LangOneOrg/langone-releases/raw/main/LangOne-v0.3.0-alpha.1/bin/langone.exe" `
                  -OutFile "C:\LangOne\bin\langone.exe" `
                  -UseBasicParsing

# Step 5: Verify download
if (Test-Path "C:\LangOne\bin\langone.exe") {
    $fileInfo = Get-Item "C:\LangOne\bin\langone.exe"
    Write-Host "✅ File downloaded successfully: $($fileInfo.Length) bytes"
    Write-Host "📅 Downloaded: $($fileInfo.LastWriteTime)"
} else {
    Write-Host "❌ Download failed"
}

# Step 6: Test again
langone --version
```

**Alternative: Try curl instead of Invoke-WebRequest**

```powershell
Remove-Item "C:\LangOne\bin\langone.exe" -ErrorAction SilentlyContinue
curl.exe -L "https://github.com/LangOneOrg/langone-releases/raw/main/LangOne-v0.3.0-alpha.1/bin/langone.exe" `
     -o "C:\LangOne\bin\langone.exe"
langone --version
```

---

### "Windows protected your PC" warning

**Solution:** Click "More info" → "Run anyway"  
(This appears because the binary isn't digitally signed yet)

---

## 💡 Quick Reference

### Common Commands

```powershell
# Run a program
langone myprogram.l1

# Check version
langone --version

# Get help
langone --help
```

### File Locations

- **LangOne executable:** `C:\LangOne\bin\langone.exe`
- **Tutorials:** `C:\LangOne\Tutorials\`
- **Examples:** `C:\LangOne\examples\`
- **Your programs:** Anywhere you like!

---

## 🌍 Why "Green" Programming?

LangOne is designed to be energy-efficient and environmentally conscious. When you write LangOne code, the language automatically optimizes it to use less energy and resources.

You're not just learning to code — you're learning to code sustainably!

Learn more in [Tutorial 6: Green Code Principles](Tutorials/06_Green_Code_Principles.l1)

---

## 📜 License

LangOne is licensed under the Apache License 2.0. See [LICENSE.txt](LICENSE.txt) for details.

---

## 🎉 Welcome to LangOne!

You're now ready to start your programming journey. Remember:

- **Take your time** - Learning is a journey, not a race
- **Experiment freely** - Try things and see what happens
- **Have fun** - Enjoy the process of creation!
- **Think green** - Every program you write can help the planet

### Next Steps:

1. ✅ Install LangOne (you just did this!)
2. ✅ Run your first program
3. ✅ Complete Tutorial 1
4. ✅ Work through all 6 tutorials
5. ✅ Start creating your own programs

Happy coding! 🚀🌱

---

## 📞 Community & Support

- **GitHub Issues:** Report bugs and request features
- **Tutorials:** Complete beginner-friendly lessons included
- **Examples:** Learn from working code samples

---

*LangOne v0.3.0-alpha.1 - October 2025*

**Remember to replace `LangOneOrg` with your actual GitHub username in the download URLs!**
