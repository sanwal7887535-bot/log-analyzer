import random
import json
from datetime import datetime, timedelta

endpoints = [
    "/api/users",
    "/api/login",
    "/api/orders",
    "/api/products",
    "/api/cart",
]

methods = ["GET", "POST", "PUT", "DELETE"]
status_codes = [200, 201, 400, 401, 403, 404, 500]

timestamp_formats = [
    "iso",      # 2024-03-15T14:23:01Z
    "slash",    # 2024/03/15 14:23:01
    "dash",     # 15-Mar-2024 14:23:01
    "epoch"     # 1710512581
]


def random_timestamp(base_time):
    fmt = random.choice(timestamp_formats)

    if fmt == "iso":
        return base_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    elif fmt == "slash":
        return base_time.strftime("%Y/%m/%d %H:%M:%S")

    elif fmt == "dash":
        return base_time.strftime("%d-%b-%Y %H:%M:%S")

    else:
        return str(int(base_time.timestamp()))


def random_response_time():
    choice = random.choice(["ms", "s", "raw"])

    if choice == "ms":
        return f"{random.randint(20, 500)}ms"
    elif choice == "s":
        return f"{round(random.uniform(0.05, 1.5), 3)}s"
    else:
        return str(random.randint(20, 500))


def generate_line(base_time):
    chance = random.random()

    # 10% malformed line
    if chance < 0.1:
        return "MALFORMED_LOG_LINE_CORRUPTED_DATA"

    # 10% JSON format log
    if chance < 0.2:
        return json.dumps({
            "time": random_timestamp(base_time),
            "ip": f"192.168.1.{random.randint(1,255)}",
            "method": random.choice(methods),
            "endpoint": random.choice(endpoints),
            "status": random.choice(status_codes),
            "response": random_response_time()
        })

    # normal log
    return f"{random_timestamp(base_time)} {random.choice(['192.168.1.1','10.0.0.7','172.16.0.5'])} " \
           f"{random.choice(methods)} {random.choice(endpoints)} " \
           f"{random.choice(status_codes)} {random_response_time()}"


def generate_logs(file_name="sample_logs/generated.log", lines=500):
    base_time = datetime.now()

    with open(file_name, "w") as f:
        for i in range(lines):
            base_time += timedelta(seconds=random.randint(1, 10))
            f.write(generate_line(base_time) + "\n")

    print(f"Generated {lines} log lines in {file_name}")


if __name__ == "__main__":
    generate_logs()