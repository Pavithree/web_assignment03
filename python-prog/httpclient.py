import socket
import sys

from urlparser import url_parser

urlInput = input('Enter url: ')
Returnedurl = url_parser(urlInput)
url = Returnedurl['domain']

request = b'GET / HTTP/1.0\nHost: '+url+'\n\n'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((url, 80))
s.send((request).encode())
result = s.recv(10000)
if "<?xml" in str(result):
    Header = str(result).split("<?xml")[0]
else:
    Header = str(result).split("<html>")[0]
s.close()

# print(result)
print(Header)

f = open('page.html', 'wb')
f.write(result)
f.close()
h = open('header.html', 'wb')
h.write(Header.encode())
h.close()
print("file created")
