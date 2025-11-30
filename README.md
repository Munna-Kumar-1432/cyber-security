# 🔒 Password Strength Checker

A comprehensive, professional-grade password strength analysis tool developed for cybersecurity education and awareness. This tool provides detailed security analysis of passwords based on industry-standard metrics including entropy calculation, pattern detection, dictionary checking, and cracking time estimation.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Security Considerations](#security-considerations)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)

## ✨ Features

### Core Analysis Features

- **Length Analysis**: Evaluates password length against security recommendations (minimum 12 characters)
- **Character Diversity Check**: Analyzes use of lowercase, uppercase, digits, symbols, and unicode characters
- **Pattern Detection**: Identifies weak patterns including:
  - Sequential digits (123, 1234, etc.)
  - Sequential letters (abc, abcd, etc.)
  - Repetitive characters (aaa, 111, etc.)
  - Keyboard patterns (qwerty, asdf, etc.)
  - Date patterns (YYYY, MM/DD/YYYY, etc.)
- **Dictionary Word Detection**: Checks against common passwords and dictionary words
- **Entropy Calculation**: Calculates password entropy in bits using the formula: `Entropy = N * log2(R)`
- **Cracking Time Estimation**: Estimates time to crack under different attack scenarios:
  - Online brute-force attacks
  - Offline CPU attacks
  - Offline GPU attacks
  - Cloud-based cracking

### Scoring System

The tool uses a weighted scoring algorithm (0-100 points):

- **30%** - Entropy (randomness)
- **20%** - Character Diversity
- **20%** - Dictionary Weakness Detection
- **15%** - Pattern Detection
- **15%** - Length

**Strength Categories:**
- 0-30: Very Weak
- 30-50: Weak
- 50-70: Medium
- 70-90: Strong
- 90-100: Very Strong

### User Interface

- **Modern GUI**: Built with tkinter, featuring:
  - Real-time password analysis
  - Visual progress bar with color coding
  - Tabbed interface for detailed results
  - Password visibility toggle
  - Export functionality (JSON, Text)

- **Command-Line Interface**: For scripted usage and automation

### Report Generation

- Detailed analysis reports in multiple formats:
  - JSON (machine-readable)
  - Text (human-readable)
- Comprehensive recommendations for password improvement

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- tkinter (usually included with Python)

### Setup

1. **Clone or download this repository**

```bash
cd "Cyber Security"
```

2. **Verify Python installation**

```bash
python --version
```

3. **Run the application**

**GUI Version:**
```bash
python gui.py
```

**Command-Line Version:**
```bash
python cli.py
```

**Direct Module Usage:**
```bash
python password_strength_checker.py
```

## 💻 Usage

### GUI Application

1. Launch the GUI:
   ```bash
   python gui.py
   ```

2. Enter a password in the input field
3. Click "Analyze Password" or the analysis will run automatically
4. View results in the tabbed interface:
   - **Overview**: Summary and key metrics
   - **Detailed Analysis**: Patterns, dictionary checks, entropy
   - **Recommendations**: Security improvement suggestions
5. Export reports using the export buttons

### Command-Line Usage

```bash
python cli.py
```

Follow the interactive prompts to analyze passwords.

### Programmatic Usage

```python
from password_strength_checker import PasswordStrengthChecker

# Initialize checker
checker = PasswordStrengthChecker()

# Analyze password
report = checker.analyze("YourPassword123!")

# Access results
print(f"Score: {report['score']}/100")
print(f"Category: {report['category']}")
print(f"Entropy: {report['entropy_bits']} bits")

# Export report
checker.export_report(report, "report.json", format="json")
```

## 📁 Project Structure

```
Cyber Security/
│
├── password_strength_checker.py  # Core analysis engine
├── gui.py                         # GUI application
├── cli.py                         # Command-line interface
├── requirements.txt               # Dependencies (optional)
├── README.md                      # This file
│
└── reports/                       # Generated reports (created automatically)
```

## 🔬 Technical Details

### Entropy Calculation

Password entropy measures the amount of randomness in a password:

```
Entropy (bits) = N × log₂(R)

Where:
  N = Password length
  R = Character set size
```

**Character Set Sizes:**
- Lowercase letters: 26
- Uppercase letters: 26
- Digits: 10
- Common symbols: 33
- Unicode: ~100 (approximate)

### Pattern Detection Algorithms

1. **Sequential Detection**: Checks for consecutive characters (123, abc)
2. **Repetition Detection**: Uses regex to find repeated characters (aaa, 111)
3. **Keyboard Pattern Matching**: Compares against known keyboard patterns
4. **Dictionary Matching**: String matching against wordlists

### Cracking Time Estimation

Based on entropy, estimates time for different attack scenarios:

- **Online Brute-Force**: 10 guesses/second (rate-limited)
- **Offline CPU**: 1 million guesses/second
- **Offline GPU**: 1 billion guesses/second
- **Cloud Cracking**: 1 trillion guesses/second

## 🔐 Security Considerations

### Privacy & Security

✅ **Implemented:**
- Passwords are never stored or logged
- No network transmission of passwords
- All analysis performed locally
- Reports mask actual passwords

⚠️ **Best Practices:**
- Use this tool only on trusted systems
- Don't analyze passwords on shared/public computers
- Clear clipboard after copying passwords
- Use HTTPS if deploying as web service

### Dictionary Files (Optional)

To enhance dictionary checking, you can add wordlist files:

1. Download wordlists (e.g., RockYou.txt, SecLists)
2. Place in project directory
3. Initialize checker with dictionary file:
   ```python
   checker = PasswordStrengthChecker(dictionary_file="rockyou.txt")
   ```

**Note**: Dictionary files are optional. The tool includes a built-in list of common weak passwords.

## 📊 Example Output

```
Password: P@ssw0rd2025!

Length: 14 characters
Entropy: 82.5 bits
Score: 72.5/100
Category: Strong

Cracking Time Estimates:
  Online Brute-Force: 2.6e+24 years
  Offline CPU: 2.6e+18 years
  Offline GPU: 2.6e+15 years
  Cloud Cracking: 2.6e+12 years

Character Analysis:
  ✓ Lowercase: 7
  ✓ Uppercase: 1
  ✓ Digits: 4
  ✓ Symbols: 2

Patterns Detected:
  ⚠️ Dictionary word: "password" (substituted)
  ⚠️ Sequential digits: "2025"

Recommendations:
  • Avoid dictionary words
  • Add more randomness
```

## 🎓 Educational Value

This project demonstrates:

- **Cryptography Basics**: Entropy, hashing concepts
- **Security Analysis**: Pattern recognition, weakness detection
- **Algorithm Design**: Scoring systems, weighted calculations
- **Software Engineering**: Modular design, clean code practices
- **User Interface Design**: GUI development, UX principles

## 🔮 Future Enhancements

Potential improvements:

- [ ] Integration with HaveIBeenPwned API
- [ ] Support for multiple wordlist formats
- [ ] Web-based interface (Flask/Django)
- [ ] Password generation suggestions
- [ ] Batch password analysis
- [ ] PDF report generation
- [ ] Multi-language support
- [ ] Advanced pattern recognition using ML

## 📝 License

This project is developed for educational purposes. Feel free to use, modify, and distribute.

## 👨‍💻 Development

### Testing

Test the tool with various password examples:

```python
test_passwords = [
    "password123",      # Weak
    "P@ssw0rd2025!",    # Medium-Strong
    "Tr0ub4dor&3",       # Medium
    "aB3$kL9mN2pQ7rT5"  # Strong
]
```

### Contributing

Contributions welcome! Areas for improvement:
- Additional pattern detection algorithms
- Performance optimization
- UI/UX enhancements
- Documentation improvements

## 📚 References

- OWASP Password Storage Cheat Sheet
- NIST Password Guidelines
- Password Entropy Theory
- Common Password Lists (RockYou, SecLists)

## 🙏 Acknowledgments

Developed for cybersecurity education and awareness. This tool helps users understand password security and make informed decisions about their digital security practices.

---

**⚠️ Disclaimer**: This tool is for educational and awareness purposes. Always follow your organization's password policies and security guidelines.

**🔒 Remember**: The best password is one you don't know - use a password manager!

