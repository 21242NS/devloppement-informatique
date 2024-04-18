import socket
import json

def send_request_to_server(server_ip, server_port, request_data):
    try:
        # Créer un socket TCP
        client_socket = socket.socket()

        # Établir une connexion avec le serveur
        client_socket.connect((server_ip, server_port))

        # Convertir le dictionnaire de la requête en chaîne JSON
        request_json = json.dumps(request_data)

        # Envoyer la requête au serveur
        client_socket.sendall(request_json.encode())

        # Attendre la réponse du serveur
        response_json = client_socket.recv(1024).decode()

        # Convertir la réponse JSON en dictionnaire
        response_data = json.loads(response_json)

        # Fermer la connexion avec le serveur
        client_socket.close()

        # Retourner la réponse du serveur
        return response_data

    except Exception as e:
        print("Une erreur s'est produite lors de l'envoi de la requête:", e)
        return None

def respond_to_ping(local_ip, server_port):
    try:
        # Créer un socket TCP
        server_socket = socket.socket()
        
        # Établir une connexion avec le client
        server_socket.bind((local_ip, server_port)) 
        server_socket.listen() 
        
        while True:
            client, adrr = server_socket.accept()
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
        server_socket.close()

# Exemple d'utilisation de la fonction send_request_to_server
local_ip = '0.0.0.0'
server_ip = '172.17.10.59'  # Adresse IP du serveur
server_port = 3000  # Port du serveur

request_data = {
    "request": "subscribe",
    "port": 3000,
    "name": "PDF_gang",
    "matricules": ["12346", "67891"]
}

response = send_request_to_server(server_ip, server_port, request_data)

if response is not None:
    print("Réponse du serveur:", response)
else:
    print("Aucune réponse reçue du serveur.")

# Réponse au ping
ping_response = respond_to_ping(local_ip, server_port)
if ping_response:
    print("Le client a répondu au ping avec succès.")
else:
    print("Une erreur s'est produite lors de la réponse au ping.")