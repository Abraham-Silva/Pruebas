import socket
from time import sleep
from os import system

if __name__ == "__main__":
    op, server, BUFFER_SIZE = None, socket.socket(socket.AF_INET,socket.SOCK_STREAM), 1024
    server.connect(('3.149.222.108',4001))
    while op != '3':
        print('SELECCIONE UNA OPCION.')
        op = input('1.- Prender LED.\n2.- Apagar LED.\n3.- Salir.\nOpcion: ')
        if op == '1':
            server.send(bytes('<digitalWrite>on','utf-8'))
        elif op == '2':
            server.send(bytes('<digitalWrite>off','utf-8'))
        elif op == '3': pass
        else:
            print('Ingrese una opción valida')
            system('pause')
    print('Saliste...')