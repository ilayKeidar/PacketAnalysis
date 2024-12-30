from packet_sniffer import sniff
from db_handler import create_db

create_db()

sniff()
print("done")