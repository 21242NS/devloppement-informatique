import socket
import json

local_ip = 'localhost'
server_ip = '172.17.3.30'  # Adresse IP du serveur
server_port = 3000  # Port du serveur

request_data = {
    "request": "subscribe",
    "port": 3000,
    "name": "PDF_gang",
    "matricules": ["12346", "67891"]
}

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
            response_json = self.__client_socket.recv(1024).decode()

            # Convertir la réponse JSON en dictionnaire
            response_data = json.loads(response_json)

            # Fermer la connexion avec le serveur
            self.__client_socket.close()

            # Retourner la réponse du serveur
            return response_data

        except Exception as e:
            print("Une erreur s'est produite lors de l'envoi de la requête:", e)
            return None
client = Client(request_data)

class Server:
    def __init__(self):
        # Créer un socket TCP
        self.__server_socket = socket.socket()
        # Établir une connexion avec le client
        self.__server_socket.bind((local_ip, server_port))

    def respond_to_ping(self):
        try:
            self.__server_socket.listen() 
            
            while True:
                client, adrr = self.__server_socket.accept()
                # Attendre la demande du client
                data = client.recv(1024).decode()
                request_ping = json.loads(data)
                # Vérifier si la demande est un "ping"
                
                if request_ping.get("request") == "ping":

                    # Répondre avec "pong"
                    response_data = {"response": "pong"}
                    response_ping = json.dumps(response_data)
                    client.sendall(response_ping.encode())
                    return True
                else:
                    return False

        except Exception as e:
            print("Une erreur s'est produite lors de la réponse au ping:", e)
            #raise e
            return False
        finally:
            self.__server_socket.close()
server = Server()
# Exemple d'utilisation de la fonction send_request_to_server
response = client.send_request_to_server()

if response is not None:
    print("Réponse du serveur:", response)
else:
    print("Aucune réponse reçue du serveur.")

# Réponse au ping
ping_response = server.respond_to_ping()
if ping_response:
    print("Le client a répondu au ping avec succès.")
else:
    print("Une erreur s'est produite lors de la réponse au ping.")