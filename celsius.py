# Definindo °Celsius
celsius = (float(input("Digite temperatura em Celsius: ")))


def resultado_celsius():
    print("-" * 54)
    print(f"|{'Celsius (°C)':<15} | {'Kelvin (°K)':<15} | {'Fahrenheit (°F)':<15} |")
    print("-" * 54)

    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.8 + 32

    print(f"|{celsius:<15.2f} | {kelvin:<15.2f} | {fahrenheit:<15.2f} |")
    print("-" * 54)



