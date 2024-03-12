# Escreva um programa em python que receba, dois números do usuário: se o primeiro número do usuário for maior calcule e mostre o quadrado da soma dos 2 números, se o segundo número for maior calcule e mostre a soma dos quadrados dos números, caso sejam iguais mostrar imagem de erro falando que são iguais.
# Entrada de dados para valores
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
if n1 > n2:
    print(f"O quadrado da soma dos dois números é: {(n1+n2)*(n1+n2)}")
elif n1 < n2:
    print(f"A soma dos quadrados dos dois números é: {(n1*n1)+(n2*n2)}")
else:
    print("Erro, tente outra vez!!!")
