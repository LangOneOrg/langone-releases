# LangOne Alpha Release Steps

**Complete step-by-step guide for creating the alpha release**

---

## 🎯 **Prerequisites**

- ✅ Private repository: `LangOneOrg/langone` (source code)
- ✅ Public repository: `LangOneOrg/langone-releases` (binaries)
- ✅ CI/CD workflows configured
- ✅ All code committed and ready

---

## 🔐 **Step 1: Set Up GitHub Personal Access Token (PAT)**

### **1.1 Create Personal Access Token**

1. **Go to GitHub**: https://github.com/settings/tokens
2. **Click**: "Generate new token (classic)"
3. **Configure token**:
   - **Note**: "LangOne Public Repo Access"
   - **Expiration**: 90 days (or your preference)
   - **Scopes**: Check `repo` (Full control of private repositories)
4. **Click**: "Generate token"
5. **Copy the token** (you won't see it again!)

### **1.2 Add Token to Repository Secrets**

1. **Go to main repository**: `https://github.com/LangOneOrg/langone`
2. **Navigate**: Settings → Secrets and variables → Actions
3. **Click**: "New repository secret"
4. **Configure secret**:
   - **Name**: `PUBLIC_REPO_TOKEN`
   - **Value**: [Paste your PAT token]
5. **Click**: "Add secret"

---

## 🏷️ **Step 2: Create Alpha Release Tag**

### **2.1 Using Command Line (Recommended)**

```bash
# Navigate to your repository
cd D:\Code\Practice\Others\langone

# Create annotated tag with detailed message
git tag -a v0.1.0-alpha.1 -m "LangOne Alpha Release v0.1.0-alpha.1

This is the first alpha release of LangOne, featuring:

- Complete language implementation with all core features
- Interactive REPL with persistent variables
- VS Code extension with syntax highlighting and IntelliSense
- 41 built-in standard library functions
- Advanced memory management and optimization
- Pattern matching with bindings and guards
- Async/await with strict validation
- Macro system for compile-time code generation
- Optimizer with constant folding
- Multi-platform support (Windows, Linux, macOS)
- Professional installation experience

This release is ready for alpha testing by 25-50 trusted developers."

# Push tag to GitHub (this triggers the release workflow)
git push origin v0.1.0-alpha.1
```

### **2.2 Using GitHub Desktop**

1. **Open GitHub Desktop**
2. **Switch to main repository** (`LangOneOrg/langone`)
3. **Go to**: Repository → Create Tag
4. **Configure tag**:
   - **Tag name**: `v0.1.0-alpha.1`
   - **Description**: [Use the same message as above]
5. **Click**: "Create Tag"
6. **Push tag**: Repository → Push origin

### **2.3 Using GitHub Web Interface**

1. **Go to**: `https://github.com/LangOneOrg/langone`
2. **Click**: "Releases" → "Create a new release"
3. **Configure release**:
   - **Choose a tag**: `v0.1.0-alpha.1` (create new tag)
   - **Release title**: "LangOne Alpha Release v0.1.0-alpha.1"
   - **Description**: [Use the same message as above]
4. **Click**: "Publish release"

---

## ⚙️ **Step 3: Monitor CI/CD Pipeline**

### **3.1 Watch the Build Process**

1. **Go to**: `https://github.com/LangOneOrg/langone/actions`
2. **Look for**: "Build and Release LangOne" workflow
3. **Monitor progress**:
   - ✅ Test job (Ubuntu, Windows, macOS)
   - ✅ Build job (all platforms)
   - ✅ Release job (creates GitHub release)
   - ✅ Publish to public repo job

### **3.2 Expected Timeline**

- **Total time**: 10-15 minutes
- **Test job**: 3-5 minutes
- **Build job**: 5-8 minutes
- **Release job**: 2-3 minutes
- **Public repo update**: 1-2 minutes

### **3.3 Verify Success**

Check that all jobs show ✅ green status:
- [ ] Test job completed successfully
- [ ] Build job completed for all platforms
- [ ] Release job created GitHub release
- [ ] Public repo job updated `langone-releases`

---

## 📦 **Step 4: Verify Release Artifacts**

### **4.1 Check GitHub Release**

1. **Go to**: `https://github.com/LangOneOrg/langone/releases`
2. **Verify**:
   - [ ] Release `v0.1.0-alpha.1` exists
   - [ ] All platform binaries are attached
   - [ ] Checksums are included
   - [ ] QUICKSTART.md is attached
   - [ ] Release notes are complete

### **4.2 Check Public Repository**

1. **Go to**: `https://github.com/LangOneOrg/langone-releases`
2. **Verify**:
   - [ ] `latest/` directory updated
   - [ ] `releases/v0.1.0-alpha.1/` directory created
   - [ ] All binaries present
   - [ ] README.md updated
   - [ ] Symlinks working

### **4.3 Test Download Links**

```bash
# Test Windows binary
curl -L https://raw.githubusercontent.com/LangOneOrg/langone-releases/main/latest/langone-windows-x64.exe -o langone.exe
.\langone.exe --version

# Test Linux binary
curl -L https://raw.githubusercontent.com/LangOneOrg/langone-releases/main/latest/langone-linux-x64 -o langone
chmod +x langone
./langone --version

# Test macOS binary
curl -L https://raw.githubusercontent.com/LangOneOrg/langone-releases/main/latest/langone-macos-x64 -o langone
chmod +x langone
./langone --version
```

---

## 🧪 **Step 5: Test Sample Programs**

### **5.1 Download and Test**

```bash
# Download sample programs
curl -L https://raw.githubusercontent.com/LangOneOrg/langone-releases/main/latest/samples/hello_world.l1 -o hello_world.l1
curl -L https://raw.githubusercontent.com/LangOneOrg/langone-releases/main/latest/samples/arithmetic.l1 -o arithmetic.l1
curl -L https://raw.githubusercontent.com/LangOneOrg/langone-releases/main/latest/samples/control_flow.l1 -o control_flow.l1
curl -L https://raw.githubusercontent.com/LangOneOrg/langone-releases/main/latest/samples/patterns.l1 -o patterns.l1
curl -L https://raw.githubusercontent.com/LangOneOrg/langone-releases/main/latest/samples/stdlib_demo.l1 -o stdlib_demo.l1

# Test each sample
./langone run hello_world.l1
./langone run arithmetic.l1
./langone run control_flow.l1
./langone run patterns.l1
./langone run stdlib_demo.l1
```

### **5.2 Test REPL**

```bash
# Start interactive REPL
./langone repl

# Test commands:
# 42 + 8
# let x = 42;
# x * 2
# upper("hello")
# exit
```

---

## 📢 **Step 6: Announce Alpha Release**

### **6.1 Update Documentation**

1. **Update**: `docs/ALPHA_READY.md` - Mark as "LAUNCHED"
2. **Update**: `docs/COMPLETED_FEATURES.md` - Add release date
3. **Create**: `docs/ALPHA_RELEASE_NOTES.md` - Document what's new

### **6.2 Send Alpha Tester Invitations**

Use the template in `docs/ALPHA_INVITATION_EMAIL.md` or send personalized emails:

**Subject**: Join LangOne Alpha Testing - Shape the Future of Programming

**Key Points**:
- LangOne is an AI-native, cloud-ready programming language
- Complete implementation with all core features
- Easy installation (no Rust required)
- 2-3 hour commitment over 2 weeks
- Direct influence on language design
- Recognition in CONTRIBUTORS.md

**Getting Started**:
1. Install: Follow the [Quick Start Guide](https://github.com/LangOneOrg/langone-releases/main/latest/QUICKSTART.md)
2. Test: Run sample programs in `/samples`
3. Explore: Use the interactive REPL
4. Report: File issues on GitHub or email feedback

### **6.3 Social Media Announcement**

**Twitter/X**:
```
🚀 LangOne Alpha Release is here! 

AI-native, cloud-ready programming language with:
✅ Complete language implementation
✅ Interactive REPL
✅ VS Code extension
✅ 41 built-in functions
✅ Multi-platform support

Download: https://github.com/LangOneOrg/langone-releases
#LangOne #ProgrammingLanguage #AI #Rust
```

**LinkedIn**:
```
Excited to announce the alpha release of LangOne, an AI-native programming language designed for the future of software development.

Key features:
• Complete language implementation with modern features
• Interactive REPL for rapid prototyping
• VS Code extension with full IDE support
• 41 built-in standard library functions
• Multi-platform support (Windows, Linux, macOS)

We're looking for alpha testers to help shape the language. If you're interested in programming language design, AI integration, or modern development tools, we'd love your feedback.

Download and try it out: https://github.com/LangOneOrg/langone-releases
```

---

## 📊 **Step 7: Monitor Alpha Testing**

### **7.1 Set Up Monitoring**

1. **Run monitoring dashboard**:
   ```bash
   cd docs
   python3 alpha_monitoring_dashboard.py
   ```

2. **Track metrics**:
   - Installation success rate (target: ≥90%)
   - Sample program success rate (target: ≥80%)
   - Active testers (target: ≥25)
   - Bug reports (target: ≤5 P0)

### **7.2 Daily Activities**

1. **Check GitHub issues** for new bug reports
2. **Monitor installation success** rates
3. **Collect feedback** from alpha testers
4. **Update documentation** based on common issues
5. **Plan fixes** for critical bugs

### **7.3 Weekly Alpha Updates**

Send weekly updates to alpha testers with:
- Progress on reported issues
- New features or improvements
- Known issues and workarounds
- What to test this week
- Feedback highlights

---

## 🚨 **Troubleshooting**

### **Common Issues**

#### **CI/CD Pipeline Fails**
- **Check**: GitHub Actions logs for specific errors
- **Verify**: PAT token has correct permissions
- **Ensure**: All secrets are properly configured

#### **Release Not Created**
- **Check**: Tag was pushed correctly
- **Verify**: Workflow is triggered by tag push
- **Ensure**: All previous jobs completed successfully

#### **Public Repo Not Updated**
- **Check**: `PUBLIC_REPO_TOKEN` secret is correct
- **Verify**: Token has access to public repository
- **Ensure**: Public repo exists and is accessible

#### **Binaries Not Working**
- **Check**: Platform compatibility
- **Verify**: Checksums match
- **Test**: On fresh machine without Rust installed

### **Getting Help**

- **GitHub Issues**: File issues in the main repository
- **Email**: team@langone.io
- **Documentation**: Check `docs/` folder for detailed guides

---

## ✅ **Success Checklist**

Before considering the alpha release complete:

- [ ] PAT token configured in repository secrets
- [ ] Release tag `v0.1.0-alpha.1` created and pushed
- [ ] CI/CD pipeline completed successfully
- [ ] GitHub release created with all artifacts
- [ ] Public repository updated with binaries
- [ ] Download links tested and working
- [ ] Sample programs tested on all platforms
- [ ] REPL functionality verified
- [ ] Alpha tester invitations sent
- [ ] Monitoring dashboard activated
- [ ] Documentation updated
- [ ] Social media announcement posted

---

## 🎉 **Congratulations!**

You've successfully launched the LangOne Alpha Release! 

The language is now available for alpha testing, and you can begin collecting feedback from the community to shape the future of LangOne.

**Next Steps**:
- Monitor alpha testing feedback
- Fix critical bugs within 24 hours
- Plan beta phase features
- Prepare for community growth

**LangOne Alpha Release is LIVE! 🚀**
