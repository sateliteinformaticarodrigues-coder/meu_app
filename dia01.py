# Dia 1 - variaveis, tipos e f-strings

nome = input("Qual é o seu nome? ").strip()
idade = int(input("Qual é a sua idade? "))
altura = float(input("Qual é a sua altura (m)? "))
peso = float(input("Qual é o seu peso (kg)? "))

imc = peso / (altura ** 2)

print(f"Olá, {nome}!")
print(f"Daqui a 10 anos você terá {idade + 10} anos.")
print(f"Seu IMC é {imc:.2f}")
print(f"imc é do tipo {type(imc).__name__}")
