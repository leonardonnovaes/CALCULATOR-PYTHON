import os

def soma():
    os.system('cls')
    res = num1 + num2
    print('________________________')
    print('')
    print(res)
    print('________________________')
    print('')

def sub():
    os.system('cls')
    res= num1 - num2
    print('________________________')
    print('')
    print(res)
    print('________________________')
    print('')

def div():
    os.system('cls')
    res= num1 / num2
    print('________________________')
    print('')
    print(res)
    print('________________________')
    print('')

def mult():
    os.system('cls')
    res = num1 * num2
    print('________________________')
    print('')
    print(res)
    print('________________________')
    print('')

def elevado():
    os.system('cls')
    res = num1 ** num2
    print('________________________')
    print('')
    print(res)
    print('________________________')
    print('')

def resto_divisao():
    os.system('cls')
    res = num1 % num2
    print('________________________')
    print('')
    print(res)
    print('________________________')
    print('')
    
def sair():
    os.system('cls')
    print('Encerrando calculadora')
    exit()

while True:
    escolha = int(input(' 1.soma\n 2.subtração\n 3.divisão\n 4.multiplicação\n 5.potencia\n 6.resto da divisão\n 7.Sair\n  Digite uma opção: '))
    if escolha == 7:
        sair()
    else:
        num1 = float(input('Primeiro numero: '))
        num2 = float(input('Segundo numero: '))
        if escolha == 1:
            soma()
        elif escolha == 2:
            sub()
        elif escolha == 3:
            div()
        elif escolha == 4:
            mult()
        elif escolha == 5:
            elevado()
        elif escolha == 6:
            resto_divisao()
        else:
            print('Opção invalida!')



