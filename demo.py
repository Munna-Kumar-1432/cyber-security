"""
Password Strength Checker - Demo Script
Demonstrates various password analysis scenarios
"""

from password_strength_checker import PasswordStrengthChecker


def print_separator():
    """Print visual separator."""
    print("\n" + "=" * 80 + "\n")


def demo():
    """Run demonstration of password strength checker."""
    try:
        print("""
    ╔══════════════════════════════════════════════════════════════════════╗
    ║     🔒 PASSWORD STRENGTH CHECKER - DEMONSTRATION                    ║
    ║     Testing Various Password Scenarios                              ║
    ╚══════════════════════════════════════════════════════════════════════╝
    """)
    except UnicodeEncodeError:
        print("""
    ========================================================================
    PASSWORD STRENGTH CHECKER - DEMONSTRATION
    Testing Various Password Scenarios
    ========================================================================
    """)
    
    # Initialize checker
    checker = PasswordStrengthChecker()
    
    # Test passwords with different strength levels
    test_cases = [
        {
            "name": "Very Weak - Common Password",
            "password": "password123",
            "description": "Common password with simple numeric suffix"
        },
        {
            "name": "Weak - Dictionary Word",
            "password": "welcome2024",
            "description": "Dictionary word with year"
        },
        {
            "name": "Medium - Substituted Word",
            "password": "P@ssw0rd!",
            "description": "Common password with character substitutions"
        },
        {
            "name": "Medium-Strong - Mixed Case",
            "password": "MySecurePass2025",
            "description": "Mixed case with numbers but no symbols"
        },
        {
            "name": "Strong - Complex Password",
            "password": "P@ssw0rd2025!Secure",
            "description": "Complex password with all character types"
        },
        {
            "name": "Very Strong - Random",
            "password": "aB3$kL9mN2pQ7rT5vW8xY1",
            "description": "Random characters with high entropy"
        },
        {
            "name": "Very Weak - Sequential",
            "password": "123456789",
            "description": "Sequential numbers"
        },
        {
            "name": "Weak - Keyboard Pattern",
            "password": "qwerty123",
            "description": "Keyboard pattern with numbers"
        }
    ]
    
    print(f"Testing {len(test_cases)} different password scenarios...\n")
    
    results = []
    
    for i, test_case in enumerate(test_cases, 1):
        print_separator()
        print(f"TEST CASE {i}/{len(test_cases)}: {test_case['name']}")
        print(f"Password: {test_case['password']}")
        print(f"Description: {test_case['description']}")
        print("-" * 80)
        
        # Analyze
        report = checker.analyze(test_case['password'])
        results.append(report)
        
        # Display key metrics
        print(f"\n📊 RESULTS:")
        print(f"  Length:        {report['length']} characters")
        print(f"  Entropy:       {report['entropy_bits']} bits")
        print(f"  Score:         {report['score']:.2f}/100")
        print(f"  Category:      {report['category']}")
        print(f"  Cracking Time: {report['cracking_time']['offline_gpu']}")
        
        # Character analysis
        ca = report['character_analysis']
        print(f"\n🔤 CHARACTER COMPOSITION:")
        try:
            check_mark = '✓'
            cross_mark = '✗'
        except:
            check_mark = '[OK]'
            cross_mark = '[X]'
        print(f"  Lowercase: {check_mark if ca['has_lowercase'] else cross_mark} ({ca['lowercase_count']})")
        print(f"  Uppercase: {check_mark if ca['has_uppercase'] else cross_mark} ({ca['uppercase_count']})")
        print(f"  Digits:    {check_mark if ca['has_digits'] else cross_mark} ({ca['digit_count']})")
        print(f"  Symbols:   {check_mark if ca['has_symbols'] else cross_mark} ({ca['symbol_count']})")
        
        # Patterns
        patterns = report['patterns_detected']
        has_patterns = any(patterns.values())
        if has_patterns:
            print(f"\n⚠️  WEAK PATTERNS DETECTED:")
            for pattern_type, pattern_list in patterns.items():
                if pattern_list:
                    print(f"  • {pattern_type.replace('_', ' ').title()}: {', '.join(pattern_list[:3])}")
        else:
            try:
                print(f"\n✓ No weak patterns detected")
            except:
                print(f"\n[OK] No weak patterns detected")
        
        # Dictionary check
        dc = report['dictionary_check']
        if dc['is_common_password'] or dc['contains_dictionary_word']:
            print(f"\n⚠️  DICTIONARY CHECK:")
            if dc['is_common_password']:
                print(f"  • Common password detected")
            if dc['contains_dictionary_word']:
                print(f"  • Dictionary words: {', '.join(dc['dictionary_words_found'][:3])}")
        
        # Top recommendation
        if report['recommendations']:
            print(f"\n💡 TOP RECOMMENDATION:")
            print(f"  • {report['recommendations'][0]}")
    
    # Summary
    print_separator()
    print("📈 SUMMARY STATISTICS")
    print("-" * 80)
    
    categories = {}
    for report in results:
        cat = report['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\nPassword Distribution by Category:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat:15} : {count} password(s)")
    
    avg_score = sum(r['score'] for r in results) / len(results)
    avg_entropy = sum(r['entropy_bits'] for r in results) / len(results)
    
    print(f"\nAverage Score:   {avg_score:.2f}/100")
    print(f"Average Entropy: {avg_entropy:.2f} bits")
    
    print_separator()
    try:
        print("✅ Demonstration complete!")
        print("\n💡 Key Takeaways:")
    except:
        print("[SUCCESS] Demonstration complete!")
        print("\nKey Takeaways:")
    print("  • Longer passwords with diverse character sets = stronger")
    print("  • Avoid dictionary words and common patterns")
    print("  • Random combinations are more secure than predictable patterns")
    print("  • Aim for entropy > 60 bits for strong passwords")
    print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    demo()

