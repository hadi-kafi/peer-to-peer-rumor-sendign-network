from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
from my_global import *
import my_global



class P2P:
    def __init__(self, port, addres=''):
        self.r_socket = socket(AF_INET, SOCK_STREAM)
        self.address = addres
        self.port = port
        # [('192.168.1.1', 60005), ('192.168.1.10', 60125)]
        self.connected_peers_list = []
        self.id = my_global.id_count
        self.rumer_list = []
        self.receiver()
        # print(my_global.id_count)

        my_global.id_count += 1

        # print(my_global.id_count)

    def receiver(self):
        def rcv():
            self.r_socket.bind(('', self.port))
            self.r_socket.listen()

            while True:
                my_global.my_lock.acquire()
                conn, addr = self.r_socket.accept()
                print('-'*20, 'A connection made to peer', self.id, 'from', addr, '-'*20)

                data = conn.recv(BYTE_SIZE)
                print('\n\nPeer', self.id, 'received: ', data.decode(), '\n\n')
                my_global.my_lock.release()

        t = Thread(target=rcv, args=())
        t.start()

    def sender(self, msg):
        if self.connected_peers_list:
            def snd(s_address):
                with socket(AF_INET, SOCK_STREAM) as s_socket:
                    s_socket.connect(s_address)
                    s_socket.sendall(msg.encode())

            for p in self.connected_peers_list:
                t = Thread(target=snd, args=(p, ))
                t.start()
        else:
            my_global.my_lock.acquire()
            print('-'*20, 'No connected peer !!', '-'*20)
            my_global.my_lock.release()