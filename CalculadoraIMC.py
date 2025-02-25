def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc <= 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc <= 34.9:
        classificacao = "Obesidade grau 1"
    elif 35 <= imc <= 39.9:
        classificacao = "Obesidade grau 2"
    else:
        classificacao = "Obesidade grau 3"

    return imc, classificacao

# Exemplo de uso
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc, classificacao = calcular_imc(peso, altura)
print(f"Seu IMC é {imc:.2f} - Classificação: {classificacao}")
