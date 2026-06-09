# Definindo °Fahrenheit
fahrenheit = float(input("Digite temperatura em Fahrenheit: "))


def resultado_fahrenheit():

    print("-" * 54)
    print(f"|{'Fahremheit (°F)':<15} | {'Celsius (°C)':<15} | {'Kelvin (°K)':<15} |")
    print("-" * 54)

    celsius = (fahrenheit - 32) / (9/5)
    kelvin = (fahrenheit - 32) * (5/9) + 273.15

    print(f"|{fahrenheit:<15.2f} | {celsius:<15.2f} | {kelvin:<15.2f} |")
    print("-" * 54)


