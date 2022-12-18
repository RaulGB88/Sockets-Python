import socket

HOST = '129.6.15.28'
PORT = 13

# 1- Creamos el Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # 2- Conectamos al Socket cliente al servidor.
    s.connect((HOST, PORT))

    print('Conectado con éxito')

    # 3- Recibimos la respuesta del servidor.
    mensaje = s.recv(1024)
    print(mensaje.decode())

except socket.error as exc:
    print("Excepción de socket: %s" % exc)
finally:
    # cerramos la conexión, aunque el servidor ya la habrá cerrado
    s.close()