import xmlrpc.client

ip_server = 'http://localhost:8000'

master = xmlrpc.client.ServerProxy(ip_server)
server = xmlrpc.client.ServerProxy('http://localhost:8001')

def menu():
    print("Chose an option: ")
    print("1. Create a new room")
    print("2. See the existing room")
    print("0. Close")

    menuOption = int(input())
    while menuOption != 1 and menuOption != 2 and menuOption != 0:
        menu()
        menuOption = int(input())

    return menuOption

if __name__ == '__main__':
    print("Hi, welcome!")

    print(master.getParties())



    menuOption = menu()

    if menuOption == 0:
        print("Bye bye :(")
        exit()



    elif menuOption == 1:
        print(master.system.listMethods())

        print(master.createParty())
        print(master.getParties())
        print(server.system.listMethods())
        print(server.createParty())

        print(server.getParties())
        print(master.getParties())



    elif menuOption == 2:
        i = 0
        print(server.getParties())
        print(master.getParties())

"""
        while i != len(master.getParties()):
            print("Room number " + i)
            i += 1
"""