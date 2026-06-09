# Definindo °Celsius
valores = (input("Digite as temperaturas em Celsius: "))
celsius = [float(x) for x in valores.split()]


def resultados_celsius():

    print("-" * 60)
    print(f"{'Ordem':<6}|{'Celsius (°C)':<15} | {'Kelvin (°K)':<15} | {'Fahrenheit (°F)':<15} |")
    print("-" * 60)

# Celsius para Kelvin = C + 273
# Celsus para Farenheit = C * 1.8 + 32

    k = 273.15 
    f = 1.8
    f2 = 32

# Em tabelas
    for indice, c in enumerate(celsius, start = 1):
        convert_k = c + k
        convert_f = c * f + f2

        ordem = (f"{indice}°")

        print(f"{ordem:<6}|{c:<15.2f} | {convert_k:<15.2f} | {convert_f:<15.2f} |")
    print("-" * 60)


resultados_celsius()
