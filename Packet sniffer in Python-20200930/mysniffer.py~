import socket
import sys
from struct import *


def to_hex(data):
    i = 0
    ans = ""
    j = 1
    while i < len(data):
        ans += str(hex(int(data[i:i+2], base=16)))[2:].zfill(2)
        ans += "  "
        i += 2
        if j == 24:
            ans += "\n"
            j = 0
        j += 1

    return ans


def getAscii(data):
    i = 0
    j = 1
    ans = ""
    while i < len(data):
        num = int(data[i:i+2], base=16)
        if num >= 32 and num <= 127:
            ans += chr(num)
        else:
            ans += "."
        if j == 94:
            ans += "\n"
            j = 0
        j += 1
        i += 2
    return ans


def get_parameters():
    destination_port = 80
    destination_ip = '210.212.183.7'
    protocol_name = 'tcp'
    for i in range(len(sys.argv) - 1):
        try:
            destination_port = int(sys.argv[i + 1])
            continue
        except:
            pass
        try:
            socket.inet_aton(sys.argv[i + 1])
            destination_ip = sys.argv[i + 1]
            continue
        except:
            pass
        try:
            protocol_name = sys.argv[i + 1]
            continue
        except:
            pass
    return destination_port, destination_ip, protocol_name


def eth_addr(a):
    a = str(a)
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]), ord(
        a[1]), ord(a[2]), ord(a[3]), ord(a[4]), ord(a[5]))
    return b


