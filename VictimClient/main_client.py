from core.connection import ClientConnection
from core.handleConnection import handleConnection

if __name__ == "__main__":
    my_socket = ClientConnection()

    my_socket.Connect("192.168.40.143", 8080)

    handleConnection(my_socket)

    my_socket.close()

