import socket
import json
from Algo import choose_move

PAWN1 = 0.0
PAWN2 = 1.0
EMPTY_PAWN = 2.0
EMPTY_BLOCKER = 3.0
BLOCKER = 4.0
IMP = 5.0

local_ip = 'localhost'
server_ip = '172.17.3.30'  # Adresse IP du serveur
server_port = 3000  # Port du serveur

request_data = {
    "request": "subscribe",
    "port": 3003,
    "name": "PDF_gang",
    "matricules": ["12346", "67891"]
}
finished = False

class Client:
    def __init__(self, request_data):
        # Créer un socket TCP
        self.__client_socket = socket.socket()
        self.__message = request_data
    
    def send_request_to_server(self):
        try:
            # Établir une connexion avec le serveur
            self.__client_socket.connect((local_ip, server_port))

            # Convertir le dictionnaire de la requête en chaîne JSON
            request_json = json.dumps(self.__message)

            # Envoyer la requête au serveur
            self.__client_socket.sendall(request_json.encode())

            # Attendre la réponse du serveur
            response_json = self.__client_socket.recv(2048).decode()

            # Convertir la réponse JSON en dictionnaire
            response_data = json.loads(response_json)

            # Fermer la connexion avec le serveur
            self.__client_socket.close()

            # Retourner la réponse du serveur
            return response_data

        except Exception as e:
            print("Une erreur s'est produite lors de l'envoi de la requête:", e)
            return None

class Server:
    def __init__(self):
        # Créer un socket TCP
        self.__server_socket = socket.socket()
        self.__server_socket.settimeout(0.5)
        # Établir une connexion avec le client
        self.__server_socket.bind((local_ip, 3003))
        # Mettre move dans la class

    def listen(self):
        try:
            while True:
                self.__server_socket.listen()
                try:
                    client, adrr = self.__server_socket.accept()
                    # Attendre la demande du client
                    with client:
                        chunks = []
                        finished = False
                        while not finished:
                            data = client.recv(2048)
                            print(data)
                            chunks.append(data)
                            try:
                                final_data = b''.join(chunks).decode("utf-8")
                                global request
                                request = json.loads(final_data)
                                finished = True
                            except json.JSONDecodeError as e:
                                finished = False
                        # Vérifier si la demande est un "ping"
                        
                        if request.get("request") == "ping":

                            # Répondre avec "pong"
                            response_data = {"response": "pong"}
                            response_ping = json.dumps(response_data)
                            client.sendall(response_ping.encode("utf-8"))
                            print("response sended", response_ping)
                            
                        elif request.get("request") == "play":
                            #self.move_comm()
                            client.sendall(self.move_comm()) # compute a move and send it to client
                            #raise NotImplemented()
                except socket.timeout:
                    pass        

        except Exception as e:
            print("Une erreur s'est produite :", e)
            raise e

    def move_comm(self):
        status = request["state"]
        #print(status)
        board = status["board"]
        if status["players"][0]=="Pululu" :
            My_Blockers = status["blockers"][0]
            Ennemy_Blockers = status["blockers"][1]
            My_pawn = PAWN1
            ennemy_pawn = PAWN2
        elif status["players"][1]=="Pululu":
            My_Blockers = status["blockers"][1]
            Ennemy_Blockers = status["blockers"][0]
            My_pawn = PAWN2
            ennemy_pawn = PAWN1
        move = choose_move(board, My_pawn, My_Blockers)
        move_send = json.dumps(move).encode('utf-8')
        print(move_send)
        return move_send
    # Le coup à faire
    """def send_move(self):
        totalsend = 0
        move_send = json.dumps(move).encode('utf-8')
        print(move_send)
        while totalsend < len(move_send):
            sent = self.__server_socket.send(move_send)
            totalsend += sent
            print("total: ", totalsend)"""

client = Client(request_data)
server = Server()

#Prinipal code
response = client.send_request_to_server()
#playing = server.move_comm()
if response is not None:
    print("Réponse du serveur:", response)
else:
    print("Aucune réponse reçue du serveur.")
# Réponse au ping
try:
    server.listen()
except KeyboardInterrupt:
    print("bye")