from scapy.all import sniff, wrpcap
import os
from datetime import datetime

def packet_callback(packet):
    # Extract relevant information from the packet
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        proto = packet['IP'].proto
        payload = bytes(packet['IP'].payload)

        # Print basic packet information
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {proto}")
        print(f"Payload: {payload}")
        print("-" * 50)

def save_packet(packet, filename):
    # Save the packet to a pcap file
    wrpcap(filename, [packet], append=True)

def enhanced_packet_sniffer(filter="", count=0, save=False, filename="captured_packets.pcap"):
    print("Starting enhanced packet sniffer...")

    if save and os.path.exists(filename):
        os.remove(filename)  # Remove the file if it already exists

    def enhanced_callback(packet):
        packet_callback(packet)
        
        if save:
            save_packet(packet, filename)

    # Sniff packets with the given filter and count
    sniff(filter=filter, prn=enhanced_callback, count=count, store=0)

    if save:
        print(f"Packets saved to {filename}")

if __name__ == "__main__":
    # Set up the sniffing parameters
    packet_filter = "tcp port 80"  # Example: Filter for HTTP traffic
    packet_count = 10  # Number of packets to capture (0 for infinite)
    save_to_file = True  # Set to True to save captured packets
    filename = f"./saved_capture/captured_packets_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pcap"  # Save with timestamp

    # Run the enhanced packet sniffer
    enhanced_packet_sniffer(filter=packet_filter, count=packet_count, save=save_to_file, filename=filename)
