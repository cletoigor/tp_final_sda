import numpy as np

cv = 0.6
h = 3000.0
h_t = 0
R0 = 1
R1 = 10
alfa = (R1 - R0)/h

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

runge_kutta(20.0,100)