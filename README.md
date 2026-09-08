# Python Network Port Scanner

A multithreaded TCP port scanner built with Python to demonstrate practical networking, cybersecurity, and Python programming concepts.

The scanner identifies open TCP ports on a target system, associates common ports with their typical services, and can export scan results to a text report.

> **Ethical Use:** This tool is intended for educational purposes and authorized security testing only. Only scan systems that you own or have explicit permission to test.

---

## Features

- TCP port scanning using Python sockets
- Custom port-range scanning
- Multithreaded scanning for improved performance
- Hostname-to-IP address resolution
- Common service identification
- Command-line interface
- Configurable thread count
- Input validation
- Scan duration tracking
- Text report exporting
- Formatted terminal output
- Error handling

---

## Technologies Used

- Python 3
- Python `socket` module
- `argparse`
- `concurrent.futures`
- TCP/IP networking
- Git
- GitHub

No external Python packages are required.

---

## Project Structure

```text
python-port-scanner/
├── scanner.py
├── README.md
├── scan_results.txt
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/jgyampoh/python-port-scanner.git
```

Enter the project directory:

```bash
cd python-port-scanner
```

Verify Python is installed:

```bash
python3 --version
```

---

## Usage

Display the help menu:

```bash
python3 scanner.py --help
```

### Basic Scan

```bash
python3 scanner.py 127.0.0.1
```

### Custom Port Range

```bash
python3 scanner.py 127.0.0.1 -p 1-1000
```

### Configure Threads

```bash
python3 scanner.py 127.0.0.1 -p 1-10000 -t 150
```

### Export Results

```bash
python3 scanner.py 127.0.0.1 -p 1-1000 -o scan_results.txt
```

Options can also be combined:

```bash
python3 scanner.py 127.0.0.1 -p 1-10000 -t 150 -o scan_results.txt
```

---

## Example Output

The following output was generated during local testing:

```text
=============================================
       PYTHON NETWORK PORT SCANNER
=============================================
Target:     127.0.0.1
IP Address: 127.0.0.1
Port Range: 1-10000
Threads:    150

Scanning...

PORT      STATE       SERVICE
--------------------------------
5000      OPEN        Unknown
7000      OPEN        Unknown
7768      OPEN        Unknown

--------------------------------
Open ports found: 3
Scan completed in 0.63 seconds.
Report saved to: scan_results.txt
```

Actual results depend on the services running on the target system.

---

## How It Works

The scanner uses TCP sockets to attempt connections to ports within a user-defined range.

Python's `socket.connect_ex()` method attempts a TCP connection to each port. If the connection succeeds, the port is reported as open.

`ThreadPoolExecutor` allows multiple ports to be tested concurrently, significantly reducing scan time compared with scanning ports sequentially.

```text
Target
   |
   v
Hostname Resolution
   |
   v
Port Range Validation
   |
   v
Multithreaded TCP Scan
   |
   v
Open Port Detection
   |
   v
Service Identification
   |
   +----> Terminal Output
   |
   +----> Text Report
```

---

## Cybersecurity Concepts Demonstrated

### TCP/IP Networking

TCP ports allow applications and services to communicate across networks. Identifying reachable ports helps analysts understand a system's network exposure.

### Network Reconnaissance

Port scanning can be used during authorized security assessments to identify exposed services and better understand a system's attack surface.

### Socket Programming

Python sockets provide the interface used by the scanner to perform TCP connection attempts.

### Multithreading

Worker threads allow multiple ports to be scanned concurrently, improving performance across larger port ranges.

### Service Identification

The scanner maps known port numbers to common services such as SSH, HTTP, HTTPS, SMB, and RDP.

Service names are based on common port assignments and do not represent full service or version fingerprinting.

---

## Input Validation

The scanner validates:

- Port numbers between 1 and 65535
- Correct port-range formatting
- Starting port cannot exceed ending port
- Thread counts between 1 and 500
- Hostname/IP resolution

---

## Limitations

This project is an educational TCP scanner and is not intended to replace professional network-scanning tools.

Current limitations include:

- TCP scanning only
- No UDP scanning
- No operating-system detection
- No service-version fingerprinting
- Service names are inferred from common port assignments
- Results can be affected by firewalls, filtering, latency, and network conditions

---

## Testing

Development and testing were performed against the local loopback interface:

```text
127.0.0.1
```

A temporary HTTP server can be created for local testing:

```bash
python3 -m http.server 8000
```

Then the scanner can check the surrounding ports:

```bash
python3 scanner.py 127.0.0.1 -p 7995-8005
```

While the temporary HTTP server is running, port `8000` should be detected as open.

---

## Future Improvements

Potential future enhancements include:

- CSV and JSON report formats
- Improved service identification
- Automated testing
- Logging
- Additional exception handling
- Modular code organization

---

## Ethical Use

This project was created for cybersecurity education and authorized security testing.

Do not use this tool to scan networks, systems, or devices without authorization.

---

## Author

**James Gyampoh**

Cybersecurity & Networking Graduate

GitHub: `jgyampoh`