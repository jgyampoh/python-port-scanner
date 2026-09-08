import argparse
import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8000: "HTTP-ALT"
}


def parse_port_range(port_range):
    try:
        start_port, end_port = map(int, port_range.split("-"))
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Port range must use the format START-END, for example 1-1000."
        )

    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
        raise argparse.ArgumentTypeError(
            "Ports must be between 1 and 65535."
        )

    if start_port > end_port:
        raise argparse.ArgumentTypeError(
            "Starting port cannot be greater than ending port."
        )

    return start_port, end_port


def scan_port(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    try:
        result = scanner.connect_ex((target, port))

        if result == 0:
            service = COMMON_SERVICES.get(port, "Unknown")
            return port, service

    finally:
        scanner.close()

    return None


def main():
    parser = argparse.ArgumentParser(
        description="Multithreaded Python TCP port scanner."
    )

    parser.add_argument(
        "target",
        help="Target IP address or hostname"
    )

    parser.add_argument(
        "-p",
        "--ports",
        type=parse_port_range,
        default=(1, 1024),
        help="Port range to scan, for example 1-1000"
    )

    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=100,
        help="Number of worker threads (default: 100)"
    )

    args = parser.parse_args()

    if args.threads < 1 or args.threads > 500:
        parser.error("Threads must be between 1 and 500.")

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print("Error: Unable to resolve target.")
        return

    start_port, end_port = args.ports

    print("\n" + "=" * 45)
    print("       PYTHON NETWORK PORT SCANNER")
    print("=" * 45)

    print(f"Target:     {args.target}")
    print(f"IP Address: {target_ip}")
    print(f"Port Range: {start_port}-{end_port}")
    print(f"Threads:    {args.threads}")

    print("\nScanning...\n")

    start_time = time.time()
    open_ports = []

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {
            executor.submit(scan_port, target_ip, port): port
            for port in range(start_port, end_port + 1)
        }

        for future in as_completed(futures):
            result = future.result()

            if result is not None:
                open_ports.append(result)

    open_ports.sort()

    print(f"{'PORT':<10}{'STATE':<12}{'SERVICE'}")
    print("-" * 32)

    for port, service in open_ports:
        print(f"{port:<10}{'OPEN':<12}{service}")

    scan_duration = time.time() - start_time

    print("\n" + "-" * 32)
    print(f"Open ports found: {len(open_ports)}")
    print(f"Scan completed in {scan_duration:.2f} seconds.")


if __name__ == "__main__":
    main()