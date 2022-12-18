import socket
import sys


def programa_servidor():
    # Decidimos la IP y el puerto del servidor
    HOST = '127.0.0.1'  # La IP del servidor es la loca de la máquina
    PORT = 5008  # El puerto tiene que ser superior a 1024, por debajo estan reservados
    fin_mensaje = b''

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
        # El Servidor queda bloquedo en esta línea esperando a que un cliente se conecte a su IP y puerto
        # Si un cliente se conecta guardamos en conn del socket y en addr la información del cliente (IP y puerto del cliente)
        socket_atiende, addr_cliente = socket_escucha.accept()

        with socket_atiende:
            # print(f"Conexión exitosa con el cliente. IP ({addr[0]}) Puerto ({addr[1]})")
            print(f"Conexión exitosa con el cliente. {addr_cliente}")
            cerrar = False

            while not cerrar:
                # El servidor queda bloqueado esperando el mensaje que le va a enviar el cliente
                data = socket_atiende.recv(1024)

                if data == fin_mensaje:
                    cerrar = True
                else:
                    # Mensaje recibido, lo imprimimos
                    print(
                        f'El cliente {addr_cliente} nos ha escrito: {data.decode()}')
                    socket_atiende.sendall(b"mensaje recibido")


if __name__ == '__main__':
    programa_servidor()
