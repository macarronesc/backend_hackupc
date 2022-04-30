from xmlrpc.client import Server, ServerProxy, Error
import logging

# variables
SERVER_PORT = 8000
SERVER_IP = 'localhost'
master = ServerProxy(f'http://{SERVER_IP}:{SERVER_PORT}')
worker = None


def ping(msg):
    result = f"{master.pingMe(msg)}\n"
    return result


# turn on the server forever until interrupt
def main():
    try:
        print("Hi")
        w = master.createParty()

        print(master.system.listMethods())

        worker = ServerProxy(w)

        print(worker.system.listMethods())


    except:
        print("Goodbye")


if __name__ == '__main__':
    main()
