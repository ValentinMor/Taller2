def modify_destiny(packet):
    if packet['ARP']['src.proto_ipv4'] == '172.31.0.164':
        packet['ARP']['dst.proto_ipv4'] = '172.31.1.164'
        return packet

def modify_opcode(packet):
    if packet['ARP']['src.proto_ipv4'] == '172.31.0.164':
        packet['ARP']['opcode'] = '4'
        return packet

def modify_destiny_mac(packet):
    if packet['ARP']['src.proto_ipv4'] == '172.31.0.164':
        packet['ARP']['dst.hw_mac'] = '02:01:ee:be:47:19'
        return packet

def modify_source_mac(packet):
    if packet['ARP']['src.proto_ipv4'] == '172.31.0.164':
        packet['ARP']['src.hw_mac'] = '02:da:df:ed:63:c4'
        return packet

def modify_hw_type(packet):
    if packet['ARP']['src.proto_ipv4'] == '172.31.0.164':
        packet['ARP']['hw_type'] = '2'
        return packet                      