def run_sniffer(destination_port, destination_ip, protocol_name):
    # receive a packet
    while True:
        packet = s.recvfrom(65565)
        # packet string from tuple
        packet = packet[0]

        # parse ethernet header
        eth_length = 14

        eth_header = packet[:eth_length]
        eth = unpack('!6s6sH', eth_header)
        eth_protocol = socket.ntohs(eth[2])

        # Parse IP packets, IP Protocol number = 8
        if eth_protocol == 8:
            # Parse IP header
            # take first 20 characters for the ip header
            ip_header = packet[eth_length:20+eth_length]

            # now unpack them :)
            iph = unpack('!BBHHHBBH4s4s', ip_header)

            version_ihl = iph[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF

            iph_length = ihl * 4

            ttl = iph[5]
            protocol = iph[6]
            s_addr = socket.inet_ntoa(iph[8])
            d_addr = socket.inet_ntoa(iph[9])

            if version != 4:
                continue

            if destination_ip != None and destination_ip not in [d_addr]:
                continue

            # TCP protocol
            if protocol == 6 and (protocol_name in ["http", "ftp", "tcp", "telnet"] or protocol_name == None):
                t = iph_length + eth_length
                tcp_header = packet[t:t+20]

                # now unpack them :)
                tcph = unpack('!HHLLBBHHH', tcp_header)

                source_port = tcph[0]
                dest_port = tcph[1]
                sequence = tcph[2]
                acknowledgement = tcph[3]
                doff_reserved = tcph[4]
                tcph_length = doff_reserved >> 4

                if destination_port != None and destination_port not in [dest_port]:
                    continue

                h_size = eth_length + iph_length + tcph_length * 4

                data_size = len(packet) - h_size

                # get data from the packet
                data = packet[h_size:].decode(
                    'ascii', errors='replace').strip("\t\r\n")

                if (protocol_name == None or protocol_name in ["ftp", "tcp"]) and (source_port == 21 or dest_port == 21):
                    print("Ethernet info")
                    print('Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(
                        packet[6:12]) + ' Protocol : ' + str(eth_protocol))
                    print("Ip info")
                    print('Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) +
                          ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))
                    print("tcp info")
                    print('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' +
                          str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length))

                    if len(data) > 0:
                        print("FTP header")
                        print(data)
                        print()
                    print("raw data")
                    print("hex")
                    print(to_hex(packet.hex()))
                    print()
                    print("ascii")
                    print(str(getAscii(packet.hex())))
                    print()
                    print()
                    print()
                elif protocol_name == None or protocol_name in ["tcp", "telnet"] and (source_port == 23 or dest_port == 23):
                    print("Ethernet info")
                    print('Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(
                        packet[6:12]) + ' Protocol : ' + str(eth_protocol))
                    print("Ip info")
                    print('Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) +
                          ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))
                    print("tcp info")
                    print('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' +
                          str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length))

                    if len(data) > 0:
                        print("Telnet header")
                        print(data)
                        print()
                    print("raw data")
                    print("hex")
                    print(to_hex(packet.hex()))
                    print()
                    print("ascii")
                    print(str(getAscii(packet.hex())))
                    print()
                    print()
                    print()
                elif (protocol_name == None or protocol_name in ["http", "tcp"]) and (data.find("HTTP/1.1") != -1 or data.find("HTTP/1.0") != -1 or data.find("HTTP/2.0") != -1):
                    print("Ethernet info")
                    print('Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(
                        packet[6:12]) + ' Protocol : ' + str(eth_protocol))
                    print("Ip info")
                    print('Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) +
                          ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))
                    print("tcp info")
                    print('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' +
                          str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length))

                    if len(data) > 0:
                        print("HTTP header")
                        print(data)
                        print()
                    print("raw data")
                    print("hex")
                    print(to_hex(packet.hex()))
                    print()
                    print("ascii")
                    print(str(getAscii(packet.hex())))
                    print()
                    print()
                    print()
                elif protocol_name == None or protocol_name == "tcp":
                    print("Ethernet info")
                    print('Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(
                        packet[6:12]) + ' Protocol : ' + str(eth_protocol))
                    print("Ip info")
                    print('Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) +
                          ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))
                    print("tcp info")
                    print('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' +
                          str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length))

                    print("raw data")
                    print("hex")
                    print(to_hex(packet.hex()))
                    print()
                    print("ascii")
                    print(str(getAscii(packet.hex())))
                    print()
                    print()
                    print()

            # ICMP Packets
            elif protocol == 1:
                u = iph_length + eth_length
                icmph_length = 4
                icmp_header = packet[u:u+4]

                # now unpack them :)
                icmph = unpack('!BBH', icmp_header)

                icmp_type = icmph[0]
                code = icmph[1]
                checksum = icmph[2]

                print('Type : ' + str(icmp_type) + ' Code : ' +
                      str(code) + ' Checksum : ' + str(checksum))

                h_size = eth_length + iph_length + icmph_length
                data_size = len(packet) - h_size

                # get data from the packet
                data = packet[h_size:].decode(errors='replace')

                print('Data : ' + data)

            # UDP packets
            elif protocol == 17 and (protocol_name == None or protocol_name == "udp"):
                u = iph_length + eth_length
                udph_length = 8
                udp_header = packet[u:u+8]

                # now unpack them :)
                udph = unpack('!HHHH', udp_header)

                source_port = udph[0]
                dest_port = udph[1]
                length = udph[2]
                checksum = udph[3]

                if destination_port != None and destination_port != dest_port:
                    continue

                print("Ethernet info")
                print('Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(
                    packet[6:12]) + ' Protocol : ' + str(eth_protocol))
                print("Ip info")
                print('Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) +
                      ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))
                print("UDP header")
                print('Source Port : ' + str(source_port) + ' Dest Port : ' +
                      str(dest_port) + ' Length : ' + str(length) + ' Checksum : ' + str(checksum))

                h_size = eth_length + iph_length + udph_length
                data_size = len(packet) - h_size

                # get data from the packet
                data = packet[h_size:].hex()

                if len(data) > 0:
                    print("UDP DATA")
                    print(data)

                print("RAW data")
                print("hex data")
                print(to_hex(packet.hex()))
                print()
                print("ascii")
                print(str(getAscii(packet.hex())))
                print()
                print()
                print()

            # some other IP packet like IGMP
            # else:
            #     print('Protocol other than TCP/UDP/ICMP')

            # print()


if __name__ == '__main__':
    destination_port, destination_ip, protocol_name = get_parameters()

    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW,
                          socket.ntohs(0x0003))
    except Exception:
        print('Socket could not be created.')
        print('Try: sudo python3 <filename>.py')
        sys.exit()

    run_sniffer(destination_port, destination_ip, protocol_name)
