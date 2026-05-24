from analyzer.parser import parse_file
from analyzer.analyzer import (
    analyze_logs,
    get_top_endpoints,
    get_top_ips,
    get_slowest_endpoints,
    calculate_error_rate
)


def main():
    file_path = "sample_logs/generated.log"

    logs, errors = parse_file(file_path)
    stats = analyze_logs(logs)

    print("\n===== LOG ANALYSIS REPORT =====\n")

    print(f"Total Requests: {stats['total_requests']}")
    print(f"Error Requests: {stats['error_requests']}")
    print(f"Error Rate: {calculate_error_rate(stats['total_requests'], stats['error_requests'])}%")

    print("\nTop Endpoints:")
    for ep, count in get_top_endpoints(stats["endpoint_count"]):
        print(ep, "->", count)

    print("\nTop IPs:")
    for ip, count in get_top_ips(stats["ip_count"]):
        print(ip, "->", count)

    print("\nSlowest Endpoints:")
    for ep, avg in get_slowest_endpoints(stats["response_times"]):
        print(ep, "->", round(avg, 2), "ms")

    print("\nParsing Errors:")
    for k, v in errors.items():
        print(k, "->", v)


if __name__ == "__main__":
    main()