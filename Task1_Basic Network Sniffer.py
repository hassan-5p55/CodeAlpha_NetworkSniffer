#!/usr/bin/env python3
"""
Basic Network Sniffer
CodeAlpha Cybersecurity Internship - Task 1
"""

from scapy.all import sniff, wrpcap, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

captured_packets = []
PACKET_COUNT = 0

def process_packet(packet):
    global PACKET_COUNT
    PACKET_COUNT += 1
    captured_packets.append(packet)

    if IP in packet:
        ip_layer = packet[IP]
        src_ip, dst_ip = ip_layer.src, ip_layer.dst
        proto_name = {1: "ICMP", 6: "TCP", 17: "UDP"}.get(ip_layer.proto, f"Other({ip_layer.proto})")

        print(f"\n{'='*60}")
        print(f"[{PACKET_COUNT}] {datetime.now().strftime('%H:%M:%S')}")
        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")
        print(f"Protocol       : {proto_name}")
        print(f"TTL            : {ip_layer.ttl}")
        print(f"Packet Length  : {len(packet)} bytes")

        if TCP in packet:
            t = packet[TCP]
            print(f"Src Port       : {t.sport}")
            print(f"Dst Port       : {t.dport}")
            print(f"Flags          : {t.flags}")
        elif UDP in packet:
            u = packet[UDP]
            print(f"Src Port       : {u.sport}")
            print(f"Dst Port       : {u.dport}")
        elif ICMP in packet:
            i = packet[ICMP]
            print(f"ICMP Type      : {i.type}")
            print(f"ICMP Code      : {i.code}")

        if Raw in packet:
            payload = packet[Raw].load
            try:
                decoded = payload.decode("utf-8", errors="replace")
                preview = decoded[:100].replace("\n", " ").replace("\r", "")
                print(f"Payload Preview: {preview}")
            except Exception:
                print(f"Payload (hex)  : {payload[:50].hex()}")

def main():
    print("="*60)
    print(" Basic Network Sniffer - CodeAlpha Internship Task 1")
    print("="*60)
    print("Press Ctrl+C to stop.\n")

    try:
        sniff(prn=process_packet, store=False, filter="ip")
    except PermissionError:
        print("ERROR: Run this script with administrator/root privileges.")
    except KeyboardInterrupt:
        print(f"\n\nCapture stopped. Total packets captured: {PACKET_COUNT}")
        if captured_packets:
            save = input("Save capture to file? (pcap) [y/N]: ").strip().lower()
            if save == "y":
                wrpcap("capture.pcap", captured_packets)
                print("Saved to capture.pcap (open with Wireshark)")

if __name__ == "__main__":
    main()