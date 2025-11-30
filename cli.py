"""
Password Strength Checker - Command Line Interface
Interactive CLI for password analysis
"""

import sys
from password_strength_checker import PasswordStrengthChecker
import getpass


def print_banner():
    """Print application banner."""
    try:
        banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║     🔒 PASSWORD STRENGTH CHECKER - CLI VERSION            ║
    ║     Comprehensive Security Analysis Tool                  ║
    ╚═══════════════════════════════════════════════════════════╝
    """
        print(banner)
    except UnicodeEncodeError:
        banner = """
    ===================================================================
    PASSWORD STRENGTH CHECKER - CLI VERSION
    Comprehensive Security Analysis Tool
    ===================================================================
    """
        print(banner)


def print_report(report):
    """Print formatted analysis report."""
    print("\n" + "=" * 70)
    print("PASSWORD STRENGTH ANALYSIS REPORT")
    print("=" * 70)
    
    # Basic Info
    print(f"\n📊 BASIC INFORMATION")
    print("-" * 70)
    print(f"Password Length:     {report['length']} characters")
    print(f"Entropy:             {report['entropy_bits']} bits")
    print(f"Strength Score:       {report['score']:.2f}/100")
    print(f"Category:            {report['category']}")
    
    # Cracking Time
    print(f"\n⏱️  CRACKING TIME ESTIMATES")
    print("-" * 70)
    ct = report['cracking_time']
    print(f"Online Brute-Force:  {ct.get('online_brute_force', 'N/A')}")
    print(f"Offline CPU Attack:  {ct.get('offline_cpu', 'N/A')}")
    print(f"Offline GPU Attack:  {ct.get('offline_gpu', 'N/A')}")
    print(f"Cloud Cracking:      {ct.get('cloud_cracking', 'N/A')}")
    print(f"Possible Combinations: {ct.get('combinations', 'N/A')}")
    
    # Character Analysis
    print(f"\n🔤 CHARACTER ANALYSIS")
    print("-" * 70)
    ca = report['character_analysis']
    try:
        check = '✓'
        cross = '✗'
    except:
        check = '[OK]'
        cross = '[X]'
    print(f"Lowercase letters:   {ca.get('lowercase_count', 0)} ({check if ca.get('has_lowercase') else cross})")
    print(f"Uppercase letters:   {ca.get('uppercase_count', 0)} ({check if ca.get('has_uppercase') else cross})")
    print(f"Digits:              {ca.get('digit_count', 0)} ({check if ca.get('has_digits') else cross})")
    print(f"Special symbols:     {ca.get('symbol_count', 0)} ({check if ca.get('has_symbols') else cross})")
    print(f"Unicode characters:  {check if ca.get('has_unicode') else cross}")
    print(f"Character Set Size:  {ca.get('character_set_size', 0)}")
    print(f"Diversity Score:     {ca.get('diversity_score', 0)}/100")
    
    # Patterns
    print(f"\n🔍 PATTERNS DETECTED")
    print("-" * 70)
    patterns = report['patterns_detected']
    pattern_found = False
    
    if patterns.get('sequential_digits'):
        pattern_found = True
        print(f"⚠️  Sequential Digits: {', '.join(patterns['sequential_digits'])}")
    
    if patterns.get('sequential_letters'):
        pattern_found = True
        print(f"⚠️  Sequential Letters: {', '.join(patterns['sequential_letters'])}")
    
    if patterns.get('repetitive_chars'):
        pattern_found = True
        print(f"⚠️  Repetitive Characters: {', '.join(patterns['repetitive_chars'])}")
    
    if patterns.get('keyboard_patterns'):
        pattern_found = True
        print(f"⚠️  Keyboard Patterns: {', '.join(patterns['keyboard_patterns'])}")
    
    if patterns.get('date_patterns'):
        pattern_found = True
        print(f"⚠️  Date Patterns: {', '.join(patterns['date_patterns'])}")
    
    if patterns.get('common_patterns'):
        pattern_found = True
        print(f"⚠️  Common Patterns: {', '.join(patterns['common_patterns'])}")
    
    if not pattern_found:
        try:
            print("✓ No weak patterns detected")
        except:
            print("[OK] No weak patterns detected")
    
    # Dictionary Check
    print(f"\n📚 DICTIONARY CHECK")
    print("-" * 70)
    dc = report['dictionary_check']
    if dc.get('is_common_password'):
        print("⚠️  WARNING: This is a common password!")
    if dc.get('contains_dictionary_word'):
        words = dc.get('dictionary_words_found', [])
        print(f"⚠️  Dictionary words found: {', '.join(words)}")
    if dc.get('contains_reversed_word'):
        print("⚠️  Reversed dictionary word detected")
    if dc.get('contains_substituted_word'):
        print("⚠️  Character substitution detected (e.g., @ for a)")
    if not any([dc.get('is_common_password'), dc.get('contains_dictionary_word'),
               dc.get('contains_substituted_word')]):
        try:
            print("✓ No dictionary words detected")
        except:
            print("[OK] No dictionary words detected")
    
    # Recommendations
    print(f"\n💡 RECOMMENDATIONS")
    print("-" * 70)
    recommendations = report.get('recommendations', [])
    if recommendations:
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
    else:
        print("No specific recommendations. Password appears strong!")
    
    print("\n" + "=" * 70)
    print(f"Analysis completed at: {report['timestamp']}")
    print("=" * 70 + "\n")


def main():
    """Main CLI function."""
    print_banner()
    
    # Initialize checker
    checker = PasswordStrengthChecker()
    
    print("Enter passwords to analyze. Type 'quit' or 'exit' to stop.\n")
    
    while True:
        try:
            # Get password input
            print("─" * 70)
            password = getpass.getpass("Enter password (hidden): ")
            
            if password.lower() in ['quit', 'exit', 'q']:
                try:
                    print("\n👋 Goodbye! Stay secure!")
                except:
                    print("\nGoodbye! Stay secure!")
                break
            
            if not password:
                print("⚠️  Please enter a password.\n")
                continue
            
            # Analyze
            print("\n🔍 Analyzing password...")
            report = checker.analyze(password)
            
            # Print report
            print_report(report)
            
            # Ask for export
            export = input("Export report? (json/txt/n): ").lower()
            if export in ['json', 'txt']:
                filename = input(f"Enter filename (without extension): ")
                if filename:
                    try:
                        checker.export_report(report, f"{filename}.{export}", export)
                        print(f"✓ Report exported to {filename}.{export}\n")
                    except Exception as e:
                        print(f"✗ Error exporting: {e}\n")
            
            # Continue?
            continue_choice = input("Analyze another password? (y/n): ").lower()
            if continue_choice not in ['y', 'yes']:
                try:
                    print("\n👋 Goodbye! Stay secure!")
                except:
                    print("\nGoodbye! Stay secure!")
                break
            print()
            
        except KeyboardInterrupt:
            try:
                print("\n\n👋 Interrupted. Goodbye!")
            except:
                print("\n\nInterrupted. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\n✗ Error: {e}\n")
            continue


if __name__ == "__main__":
    main()

