# Python Network Port Scanner

A lightweight command-line port scanner built in Python. Designed to identify open ports on a target host, label common services, and report scan timing — core functionality used in real-world network reconnaissance and security assessments.

---

## Features

- Scans a user-defined port range on any target IP address
- Detects and labels common services (HTTP, HTTPS, SSH, FTP, MySQL, etc.)
- Displays scan start time, end time, and total duration
- Optional closed port output for full scan visibility
- Graceful handling of unrecognized ports

---

## Technologies

- Python 3.x
- `socket` — native network connection library
- `datetime` — scan timing and timestamps

---

## Usage

**1. Clone the repository**
```bash
git clone https://github.com/oyezenu/port-scanner.git
cd port-scanner
```

**2. Run the scanner**
```bash
python scanner.py
```

**3. Follow the prompts**
```
========================================
   Python Port Scanner
========================================
Enter target IP address: 127.0.0.1
Enter start port: 8070
Enter end port: 8090
Show closed ports? (y/n): n
```

---

## Example Output

```
Scan started at: 2026-05-08 12:03:20

Scanning 127.0.0.1 from port 8070 to 8090...

Port 8080 --> OPEN (HTTP-Alt)

Scan completed at: 2026-05-08 12:03:40
Total time: 0:00:20.222593
```

---

## Concepts Demonstrated

- TCP socket programming
- Network port enumeration
- Service fingerprinting via port mapping
- Input sanitization and error handling
- Scan performance tuning via configurable timeouts

---

## Disclaimer

This tool is intended for educational purposes and authorized testing only. Do not scan networks or systems without explicit permission.

---

## Author

**Anthony Gonzalez**  
Cybersecurity Student  
[GitHub](https://github.com/oyezenu) • [LinkedIn](https://www.linkedin.com/in/anthony-gonzalez-1701a2285)
