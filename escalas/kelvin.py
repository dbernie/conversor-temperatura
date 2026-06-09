# Definindo  °Kelvin
kelvin = (float(input("Digite temperatura em Kelvin: ")))


def resultado_kelvin():

    print("-" * 54)
    print(f"|{'Kelvin (°K)':<15} | {'Celsius (°C)':<15} | {'Fahrenheit (°F)':<15} |")
    print("-" * 54)

    celsius = kelvin - 273.15
    fahrenheit = 1.8 * (kelvin - 273.15) + 32

    print(f"|{kelvin:<15.2f} | {celsius:<15.2f} | {fahrenheit:<15.2f} |")
    print("-" * 54)


