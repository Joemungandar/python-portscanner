import socket

def scan_port(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=1):
            print(f"[+] Port {port} is open on {ip}")
    except:
        pass
