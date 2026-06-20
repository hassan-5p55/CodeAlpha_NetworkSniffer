# CodeAlpha_NetworkSniffer

**CodeAlpha Cybersecurity Internship — Task 1**

A Python-based network packet sniffer that captures live traffic on a network interface and displays key information about each packet — source/destination IPs, protocol, ports, TTL, and a payload preview.

## Overview

This tool uses the `scapy` library to capture and parse network packets in real time. It is built as a learning exercise to understand how data flows across a network and how protocols like TCP, UDP, and ICMP are structured.

## Features

- Live packet capture on any available network interface
- Displays source IP, destination IP, and protocol (TCP/UDP/ICMP)
- Shows TTL and total packet length
- Extracts source/destination ports for TCP and UDP traffic
- Extracts ICMP type/code for ping-related traffic
- Previews readable payload data where available
- Optional export of captured packets to a `.pcap` file for analysis in Wireshark

## Tech Stack

- Python 3.8+
- [Scapy](https://scapy.net/)

## Installation

```bash
git clone https://github.com/<your-username>/CodeAlpha_NetworkSniffer.git
cd CodeAlpha_NetworkSniffer
pip install -r requirements.txt
```

## Usage

Packet capturing requires elevated/administrator privileges since it accesses raw sockets.

**Linux / macOS:**
```bash
sudo python3 sniffer.py
```

**Windows:**
1. Install [Npcap](https://npcap.com/) (required for Scapy to capture packets on Windows).
2. Run your terminal as Administrator.
```bash
python sniffer.py
```

Press `Ctrl+C` to stop the capture. You'll be prompted to save the session to a `.pcap` file.

## Sample Output

```
============================================================
[1] 14:32:10
Source IP      : 192.168.1.5
Destination IP : 142.250.183.78
Protocol       : TCP
TTL            : 64
Packet Length  : 74 bytes
Src Port       : 51322
Dst Port       : 443
Flags          : S
```

## ⚠️ Legal Disclaimer

This tool is intended **strictly for educational purposes** and for use on networks you own or have explicit written permission to monitor. Capturing network traffic on networks without authorization is illegal under most jurisdictions' computer misuse / cybercrime laws. The author and CodeAlpha are not responsible for any misuse of this tool.

## Project Structure

```
CodeAlpha_NetworkSniffer/
├── sniffer.py
├── requirements.txt
└── README.md
```

## Author

Muhammad Hassan Ali — Computer Engineering, NUST College of E&ME
CodeAlpha Cybersecurity Internship
