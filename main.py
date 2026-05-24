import sys

from analyzer.parser import parse_file
from analyzer.analyzer import (
    analyze_logs,
    calculate_error_rate,
    export_report,
    export_csv
)

from analyzer.visualizer import (
    plot_top_endpoints,
    plot_status_codes
)

from colorama import Fore, Style, init

init()


def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file_path>")
        return

    file_path = sys.argv[1]

    logs, errors = parse_file(file_path)

    stats = analyze_logs(logs)

    print(Fore.CYAN + "\n===== LOG ANALYSIS REPORT =====\n" + Style.RESET_ALL)

    print(Fore.GREEN + f"Total Requests: {stats['total_requests']}")
    print(Fore.RED + f"Error Requests: {stats['error_requests']}")
    print(
        Fore.YELLOW
        + f"Error Rate: {calculate_error_rate(stats['total_requests'], stats['error_requests'])}%"
    )

    print("\nTop Endpoints:")
    for ep, count in stats["endpoint_count"].items():
        print(ep, "->", count)

    print("\nTop IPs:")
    for ip, count in stats["ip_count"].items():
        print(ip, "->", count)

    print("\nParsing Errors:")
    for k, v in errors.items():
        print(k, "->", v)

    # JSON Export
    report_file = export_report(stats)
    print(Fore.CYAN + f"\nJSON report saved to: {report_file}")

    # CSV Export
    export_csv(stats)
    print(Fore.CYAN + "CSV report saved: report.csv")

    # Charts
    plot_top_endpoints(stats["endpoint_count"])
    plot_status_codes(stats["status_count"])


if __name__ == "__main__":
    main()