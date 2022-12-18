import socket

ip = "213.201.83.138" 

try:
    dominio = socket.gethostbyaddr(ip)[0]
    print ("La IP %s tiene una entrada DNS: %s" %(ip, dominio))

except socket.error as msg:
    print ("%s: %s" %(ip, msg))