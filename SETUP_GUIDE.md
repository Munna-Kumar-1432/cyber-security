# 🚀 Setup Guide - Password Strength Checker

## दूसरे System पर Clone करने के बाद क्या करना होगा

यह guide step-by-step बताती है कि GitHub से code clone करने के बाद कैसे setup करें।

---

## 📋 Step 1: Prerequisites Check (जरूरी चीजें)

### Python Installation Check करें

**Windows:**
```bash
python --version
```
या
```bash
python3 --version
```

**Linux/Mac:**
```bash
python3 --version
```

**अगर Python नहीं है तो:**
- Download करें: https://www.python.org/downloads/
- Python 3.7 या उससे ऊपर version install करें
- Installation के समय "Add Python to PATH" checkbox को check करें

---

## 📥 Step 2: Repository Clone करें

### GitHub से Code Download करें

**Option 1: Git Command से (अगर Git installed है)**
```bash
git clone https://github.com/Munna-Kumar-1432/cyber-security.git
cd cyber-security
```

**Option 2: Manual Download**
1. GitHub repository पर जाएं: https://github.com/Munna-Kumar-1432/cyber-security
2. "Code" button पर click करें
3. "Download ZIP" पर click करें
4. ZIP file को extract करें
5. Extracted folder में जाएं

---

## 📁 Step 3: Project Files Check करें

Clone करने के बाद आपको ये files दिखनी चाहिए:

```
cyber-security/
├── password_strength_checker.py  (Main engine)
├── gui.py                        (GUI application)
├── cli.py                        (Command-line interface)
├── demo.py                       (Demo script)
├── test_simple.py                (Test file)
├── README.md                     (Documentation)
├── QUICKSTART.md                 (Quick start)
├── SETUP_GUIDE.md                (यह file)
├── PROJECT_SUMMARY.md            (Project summary)
├── requirements.txt              (Dependencies)
└── .gitignore                    (Git ignore)
```

**अगर सभी files नहीं दिख रही हैं:**
- Terminal/Command Prompt में project folder में जाएं
- `dir` (Windows) या `ls` (Linux/Mac) command से files check करें

---

## ✅ Step 4: Dependencies Check (Optional)

**Good News:** इस project में कोई external dependencies नहीं हैं!

सभी libraries Python standard library से आती हैं:
- `re` - Regular expressions (built-in)
- `math` - Mathematical functions (built-in)
- `string` - String operations (built-in)
- `json` - JSON handling (built-in)
- `tkinter` - GUI (usually comes with Python)

**अगर tkinter नहीं है (कुछ Linux systems पर):**

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

**Fedora:**
```bash
sudo dnf install python3-tkinter
```

**Mac:**
- tkinter usually comes with Python installation

**Windows:**
- tkinter automatically included

---

## 🧪 Step 5: Test करें कि सब काम कर रहा है

### Quick Test

**Windows:**
```bash
python test_simple.py
```

**Linux/Mac:**
```bash
python3 test_simple.py
```

**Expected Output:**
```
Test successful! Score: 63.32/100, Category: Medium
```

**अगर error आए:**
- Python version check करें (3.7+ होना चाहिए)
- File path सही है या नहीं check करें
- Python command `python` या `python3` try करें

---

## 🎮 Step 6: Application Run करें

### Option A: GUI Application (सबसे आसान)

**Windows:**
```bash
python gui.py
```

**Linux/Mac:**
```bash
python3 gui.py
```

**क्या होगा:**
- एक window खुलेगी
- Password enter करें
- "Analyze Password" button click करें
- Results देखें

### Option B: Command-Line Interface

**Windows:**
```bash
python cli.py
```

**Linux/Mac:**
```bash
python3 cli.py
```

**क्या होगा:**
- Terminal में password enter करने को कहेगा
- Password hidden रहेगा (security के लिए)
- Detailed report show होगा

### Option C: Demo Script

**Windows:**
```bash
python demo.py
```

**Linux/Mac:**
```bash
python3 demo.py
```

**क्या होगा:**
- 8 different passwords automatically test होंगे
- हर password का analysis दिखेगा
- Summary statistics show होगी

---

## 🔧 Troubleshooting (समस्याएं और समाधान)

### Problem 1: "python: command not found"

