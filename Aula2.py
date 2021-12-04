print("iremos verificar os demais operadores Aritimeticos")
a = int(input("Entre com o primeiro valor: ")) #não consigo fazer uma soma de um texto por esse motivo utilizo o int()para conerter para inteiro
b = int(input("Entre com o segundo valor: "))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
#print("A soma é : {}. A subtração é : {}. A Multiplicação é : {}. A divisão é : {}. " .format(soma,subtracao,multiplicacao,divisao) #outra forma de converter a variavel ele print("A soma é: " + str(soma)) #para converter número inteiro em string (str) concatenou
print("A Soma é: " +str(soma))
print("A Subtração é: " + str(subtracao))
print("A multiplicação é :" + str(multiplicacao))
print("A divisão é: " + str(divisao)) #para converter de float para int, utiliza o int. ex: print(int(divisão))
print("O resto é : " + str(resto))
print(type(divisao)) #type para saber qual é o tipo da variavel
x = "1"
soma2 = int(x) + 1
print(soma2)

