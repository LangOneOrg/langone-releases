# Manual Upload Instructions for LangOne v0.1.0-alpha.1

## Files Ready for Upload

The following files are ready to be uploaded to the `langone-releases` repository:

### Windows x64 Release
```
release-assets/windows-x64/
├── langone.exe (2.3MB)
├── langone.exe.sha256 (64 bytes)
├── lo.exe (2.3MB)
├── lo.exe.sha256 (64 bytes)
└── README.md (1.5KB)
```

### Additional Documentation
```
release-assets/
├── RELEASE_NOTES.md (4.2KB)
└── upload-instructions.md (this file)
```

## Upload Steps

### 1. Navigate to langone-releases Repository
- Go to your `langone-releases` repository on GitHub
- Create a new folder: `v0.1.0-alpha.1/windows-x64/`

### 2. Upload Windows Binaries
Upload these files to `v0.1.0-alpha.1/windows-x64/`:
- `langone.exe`
- `langone.exe.sha256`
- `lo.exe`
- `lo.exe.sha256`
- `README.md`

### 3. Upload Release Documentation
Upload these files to `v0.1.0-alpha.1/`:
- `RELEASE_NOTES.md`

### 4. Create GitHub Release (Optional)
If you want to create a proper GitHub release:
1. Go to "Releases" in your langone-releases repo
2. Click "Create a new release"
3. Tag: `v0.1.0-alpha.1`
4. Title: `LangOne v0.1.0-alpha.1 - Alpha Release`
5. Description: Copy content from `RELEASE_NOTES.md`
6. Attach the binary files as release assets

## File Verification

After upload, users can verify the binaries using:

```bash
# Windows
certutil -hashfile langone.exe SHA256
# Should match: 988ae96b42585511f6b1668298b0d2d78c54d4631716f3b71ca9dc239c610c1b

certutil -hashfile lo.exe SHA256  
# Should match: c0020114ecb9c9cce97287c36ed24d2fb516b9073b17630467355c75292b31cc
```

## Directory Structure After Upload

```
langone-releases/
└── v0.1.0-alpha.1/
    ├── RELEASE_NOTES.md
    └── windows-x64/
        ├── langone.exe
        ├── langone.exe.sha256
        ├── lo.exe
        ├── lo.exe.sha256
        └── README.md
```

## Next Steps After Upload

1. **Test the uploaded binaries** to ensure they work correctly
2. **Update the main README.md** in langone-releases with download links
3. **Create symlinks** for `latest` pointing to `v0.1.0-alpha.1`
4. **Announce the release** on your preferred channels

## Quick Commands to Copy Files

If you're using GitHub Desktop or command line:

```bash
# Copy all files to your langone-releases directory
cp -r release-assets/* /path/to/langone-releases/
```

The release is ready! All files are properly signed and documented.
