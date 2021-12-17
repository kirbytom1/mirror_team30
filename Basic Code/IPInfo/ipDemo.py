import ipinfo
import socket
import sys

access_token = '7988f883b8fd54'
handler = ipinfo.getHandler(access_token)
hostname = sys.argv[1]
ip_address = socket.gethostbyname(hostname)
details = handler.getDetails(ip_address)
print(details.all)