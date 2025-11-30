"""
Password Strength Checker - Comprehensive Security Analysis Tool
Developed for Cybersecurity Education and Awareness
"""

import re
import math
import string
import hashlib
import json
from datetime import datetime
from collections import Counter
from typing import Dict, List, Tuple, Optional


class PasswordStrengthChecker:
    """
    Comprehensive password strength analysis engine.
    Analyzes passwords based on length, entropy, patterns, dictionary words, and more.
    """
    
    def __init__(self, dictionary_file: Optional[str] = None):
        """
        Initialize the password strength checker.
        
        Args:
            dictionary_file: Path to dictionary wordlist file (optional)
        """
        self.dictionary_file = dictionary_file
        self.dictionary_words = set()
        self.common_passwords = self._load_common_passwords()
        self.keyboard_patterns = self._load_keyboard_patterns()
        
        if dictionary_file:
            self._load_dictionary()
    
    def _load_common_passwords(self) -> set:
        """Load common weak passwords."""
        return {
            'password', '123456', '12345678', '123456789', '1234567890',
            'qwerty', 'abc123', 'password1', 'welcome', 'monkey',
            '1234567', 'letmein', 'trustno1', 'dragon', 'baseball',
            'iloveyou', 'master', 'sunshine', 'ashley', 'bailey',
            'passw0rd', 'shadow', '123123', '654321', 'superman',
            'qazwsx', 'michael', 'football', 'welcome123', 'jesus',
            'ninja', 'mustang', 'password123', 'admin', 'login'
        }
    
    def _load_keyboard_patterns(self) -> List[str]:
        """Load common keyboard patterns."""
        return [
            'qwerty', 'qwertyuiop', 'asdfgh', 'asdfghjkl', 'zxcvbn',
            '123456', '12345678', '123456789', '1234567890',
            'abcdef', 'abcdefgh', 'qwerty123', 'asdf123', 'zxcv123'
        ]
    
    def _load_dictionary(self):
        """Load dictionary words from file if provided."""
        if not self.dictionary_file:
            return
        
        try:
            with open(self.dictionary_file, 'r', encoding='utf-8', errors='ignore') as f:
                self.dictionary_words = {line.strip().lower() for line in f if line.strip()}
        except FileNotFoundError:
            print(f"Warning: Dictionary file '{self.dictionary_file}' not found.")
    
    def analyze(self, password: str) -> Dict:
        """
        Perform comprehensive password strength analysis.
        
        Args:
            password: The password to analyze
            
        Returns:
            Dictionary containing complete analysis report
        """
        if not password:
            return self._empty_report()
        
        # Core analysis
        length = len(password)
        char_analysis = self._analyze_characters(password)
        patterns = self._detect_patterns(password)
        dictionary_check = self._check_dictionary(password)
        entropy = self._calculate_entropy(password, char_analysis)
        cracking_time = self._estimate_cracking_time(entropy)
        score = self._calculate_score(length, char_analysis, patterns, dictionary_check, entropy)
        category = self._categorize_strength(score)
        
        # Generate comprehensive report
        report = {
            'password': '*' * len(password),  # Never store actual password
            'length': length,
            'entropy_bits': round(entropy, 2),
            'score': round(score, 2),
            'category': category,
            'cracking_time': cracking_time,
            'character_analysis': char_analysis,
            'patterns_detected': patterns,
            'dictionary_check': dictionary_check,
            'recommendations': self._generate_recommendations(
                length, char_analysis, patterns, dictionary_check, entropy, score
            ),
            'timestamp': datetime.now().isoformat()
        }
        
        return report
    
    def _analyze_characters(self, password: str) -> Dict:
        """Analyze character composition of password."""
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_symbol = bool(re.search(r'[^a-zA-Z0-9]', password))
        has_unicode = bool(re.search(r'[^\x00-\x7F]', password))
        
        # Count character types
        lowercase_count = len(re.findall(r'[a-z]', password))
        uppercase_count = len(re.findall(r'[A-Z]', password))
        digit_count = len(re.findall(r'\d', password))
        symbol_count = len(re.findall(r'[^a-zA-Z0-9]', password))
        
        # Calculate character set size
        char_set_size = 0
        if has_lower:
            char_set_size += 26
        if has_upper:
            char_set_size += 26
        if has_digit:
            char_set_size += 10
        if has_symbol:
            char_set_size += 33  # Common symbols
        if has_unicode:
            char_set_size += 100  # Approximate for unicode
        
        return {
            'has_lowercase': has_lower,
            'has_uppercase': has_upper,
            'has_digits': has_digit,
            'has_symbols': has_symbol,
            'has_unicode': has_unicode,
            'lowercase_count': lowercase_count,
            'uppercase_count': uppercase_count,
            'digit_count': digit_count,
            'symbol_count': symbol_count,
            'character_set_size': char_set_size,
            'diversity_score': self._calculate_diversity(has_lower, has_upper, has_digit, has_symbol, has_unicode)
        }
    
    def _calculate_diversity(self, lower: bool, upper: bool, digit: bool, symbol: bool, unicode: bool) -> float:
        """Calculate character diversity score (0-100)."""
        types = sum([lower, upper, digit, symbol, unicode])
        if types == 0:
            return 0
        elif types == 1:
            return 20
        elif types == 2:
            return 40
        elif types == 3:
            return 60
        elif types == 4:
            return 80
        else:  # 5 types
            return 100
    
    def _detect_patterns(self, password: str) -> Dict:
        """Detect common weak patterns in password."""
        patterns = {
            'sequential_digits': [],
            'sequential_letters': [],
            'repetitive_chars': [],
            'keyboard_patterns': [],
            'common_patterns': [],
            'date_patterns': []
        }
        
        password_lower = password.lower()
        
        # Sequential digits (123, 1234, etc.)
        sequential_digit = re.findall(r'\d{3,}', password)
        for seq in sequential_digit:
            if self._is_sequential(seq, True):
                patterns['sequential_digits'].append(seq)
        
        # Sequential letters (abc, abcd, etc.)
        sequential_letter = re.findall(r'[a-z]{3,}', password_lower)
        for seq in sequential_letter:
            if self._is_sequential(seq, False):
                patterns['sequential_letters'].append(seq)
        
        # Repetitive characters (aaa, 111, etc.)
        repetitive = re.findall(r'(.)\1{2,}', password)
        patterns['repetitive_chars'] = [match[0] * len(match.group()) for match in re.finditer(r'(.)\1{2,}', password)]
        
        # Keyboard patterns
        for pattern in self.keyboard_patterns:
            if pattern in password_lower:
                patterns['keyboard_patterns'].append(pattern)
        
        # Date patterns (YYYY, YYYY-MM-DD, etc.)
        date_patterns = [
            r'\d{4}',  # Year
            r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',  # Date format
        ]
        for pattern in date_patterns:
            matches = re.findall(pattern, password)
            if matches:
                patterns['date_patterns'].extend(matches)
        
        # Common weak patterns
        if re.search(r'^(.)\1+$', password):  # All same character
            patterns['common_patterns'].append('All same character')
        if password.isdigit():
            patterns['common_patterns'].append('All digits')
        if password.isalpha():
            patterns['common_patterns'].append('All letters')
        
        return patterns
    
    def _is_sequential(self, sequence: str, is_digit: bool) -> bool:
        """Check if sequence is sequential (123, abc, etc.)."""
        if len(sequence) < 3:
            return False
        
        if is_digit:
            for i in range(len(sequence) - 1):
                if int(sequence[i+1]) - int(sequence[i]) != 1:
                    return False
        else:
            for i in range(len(sequence) - 1):
                if ord(sequence[i+1]) - ord(sequence[i]) != 1:
                    return False
        
        return True
    
    def _check_dictionary(self, password: str) -> Dict:
        """Check password against dictionary words and common passwords."""
        password_lower = password.lower()
        password_reversed = password_lower[::-1]
        
        findings = {
            'is_common_password': False,
            'contains_dictionary_word': False,
            'contains_reversed_word': False,
            'contains_substituted_word': False,
            'dictionary_words_found': [],
            'substitutions_detected': []
        }
        
        # Check common passwords
        if password_lower in self.common_passwords:
            findings['is_common_password'] = True
            findings['dictionary_words_found'].append(password_lower)
        
        # Check dictionary words
        if self.dictionary_words:
            # Direct match
            if password_lower in self.dictionary_words:
                findings['contains_dictionary_word'] = True
                findings['dictionary_words_found'].append(password_lower)
            
            # Check if password contains dictionary words
            for word in self.dictionary_words:
                if len(word) >= 4 and word in password_lower:
                    findings['contains_dictionary_word'] = True
                    if word not in findings['dictionary_words_found']:
                        findings['dictionary_words_found'].append(word)
            
            # Check reversed words
            if password_reversed in self.dictionary_words:
                findings['contains_reversed_word'] = True
                findings['dictionary_words_found'].append(f"{password_reversed} (reversed)")
        
        # Check for common substitutions (p@ssw0rd, etc.)
        substitutions = {
            'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 't': '7'
        }
        substituted_word = password_lower
        for char, sub in substitutions.items():
            substituted_word = substituted_word.replace(sub, char)
        
        if substituted_word in self.dictionary_words or substituted_word in self.common_passwords:
            findings['contains_substituted_word'] = True
            findings['substitutions_detected'].append(substituted_word)
        
        return findings
    
    def _calculate_entropy(self, password: str, char_analysis: Dict) -> float:
        """
        Calculate password entropy in bits.
        Entropy = log2(R^N) = N * log2(R)
        where R = character set size, N = password length
        """
        length = len(password)
        char_set_size = char_analysis['character_set_size']
        
        if char_set_size == 0 or length == 0:
            return 0.0
        
        entropy = length * math.log2(char_set_size)
        return entropy
    
    def _estimate_cracking_time(self, entropy: float) -> Dict:
        """
        Estimate time to crack password based on entropy.
        Assumes different attack scenarios.
        """
        # Guesses per second for different scenarios
        # These are approximate values
        online_brute_force = 10  # 10 guesses/second (rate-limited)
        offline_cpu = 1e6  # 1 million guesses/second
        offline_gpu = 1e9  # 1 billion guesses/second
        cloud_cracking = 1e12  # 1 trillion guesses/second
        
        # Total possible combinations
        combinations = 2 ** entropy
        
        def format_time(seconds: float) -> str:
            """Format time in human-readable format."""
            if seconds < 1:
                return "Instant"
            elif seconds < 60:
                return f"{int(seconds)} seconds"
            elif seconds < 3600:
                return f"{int(seconds/60)} minutes"
            elif seconds < 86400:
                return f"{int(seconds/3600)} hours"
            elif seconds < 31536000:
                return f"{int(seconds/86400)} days"
            elif seconds < 3153600000:
                return f"{int(seconds/31536000)} years"
            else:
                return f"{int(seconds/31536000)} years (centuries)"
        
        return {
            'online_brute_force': format_time(combinations / online_brute_force),
            'offline_cpu': format_time(combinations / offline_cpu),
            'offline_gpu': format_time(combinations / offline_gpu),
            'cloud_cracking': format_time(combinations / cloud_cracking),
            'combinations': f"{combinations:.2e}"
        }
    
    def _calculate_score(self, length: int, char_analysis: Dict, patterns: Dict,
                        dictionary_check: Dict, entropy: float) -> float:
        """
        Calculate overall password strength score (0-100).
        Weighted scoring system:
        - 30% Entropy
        - 20% Character Diversity
        - 20% Dictionary Weakness
        - 15% Pattern Detection
        - 15% Length
        """
        # Length score (0-15 points)
        if length < 8:
            length_score = 0
        elif length < 12:
            length_score = 5
        elif length < 16:
            length_score = 10
        elif length < 20:
            length_score = 13
        else:
            length_score = 15
        
        # Entropy score (0-30 points) - normalized to 0-30
        max_entropy = 128  # Maximum practical entropy
        entropy_score = min(30, (entropy / max_entropy) * 30)
        
        # Diversity score (0-20 points)
        diversity_score = (char_analysis['diversity_score'] / 100) * 20
        
        # Dictionary weakness penalty (0-20 points, inverted)
        dict_score = 20
        if dictionary_check['is_common_password']:
            dict_score -= 15
        if dictionary_check['contains_dictionary_word']:
            dict_score -= 10
        if dictionary_check['contains_reversed_word']:
            dict_score -= 5
        if dictionary_check['contains_substituted_word']:
            dict_score -= 8
        dict_score = max(0, dict_score)
        
        # Pattern detection penalty (0-15 points, inverted)
        pattern_score = 15
        if patterns['sequential_digits']:
            pattern_score -= 5
        if patterns['sequential_letters']:
            pattern_score -= 5
        if patterns['repetitive_chars']:
            pattern_score -= 4
        if patterns['keyboard_patterns']:
            pattern_score -= 6
        if patterns['common_patterns']:
            pattern_score -= 3
        pattern_score = max(0, pattern_score)
        
        total_score = length_score + entropy_score + diversity_score + dict_score + pattern_score
        return min(100, max(0, total_score))
    
    def _categorize_strength(self, score: float) -> str:
        """Categorize password strength based on score."""
        if score < 30:
            return "Very Weak"
        elif score < 50:
            return "Weak"
        elif score < 70:
            return "Medium"
        elif score < 90:
            return "Strong"
        else:
            return "Very Strong"
    
    def _generate_recommendations(self, length: int, char_analysis: Dict,
                                 patterns: Dict, dictionary_check: Dict,
                                 entropy: float, score: float) -> List[str]:
        """Generate security recommendations based on analysis."""
        recommendations = []
        
        if length < 12:
            recommendations.append(f"Increase password length to at least 12 characters (currently {length})")
        
        if not char_analysis['has_lowercase']:
            recommendations.append("Add lowercase letters")
        if not char_analysis['has_uppercase']:
            recommendations.append("Add uppercase letters")
        if not char_analysis['has_digits']:
            recommendations.append("Add numbers")
        if not char_analysis['has_symbols']:
            recommendations.append("Add special characters (!@#$%^&*)")
        
        if dictionary_check['is_common_password']:
            recommendations.append("Avoid using common passwords - use a unique password")
        if dictionary_check['contains_dictionary_word']:
            recommendations.append("Avoid dictionary words - use random combinations")
        if dictionary_check['contains_substituted_word']:
            recommendations.append("Simple character substitutions (like @ for a) are easily detected")
        
        if patterns['sequential_digits']:
            recommendations.append("Avoid sequential numbers (123, 1234, etc.)")
        if patterns['sequential_letters']:
            recommendations.append("Avoid sequential letters (abc, abcd, etc.)")
        if patterns['repetitive_chars']:
            recommendations.append("Avoid repetitive characters (aaa, 111, etc.)")
        if patterns['keyboard_patterns']:
            recommendations.append("Avoid keyboard patterns (qwerty, asdf, etc.)")
        
        if entropy < 40:
            recommendations.append("Password has low entropy - add more randomness")
        
        if not recommendations:
            recommendations.append("Password meets most security requirements. Keep it unique and don't reuse it!")
        
        return recommendations
    
    def _empty_report(self) -> Dict:
        """Return empty report structure."""
        return {
            'password': '',
            'length': 0,
            'entropy_bits': 0.0,
            'score': 0.0,
            'category': 'Very Weak',
            'cracking_time': {},
            'character_analysis': {},
            'patterns_detected': {},
            'dictionary_check': {},
            'recommendations': ['Please enter a password to analyze'],
            'timestamp': datetime.now().isoformat()
        }
    
    def export_report(self, report: Dict, filename: str, format: str = 'json'):
        """
        Export analysis report to file.
        
        Args:
            report: The analysis report dictionary
            filename: Output filename
            format: Export format ('json', 'txt')
        """
        if format.lower() == 'json':
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
        elif format.lower() == 'txt':
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self._format_text_report(report))
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _format_text_report(self, report: Dict) -> str:
        """Format report as human-readable text."""
        lines = [
            "=" * 60,
            "PASSWORD STRENGTH ANALYSIS REPORT",
            "=" * 60,
            "",
            f"Analysis Date: {report['timestamp']}",
            f"Password Length: {report['length']} characters",
            f"Entropy: {report['entropy_bits']} bits",
            f"Strength Score: {report['score']}/100",
            f"Category: {report['category']}",
            "",
            "CRACKING TIME ESTIMATES:",
            f"  Online Brute-Force: {report['cracking_time'].get('online_brute_force', 'N/A')}",
            f"  Offline CPU: {report['cracking_time'].get('offline_cpu', 'N/A')}",
            f"  Offline GPU: {report['cracking_time'].get('offline_gpu', 'N/A')}",
            f"  Cloud Cracking: {report['cracking_time'].get('cloud_cracking', 'N/A')}",
            "",
            "CHARACTER ANALYSIS:",
        ]
        
        if 'character_analysis' in report:
            ca = report['character_analysis']
            lines.extend([
                f"  Lowercase: {ca.get('has_lowercase', False)} ({ca.get('lowercase_count', 0)} chars)",
                f"  Uppercase: {ca.get('has_uppercase', False)} ({ca.get('uppercase_count', 0)} chars)",
                f"  Digits: {ca.get('has_digits', False)} ({ca.get('digit_count', 0)} chars)",
                f"  Symbols: {ca.get('has_symbols', False)} ({ca.get('symbol_count', 0)} chars)",
                f"  Character Set Size: {ca.get('character_set_size', 0)}",
            ])
        
        lines.append("")
        lines.append("PATTERNS DETECTED:")
        if 'patterns_detected' in report:
            patterns = report['patterns_detected']
            if any(patterns.values()):
                for pattern_type, pattern_list in patterns.items():
                    if pattern_list:
                        lines.append(f"  {pattern_type.replace('_', ' ').title()}: {', '.join(pattern_list)}")
            else:
                lines.append("  No weak patterns detected")
        
        lines.append("")
        lines.append("DICTIONARY CHECK:")
        if 'dictionary_check' in report:
            dc = report['dictionary_check']
            if dc.get('is_common_password'):
                lines.append("  ⚠️  Common password detected!")
            if dc.get('contains_dictionary_word'):
                lines.append(f"  ⚠️  Dictionary words found: {', '.join(dc.get('dictionary_words_found', []))}")
            if dc.get('contains_substituted_word'):
                lines.append("  ⚠️  Character substitution detected")
            if not any([dc.get('is_common_password'), dc.get('contains_dictionary_word'),
                       dc.get('contains_substituted_word')]):
                lines.append("  ✓ No dictionary words detected")
        
        lines.append("")
        lines.append("RECOMMENDATIONS:")
        for rec in report.get('recommendations', []):
            lines.append(f"  • {rec}")
        
        lines.append("")
        lines.append("=" * 60)
        
        return "\n".join(lines)


if __name__ == "__main__":
    # Example usage
    checker = PasswordStrengthChecker()
    
    test_passwords = [
        "password123",
        "P@ssw0rd2025!",
        "Tr0ub4dor&3",
        "MyP@ssw0rd!",
        "aB3$kL9mN2pQ7rT5"
    ]
    
    print("Password Strength Checker - Test Run\n")
    print("=" * 60)
    
    for pwd in test_passwords:
        report = checker.analyze(pwd)
        print(f"\nPassword: {pwd}")
        print(f"Score: {report['score']}/100")
        print(f"Category: {report['category']}")
        print(f"Entropy: {report['entropy_bits']} bits")
        print("-" * 60)

