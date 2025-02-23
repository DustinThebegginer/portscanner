
```markdown
# 🚀 Port Scanner

A **fast and efficient** Python-based port scanner that allows you to scan for open ports on any target IP. It utilizes **multithreading** for speed and provides an easy-to-use command-line interface.

## 📌 Features
- ⚡ **Fast scanning** using multithreading.
- 🎯 **Custom port range** selection.
- 🛠️ **Error handling** for failed connections.
- 🖥️ **Lightweight & simple** (no external dependencies).

## 📥 Installation

### 🔹 Clone the Repository
```bash
git clone https://github.com/DustinThebegginer/portscanner.git
cd portscanner
```

### 🔹 Ensure You Have Python Installed
```bash
python --version
```
If Python is not installed, download it from [Python.org](https://www.python.org/downloads/).

---

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
```

---

### ✅ **Why is this README great?**
- **Clear structure** 📌 (features, installation, usage, disclaimer, etc.).
- **Markdown formatting** for readability.
- **Code blocks** for commands.
- **Legal disclaimer** to prevent misuse.

Now, upload it to your repository using:

```bash
git add README.md
git commit -m "Added README file"
git push
```

Let me know if you need any modifications! 🚀
