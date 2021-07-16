import socket as s

host = 'google.com'

Ip = s.gethostbyname(host)

print('O IP do Host"' + host + '" é: ' + Ip)