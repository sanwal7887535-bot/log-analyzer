# Log Analyzer Tool

A Python-based log analysis tool that processes messy real-world server logs and generates operational insights such as error rates, traffic distribution, slow endpoints, and parsing anomaly reports.

This project is designed to be fault-tolerant and production-inspired. It safely handles malformed lines, mixed log formats, inconsistent timestamps, JSON logs, missing fields, and corrupted entries without crashing.

---

# 🚀 Features

- Parses multiple timestamp formats
- Handles malformed and corrupted log lines safely
- Supports mixed log formats
- Supports JSON-formatted log entries
- Parses multiple response time formats
- Processes large files line-by-line for memory efficiency
- Generates operational insights and reports
- Exports reports to JSON and CSV
- Visualizes metrics using charts
- CLI-based usage
- Never crashes on malformed input

---

# 📂 Supported Log Variations

The analyzer supports logs such as:

```text
2024-03-15T14:23:01Z 192.168.1.42 GET /api/users 200 142ms
2024/03/15 14:23:01 10.0.0.7 POST /api/login 401 0.142s
15-Mar-2024 14:23:01 192.168.1.1 GET /home 200 142
1710512581 192.168.1.10 DELETE /api/user/1 500 88ms
```

It also safely handles:

- Blank lines
- Corrupted lines
- Partial writes
- Invalid JSON
- Missing status codes
- Extra appended fields
- Mixed formatting styles

---

# 📊 Generated Insights

The tool generates:

- Total requests
- Error requests
- Error rate
- Top endpoints
- Top IP addresses
- Status code distribution
- Parsing anomaly statistics
- JSON report export
- CSV report export
- Visualization charts

---

# 🏗️ Project Structure

```text
log-analyzer/
│
├── analyzer/
│   ├── analyzer.py
│   ├── parser.py
│   ├── visualizer.py
│   ├── models.py
│   └── utils.py
│
├── scripts/
│   └── generate_logs.py
│
├── sample_logs/
│   └── generated.log
│
├── tests/
│   └── test_parser.py
│
├── main.py
├── README.md
├── ANSWERS.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/sanwal7887535-bot/log-analyzer.git
```

## 2. Navigate Into Project

```bash
cd log-analyzer
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows PowerShell

```bash
venv\Scripts\activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧪 Generate Sample Logs

Generate a representative log file with malformed lines and mixed formats:

```bash
python scripts/generate_logs.py
```

This creates:

```text
sample_logs/generated.log
```

---

# ▶️ Run the Analyzer

Analyze generated logs:

```bash
python main.py sample_logs/generated.log
```

Or analyze any custom log file:

```bash
python main.py path/to/logfile.log
```

---

# 📄 Output Files

The analyzer generates:

## JSON Report

```text
report.json
```

## CSV Report

```text
report.csv
```

---

# 📈 Visualization

The analyzer also displays:

- Top endpoints chart
- Status code distribution chart

using matplotlib.

---

# 🧠 Design Goals

This project was designed with:

- fault tolerance
- scalability
- defensive programming
- real-world log unpredictability
- modular architecture

in mind.

The system intentionally prioritizes graceful degradation over strict parsing assumptions.

---

# 🛡️ Error Handling Strategy

Malformed or unexpected log entries never crash the system.

Instead, logs are categorized into error types such as:

- EMPTY_LINE
- MALFORMED_LINE
- MALFORMED_JSON
- ERROR

and included in parsing statistics.

---

# ⚡ Performance Considerations

- Files are processed line-by-line
- UTF-8 decoding errors are ignored safely
- Parsing logic avoids loading unnecessary data into memory
- Suitable for large log files

---

# 🧪 Running Tests

Run parser tests:

```bash
python -m pytest
```

---

# 🔥 Example CLI Output

```text
===== LOG ANALYSIS REPORT =====

Total Requests: 448
Error Requests: 183
Error Rate: 40.85%

Top Endpoints:
/api/users -> 42
/api/login -> 31

Top IPs:
192.168.1.1 -> 19
10.0.0.7 -> 17

JSON report saved to: report.json
CSV report saved: report.csv
```

---

# 📚 Technologies Used

- Python 3
- matplotlib
- colorama
- pytest

---

# 👨‍💻 Author

Muhammad Sanwal

---

# 📜 License

This project is for technical assessment and educational purposes.