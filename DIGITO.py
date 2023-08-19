import random
import time
import py_compile


cores = {'azul': '\33[34m',
         'amarelo': '\33[33m',
         'verde': '\33[32m',
         'vermelho': '\33[31m',
         'limpa': '\33[m'}

def adivinha ():
    ##JOGO DE ADIVINHAÇÃO##
    print("Ótimo vamos começar!!!")
    time.sleep(1)
    print(f'{cores["verde"]}--+--{cores["limpa"]}' * 15)
    print(f'{cores["verde"]}Pensarei em um numero de 0 a 10 tente adivinhar !!')  # começa o jogo
    print(f'{cores["verde"]}--+--{cores["limpa"]}' * 15)
    time.sleep(1)
    num = int(input('Em que numero estou pensando ?'))
    time.sleep(1)
    print('ANALISANDO...'),
    time.sleep(1)
    print('ANALISANDO...')
    time.sleep(1)
    print('ANALISANDO...')
    time.sleep(2)
    n1 = random.randint(0, 10)
    if n1 == num:
        print(f'{cores["azul"]}Meus parabéns !!, você me VENCEU!! Estava pensando no numero {n1}\33[m')
    else:
        print(f'{cores["vermelho"]}Que pena você PERDEU ,estava pensando no numero {n1}\33[m')
    time.sleep(3)


def jokepo():
    # JOGA JOKENPO
    print('Beleza vamos jogar jokenpo')

    print('vamos jogar JOKENPO !!')
    time.sleep(2)
    print("Suas opções:")
    print('''
               |         [1] pedra          |
               |         [2] papel          |
               |         [3] tesoura        |''')

    usuario = int(input('Digite a sua escolha ?'))

    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO')

    itens = ["nulo", 'Pedra', 'Papel', 'Tesoura']
    computador = random.randint(1, 4)

    print('=*=' * 20)  # EFEITO VISUAL

    if usuario == computador:  # Os dois escolhem a mesma coisa
        print('Ambos escolhemos o mesmo, deu EMPATE')

    if computador == 1:  # O computador joga pedra
        if usuario == 3:  # O utilizador joga tesoura
            print(f'Você perdeu! eu joguei {itens[computador]}  e você jogou {itens[usuario]}!')
        elif usuario == 2:  # O utilizador joga papel
            print(f'PARABENS!!Você ganhou escolheu {itens[usuario]}, e eu escolhi {itens[computador]}')

    if computador == 2:  # O computador joga papel
        if usuario == 1:  # O utilizador joga pedra
            print(f'Você perdeu! eu joguei {itens[computador]}  e você jogou {itens[usuario]}!')
        elif usuario == 3:  # O utilizador joga tesoura
            print(f'PARABENS!!Você ganhou escolheu {itens[usuario]}, e eu escolhi {itens[computador]}')

    if computador == 3:  # o computador joga tesoura
        if usuario == 2:  # O usuario joga papel
            print(computador)
            print(f'Você perdeu! eu joguei {itens[computador]}  e você jogou {itens[usuario]}!')
        elif usuario == 1:  # O usuário joga pedra
            print(f'PARABENS!!Você ganhou escolheu {itens[usuario]}, e eu escolhi {itens[computador]}')

    print('=*=' * 20)  # EFEITO VISUAL


def piada():
    ##CONTA PIADA###

        print('Certo essa é boa !!')
        time.sleep(2)
        piada1 = input('por que ninguem gosta de bonecas russas?')

        if piada1 == 'são muito cheias de si.':
            print('Isso! Muito boa né ? kkkkk')
        else:
            print('por que elas são muito cheias de si')
            print('muito boa né ? kkkk')


