import socket
import sys

from urlparser import url_parser

urlInput = input('Enter url: ')
Returnedurl = url_parser(urlInput)
url = Returnedurl['domain']
request = b"GET / HTTP/1.1\nHost: stackoverflow.com\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((url, 80))
s.send(request)
result = s.recv(10000)
if "<?xml" in str(result):
    Header = str(result).split("<?xml")[0]
else:
    Header = str(result).split("<html>")[0]
s.close()

# print(result)
print(Header)

download_folder = '/Users/gauravkumar/Documents/sem1/intro_to_web/assignments/assignment-3/python-prog/nisha'

f = open(download_folder + 'page.html', 'wb')
f.write(result)
f.close()
h = open(download_folder + 'header.html', 'wb')
h.write(Header.encode())
h.close()
print("file created")
