
# Log Analyzer Tool

A Python-based log analysis tool that processes server logs, handles malformed entries, and generates useful operational insights like error rates, slow endpoints, and traffic distribution.

---

## 🚀 Features

- Parses multiple log formats (ISO, slash, dash, epoch)
- Handles malformed and corrupted lines safely
- Supports JSON log entries
- Computes:
  - Total requests
  - Error rate
  - Top endpoints
  - Top IPs
  - Slowest endpoints
  - Status code distribution
- Never crashes on bad data


---
## ⚙️ Setup & Run
1. Install Python

    Make sure Python 3.10+ is installed.

2. Generate Logs

python scripts/generate_logs.py

3. Run Analyzer

4. python main.py

5. python scripts/generate_logs.py

6. python main.py sample_logs/generated.log

7. python main.py path/to/logfile.log
 
---

## 📁 Project Structure
log-analyzer/
│
├── analyzer/
│   ├── parser.py
│   ├── analyzer.py
│   ├── utils.py
│   └── models.py
│
├── scripts/
│   └── generate_logs.py
│
├── sample_logs/
│   └── generated.log
│
├── main.py
├── README.md
├── ANSWERS.md
├── requirements.txt

---

## 📊 Sample Output
Total Requests: 500
Error Requests: 32
Error Rate: 6.4%

Top Endpoints:
 /api/users -> 120
 /api/login -> 90

Slowest Endpoints:
 /api/orders -> 245.3 ms
---

## 🔥 Notes

- Built to handle real-world messy log data
- Designed with scalability and error tolerance in mind
- Focused on production-like log processing behavior

