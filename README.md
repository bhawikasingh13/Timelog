# Timelog Monitor

A simple Python script to monitor log files in real-time, detecting traffic and flagging server errors.

## Usage

1. **Start the monitor:**
   ```bash
   python3 timelog.py
   ```
   This will start watching `server.log`.

2. **Generate test traffic (optional):**
   In a separate terminal, run:
   ```bash
   python3 generate_logs.py
   ```

## Features
- Real-time log monitoring
- 500 Server Error alerts
- Periodic status statistics
