``markdown
# NmapTool

NmapTool is a Python-based tool for performing network scans using Nmap. The tool allows you to run different types of Nmap scans on a target IP, such as basic scans, service version scans, and more.

## Requirements

Before running the tool, you need to install the necessary dependencies. Make sure you have `Python` installed on your system.

## Installation

Follow these steps to set up and run the NmapTool:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SkyzzTech/NmapTool.git
   ```

2. **Navigate to the project folder:**

   ```bash
   cd NmapTool
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the NmapTool script:**

   ```bash
   python NmapTool.py
   ```

## Features

NmapTool provides the following scan options:

| Option | Description |
|--------|-------------|
| **Basic Scan** | Performs a basic scan of the target IP. |
| **Service Version Scan (`-sV`)** | Detects the versions of services running on open ports. |
| **Service and Version Scan** | Combines basic scanning with service version detection. |
| **Bypass Firewall Scan** | Attempts to bypass firewalls to discover services. |

## Usage

After running the script, you'll be prompted with the following options:

```bash
[1] Basic Scan
[2] Service Version Scan (-sV)
[3] Service and Version Scan
[4] Bypass Firewall Scan
```

Choose an option and enter the target IP when prompted.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Explanations:
- The **Installation** section guides users through the steps to clone the repository, install dependencies, and run the script.
- The **Features** section presents a table summarizing the scan options available.
- The **Usage** section briefly describes what users will encounter when running the script.
