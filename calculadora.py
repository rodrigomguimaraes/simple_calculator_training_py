# fazer uma calculadora armazenando dados e realizando contas simples

#Separando as variaveis

num1     = 0
num2     = 0
result   = 0
operador = 0

# Atribuindo valor as variaveis com o comando input
while True:
    num1 = float (input("Digite o primeiro número: "))
    operador = (input("Digite a operação matematica desejada: "))
    num2 = float (input("Digite o segundo número: "))

    #Fazendo as condicionais para resolver o que foi digitado

    if operador == "+":
        result = num1 + num2
    elif operador == "-":
        result = num1 - num2
    elif operador == "/":
        result = num1 / num2
    elif operador == "*":
        result = num1 * num2
    else:
        print ("Operação não reconhecida!")

    #Agora a formatação do resultado da operção

    print("{} {} {} = {}" .format(num1, operador, num2, result))