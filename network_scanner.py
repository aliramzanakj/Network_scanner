import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("192.168.128.1/24")
