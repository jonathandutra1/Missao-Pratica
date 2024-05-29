#Adiçao #########################################################
def adicao(a, b):
    return a + b

resultado = adicao(5, 3)

print(f'O resultado da soma é: {resultado}')


#Subtraçao ######################################################


def subtração(a, b):
    return a - b

resultado = subtração(5, 3)

print(f'O resultado da Subtração é: {resultado}')

#Multiplocaçao #####################################################

def multiplicação(a, b):
    return a * b

resultado = multiplicação(5, 3)

print(f'O resultado da Multiplicação é: {resultado}')



#Divisao  ##################################################


def divisao(a, b):
   
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b


resultado = divisao(5, 3)
print(f"O resultado da divisão é: {resultado}")

resultado = divisao(5, 0)
print(f"O resultado da divisão é: {resultado}")

#########################################################

#Calculadora ############################################



a = float(input("Primeiro número:"))
b = float(input("Segundo número:"))
operação = input("Digite a operação a realizar (+,-,* ou /):")
if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)

saida = input("Deseja continuar (S/N)? ").upper()
while str(resultado) != 'N':
    resultado = input("Deseja continuar? ")
    if resultado != 'S' and resultado != 's':
        break