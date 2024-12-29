class Frame:
    def __init__(self, src_mac, dst_mac, protocol, timestamp):
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.protocol = protocol
        self.timestamp = timestamp

    def __repr__(self):
        return f"Packet(src_mac={self.src_mac}, dst_mac={self.dst_mac}, protocol={self.protocol}, timestamp={self.timestamp})"

    def display(self):
        return f"Source MAC: {self.src_mac}, Destination MAC: {self.dst_mac}, Protocol: {self.protocol}, Timestamp: {self.timestamp}"