def analizador():

    print('BELEZA!! posso fazer isso !')

    print('\33[34m+-=\33[m' * 20)
    print('\33[34mANALIZADOR DE TRIANGULOS V2\33[m')
    print('\33[34m+-=\33[m' * 20)

    a = float(input('Digite o comprimento de A :'))
    b = float(input('Digite o comprimento de B :'))
    c = float(input('Digite o comprimento de C :'))

    print('\33[34m+-=\33[m' * 20)
    print('\33[34mANALIZANDO...\33[m')
    print('\33[34m+-=\33[m' * 20)
    time.sleep(2)
    if a + b > c and a + c > b and b + c > a:  # Verifica se é possivel cirar um triangulo a partir desses segumentos
        print('Esses seguimentos {} PODEM FORMAR {} um triangulo!'.format('\33[32m', '\33[m'), end='')
        if a == b == c:  # Verifica se é um triangulo equilatero
            print('\33[32mEQUILÁTERO[m!!!\33[m')
            print('Pois todos os lados são iguais !!!')

        elif a == b or b == c or a == c:  # verifica se é um triangulo isóceles
            print('\33[32mISÓCELES!!!\33[m')
            print('Pois dois lados são iguais')

        elif a != b and a != c and b != c:  # verifica se é um triangulo escaleno
            print('\33[32mESCALENO!!!\33[m')
            print('Pois todos os lados são diferentes')
    else:
        print('\33[31mEsses seguimentos NÃO PODEM FORMAR um triangulo\33[m')
    time.sleep(2)

def soma(n):
    somas = cont2 = 0
    while True:

        nS = float(input("Digite outro numero para somar:"))

        cont2 += 1
        print("=" * 10, end='>')
        print(" SOMANDO ",end='<' )
        print("=" * 10)

        if cont2 <=1:
            somas += nS + n
        else:
            somas += nS
        print(f"==> O resultado é {somas}")
        perg = str(input("Quer continuar ?[S/N]"))[0].strip()


        if perg in "Nn":
            break
        while perg not in "SsNn":
            print("Por favor apenas sim ou não ")
    print(f"A quantidade de numeros digitados foi de {cont2+1},e a SOMA deles é {somas}")
    return somas


def mult(n):
    cont  = 0
    mults = 1
    while True:
        nM = float(input("Digite outro numero para multiplicar:"))

        cont += 1
        print("=" * 10, end='>')
        print(" MULTIPLICANDO ", end='<')
        print("=" * 10)

        if cont <= 1:
            mults *= nM * n
        else:
            mults *= nM
        print(f"==> O resultado é {mults}")
        perg = str(input("Quer continuar ?[S/N]"))[0].strip()

        if perg in "Nn":
            break
        while perg not in "SsNn":
            print("Por favor apenas sim ou não ")

    print(f"A quantidade de numeros digitados foi de {cont},e a MULTIPLICAÇÃO  deles é {mults}")
    return mults


def sub(n):
    cont = 0
    subs = 0
    while True:
        cont += 1
        nSB = float(input("Digite outro numero para subtrair:"))
        print("=" * 10, end='>')
        print(" SUBTRAINDO ", end='<')
        print("=" * 10)

        if cont <= 1:
            subs -= nSB - n
        else:
            subs -= nSB
        print(f"==> O resultado é {subs}")
        perg = str(input("Quer continuar ?[S/N]"))[0].strip()

        if perg in "Nn":
            break
        while perg not in "SsNn":
            print("Por favor apenas sim ou não ")

    print(f"A quantidade de numeros digitados foi de {cont},e a SUBTRAÇÃO  deles é {subs}")
    return subs


def div(n):
    cont = 0
    divs = 1
    while True:
        cont += 1
        nDV = float(input("Digite outro numero para dividir:"))
        print("=" * 10, end='>')
        print(" DIVIDINDO ", end='<')
        print("=" * 10)

        if cont <= 1:
            divs /= nDV / n
        else:
            divs /= nDV
        print(f"==> O resultado é {divs}")
        perg = str(input("Quer continuar ?[S/N]"))[0].strip()

        if perg in "Nn":
            break
        while perg not in "SsNn":
            print("Por favor apenas sim ou não ")
    print(f"A quantidade de numeros digitados foi de {cont},e a DIVISÃO  deles é {divs}")
    return divs


