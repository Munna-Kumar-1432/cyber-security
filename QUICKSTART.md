# 🚀 Quick Start Guide

Get started with the Password Strength Checker in 3 simple steps!

## Step 1: Verify Python Installation

Open your terminal/command prompt and check Python version:

```bash
python --version
```

You should see Python 3.7 or higher. If not, download from [python.org](https://www.python.org/downloads/).

## Step 2: Run the Application

### Option A: GUI (Recommended for beginners)

```bash
python gui.py
```

A window will open. Enter a password and click "Analyze Password"!

### Option B: Command Line

```bash
python cli.py
```

Follow the interactive prompts.

### Option C: Demo Script

```bash
python demo.py
```

See various password examples analyzed automatically.

## Step 3: Try It Out!

Test with these example passwords:

- **Weak**: `password123`
- **Medium**: `MyPassword2024`
- **Strong**: `P@ssw0rd2025!Secure`

## 📋 What You'll See

The tool analyzes:
- ✅ Password length
- ✅ Character diversity
- ✅ Entropy (randomness)
- ✅ Weak patterns
- ✅ Dictionary words
- ✅ Estimated cracking time
- ✅ Security recommendations

## 🎯 Example Output

```
Password: P@ssw0rd2025!

Score: 72.5/100
Category: Strong
Entropy: 82.5 bits
Cracking Time: 2.6e+15 years (GPU attack)
```

## 💡 Tips

1. **Use the GUI** for visual analysis
2. **Export reports** for documentation
3. **Try the demo** to see different scenarios
4. **Read recommendations** to improve weak passwords

## ❓ Troubleshooting

**Problem**: "Module not found" error
- **Solution**: Make sure you're in the project directory

**Problem**: GUI doesn't open
- **Solution**: Install tkinter: `sudo apt-get install python3-tk` (Linux) or it should be included with Python on Windows/Mac

**Problem**: Import errors
- **Solution**: All dependencies are built-in. Make sure you're using Python 3.7+

## 🎓 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Explore the code to understand the algorithms
- Try analyzing your own passwords (safely!)
- Export reports to see detailed analysis

---

**Ready to go!** Launch the GUI and start analyzing! 🔒

