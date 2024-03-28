import socket
import json

def send_request_to_server(server_ip, server_port, request_data):
    try:
        # Créer un socket TCP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

# Exemple d'utilisation de la fonction send_request_to_server
server_ip = 'localhost'  # Adresse IP du serveur
server_port = 3000  # Port du serveur

request_data = {
    "request": "subscribe",
    "port": 3000,
    "name": "Lolo white",
    "matricules": ["12346", "67891"]
}

response = send_request_to_server(server_ip, server_port, request_data)

if response is not None:
    print("Réponse du serveur:", response)
else:
    print("Aucune réponse reçue du serveur.")
