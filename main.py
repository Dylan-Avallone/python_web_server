import socket
import sys
import time

s = socket.socket()
if len(sys.argv) == 2: port = 80
else: port = int(sys.argv[2])
domain_name = sys.argv[1]


s.connect((domain_name, port))


print("HTTP REQUEST")
httprequest =   "GET / HTTP/1.1\r\n" \
               f"Host: {domain_name}\r\n" \
                "Connection: close\r\n" \
                "\r\n"
print(httprequest)
httprequestbytes = httprequest.encode("ISO-8859-1")
s.sendall(httprequestbytes)
final_string = ""
while True:
    d = s.recv(4096)
    final_string += d.decode("ISO-8859-1")
    if len(d) == 0:
        s.close()
        break
print(final_string)