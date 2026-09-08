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


def scan_port(target, port):
    """Attempt a TCP connection to a single port."""

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


target_input = input("Enter a target IP address or hostname: ")

try:
    target = socket.gethostbyname(target_input)
except socket.gaierror:
    print("Error: Unable to resolve target.")
    exit()

try:
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
except ValueError:
    print("Error: Ports must be numbers.")
    exit()

if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
    print("Error: Ports must be between 1 and 65535.")
    exit()

if start_port > end_port:
    print("Error: Starting port cannot be greater than ending port.")
    exit()


print("\n" + "=" * 45)
print("       PYTHON NETWORK PORT SCANNER")
print("=" * 45)

print(f"Target:     {target_input}")
print(f"IP Address: {target}")
print(f"Port Range: {start_port}-{end_port}")

print("\nScanning...\n")

start_time = time.time()

open_ports = []

# Scan multiple ports concurrently.
with ThreadPoolExecutor(max_workers=100) as executor:

    futures = {
        executor.submit(scan_port, target, port): port
        for port in range(start_port, end_port + 1)
    }

    for future in as_completed(futures):
        result = future.result()

        if result is not None:
            open_ports.append(result)


# Sort results because threads may finish in any order.
open_ports.sort()

print(f"{'PORT':<10}{'STATE':<12}{'SERVICE'}")
print("-" * 32)

for port, service in open_ports:
    print(f"{port:<10}{'OPEN':<12}{service}")


end_time = time.time()
scan_duration = end_time - start_time

print("\n" + "-" * 32)
print(f"Open ports found: {len(open_ports)}")
print(f"Scan completed in {scan_duration:.2f} seconds.")