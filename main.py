import xmlrpc.client

ip_server = 'http://localhost:8000'

master = xmlrpc.client.ServerProxy(ip_server)

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
        test = master.createParty()
        print(test)
        server = xmlrpc.client.ServerProxy(test)
        print(xmlrpc.client.ServerProxy(test).getGameStarted())



    elif menuOption == 2:
        i = 0
        print(master.getParties())


        while i != len(master.getParties()):
            print("Room number " + i)
            i += 1
