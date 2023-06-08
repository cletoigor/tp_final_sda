import socket
from opcua import Client

# def server_tcpip():
#     # Configurações do servidor TCP IP
#     host = '127.0.0.1'  # Endereço IP do servidor
#     port = 12345  # Porta do servidor

#     # Criação do socket
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # Vincula o socket ao endereço IP e à porta
#     server_socket.bind((host, port))
#     # Aguarda conexões
#     server_socket.listen(1)

#     print("Servidor TCP/IP iniciado. Aguardando conexões...")

#     while True:
#         # Aceita uma nova conexão
#         client_socket, client_address = server_socket.accept()
#         print("Conexão estabelecida com:", client_address)

#         try:
#             # Recebe dados do cliente
#             qin = client_socket.recv(1024)
#             if qin:
#                 # Processa os dados recebidos
#                 print("Dados recebidos:", qin.decode())

#                 # Envie uma resposta para o cliente
#                 response = "Mensagem recebida pelo servidor."
#                 client_socket.sendall(response.encode())

#         except Exception as e:
#             print("Erro durante a comunicação:", str(e))

#         finally:
#             # Fecha a conexão com o cliente
#             client_socket.close()
#             print("Conexão encerrada com:", client_address)

#         return qin

def client_opcua(qin):
        
    # Endereço do servidor OPC UA
    server_url = "opc.tcp://localhost:4840"

    # Criar instância do cliente OPC UA
    client = Client(server_url)
    try:
        # Conectar ao servidor OPC UA
        client.connect()
        print("Conexão estabelecida com o servidor OPC UA.")
        var_node = client.get_node("ns=2;i=1")  # Substitua pelo NodeID da variável desejada

        new_value = qin  # Substitua pelo valor que você deseja escrever

        var_node.set_value(new_value)
        print("Valor da variável qin atualizado para: ", new_value)

    finally:
        # Desconectar do servidor OPC UA
        client.disconnect()

client_opcua(10)