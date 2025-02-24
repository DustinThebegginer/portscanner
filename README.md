## 🚀 Usage

Run the script with the following syntax:

```bash
python portscanner.py <target_ip> <start_port-end_port>
```

### ✅ Example:
```bash
python portscanner.py 192.168.1.1 20-100
```
This scans ports **20 to 100** on `192.168.1.1`.

### 📌 Expected Output:
```bash
Scanning 192.168.1.1 from port 20 to 100...
Open ports on 192.168.1.1: [22, 80, 443]
```
If no open ports are found:
```bash
No open ports found on 192.168.1.1.
```

---

## ⚙️ How It Works
1. The script takes **target IP** and **port range** as input.
2. It creates **multiple threads** to speed up scanning.
3. It attempts to establish a **socket connection** to each port.
4. If the connection succeeds, the port is **open** and displayed.

---

## 🛠️ Customization
You can modify the **timeout duration** for faster/slower scanning:
```python
socket.setdefaulttimeout(1)  # Adjust timeout (1 second default)
```
Increase timeout for **more accuracy** or decrease for **faster scanning**.

---

## 🔒 Disclaimer
This tool is intended for **educational and ethical hacking** purposes **only**.  
Do **not** use it on networks without **explicit permission**. Unauthorized scanning is **illegal** in many countries. Use responsibly.

---

## 🤝 Contributing
Feel free to fork the repository and submit a pull request if you want to enhance the tool.

---

## 📜 License
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.
