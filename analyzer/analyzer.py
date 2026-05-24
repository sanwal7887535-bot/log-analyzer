from collections import defaultdict, Counter


def analyze_logs(parsed_logs):
    stats = {
        "total_requests": 0,
        "error_requests": 0,
        "endpoint_count": defaultdict(int),
        "ip_count": defaultdict(int),
        "status_count": defaultdict(int),
        "response_times": defaultdict(list),
    }

    for log in parsed_logs:
        stats["total_requests"] += 1

        endpoint = log.get("endpoint")
        ip = log.get("ip")
        status = str(log.get("status"))

        # count endpoints
        if endpoint:
            stats["endpoint_count"][endpoint] += 1

        # count IPs
        if ip:
            stats["ip_count"][ip] += 1

        # status distribution
        if status:
            stats["status_count"][status] += 1

        # error tracking
        if status.startswith("4") or status.startswith("5"):
            stats["error_requests"] += 1

        # response times
        if log.get("response_time") is not None:
            stats["response_times"][endpoint].append(log["response_time"])

    return stats


def get_top_endpoints(endpoint_count, top_n=10):
    return sorted(endpoint_count.items(), key=lambda x: x[1], reverse=True)[:top_n]


def get_top_ips(ip_count, top_n=10):
    return sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:top_n]


def get_slowest_endpoints(response_times, top_n=10):
    avg_times = []

    for endpoint, times in response_times.items():
        if times:
            avg = sum(times) / len(times)
            avg_times.append((endpoint, avg))

    return sorted(avg_times, key=lambda x: x[1], reverse=True)[:top_n]


def calculate_error_rate(total, errors):
    if total == 0:
        return 0
    return round((errors / total) * 100, 2)