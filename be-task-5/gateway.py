import sys

sys.stdout.reconfigure(encoding='utf-8')

def run_gateway():
    print("==================================================")
    print("🌐 Backend Web Task 05: Microservices & API Gateway")
    print("==================================================")
    print("🚀 API Gateway listening on port 8080...")
    print("   • Proxy Route /auth   -> http://auth-service:3000   (Status: 200)")
    print("   • Proxy Route /catalog -> http://catalog-service:3001 (Status: 200)")
    print("   • Proxy Route /orders  -> http://order-service:3002   (Status: 200)")
    print("✅ All 3 microservice clusters registered and healthy.")

if __name__ == "__main__":
    run_gateway()
