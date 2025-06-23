import socket

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # 1 second timeout
            try:
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"Port {port}: Open")
                else:
                    print(f"Port {port}: Closed")
            except Exception as e:
                print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    # Basic test scanning localhost ports 20 to 30
    scan_ports('127.0.0.1', 20,30)



      