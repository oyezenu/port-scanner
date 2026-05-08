import socket
import datetime

print("=" * 40)
print("  python port scanner")
print("=" * 40)

target = input("Enter the target IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
start_time = datetime.datetime.now()

print(f"\nScan started at: {start_time}\n")

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open")

    sock.close()
end_time = datetime.datetime.now()
print(f"\nScan completed at: {end_time}")
print(f"Total time: {end_time - start_time}")