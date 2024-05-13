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
# Les données que à envoyer au serveur pour se connecter
request_data = {
    "request": "subscribe",
    "port": 3009,
    "name": "Pululu",
    "matricules": ["11111", "22222"]
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
        # Établir un temps de réaction
        self.__server_socket.settimeout(0.5)
        # Établir une connexion avec le client
        self.__server_socket.bind((local_ip, 3009))
    # Fonction principale de la communication avec le serveur
    def listen(self):
        try:
            while True:
                # Écoute sur le socket créé
                self.__server_socket.listen()
                try:
                    # Accepte la connection
                    client, adrr = self.__server_socket.accept()
                    # Attendre la demande du client
                    with client:
                        # Boucle de réception
                        chunks = []
                        finished = False
                        while not finished:
                            data = client.recv(10000)
                            print(data)
                            chunks.append(data)
                            finished = data
                            try:
                                final_data = b''.join(chunks).decode("utf-8")
                                global request
                                request = json.loads(final_data)
                            except json.JSONDecodeError as e:
                                raise e
                        # Vérifier si la demande est un "ping"
                        if request.get("request") == "ping":

                            # Répondre avec "pong"
                            response_data = {"response": "pong"}
                            response_ping = json.dumps(response_data)
                            client.sendall(response_ping.encode("utf-8"))
                            print("response sended", response_ping)
                        # Vérifier si la demande est un "play"    
                        elif request.get("request") == "play":
                            # Envois du coups à jouer
                            client.sendall(self.move_comm()) # compute a move and send it to client
                            #raise NotImplemented()
                except socket.timeout:
                    pass        

        except Exception as e:
            print("Une erreur s'est produite lors de la réponse au ping:", e)
            raise e
    # Le coup à faire
    def move_comm(self):
        # Définition des variables
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
        # Encoder le message
        move = choose_move(board, My_pawn, My_Blockers,ennemy_pawn)
        move_send = json.dumps(move).encode('utf-8')
        print(move_send)
        return move_send

    """def send_move(self, move):
        totalsend = 0
        move_send = json.dumps(move).encode('utf-8')
        print(move_send)
        while totalsend < len(move_send):
            sent = self.__server_socket.send(move_send)
            totalsend += sent
            print("Total :", totalsend)"""

client = Client(request_data)
server = Server()

#Prinipal code
response = client.send_request_to_server()
if response is not None:
    print("Réponse du serveur:", response)
else:
    print("Aucune réponse reçue du serveur.")
try:
    server.listen()
except KeyboardInterrupt:
    print("bye")