import os
import sys
import time
import subprocess
import socket
from scapy.all import ARP, Ether, srp

if sys.platform.startswith("win"):
    os.system("")

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

PURPLE = "\033[35m"
GREEN = "\033[32m"
RESET = "\033[0m"
RED = "\033[31m"
BLUE = "\033[34m"

def get_local_network():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    return f"{local_ip}/24"

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]  
    except socket.herror:
        return "Unknown"

def discover_network():
    clear_screen()
    network = get_local_network()
    print(f"\nScanning network: {network}...\n")

    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, verbose=False)[0]

    print("IP Address          MAC Address          Hostname")
    print("------------------------------------------------")
    for sent, received in result:
        hostname = get_hostname(received.psrc)
        print(f"{received.psrc:<20}{received.hwsrc:<20}{hostname}")

    input("\nPress Enter to continue...")
    main()

def main():
    clear_screen()

    print(GREEN + """\n\n ███▄    █  ███▄ ▄███▓ ▄▄▄       ██▓███     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
 ██ ▀█   █ ▓██▒▀█▀ ██▒▒████▄    ▓██░  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▓██  ▀█ ██▒▓██    ▓██░▒██  ▀█▄  ▓██░ ██▓▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
▓██▒  ▐▌██▒▒██    ▒██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██░   ▓██░▒██▒   ░██▒ ▓█   ▓██▒▒██▒ ░  ░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░ ▒░   ▒ ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░ ░░   ░ ▒░░  ░      ░  ▒   ▒▒ ░░▒ ░            ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
   ░   ░ ░ ░      ░     ░   ▒   ░░            ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
         ░        ░         ░  ░                         ░ ░      ░ ░      ░  ░""" + RESET)

    n = input(BLUE + "\n[D] Discover Local IP on Network\n\n\n" + RESET +
                    "[1] Basic Scan (Very fast)\n" +
                    "[2] Service And Version Scan (Fast)\n" +
                    "[3] Bypass Firewall Scan (Very fast)\n" +
                    "[4] Best Nmap Scan (Long)\n" +
                    "\n\n[H] Help\n\n:" + RESET)

    if n == '1':
        basic()

    elif n == '2':
        service()

    elif n == '3':
        firewall()

    elif n == '4':
        best()    

    elif n == 'D':
        discover_network()
    elif n == 'd':
        discover_network() 

    elif n == 'H':
        help_menu()
    elif n == 'h':
        help_menu()     

    else:
        print(RED + "Invalid Choice..." + RESET)
        time.sleep(2)
        main()

def basic():
    ip = input("\nTarget IP: ")
    print(f"\nScanning {ip}...")
    command = ["nmap", ip]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    display_results(result.stdout)
    input("\nPress Enter to continue...")
    main()

def service():
    ip = input("\nTarget IP: ")
    print(f'\nScanning Ports Services of {ip}...')
    command = ["nmap", "-sV", ip]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    display_results(result.stdout)
    input("\nPress Enter to continue...")
    main()

def firewall():
    ip = input("\nTarget IP:")
    print(f'\nScanning Ports Bypassing The Firewall of {ip}')
    command = ["nmap", "--disable-arp-ping", "--source-port", "53", "-sS", "-Pn", "-n", ip]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    display_results(result.stdout)
    input("\nPress Enter to continue...")
    main()

def best():
    ip = input("\nTarget IP:")
    print(f'\nScanning with Best Config of {ip}')
    command = ["nmap", "-A", "-p-", "-v", ip]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    display_results(result.stdout)
    input("\nPress Enter to continue...")
    main()



def display_results(scan_result):
    print(scan_result)

def help_menu():
    clear_screen()
    print(GREEN + "Help Menu\n" + RESET)
    print("[1] Basic Scan:                    - Scans open ports without version detection   Command: nmap 'ip'.")
    print("[2] Service and Version Scan:      - Identifies open ports and detects services running on them.   Command: nmap -sV 'ip'.")
    print("[3] Bypass Firewall Scan:          - Uses stealth techniques to evade firewalls.   Command: nmap --disable-arp-ping --source-port 53 -sS -Pn -n 'ip'.")
    print("[4] Best Nmap Scan:                - Comprehensive scan with service detection and OS fingerprinting   Command: nmap -A -p- -v 'ip'.")
    print("[D] Discover Local IP on Network:  - Lists active devices on the network, our IP Adress and our MAC Adress.")
    print("[H] Help                           - Show this help menu.")
    input("\nPress Enter to continue...")
    main()


if __name__ == "__main__":
    main()
