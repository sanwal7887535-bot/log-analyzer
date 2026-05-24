# ANSWERS.md

## 1. How to run

### Clone the repository

```bash
git clone https://github.com/sanwal7887535-bot/log-analyzer.git
```

### Navigate into project

```bash
cd log-analyzer
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

#### Windows PowerShell

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Generate sample logs

```bash
python scripts/generate_logs.py
```

### Run the analyzer

```bash
python main.py sample_logs/generated.log
```

You can also analyze any custom log file:

```bash
python main.py path/to/logfile.log
```

---

# 2. Stack choice

I selected Python for this task because it is highly effective for text processing, parsing, data aggregation, and rapid prototyping.

Python's standard libraries such as `json`, `datetime`, `collections`, and file handling utilities made it suitable for handling inconsistent and malformed log data efficiently.

I also used:
- `matplotlib` for visualization
- `colorama` for improved CLI readability
- `pytest` for testing

A worse choice for this task would have been a frontend-heavy framework or a low-level systems language because the project primarily focuses on data parsing, resilience, and file processing rather than UI rendering or low-level optimization.

---

# 3. One real edge case

One important edge case handled correctly is malformed or incomplete log lines.

Example:

```text
INVALID LOG ENTRY
```

This is handled safely inside:

```text
analyzer/parser.py
```

Specifically in the section:

```python
if len(parts) < 5:
    return None, "MALFORMED_LINE"
```

Without this validation, the parser would attempt to access missing fields and crash with an index error.

Instead, the system classifies the line as malformed and continues processing the remaining logs safely.

---

# 4. AI usage

AI tools used:
- ChatGPT

AI was used for:
- architecture brainstorming
- improving README structure
- refining parser organization
- generating ideas for edge-case handling
- improving CLI formatting
- improving visualization ideas

One example where I modified AI-generated output:

The initial parser structure mixed file-reading logic inside line-parsing logic. I reorganized the implementation so that:
- `parse_line()` only parses a single line
- `parse_file()` handles file streaming separately

This improved separation of concerns, readability, and maintainability.

I also adjusted parsing logic and error handling behavior manually during debugging and testing.

---

# 5. Honest gap

One area that is not fully production-ready is scalability for extremely large log files processed in parallel.

Currently, the system processes logs efficiently line-by-line, but with another day I would improve:
- parallel processing
- asynchronous file handling
- real-time streaming support
- more advanced anomaly detection
- dashboard-based visualization

I would also add:
- Docker support
- CI/CD automation
- additional unit and integration tests
- benchmark testing for very large datasets