# Definindo °Celsius
valores = input("Digite as temperaturas em Kelvin: ")
Kelvin = [float(x) for x in valores.split()]


def resultados_kelvin():

    print("-" * 54)
    print(f"{'Ordem':<6}|{'Kelvin (°K)':<15} | {'Celsius (°C)':<15} | {'Fahrenheit (°F)':<15} |")
    print("-" * 54)

# Kelvin para Celsius = K - 273
# Kelvin para Fahrenheit = (K - 273) * 1.8 + 32

    k = 273.15
    f = 1.8
    f2 = 32

# Em tabelas
    for indice, k1 in enumerate(Kelvin, start=1):
        convert_c = k1 - k  # K1 = representação necessária para calcular Celcius
        convert_f = (k1 - k) * f + f2

        ordem = (f"{indice}°")

        print(f"{ordem:<6}|{k1:<15.2f} | {convert_c:<15.2f} | {convert_f:<15.2f} |")
    print("-" * 54)


resultados_kelvin()
