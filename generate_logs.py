import time
import random

LOG_FILE = "server.log"
IPS = ["192.168.1.1", "10.0.0.1", "127.0.0.1", "172.16.0.5"]
STATUSES = ["200", "404", "500", "301"]

def generate_log():
    ip = random.choice(IPS)
    date = time.strftime("%d/%b/%Y:%H:%M:%S +0000")
    status = random.choice(STATUSES)
    log_line = f'{ip} - - [{date}] "GET /index.html HTTP/1.1" {status} 1024\n'
    
    with open(LOG_FILE, "a") as f:
        f.write(log_line)
    print(f"Written: {log_line.strip()}")

if __name__ == "__main__":
    print(f"Generating logs to {LOG_FILE}...")
    try:
        while True:
            generate_log()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped generating logs.")
