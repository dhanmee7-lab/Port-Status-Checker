import socket

def check_port(host, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))

        if result == 0:
            return "Open"
        return "Closed"

    except socket.gaierror:
        return "Invalid host"
    except socket.timeout:
        return "Filtered / Timeout"
    except OSError as error:
        return f"Error: {error}"

def main():
    host = input("Enter target hostname or IP: ").strip()

    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        if not (1 <= start_port <= end_port <= 65535):
            print("Enter a valid port range from 1 to 65535.")
            return
    except ValueError:
        print("Ports must be numbers.")
        return

    print(f"\nPort scan results for {host}")
    print("-" * 40)
    print(f"{'PORT':<10}STATUS")
    print("-" * 40)

    for port in range(start_port, end_port + 1):
        status = check_port(host, port)
        print(f"{port:<10}{status}")

if __name__ == "__main__":
    main()