from scapy.all import *

def read_data_file(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
    return data

def send_http_request(target_ip, target_port, method="GET", num_packets=100, data=b''):
    for _ in range(num_packets):
        ip = IP(dst=target_ip)
        tcp = TCP(dport=target_port)
        http = bytes(
            f"{method} / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n",
            encoding="utf-8"
        ) + data
        pkt = ip / tcp / http
        send(pkt)

target_ip = input("Enter the target IP address: ")
target_port = int(input("Enter the target port: "))
data_file_path = input("Enter the path to the data file: ")

data = read_data_file(data_file_path)

send_http_request(target_ip, target_port, data=data)