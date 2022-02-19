from socket import socket
from threading import Thread, Lock
from time import sleep


BYTE_SIZE = 1024

id_count = 0

all_peers = [] #[('192.168.1.1', 100098), ('192.168.1.1', 100098)]

current_peer = None
last_peer = None
my_lock = Lock()
