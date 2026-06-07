# Definindo °Fahrenheit
fahrenheit = float(input("Digite temperatura em Fahrenheit: "))


def resultado_fahrenheit():
    # Convertendo °F para °C
    celsius = (fahrenheit - 32) / (9/5)
    print(f"{fahrenheit:.2}°F convertido para Celsius: {celsius:.2f}°C")
# Convertendo °F para °K
    kelvin = (fahrenheit - 32) * (5/9) + 273.15
    print(f"{fahrenheit:.2}°F convertido para Kelvin: {kelvin:.2f}°K")
