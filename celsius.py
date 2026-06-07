# Definindo °Celsius
celsius = (float(input("Digite temperatura em Celsius: ")))


def resultado_celsius():
    # Convertendo °C para °K
    kelvin = celsius + 273.15
    print(f"{celsius:.2f}°C convertido para Kelvin: {kelvin:.2f}°K")
# Convertendo °C para °F
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius:.2f}°C convertido para Fahrenheit: {fahrenheit:.2f}°F")
