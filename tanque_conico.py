import numpy as np
from opcua import ua, uamethod, Server

cv = 0.6
h = 3000.0
h_t = 0
R0 = 1
R1 = 10
alfa = (R1 - R0)/h

def server_opcua():
    # # Criando o servidor OPC UA
    server = Server()

    # Definindo o endpoint do servidor
    url = "opc.tcp://localhost:4840"
    server.set_endpoint(url)

    # Definindo o nome do namespace
    namespace = server.register_namespace("MyNamespace")

    # Criando o objeto de nó raiz
    root_node = server.get_objects_node()
    obj = root_node.add_object(namespace, "MyObject")

    # Adicionando uma variável ao objeto
    var = obj.add_variable(namespace, "MyVariable", 0)
    var.set_writable()  # Permitir escrita na variável

    #Inicializando o servidor
    server.start()
    print("Servidor OPC UA iniciado. Aguardando conexões...")
    # Mantendo o servidor em execução
    try:
        while True:
            pass
    except KeyboardInterrupt:
        # Encerrando o servidor quando o usuário pressionar Ctrl+C
        server.stop()
    return var

def runge_kutta(qin,duration):

    if duration < 100:
        return print('escolha um valor de pelo menos 100ms')
    
    else:

        h = 3000.0
        t = 0.0
        qout = (cv * np.sqrt(h))
        qout = round(qout.real,2)
        h = h - qout
        h = round(h,2)

        # Lista para armazenar os valores calculados
        t_values = [t]
        h_values = [h_t]

        while t < duration:
            # Cálculo do próximo valor usando o método de Runge-Kutta de quarta ordem
            k1 = h * ((((-1.0 * cv) * np.sqrt(h)) / (np.pi * (R0 + alfa * h)**2.0)) + ((1.0 / (np.pi * (R1 + alfa * h)**2.0)) * qin))
            k2 = h * ((((-1.0 * cv) * np.sqrt(h)) / (np.pi * (R0 + alfa * (h + 0.5 * k1))**2.0)) + ((1.0 / (np.pi * (R1 + alfa * (h + 0.5 * k1))**2.0)) * qin))
            k3 = h * ((((-1.0 * cv) * np.sqrt(h)) / (np.pi * (R0 + alfa * (h + 0.5 * k2))**2.0)) + ((1.0 / (np.pi * (R1 + alfa * (h + 0.5 * k2))**2.0)) * qin))
            k4 = h * ((((-1.0 * cv) * np.sqrt(h)) / (np.pi * (R0 + alfa * (h + k3))**2.0)) + ((1.0 / (np.pi * (R1 + alfa * (h + k3))**2.0)) * qin))

            h = h + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            t += h

            # Armazenar os valores calculados
            t_values.append(t)
            h_values.append(h)

        print(round(h_values[-1],2))
        return round(h_values[-1],2)

var = server_opcua()
print("valor da variavel atualizada")
print(var)
#runge_kutta(20.0,100)