**Solution:**
- `python3` try करें
- Python install करें और PATH में add करें
- Windows पर Python installer में "Add to PATH" option select करें

### Problem 2: "ModuleNotFoundError: No module named 'tkinter'"

**Solution:**
- Linux पर: `sudo apt-get install python3-tk` (Ubuntu/Debian)
- या `sudo dnf install python3-tkinter` (Fedora)
- Windows/Mac पर usually automatically included होता है

### Problem 3: GUI window नहीं खुल रही

**Solution:**
- tkinter install करें (ऊपर देखें)
- Display server check करें (Linux पर)
- Python version check करें (3.7+)

### Problem 4: Unicode characters display नहीं हो रहे

**Solution:**
- Windows Command Prompt में: `chcp 65001` run करें
- या PowerShell use करें
- Linux/Mac पर usually problem नहीं होती

### Problem 5: "Permission denied" error

**Solution:**
- File permissions check करें
- `chmod +x filename.py` (Linux/Mac)
- Administrator rights check करें

---

## 📝 Step 7: Usage Examples

### Example 1: GUI में Password Check करना

1. `python gui.py` run करें
2. Password field में password enter करें
3. "Analyze Password" click करें
4. Results देखें:
   - Score (0-100)
   - Category (Very Weak to Very Strong)
   - Cracking time estimates
   - Recommendations

### Example 2: CLI में Password Check करना

```bash
python cli.py
```

फिर:
1. Password enter करें (hidden होगा)
2. Report automatically show होगी
3. Export option मिलेगा (json/txt)

### Example 3: Programmatic Usage (Code में use करना)

```python
from password_strength_checker import PasswordStrengthChecker

# Initialize
checker = PasswordStrengthChecker()

# Analyze password
report = checker.analyze("MyPassword123!")

# Access results
print(f"Score: {report['score']}/100")
print(f"Category: {report['category']}")
print(f"Entropy: {report['entropy_bits']} bits")

# Export report
checker.export_report(report, "my_report.json", format="json")
```

---

## 🎯 Quick Commands Summary

### Windows Commands:
```bash
# Test
python test_simple.py

# Run GUI
python gui.py

# Run CLI
python cli.py

# Run Demo
python demo.py
```

### Linux/Mac Commands:
```bash
# Test
python3 test_simple.py

# Run GUI
python3 gui.py

# Run CLI
python3 cli.py

# Run Demo
python3 demo.py
```

---

## 📚 Additional Resources

### Documentation Files:
- **README.md** - Complete project documentation
- **QUICKSTART.md** - Quick start guide
- **PROJECT_SUMMARY.md** - Project overview

### Help Commands:
```bash
# Python help
python --help

# Check Python version
python --version

# List files
dir          # Windows
ls           # Linux/Mac
```

---

## ✅ Verification Checklist

Setup complete है या नहीं check करने के लिए:

- [ ] Python installed है (3.7+)
- [ ] Repository clone हो गई है
- [ ] सभी files present हैं
- [ ] `test_simple.py` successfully run हो रहा है
- [ ] GUI application (`gui.py`) खुल रही है
- [ ] CLI application (`cli.py`) काम कर रही है
- [ ] Demo script (`demo.py`) run हो रहा है

**अगर सभी checkboxes tick हैं, तो setup complete है!** ✅

---

## 🆘 अगर अभी भी Problem है

1. **Error message को carefully पढ़ें**
2. **Python version check करें**: `python --version`
3. **File path check करें**: सही folder में हैं या नहीं
4. **Dependencies check करें**: tkinter installed है या नहीं
5. **README.md file पढ़ें**: Detailed documentation
6. **GitHub Issues check करें**: अगर कोई known issue है

---

## 🎉 Success!

अगर आप यहाँ तक पहुँच गए हैं और सब कुछ काम कर रहा है, तो:

**Congratulations! 🎊**

आपका Password Strength Checker tool ready है use करने के लिए!

---

## 📞 Quick Reference

**Repository:** https://github.com/Munna-Kumar-1432/cyber-security

**Main Files:**
- `gui.py` - GUI application (सबसे आसान)
- `cli.py` - Command-line interface
- `password_strength_checker.py` - Core engine

**Test Files:**
- `test_simple.py` - Quick test
- `demo.py` - Full demonstration

---

**Happy Coding! 🔒✨**

