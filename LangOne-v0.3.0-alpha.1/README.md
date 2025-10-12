# LangOne — The AI-Native Green Programming Language for Everyone

**Version:** 0.3.0-alpha.1  
**Platform:** Windows 10/11 (64-bit)  
**Release Date:** October 12, 2025

## What is LangOne?

LangOne is a new kind of programming language — intelligent, eco-friendly, and designed for people of all backgrounds to learn coding easily.

You don't need prior experience. Just download, run, and start learning!

---

## 🚀 Quick Install

Choose your preferred installation method:

### Method 1: Download with PowerShell (Recommended)

Open PowerShell as Administrator and run:

```powershell
# Step 1: Create installation directory
New-Item -ItemType Directory -Path "C:\LangOne\bin" -Force

# Step 2: Download LangOne
Invoke-WebRequest -Uri "https://github.com/LangOneOrg/langone-releases/raw/main/langone.exe" `
                  -OutFile "C:\LangOne\bin\langone.exe"

# Step 3: Add to PATH (for current session)
$env:PATH += ";C:\LangOne\bin"

# Step 4: Add to PATH permanently
setx PATH "$env:PATH;C:\LangOne\bin" /M

# Step 5: Restart PowerShell and test
langone --version
```

### Method 2: Download with Curl

If you have curl installed:

```powershell
# Step 1: Create installation directory
New-Item -ItemType Directory -Path "C:\LangOne\bin" -Force

# Step 2: Download LangOne
curl -L "https://github.com/LangOneOrg/langone-releases/raw/main/langone.exe" `
     -o "C:\LangOne\bin\langone.exe"

# Step 3: Add to PATH
$env:PATH += ";C:\LangOne\bin"
setx PATH "$env:PATH;C:\LangOne\bin" /M

# Step 4: Restart PowerShell and test
langone --version
```

### Method 3: Manual Installation

1. **Download** `langone.exe` from the [releases page](https://github.com/LangOneOrg/langone-releases)
2. **Create folder** `C:\LangOne\bin`
3. **Move** `langone.exe` to `C:\LangOne\bin\`
4. **Add to PATH:**
   - Open PowerShell as Administrator
   - Run: `setx PATH "$env:PATH;C:\LangOne\bin" /M`
5. **Restart** your terminal
6. **Test:** Run `langone --version`

---

## 📚 Download Tutorials

After installing LangOne, download the tutorial files:

```powershell
# Create tutorials directory
New-Item -ItemType Directory -Path "C:\LangOne\Tutorials" -Force

# Download all tutorials (you'll need to do this for each file)
# Or clone the repository with tutorials included
```

**Or** extract the full release package which includes all tutorials!

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

### "langone is not recognized as a command"

**Solution:** PATH not set correctly. Try:

```powershell
# Check if LangOne exists
Test-Path C:\LangOne\bin\langone.exe

# If true, add to PATH again:
setx PATH "$env:PATH;C:\LangOne\bin" /M

# Then restart PowerShell
```

### Download fails with Invoke-WebRequest

**Solution 1:** Try curl instead  
**Solution 2:** Download manually from GitHub  
**Solution 3:** Check your internet connection  

### Permission denied errors

**Solution:** Run PowerShell as Administrator

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
