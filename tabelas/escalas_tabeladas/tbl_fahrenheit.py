# Definindo °Celsius
valores = input("Digite as temperaturas em Fahrenheit: ")
Fahrenheit = [float(x) for x in valores.split()]


def resultados_fahrenheit():

    print("-" * 60)
    print(f"{'Ordem':<6}|{'Fahrenheit (°F)':<15} | {'Celsius (°C)':<15} | {'Kelvin (°K)':<15} |")
    print("-" * 60)

# Fahrenheit para Celsius = (fahrenheit - 32) / (9/5)
# Fahrenheit para Kelvin = (fahrenheit - 32) * (5/9) + 273.15

    k = 273.15
    f1_k = (5/9)
    f1_c = (9/5)
    f2 = 32

# Em tabelas
    for indice, f in enumerate(Fahrenheit, start=1):
        convert_c = (f - f2) / f1_c
        convert_k = (f - f2) * f1_k + k

        ordem = (f"{indice}°")

        print(f"{ordem:<6}|{f:<15.2f} | {convert_c:<15.2f} | {convert_k:<15.2f} |")
    print("-" * 60)


resultados_fahrenheit()
