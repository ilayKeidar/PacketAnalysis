class Frame:
    def __init__(self, src_mac, dst_mac, protocol):
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.protocol = protocol

    def __repr__(self):
        return f"Packet(src_mac={self.src_mac}, dst_mac={self.dst_mac}, protocol={self.protocol})"

    def display(self):
        return f"Source MAC: {self.src_mac}, Destination MAC: {self.dst_mac}, Protocol: {self.protocol}"
