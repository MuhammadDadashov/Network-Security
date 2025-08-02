import socket
from datetime import datetime

def scan_ports(target, ports):
    print(f"\n[+] Target: {target}")
    print(f"[+] Scan started at: {datetime.now()}\n")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open")
            sock.close()
        except Exception as e:
            print(f"[!] Error: {e}")

    print(f"\n[+] Scan finished at: {datetime.now()}")

if __name__ == "__main__":
    target_ip = input("Enter target IP or domain: ")
    port_list = list(range(1, 65536))  # Now scanning all ports
    scan_ports(target_ip, port_list)
