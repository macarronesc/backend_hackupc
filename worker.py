import sys
from random import random
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


ip = ('localhost', int(sys.argv[1]))
with SimpleXMLRPCServer(ip, requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    print("ON")

    print("Server at " + str(ip) + " created successfuly!")

    # False if the Game not started // True anyelse
    gameStarted = False

    # False if not answered // True if the client answered
    waitingClient = True

    # Value of word of the game
    word = ""
    oldWord = ""

    # Num Clients Online
    numClients = 0

    # Turn
    turnClient = 0

    # Know if the game started
    # @return value of gameStarted
    def getGameStarted():
        return gameStarted


    # Start the game
    # @return True 4 the client know that all is done
    def startGame():
        global gameStarted
        gameStarted = True
        return True


    # Know if must wait an another client
    # @return value of waitingClient
    def getWaitingClient():
        return waitingClient


    # Method to recibe (server) the word from the client
    # param wordSended is String with the word to send to the server from the client
    # @return if the word is correctly or not
    def sendWord(wordSended):
        global word, oldWord, waitingClient
        oldWord = word
        word = wordSended

        waitingClient = False
        pickTurn()

        return correctWord(wordSended)


    # Send to client the last word
    # @return value of word
    def getRecibeWord():
        return word


    # Send the number of client that who has the next round
    # @return value of turnClient
    def getWhoNextRound():
        return turnClient


    # Method local to pick the next client that who has the next round
    def pickTurn():
        global numClients, turnClient
        turnClient = random.randint(1, numClients)


    # Add a new client to the party
    # @return the number that correspond to the new client in the party
    def addClient():
        global numClients
        numClients += 1
        return numClients


    # Get the number of clients in the party
    # @return value of numClients
    def getNumClients():
        return numClients


    # Know if a word exist in Diccionary
    # @param word string with the word to check in the Diccionary
    # @return True if exist or False if not
    def existentWordInDictionary(word):
        exist = False
        file = open("diccionary.txt")
        for line in file.readlines():
            line = line.replace("\n", "")
            if line == word:
                exist = True
        file.close()
        return exist


    # Method local to get the next random position to make the telephone
    # @param integer with th lenght of the word
    # @return random value of the position
    def getPosition(lenght):
        possi = lenght / 2
        return random.randint(0, possi)


    # Know if the Word recibed there is in the correct position
    # @param string with the word to check
    # @return True if the word is correct or False if not
    def correctWord(word):
        correct = False
        part = getPosition(len(word))

        if existentWordInDictionary(word) and oldWord[part:part + 2].lower() == word[0:2].lower():
            correct = True
            return correct

        return correct

    # Chose a random word for the first word to play
    # @return the word
    def randomWord():
        print("Making a random word")
        pickTurn()

        file = open("diccionary.txt")
        num_lines = random.randint(0, sum(1 for line in file))

        randomWordString = [line for line in [file.readline() for _ in range(num_lines)] if len(line)]

        file.close()
        return randomWordString


    server.register_function(getGameStarted, 'getGameStarted')
    server.register_function(startGame, 'startGame')

    server.register_function(getWaitingClient, 'getWaitingClient')

    server.register_function(sendWord, 'sendWord')
    server.register_function(getRecibeWord, 'getRecibeWord')

    server.register_function(getWhoNextRound, 'getWhoNextRound')

    server.register_function(addClient, 'addClient')
    server.register_function(getNumClients, 'getNumClients')

    server.register_function(getPosition, 'getPosition')

    server.register_function(correctWord, 'correctWord')
    server.register_function(randomWord, 'randomWord')

    server.serve_forever()
