import socket 
import struct
from struct import *
import sys
import binascii


def ethernet_head(raw_data):     
        dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])      
        dest_mac = binascii.hexlify(dest).decode('ascii')     
        src_mac = binascii.hexlify(src).decode('ascii')
        proto = socket.htons(prototype)     
        data = raw_data[14:]
        return dest_mac, src_mac, proto, data 

def ipv4_head(raw_data):     
        version_header_length = raw_data[0]     
        version = version_header_length >> 4     
        header_length = (version_header_length & 15) * 4     
        ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', raw_data[:20])     
        data = raw_data[header_length:]     
        src = int(binascii.hexlify(src).decode('ascii'), 16)
        src = socket.inet_ntoa(struct.pack("<L", src))
        dst = int(binascii.hexlify(target).decode('ascii'), 16)
        dst = socket.inet_ntoa(struct.pack("<L", dst))

        return version, header_length, ttl, proto, src, dst, data



sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
while True:   
        raw_data, addr = sock.recvfrom(65565)
        dest_mac, src_mac, proto, data = ethernet_head(raw_data)
        #print(dest_mac, "\n", src_mac, "\n", proto, "\n", data, "\n")
        
        print(ipv4_head(data))
        