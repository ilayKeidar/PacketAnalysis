class Packet:
    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port
        self.protocol = protocol
        
    def __repr__(self):
        return f"Packet(src_ip={self.src_ip}, dst_ip={self.dst_ip}, src_port={self.src_port}, dst_port={self.dst_port}, protocol={self.protocol})"

    def display(self):
        return f"Source IP: {self.src_ip}, Destination IP: {self.dst_ip}, Source Port: {self.src_port}, Destination Port: {self.dst_port}, Protocol: {self.protocol}"
