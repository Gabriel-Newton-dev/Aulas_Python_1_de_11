#programa para verificar a média do bimestre.
a = int(input("Primeiro bimestre: "))
if a > 10:
    a = int(input("Você digitou a nota errada. Primero bimestre:  "))
b = int(input("Segundo bimestre: "))
if b > 10:
    b = int(input("Você digitou a nota errada. Segundo bimestre:  "))
c = int(input("Terceiro bimestre: "))
if c > 10:
    c = int(input("Você digitou a nota errada. Terceiro bimestre:  "))
d = int(input("Quarto bimestre: "))
if d > 10:
    d = int(input("Você digitou a nota errada. Quarto bimestre:  "))
media = (a + b  + c + d) / 4
print("media: {} " .format(media) )

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print("media: {} " .format(media) )
# else:
#     print("Foi informada alguma nota inválida, favor revisar as notas inseridas ")


#programa para verificar se o número é par
# a = int(input("Entre com o primeiro valor: "))
# b = int(input("Entre com o segundo valor: "))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print("Foi digitado um número par")
# else:
#     print("Nenhum número par foi digitado")


#programa para verificar qual maior número digitado pelo usuário
# para verificar qual maior número temos que fazer a conversão de string para inteiros
# a = int(input("A - Favor inserir primeiro valor: "))
# b = int(input("B - Favor inserir segundo valor: "))
# c = int(input("C - Favor inserir o terceiro valor: "))
# if a > b and a > c:
#     print("O maior número que foi solicitado é o da letra A, número: {} " .format(a))
# elif b > a and b > c: #else com if é elif
#     print("O maior número que foi solicitado é o da letra B, número: {}" .format(b))
# else:
#     print("O maior número que foi solicitado é o da letra C, número: {}" .format(c))
# print("Final do programa")
