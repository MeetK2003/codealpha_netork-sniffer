from scapy.all import sniff

# Function to process each captured packet
def process_packet(packet):
    print(packet.summary())  # Print a summary of the packet

def main():
    print("Starting packet capture...")
    # Start sniffing packets on your network interface
    sniff(prn=process_packet, count=10)  # Adjust count or remove for continuous capture

if __name__ == "__main__":
    main()
