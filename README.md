```markdown
# NmapTool

Do you always forget specific nmap commands like commands to get the service version? Install NmapTool! It's a tool made in python that is designed for those who like me forget nmap commands. It groups together a lot of very useful commands in a lot of different situations.
## Requirements

- Python 3.x
- `scapy` library for network discovery

## Installation

Follow the steps below to set up and run the NmapTool:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SkyzzTech/NmapTool.git
   ```

2. **Navigate to the project folder:**

   ```bash
   cd NmapTool
   ```

3. **Install the required dependencies:**

   You will need to install the `scapy` library for the tool to function properly. Use the following command to install it:

   ```bash
   pip install scapy
   ```

4. **Run the NmapTool script:**

   ```bash
   python NmapTool.py
   ```

## Features

NmapTool provides the following scan options:

| Option | Description |
|--------|-------------|
| **Basic Scan** | Scans open ports on the target IP. |
| **Service and Version Scan** | Detects services and their versions running on open ports. |
| **Bypass Firewall Scan** | Attempts to bypass firewalls and scan the target. |
| **Best Nmap Scan** | A comprehensive scan that performs service detection and OS fingerprinting. |
| **Discover Local Network** | Scans the local network and lists all active devices along with their IP and MAC addresses. |

## Usage

After running the script, you will be presented with a menu:

```bash
[D] Discover Local IP on Network
[1] Basic Scan (Very fast)
[2] Service and Version Scan (Fast)
[3] Bypass Firewall Scan (Very fast)
[4] Best Nmap Scan (Long)
[H] Help
```

### Options:
print("[1] Basic Scan:               - Scans open ports without version detection                                                                       Command: nmap 'ip'.
- [2] Service and Version Scan:      - Identifies open ports and detects services running on them.                                                      Command: nmap -sV 'ip'.
- [3] Bypass Firewall Scan:          - Uses stealth techniques to evade firewalls.                                                                      Command: nmap --disable-arp-ping --source-port 53 -sS -Pn -n 'ip'.
- [4] Best Nmap Scan:                - Comprehensive scan with service detection and OS fingerprinting                                                  Command: nmap -A -p- -v 'ip'.")
- [5] Mask IP Scan:                  - Mix your IP address with others to confuse the target machine (your IP is still displayed but mixed with others) Command: nmap -sS -Pn -D RND,RND,ME 'ip'.
- [6] Very Fast Scanner              - Uses The Bests Options To Scan Most Faster (much more likely to get spotted)                                     Command: nmap -T5 --min-rate 10000 --max-retries 1 --min-parallelism 50 -Pn -n -sS           
- [D] Discover Local IP on Network:  - Lists active devices on the network, our IP Adress and our MAC Adress.")
- [H] Help                           - Show this help menu.")

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Explanations:
- **Installation:** This section provides the steps for cloning the repository, installing dependencies, and running the script.
- **Features:** A table summarizes the available scan options.
- **Usage:** The available options are described with the corresponding commands. Users can select a scan type or discover devices on their local network.
