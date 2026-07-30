import sys

sys.stdout.reconfigure(encoding='utf-8')

class BugTracker:
    def __init__(self):
        self.bugs = [
            {"id": "BUG-101", "title": "JWT Token Expiration NullPointer", "sev": "CRITICAL", "status": "OPEN"},
            {"id": "BUG-102", "title": "Mobile Viewport Navbar Offset", "sev": "MAJOR", "status": "IN_REVIEW"}
        ]

    def print_summary(self):
        print("==================================================")
        print("🐞 Software Testing Task 05: Bug Tracking System")
        print("==================================================")
        print("📋 Active Defect Triage Status:\n")
        for b in self.bugs:
            print(f"   • [{b['id']}] {b['title']:<35} | Severity: {b['sev']:<8} | Status: {b['status']}")

if __name__ == "__main__":
    bt = BugTracker()
    bt.print_summary()
