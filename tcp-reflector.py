import socket
from threading import Thread

def relay(src, dst):
    try:
        while data := src.recv(4096):
            print(data.decode(errors='ignore'))
            dst.sendall(data)
    except:
        pass
    finally:
        src.close(); dst.close()

def handle(client, target):
    try:
        server = socket.create_connection(target)
    except Exception as e:
        print(f"[!] Failed to connect to target {target}: {e}")
        client.close()
        return
    Thread(target=relay, args=(client, server), daemon=True).start()
    Thread(target=relay, args=(server, client), daemon=True).start()

def main():
    listen_host = input("🖥️  Listen interface (e.g. 0.0.0.0): ").strip()
    listen_port = int(input("🔌 Listen port: ").strip())
    target_host = input("🎯 Target IP: ").strip()
    target_port = int(input("📡 Target port: ").strip())

    with socket.socket() as s:
        try:
            s.bind((listen_host, listen_port))
            s.listen()
            print(f"[+] Listening on {listen_host}:{listen_port} -> Forwarding to {target_host}:{target_port}")
        except Exception as e:
            print(f"[!] Error binding to {listen_host}:{listen_port}: {e}")
            return

        while True:
            client, addr = s.accept()
            print(f"[+] Connection from {addr[0]}:{addr[1]}")
            Thread(target=handle, args=(client, (target_host, target_port)), daemon=True).start()

if __name__ == "__main__":
    main()
