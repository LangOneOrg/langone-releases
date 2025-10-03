# 📥 Quick Install Guide

**Get LangOne running in 5 minutes!**

This guide will help you install LangOne on your system quickly and easily. Choose your operating system below.

---

## 🪟 **Windows Installation**

### **Step 1: Download**
**Recommended: Use curl to avoid Windows Defender triggers**

```cmd
# Download using curl (recommended)
curl -L -o LangOne-v0.2.0-alpha.1-Complete-Release.zip https://github.com/langone-project/langone-releases/releases/download/v0.2.0-alpha.1/LangOne-v0.2.0-alpha.1-Complete-Release.zip
```

**Alternative: Browser download**
1. Click [Download LangOne for Windows](releases/v0.2.0-alpha.1/LangOne-v0.2.0-alpha.1-Complete-Release.zip)
2. Save the file to your Downloads folder

### **Step 2: Extract**
1. Right-click the downloaded ZIP file
2. Select "Extract All..."
3. Choose a location (e.g., `C:\LangOne\`)

### **Step 3: Install**
1. Open Command Prompt as Administrator
2. Navigate to the extracted folder:
   ```cmd
   cd C:\LangOne\v0.2.0-alpha.1\windows-x64
   ```
3. Copy executables to a system folder:
   ```cmd
   copy langone.exe C:\Windows\System32\
   copy lo.exe C:\Windows\System32\
   ```

### **Step 4: Test Installation**
```cmd
langone --help
lo --help
```

**✅ You're ready to go!** Try [Basic Usage](basic-usage.md) next.

---

## 🍎 **macOS Installation** *(Coming Soon)*

### **Step 1: Download**
1. Click [Download LangOne for macOS](../marketing/complete-release/macos-x64/)
2. Save the DMG file to your Downloads folder

### **Step 2: Install**
1. Double-click the DMG file
2. Follow the installation wizard
3. Enter your password when prompted

### **Step 3: Test Installation**
```bash
langone --help
lo --help
```

**✅ You're ready to go!** Try [Basic Usage](basic-usage.md) next.

---

## 🐧 **Linux Installation** *(Coming Soon)*

### **Step 1: Download**
Choose your preferred package format:

**For Ubuntu/Debian:**
```bash
wget [Download LangOne .deb package]
sudo dpkg -i langone_0.2.0-alpha.1_amd64.deb
```

**For CentOS/RHEL/Fedora:**
```bash
wget [Download LangOne .rpm package]
sudo rpm -i langone-0.2.0-alpha.1-1.x86_64.rpm
```

**For any Linux:**
```bash
wget [Download LangOne .tar.gz package]
tar -xzf langone-0.2.0-alpha.1-linux-x86_64.tar.gz
cd langone-0.2.0-alpha.1
sudo ./install.sh
```

### **Step 2: Test Installation**
```bash
langone --help
lo --help
```

**✅ You're ready to go!** Try [Basic Usage](basic-usage.md) next.

---

## 🔧 **Troubleshooting**

### **Windows Issues**

**Problem**: "langone is not recognized as an internal or external command"
**Solution**: Make sure you copied the files to a folder in your PATH, or use the full path:
```cmd
C:\LangOne\v0.2.0-alpha.1\windows-x64\langone.exe --help
```

**Problem**: Windows Defender blocks the executable
**Solution**: This is normal for new programs. To avoid this:
1. Use curl download method (recommended above)
2. If using browser download, click "More info" → "Run anyway"
3. Add the folder to Windows Defender exclusions if needed

### **macOS Issues**

**Problem**: "langone: command not found"
**Solution**: Make sure the installation completed successfully and try:
```bash
which langone
```

### **Linux Issues**

**Problem**: Permission denied
**Solution**: Make sure the executable has the right permissions:
```bash
chmod +x langone
```

---

## ✅ **Installation Complete!**

Once you see the help message, you're ready to start using LangOne!

### **What's Next?**
- [🎮 Basic Usage](basic-usage.md) - Write your first LangOne program
- [🚀 Next Steps](next-steps.md) - Explore advanced features
- [📖 Complete Documentation](index.md) - Comprehensive guides

### **Need Help?**
- [💬 Community Discussions](https://github.com/langone-project/langone/discussions)
- [🐛 Report Issues](https://github.com/langone-project/langone/issues)

---

**Welcome to LangOne! 🚀**
