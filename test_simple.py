"""Simple test to verify password checker works"""
from password_strength_checker import PasswordStrengthChecker

checker = PasswordStrengthChecker()
result = checker.analyze("Test123!")
print(f"Test successful! Score: {result['score']}/100, Category: {result['category']}")

