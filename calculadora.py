# importando a biblioteca os
import os
# função para somar os números
def soma():
    os.system('cls')
    res = num1 + num2
    print('________________________')
    print('')
    print(res)
    print('________________________')
    print('')
# função para subtrair os números 
def sub():
    os.system('cls')
    res= num1 - num2
    print('________________________')
    print('')
    print(res)
    print('________________________')
    print('')
# função para dividir os números 
def div():
    os.system('cls')
    res= num1 / num2
    print('________________________')
    print('')
    print(res)
    print('________________________')
    print('')
# função para multiplicar os numeros
def mult():
    os.system('cls')
    res = num1 * num2
    print('________________________')
    print('')
    print(res)
    print('________________________')
    print('')
# função para potencializar os números 
def elevado():
    os.system('cls')
    res = num1 ** num2
    print('________________________')
    print('')
    print(res)
    print('________________________')
    print('')
# função para mostrar o resto da divisão
def resto_divisao():
    os.system('cls')
    res = num1 % num2
    print('________________________')
    print('')
    print(res)
    print('________________________')
    print('')
# função para encerrar o programa    
def sair():
    os.system('cls')
    print('Encerrando calculadora')
    exit()
# iniciamos o códigos de repetição, enqunato o cliente não escolher a opção sair o código continuará 
while True:
    escolha = int(input(' 1.soma\n 2.subtração\n 3.divisão\n 4.multiplicação\n 5.potencia\n 6.resto da divisão\n 7.Sair\n  Digite uma opção: '))
    if escolha == 7:
        # se a escolha do usuário for 7 o programa encerra
        sair()
    else:
        # caso não seja, o programa pede 2 numeros para o usuário 
        num1 = float(input('Primeiro numero: '))
        num2 = float(input('Segundo numero: '))
        if escolha == 1:
            # caso o usuário escolha a opção 1, chamamos a função soma 
            soma()
        elif escolha == 2:
             # caso o usuário escolha a opção 2, chamamos a função sub
            sub()
        elif escolha == 3:
             # caso o usuário escolha a opção 3, chamamos a função div 
            div()
        elif escolha == 4:
             # caso o usuário escolha a opção 4, chamamos a função mult 
            mult()
        elif escolha == 5:
             # caso o usuário escolha a opção 5, chamamos a função elevado
            elevado()
        elif escolha == 6:
             # caso o usuário escolha a opção 6, chamamos a função resto_divisao
            resto_divisao()
        else:
            # caso não seja nenhuma a opção é inválida 
            print('Opção invalida!')



