import json
import os

class ContactManager:
    def __init__(self, filename="data/contacts.json"):
        self.filename = filename
        self.contacts = {}
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.contacts = json.load(f)
        else:
            self.contacts = {
                "Nalina H M": {"phone": "+91 9876543210", "email": "nalina@example.com"},
                "Prodigy Support": {"phone": "+1 800-555-0199", "email": "support@prodigyinfotech.dev"}
            }

    def add_contact(self, name, phone, email):
        self.contacts[name] = {"phone": phone, "email": email}
        print(f"✅ Contact '{name}' added successfully.")

    def list_contacts(self):
        print("\n📇 CONTACT LIST:")
        for name, info in self.contacts.items():
            print(f"   • {name}: {info['phone']} | {info['email']}")

if __name__ == "__main__":
    cm = ContactManager()
    cm.add_contact("Alex Johnson", "+1 555-0142", "alex@example.com")
    cm.list_contacts()
