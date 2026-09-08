import socket

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

target = input("Enter a target IP address: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

print(f"{'PORT':<10}{'STATE':<12}{'SERVICE'}")
print("-" * 32)

for port in range(start_port, end_port + 1):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    result = scanner.connect_ex((target, port))

    if result == 0:
        service = COMMON_SERVICES.get(port, "Unknown")
        print(f"{port:<10}{'OPEN':<12}{service}")

    scanner.close()