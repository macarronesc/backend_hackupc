import subprocess
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


ip = ('localhost', 8000)
with SimpleXMLRPCServer(ip, requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    print("ON")

    listWorkers = []


    def createParty():
        numWorkers = 8001 + len(listWorkers)
        urlWorker = 'http://localhost:' + str(numWorkers)

        listWorkers.append(urlWorker)
        subprocess.Popen('python worker.py ' + str(numWorkers), shell=True)

        print("Creating Party: " + urlWorker)
        print(listWorkers)
        return urlWorker


    def getParties():
        print("Get Parties")
        print(listWorkers)
        return listWorkers


    server.register_function(createParty, 'createParty')
    server.register_function(getParties, 'getParties')

    server.serve_forever()