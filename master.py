import subprocess
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


ip = ('localhost', 8000)
with SimpleXMLRPCServer(ip, requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    print("ON")

    listWorkers = []


    def createParty():
        numWorkers = 8005 + len(listWorkers)

        listWorkers.append('http://localhost:' + str(numWorkers))
        listWorkers[len(listWorkers) - 1] = subprocess.Popen('python worker.py ' + str(numWorkers), shell=True)

        print("Creating Party: ")
        print("Party: http://localhost:" + str(numWorkers))


    def getParties():
        print("Get Parties")
        return listWorkers


    server.register_function(createParty, 'createParty')
    server.register_function(getParties, 'getParties')

    server.serve_forever()
