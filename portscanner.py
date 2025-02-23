import socket
import threading
import queue
import sys

def scan_port(target, port, q):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            q.put(port)
        s.close()
    except socket.error:
        pass

def scan_ports(target, ports):
    q = queue.Queue()
    threads = []

    for port in ports:
        thread = threading.Thread(target=scan_port, args=(target, port, q))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    open_ports = []
    while not q.empty():
        open_ports.append(q.get())

    return open_ports

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 port_scanner.py <target_ip> <start_port-end_port>")
        sys.exit(1)

    target = sys.argv[1]
    port_range = sys.argv[2].split('-')
    start_port = int(port_range[0])
    end_port = int(port_range[1])

    ports = range(start_port, end_port + 1)

    print(f"Scanning {target} from port {start_port} to {end_port}...")

    open_ports = scan_ports(target, ports)

    if open_ports:
        print(f"Open ports on {target}: {open_ports}")
    else:
        print(f"No open ports found on {target}.")

if __name__ == "__main__":
    main()
