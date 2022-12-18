import socket
import time
import sys
import threading

HOST = '127.0.0.1'
PORT = 5008
fin_mensaje = b''

def hilo(lock, socket_atiende, addr_cliente):

    with lock:
        with socket_atiende:
            # print(f"Conexión exitosa con el cliente. IP ({addr[0]}) Puerto ({addr[1]})")
            print(f"Conexión exitosa con el cliente. {addr_cliente}")
            cerrar = False

            hour = time.localtime()
            hour = time.mktime(hour)
            hour_format = time.strftime("%m/%d/%Y, %H:%M:%S")

            socket_atiende.sendall(hour_format.encode())
            socket_atiende.close()


def programa_servidor():
    try:
        socket_escucha = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket servidor creado')
    except socket.error:
        print('Fallo en la creación del socket servidor')
        sys.exit()

    try:
        # Definimosel punto de enlace del ervidor. El servidor está preparado en la IP 127.0.0.1 y puerto 5000
        socket_escucha.bind((HOST, PORT))
    except socket.error as e:
        print('Error socket: %s' % e)
        sys.exit()
        
    # El servidor puede escuchar hasta 5 clientes. En este ejmeplo sólo escuchará a 1 y se rompe la conexión
    socket_escucha.listen(5)

    while True:
        socket_atiende, addr_cliente = socket_escucha.accept()

        # Ejecución con Threads.
        lock = threading.Lock()
        t = threading.Thread(target=hilo, args=(lock,socket_atiende,addr_cliente))
        t.start()
        
        # Ejecución sin Threads.
        #hour = time.localtime()
        #hour = time.mktime(hour)
        #hour_format = time.strftime("%m/%d/%Y, %H:%M:%S")

        #socket_atiende.sendall(hour_format.encode())
        #socket_atiende.close()


if __name__ == '__main__':
    programa_servidor()