# SrvPrint.py

import socket
import struct

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8080  # Port to listen on (non-privileged ports are > 1023)


# Get TCP packet info
def getTcpInfo(s):
    fmt = "B"*7 + "I"*21
    x = struct.unpack(fmt, s.getsockopt(socket.IPPROTO_TCP, socket.TCP_INFO, 92))
    return x[12]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    total_payload = 0
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            # Get Payload Size
            payload = getTcpInfo(s)
            seg = int((payload/16)-1)*4*7
            if total_payload == 0:
                chunk = b''
            total_payload += len(data)
            if not data:
               break
            chunk += data
            if total_payload == seg:
                print('assemble', len(chunk))
                total_payload = 0
                print('get another payload')
