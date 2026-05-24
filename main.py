from colorama import Fore, Style, init
init()
import sys
from analyzer.visualizer import plot_top_endpoints, plot_status_codes
from analyzer.analyzer import export_csv
from analyzer.analyzer import export_report
from analyzer.parser import parse_file
from analyzer.analyzer import (
    analyze_logs,
    get_top_endpoints,
    get_top_ips,
    get_slowest_endpoints,
    calculate_error_rate
)

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
    print(Fore.YELLOW + f"Error Rate: {calculate_error_rate(stats['total_requests'], stats['error_requests'])}%")
    report_file = export_report(stats)
    print(Fore.CYAN + f"\nJSON report saved to: {report_file}")
    csv_file = export_csv(stats)
    print(Fore.CYAN + f"CSV report saved to: {csv_file}")


    export_csv(stats)
    print("CSV report saved: report.csv")

    plot_top_endpoints(stats["endpoint_count"])
    plot_status_codes(stats["status_count"])

if __name__ == "__main__":
    main()

plot_top_endpoints(stats["endpoint_count"])
plot_status_codes(stats["status_count"])