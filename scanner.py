import socket
import datetime

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
}

print("=" * 40)
print("  python port scanner")
print("=" * 40)

target = input("Enter the target IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
start_time = datetime.datetime.now()
show_closed = input("Show closed ports? (y/n): ").lower()

print(f"\nScan started at: {start_time}\n")

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))

    if result == 0:
        service = common_ports.get(port, "Unknown")
        print(f"Port {port} --> OPEN ({service})")
    else:
        if show_closed == "y":
            print(f"Port {port} --> closed")

    sock.close()
end_time = datetime.datetime.now()
print(f"\nScan completed at: {end_time}")
print(f"Total time: {end_time - start_time}")