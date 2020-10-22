def modify_destiny(packet):
    if packet['ARP']['src.proto_ipv4'] == '172.31.0.164':
        packet['ARP']['dst.proto_ipv4'] = '172.31.1.164'
        return packet