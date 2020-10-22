def modify_opcode(packet):
    if packet['ARP']['src.proto_ipv4'] == '172.31.0.164':
        packet['ARP']['opcode'] = '4'
        return packet