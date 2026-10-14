# 🛰️ tcp-reflector

A lightweight, interactive TCP proxy written in Python. It allows you to forward traffic from any local interface and port to a remote target, making it ideal for debugging, traffic interception, or service spoofing in red team operations.

## 🚀 Features

- Fully interactive: specify listening interface, local port, and target IP/port at runtime.
- Supports any TCP-based protocol (HTTP, NATS, Redis, FTP, etc).
- Minimal dependencies (only uses Python standard libraries).
- Real-time data logging.
- Simple to extend for custom data manipulation or MITM operations.

## 🛠️ Requirements

- Python 3.8+
- No external dependencies

## 📦 Usage

```bash
python3 tcp-reflector.py
```

You will be prompted for:

- Local interface to bind to (e.g., 0.0.0.0)
- Local port (e.g., 4222)
- Target IP (e.g., 192.168.1.100)
- Target port (e.g., 4222)

Example session:

```yaml
🖥️  Listen interface (e.g. 0.0.0.0): 0.0.0.0
🔌 Listen port: 4222
🎯 Target IP: 192.168.1.100
📡 Target port: 4222
[+] Listening on 0.0.0.0:4222 -> Forwarding to 192.168.1.100:4222
```

All TCP data is printed to the console in real time.

## 🔐 Disclaimer

This tool is intended for educational and ethical testing purposes only. Do not use it on systems you don't own or have permission to test.

## 📂 License

MIT License
