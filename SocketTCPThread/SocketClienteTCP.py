import socket
import sys

HOST = '127.0.0.1'
PORT = 5008


def programa_cliente():
    try:
        # 1- Creamos el Socket.
        socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket cliente creado')
    except socket.error:
        print('Fallo en la creación del socket cliente')
        sys.exit()

    # 2- Conectamos el Socket cliente al servidor
    socket_cliente.connect((HOST, PORT))
    mensaje = 'Conectado con el servidor' # El programa cliente escribe esto al servidor

    with socket_cliente:
        while mensaje != 'bye':
            # 3- Codificamos el mensaje a bytes y le indicamos que lo envíe todo
            socket_cliente.sendall(mensaje.encode())
            #numBytes = s.sendall(mensaje.encode())
            #print (numBytes)

            # 4- Esperamos respuesta. Línea bloqueante, esperamos que el servidor nos conteste
            data = socket_cliente.recv(1024)
            print('Recibido del servidor:' + data.decode())
            
            mensaje = input(
                'Escribe tu mensaje (Para finalizar escribe: bye)--> ')


if __name__ == '__main__':
    programa_cliente()
