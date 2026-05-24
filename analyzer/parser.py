import json
from datetime import datetime


# ---------------------------
# TIMESTAMP PARSER
# ---------------------------
def parse_timestamp(raw):
    try:
        if not raw:
            return None

        if "T" in raw:
            return datetime.strptime(raw, "%Y-%m-%dT%H:%M:%SZ")

        elif "/" in raw:
            return datetime.strptime(raw, "%Y/%m/%d %H:%M:%S")

        elif "-" in raw and len(raw.split("-")[0]) == 2:
            return datetime.strptime(raw, "%d-%b-%Y %H:%M:%S")

        elif raw.isdigit():
            return datetime.fromtimestamp(int(raw))

    except:
        return None

    return None


# ---------------------------
# RESPONSE TIME PARSER
# ---------------------------
def parse_response_time(value):
    try:
        if not value:
            return None

        if value.endswith("ms"):
            return float(value.replace("ms", ""))

        elif value.endswith("s"):
            return float(value.replace("s", "")) * 1000

        else:
            return float(value)

    except:
        return None


# ---------------------------
# PARSE SINGLE LINE
# ---------------------------
def parse_line(line):
    line = line.strip()

    # empty line
    if not line:
        return None, "EMPTY_LINE"

    # JSON log
    if line.startswith("{"):
        try:
            data = json.loads(line)
            return {
                "timestamp": parse_timestamp(str(data.get("time", ""))),
                "ip": data.get("ip"),
                "method": data.get("method"),
                "endpoint": data.get("endpoint"),
                "status": data.get("status"),
                "response_time": parse_response_time(str(data.get("response")))
            }, "OK_JSON"
        except:
            return None, "MALFORMED_JSON"

    # normal log
    parts = line.split()

    if len(parts) < 5:
        return None, "MALFORMED_LINE"

    try:
        return {
            "timestamp": parse_timestamp(parts[0]),
            "ip": parts[1],
            "method": parts[2],
            "endpoint": parts[3],
            "status": parts[4],
            "response_time": parse_response_time(parts[5]) if len(parts) > 5 else None
        }, "OK"

    except:
        return None, "ERROR"


# ---------------------------
# FILE PARSER (OPTIMIZED VERSION)
# ---------------------------
def parse_file(file_path):
    parsed = []
    errors = {
        "EMPTY_LINE": 0,
        "MALFORMED_LINE": 0,
        "MALFORMED_JSON": 0,
        "ERROR": 0
    }

    # ✅ optimized streaming read (safe for large files)
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            result, status = parse_line(line)

            if status in ("OK", "OK_JSON"):
                parsed.append(result)
            else:
                errors[status] = errors.get(status, 0) + 1

    return parsed, errors