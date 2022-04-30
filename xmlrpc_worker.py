from xmlrpc.server import SimpleXMLRPCServer
import logging
import sys

# lib

server:SimpleXMLRPCServer

def init(ip, port):
    global server
    # define the server
    server = SimpleXMLRPCServer(
        (ip, port),    # IP, port
        logRequests=True,
        allow_none=True,
    )
    logging.info(f"Server at {sys.argv[1]}:{sys.argv[2]} created successfuly!")

def main():
    try:
        server.serve_forever()
    except:
        logging.info("Shutting down")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format=f'%(asctime)s WORKER({sys.argv[2]}) - %(message)s')
    logging.info(f"Started worker: {sys.argv[1]}:{sys.argv[2]}")

    if sys.argv[1] and sys.argv[2]:
        init(sys.argv[1], int(sys.argv[2]))

        main()