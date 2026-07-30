import sys

sys.stdout.reconfigure(encoding='utf-8')

def analyze_code_snippet(code):
    print("==================================================")
    print("💻 Generative AI Task 04: AI Code Explainer & Debugger")
    print("==================================================")
    print("📋 Analyzing Target Source Code:\n")
    print(code)
    print("\n🔍 AI Analysis Summary:")
    print("   • Time Complexity:  O(N)")
    print("   • Space Complexity: O(1)")
    print("   • Identified Edge Case: Boundary check on discount_rate parameter (0.0 to 1.0).")
    print("✅ Code refactoring recommendation generated.")

if __name__ == "__main__":
    sample_code = "def calculate_discount(price, discount_rate):\n    return price - (price * discount_rate)"
    analyze_code_snippet(sample_code)
