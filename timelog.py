import time
import re
from collections import Counter

#Simulated log pattern: IP - - [Date] "Request" Status Size
LOG_PATTERN = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] ".*?" (?P<status>\d+) \d+'

def monitor_log(filename):
    print(f"--- Monitoring {filename} in real time ---")
    #Use 'with' for safe file handling
    with open(filename, "r") as f:
        #Move to the end of the file
        f.seek(0, 2)

        status_counts = Counter()
        
        try:
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)   #Sleep briefly to save CPU 
                    continue

                match = re.search(LOG_PATTERN, line)
                if match:
                    status = match.group("status")
                    status_counts[status] += 1

                #Print alert if we see a 500 Server Error
                if status == "500":
                    print(f"ALERT: 500 Server Error detected at {match.group('ip')}!")

                #Periodically show stats
                if sum(status_counts.values()) % 10 == 0:
                    print(f"Current Stats: {dict(status_counts)}")


        except KeyboardInterrupt:
            print("\nMonitoring Stopped.")


#To test this, create a 'server.log' file and manually add lines to it.
if __name__ == "__main__":
    monitor_log("server.log")
                