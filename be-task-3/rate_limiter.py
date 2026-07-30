import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

class TokenBucketRateLimiter:
    def __init__(self, capacity=5, refill_rate=1):
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill = time.time()
        self.refill_rate = refill_rate

    def allow_request(self):
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now
        
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

if __name__ == "__main__":
    print("==================================================")
    print("🛡️ Backend Web Task 03: API Rate Limiter & Security")
    print("==================================================")
    limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1)
    
    for i in range(1, 8):
        allowed = limiter.allow_request()
        status = "HTTP 200 OK" if allowed else "HTTP 429 Too Many Requests"
        print(f"Request #{i}: {status}")