def calc():
    op = 0
    print('-=-' * 10)
    print('Bem vindo a super calculadora:')
    print('-=-' * 10)
    time.sleep(1)
    n = float(input("->> Digite um numero :"))

    cont = 0
    while True:
        cont += 1
        print('=-' * 20)
        print('''isso é o que eu posso fazer !!
            [ 1 ] somar
            [ 2 ] subtrair
            [ 3 ] multiplicar
            [ 4 ] dividir
            [ 5 ] adicionar um numero
            [ 6 ] calcular fatoriais
            [ 7 ] calcular progressão aritimética 
            [ 8 ] verificar TABUADA
            [ 9 ] sair do programa''')
        print(' ')
        print('=-' * 20)
        op = int(input('>>>que operação gostaria de fazer ? '))
        # SOMA
        if op == 1:
            soma(n)

        # SUBTRAÇÃO
        if op == 2:
            sub(n)

        # MULTIPLICAÇÃO
        if op == 3:
            mult(n)

        # DIVISÃO
        if op == 4:
            div(n)

        # ADICIONAR
        if op == 5:
            n = float(input("Digite um numero:"))

        # FATORIAL
        if op == 6:
            print("+=" * 10)
            print("Calculador de fatoriais!!")
            print("+=" * 10)
            time.sleep(1)
            print('Analizando...')
            c = n
            f = 1
            print('Calculando {}! = '.format(n), end='')
            while c > 0:
                print('{}'.format(c), end='')
                print(' x ' if c > 1 else ' = ', end='')
                f *= c
                c -= 1
            print('{}'.format(f))

            time.sleep(5)
        # CALCULO DE PA
        elif op == 7:
            print("+=" * 20)
            print("Progressão aritimética V3.O ")
            print("+=" * 20)
            p: int = int(input("Digite o primeiro termo:"))
            r = int(input("Digite a razão : "))
            termo = p
            c = 1
            mais = 10
            total = 0
            vic = 0
            print(p, '->', end='')
            while mais != 0:
                total = total + mais
                while c != total:
                    termo += r
                    c += 1
                    print('{}->'.format(termo), end='')
                print('PAUSA ')
                mais = int(input('Quanto termos quer mostrar a mais ?'))
            print('Progressão finalizada com {} termos'.format(total))
        # VERIFICAR TABUADA
        elif op == 8:
            while True:
                n = int(input("Digite um número real para conferir a TABUADA:"))
                print('-' * 47)
                if n < 0:
                    break
                for c in range(1, 11):
                    s = n * c
                    print(f"{n} X {c} = {s}")
                print('-' * 47)
            print("Programa Tabuada ENCERRADO!!")
        if op == 9:
            print("Fim do programa Calculadora")
            break

##--Programa principal--##

print('Olá!', end='')
time.sleep(1)
print('Eu sou DIGITO!', end=' ')
time.sleep(1)
print('Seu assistente pessoal !', end=' ')  # apresentação do DÍGITO
time.sleep(1)

while True:
    msg = input('tudo bem ?[S/n]')[0].strip()  # começa a interagir
    if msg in "Ss":
        print('Que bom que esta bem!!!')
        break
    if msg in "Nn":
        print('O que aconteceu ?')
        break
    print("Por favor apenas sim ou não")


while True:
    print('Isso é o que eu posso fazer :')
    print('[1] Abrir um analizador de triangulos')
    print('[2] Jogar um jogo de adivinhação')
    print('[3] jogar Jokenpo')
    print('[5] Abrir super calculadora ')
    print('[7] Standby')
    print('[8] Finalizar por completo')
    varmsg2 = int(input('No que posso ser útil ?'))

    #if 'myadimin' in msg :
     #   comand= str(input('Olá Lucas, tudo bem ? o que gostaria de ver :'))
    if varmsg2 == 1:
        analizador()

    elif varmsg2 == 2:
        adivinha()

    elif varmsg2 == 3:
       jokepo()

    elif varmsg2 == 4:
        piada()

    # SUPER CALCULADORA
    elif varmsg2 == 5:
        calc()





    # STANDBY
    elif varmsg2 == 7:
        print('tenha um bom dia ! ')
        rap = str(input('Se precisar, digite meu nome para reiniciar o programa: ')).strip().upper()
        if rap != 'DIGITO':
            print('dica : meu nome envolve o que você faz no computador')
        print("OLá novamente !!")
        time.sleep(2)
# Caso o usuário saia do programa
    elif varmsg2 == 8:
        print('tenha um bom dia ! ')
        print('Até a proxima , espero ter ajudado')
        break
