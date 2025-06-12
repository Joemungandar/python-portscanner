import socket

def scan_port(ip: str, port: int):
    try:
        with socket.create_connection((ip, port), timeout=1):
            print(f"[+] Port {port} is open on {ip}")
    except (socket.timeout, ConnectionRefusedError):
        print(f"[-] Port {port} is closed")
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")
        

if __name__ == "__main__":
    target_ip = "scanme.nmap.org"  # Zum Testen erlaubt
    for port in range(20, 1025):  # Nur Ports 20–1024
        scan_port(target_ip, port)