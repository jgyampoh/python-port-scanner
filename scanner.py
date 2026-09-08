import socket

target = input("Enter a target IP address: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    scanner.close()