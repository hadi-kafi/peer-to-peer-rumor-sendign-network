import my_global
import time
import os
from peer import *

# my_global.current_peer = None


menu_options = {
    1: 'Send a command',
    2: 'Switch to another peer',
    3: 'Exit',
}


def print_menu():
    print('-'*20)
    for key in menu_options.keys():
        print('|', key, '--', menu_options[key], '|')
    print('-'*20)


def option1():
    # print('''\nOK, Now, Please enter the command:
    #             peer <ip:port>
    #             rumor <body of the rumor>''')
    global userInput
    print('-'*20, 'rumer / peer ??', '-'*20)
    userInput = str(input(''))

    if userInput == 'peer':
        os.system('cls||clear')
        # print('Enter new peer in this format <ip:port>: ')
        inp = str(input('Enter new peer in this format <ip:port>: '))
        colonIndex = inp.find(':')
        address = inp[0:colonIndex]
        port = inp[colonIndex + 1:]
        os.system('cls||clear')
        print('\n\nConnected to new peer with address: ',
              address, 'and port: ', port, '\n\n')
        time.sleep(2)
        os.system('cls||clear')
        new_peer = P2P(int(port), address)
        new_peer.connected_peers_list.append(
            (my_global.current_peer.address, my_global.current_peer.port))
        # new_peer.connected_peers_list.append(my_global.current_peer.connected_peers_list)
        my_global.all_peers.append(new_peer)

        my_global.current_peer.connected_peers_list.append(
            (address, int(port)))

        # create P2P instance

    elif userInput == 'rumer':
        inp2 = str(input('\n<body of the rumor>\n'))
        if inp2 not in my_global.current_peer.rumer_list:
            my_global.current_peer.sender(inp2)


def option2():
    print('List of peers:\n')
    # i = 0
    for peer in my_global.all_peers:
        print('\tPeer', peer.id, ':', f'{peer.address}:{peer.port}')
        # i += 1

    userInput = None

    while not userInput:
        userInput = input("Which peer do you want to connect: ")
        if userInput:
            if userInput == str(my_global.current_peer.id):
                print(f'\n\nYou already connected to peer {userInput}\n\n')
                time.sleep(2)
                os.system('cls||clear')
            else:
                my_global.current_peer = my_global.all_peers[int(userInput)]
                print('Switched to peer', my_global.current_peer.id)


if __name__ == "__main__":
    os.system('cls||clear')
    # When the program starts at first a peer will be made to start the network
    print('\n\nMaking the first peer...')
    time.sleep(2)

    # my_global.current_peer = P2P(id_count, 10057, '127.0.0.1')
    my_global.current_peer = P2P(10057, '127.0.0.1')

    my_global.all_peers.append(my_global.current_peer)
    print('\n\nFirst peer with address', my_global.current_peer.address,
          'and port', my_global.current_peer.port, 'made successfully')
    time.sleep(2)
    os.system('cls||clear')

    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            print('Good bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
