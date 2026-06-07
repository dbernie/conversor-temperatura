# Definindo  °Kelvin
kelvin = (float(input("Digite temperatura em Kelvin: ")))


def resultado_kelvin():
# Convertendo °K para °C
    celsius = kelvin - 273.15
    print(f"{kelvin:.2f}°K convertido para Celsius: {celsius:.2f}°C")
# Convertendo °K para °F
    fahrenheit = 1.8 * (kelvin - 273.15) + 32
    print(f"{kelvin:.2f}°K convertido para Fahrenheit: {fahrenheit:.2f}°F")
