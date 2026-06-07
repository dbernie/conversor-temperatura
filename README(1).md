<div align="center">

# 🌡️ Conversor de Temperatura

**Conversor de escalas termométricas via terminal, desenvolvido em Python.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/Licença-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)
![Terminal](https://img.shields.io/badge/Interface-Terminal-black?style=for-the-badge&logo=gnometerminal&logoColor=white)

<br/>

> Projeto educacional que demonstra o uso de **módulos**, **funções** e **entrada de dados** em Python,  
> realizando conversões entre Celsius, Kelvin e Fahrenheit com precisão de duas casas decimais.

</div>

---

## 📑 Índice

- [Sobre o projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Fórmulas utilizadas](#-fórmulas-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Como executar](#-como-executar)
- [Exemplos de uso](#-exemplos-de-uso)
- [Conceitos aplicados](#-conceitos-aplicados)
- [Possíveis melhorias](#-possíveis-melhorias)
- [Autor](#-autor)
- [Licença](#-licença)

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar os fundamentos de Python, como **modularização de código**, **definição de funções**, **importação entre arquivos** e **manipulação de entrada do usuário**.

O programa recebe uma temperatura em uma das três escalas termométricas e exibe automaticamente os valores equivalentes nas outras duas escalas, com formatação precisa e legível no terminal.

---

## ✅ Funcionalidades

- [x] Conversão de **Celsius** para Kelvin e Fahrenheit
- [x] Conversão de **Kelvin** para Celsius e Fahrenheit
- [x] Conversão de **Fahrenheit** para Celsius e Kelvin
- [x] Menu interativo no terminal
- [x] Saída formatada com duas casas decimais
- [x] Código organizado em módulos separados por escala

---

## 📁 Estrutura do projeto

```
conversor-temperatura/
│
├── conversor.py       # Ponto de entrada: exibe o menu e importa o módulo correto
├── celsius.py         # Recebe °C e converte para Kelvin e Fahrenheit
├── kelvin.py          # Recebe K e converte para Celsius e Fahrenheit
├── fahrenheit.py      # Recebe °F e converte para Celsius e Kelvin
│
└── README.md
```

### Responsabilidade de cada arquivo

| Arquivo | Responsabilidade |
|---|---|
| `conversor.py` | Menu principal, leitura da escolha e importação dinâmica do módulo |
| `celsius.py` | Leitura da temperatura em °C e cálculo das conversões |
| `kelvin.py` | Leitura da temperatura em K e cálculo das conversões |
| `fahrenheit.py` | Leitura da temperatura em °F e cálculo das conversões |

---

## 🧮 Fórmulas utilizadas

| De \ Para | Celsius | Kelvin | Fahrenheit |
|---|---|---|---|
| **Celsius** | — | `K = °C + 273.15` | `°F = °C × 1.8 + 32` |
| **Kelvin** | `°C = K − 273.15` | — | `°F = 1.8 × (K − 273.15) + 32` |
| **Fahrenheit** | `°C = (°F − 32) / 1.8` | `K = (°F − 32) × 5/9 + 273.15` | — |

> **Referência:** As fórmulas seguem os padrões definidos pelo *International Bureau of Weights and Measures (BIPM)*.

---

## 🔧 Pré-requisitos

Antes de executar, certifique-se de ter instalado:

- [Python 3.x](https://www.python.org/downloads/) — nenhuma biblioteca externa é necessária.

Para verificar sua versão do Python:

```bash
python --version
# ou
python3 --version
```

---

## 🚀 Como executar

**1. Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/conversor-temperatura.git
```

**2. Acesse a pasta do projeto:**

```bash
cd conversor-temperatura
```

**3. Execute o conversor:**

```bash
python conversor.py
```

> ⚠️ Em sistemas Linux/macOS, pode ser necessário usar `python3` no lugar de `python`.

---

## 💡 Exemplos de uso

### Convertendo Celsius

```
1 - Celsius
2 - Kelvin
3 - Fahrenheit
Digite a escala base que deseja converter: 1
Digite temperatura em Celsius: 100
100.00°C convertido para Kelvin: 373.15°K
100.00°C convertido para Fahrenheit: 212.00°F
```

### Convertendo Kelvin

```
1 - Celsius
2 - Kelvin
3 - Fahrenheit
Digite a escala base que deseja converter: 2
Digite temperatura em Kelvin: 0
0.00°K convertido para Celsius: -273.15°C
0.00°K convertido para Fahrenheit: -459.67°F
```

### Convertendo Fahrenheit

```
1 - Celsius
2 - Kelvin
3 - Fahrenheit
Digite a escala base que deseja converter: 3
Digite temperatura em Fahrenheit: 32
32°F convertido para Celsius: 0.00°C
32°F convertido para Kelvin: 273.15°K
```

---

## 🧠 Conceitos aplicados

Este projeto cobre os seguintes conceitos fundamentais de Python:

- **Modularização** — separação da lógica em arquivos independentes (`.py`)
- **Importação dinâmica** — uso de `from módulo import função` dentro de condicionais
- **Funções** — encapsulamento da lógica de conversão em `def`
- **Entrada de dados** — uso de `input()` com conversão de tipo (`float`, `int`)
- **f-strings** — formatação de saída com precisão decimal (`:.2f`)
- **Estruturas condicionais** — `if / elif / else` para controle de fluxo

---

## 🔮 Possíveis melhorias

Algumas evoluções que podem ser implementadas futuramente:

- [ ] Validação de entrada (tratar valores não numéricos ou temperaturas abaixo do zero absoluto)
- [ ] Suporte à escala **Rankine**
- [ ] Modo de conversão em lote (múltiplas temperaturas de uma vez)
- [ ] Interface gráfica com `tkinter` ou `customtkinter`
- [ ] Versão web com `Flask` ou `FastAPI`
- [ ] Testes automatizados com `unittest` ou `pytest`
- [ ] Empacotamento como CLI com `argparse`

---

## 👤 Autor

Feito por **[seu nome]** — sinta-se à vontade para entrar em contato!

[![GitHub](https://img.shields.io/badge/GitHub-seu--usuario-181717?style=flat-square&logo=github)](https://github.com/seu-usuario)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-seu--perfil-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/seu-perfil)

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">
  <sub>Desenvolvido com 🐍 Python · Feito para aprender e compartilhar</sub>
</div>
