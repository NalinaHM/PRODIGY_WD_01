import queue
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def worker():
    q = queue.Queue()
    print("==================================================")
    print("⏳ Backend Web Task 04: Background Job Queue")
    print("==================================================")
    print("🚀 Worker thread started. Listening on Redis queue...")

    jobs = ["send_welcome_email", "generate_pdf_report", "process_payment_webhook"]
    for j in jobs:
        q.put(j)
        print(f"   [Enqueued] Job '{j}' added to queue.")

    while not q.empty():
        job = q.get()
        print(f"⚡ [Processing] Executing background task '{job}'...")
        time.sleep(0.2)
        print(f"✅ [Completed] Task '{job}' finished successfully.")

if __name__ == "__main__":
    worker()
