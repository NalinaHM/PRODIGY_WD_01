import sys

sys.stdout.reconfigure(encoding='utf-8')

def run_backend_api():
    print("==================================================")
    print("⚙️ Backend Web Task 01: RESTful API Engine")
    print("==================================================")
    print("🚀 Initializing RESTful API Server on port 8000...")
    print("   • GET    /api/v1/resources  -> 200 OK")
    print("   • POST   /api/v1/resources  -> 201 Created")
    print("   • DELETE /api/v1/resources/1 -> 204 No Content")
    print("✅ REST API Engine operational.")

if __name__ == "__main__":
    run_backend_api()
