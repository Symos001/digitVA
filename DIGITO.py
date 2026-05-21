import random
import time

class Digito:
    def __init__(self):
        self.nome = "DÍGITO"
        self.cores = {
            'azul': '\33[34m',
            'amarelo': '\33[33m',
            'verde': '\33[32m',
            'vermelho': '\33[31m',
            'limpa': '\33[m'
        }

    def apresentar(self):
        print('Olá!', end='')
        time.sleep(1)
        print(f'Eu sou {self.nome}!', end=' ')
        time.sleep(1)
        print('Seu assistente pessoal!')
        time.sleep(1)

    def cumprimento_inicial(self):
        while True:
            msg = input('Tudo bem? [S/n] ').strip()
            if msg and msg[0] in "Ss":
                print('Que bom que está bem!!!')
                break
            elif msg and msg[0] in "Nn":
                print('O que aconteceu?')
                break
            else:
                print("Por favor, apenas sim ou não.")

    def mostrar_menu(self):
        print("\nIsso é o que eu posso fazer:")
        print('[1] Analisador de triângulos')
        print('[2] Jogo de adivinhação')
        print('[3] Jokenpô')
        print('[4] Ouvir uma piada')
        print('[5] Super calculadora')
        print('[6] Standby')
        print('[7] Finalizar programa')
        try:
            return int(input('No que posso ser útil? '))
        except ValueError:
            return -1

    def analisador(self):
        print('\nBELEZA!! posso fazer isso!')
        print(f'{self.cores["azul"]}+-={self.cores["limpa"]}' * 20)
        print(f'{self.cores["azul"]}ANALISADOR DE TRIÂNGULOS V2{self.cores["limpa"]}')
        print(f'{self.cores["azul"]}+-={self.cores["limpa"]}' * 20)

        a = float(input('Digite o comprimento de A: '))
        b = float(input('Digite o comprimento de B: '))
        c = float(input('Digite o comprimento de C: '))

        print(f'{self.cores["azul"]}+-={self.cores["limpa"]}' * 20)
        print(f'{self.cores["azul"]}ANALISANDO...{self.cores["limpa"]}')
        print(f'{self.cores["azul"]}+-={self.cores["limpa"]}' * 20)
        time.sleep(2)

        if a + b > c and a + c > b and b + c > a:
            print(f'Esses segmentos {self.cores["verde"]}PODEM FORMAR{self.cores["limpa"]} um triângulo!', end=' ')
            if a == b == c:
                print(f'{self.cores["verde"]}EQUILÁTERO!!!{self.cores["limpa"]}')
                print('Pois todos os lados são iguais!')
            elif a == b or b == c or a == c:
                print(f'{self.cores["verde"]}ISÓSCELES!!!{self.cores["limpa"]}')
                print('Pois dois lados são iguais.')
            else:
                print(f'{self.cores["verde"]}ESCALENO!!!{self.cores["limpa"]}')
                print('Pois todos os lados são diferentes.')
        else:
            print(f'{self.cores["vermelho"]}Esses segmentos NÃO PODEM FORMAR um triângulo.{self.cores["limpa"]}')
        time.sleep(2)

    def adivinha(self):
        print("Ótimo, vamos começar!!!")
        time.sleep(1)
        print(f'{self.cores["verde"]}--+--{self.cores["limpa"]}' * 15)
        print(f'{self.cores["verde"]}Pensarei em um número de 0 a 10, tente adivinhar!!{self.cores["limpa"]}')
        print(f'{self.cores["verde"]}--+--{self.cores["limpa"]}' * 15)
        time.sleep(1)

        num = int(input('Em que número estou pensando? '))
        for _ in range(3):
            print('ANALISANDO...')
            time.sleep(1)
        time.sleep(1)

        n1 = random.randint(0, 10)
        if n1 == num:
            print(f'{self.cores["azul"]}Meus parabéns!! Você me VENCEU! Estava pensando no número {n1}{self.cores["limpa"]}')
        else:
            print(f'{self.cores["vermelho"]}Que pena, você PERDEU. Estava pensando no número {n1}{self.cores["limpa"]}')
        time.sleep(3)

    def jokepo(self):
        print('Beleza, vamos jogar JOKENPÔ!!')
        time.sleep(2)
        print("Suas opções:")
        print('''
                   |         [1] pedra          |
                   |         [2] papel          |
                   |         [3] tesoura        |''')

        usuario = int(input('Digite a sua escolha: '))

        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PÔ!')

        itens = ["nulo", 'Pedra', 'Papel', 'Tesoura']
        computador = random.randint(1, 3)   # CORRIGIDO: agora só 1, 2 ou 3

        print('=*=' * 20)

        if usuario == computador:
            print('Ambos escolhemos o mesmo, deu EMPATE!')
        elif computador == 1:
            if usuario == 3:
                print(f'Você perdeu! Eu joguei {itens[computador]} e você jogou {itens[usuario]}.')
            elif usuario == 2:
                print(f'PARABÉNS!! Você ganhou! Escolheu {itens[usuario]} e eu escolhi {itens[computador]}.')
        elif computador == 2:
            if usuario == 1:
                print(f'Você perdeu! Eu joguei {itens[computador]} e você jogou {itens[usuario]}.')
            elif usuario == 3:
                print(f'PARABÉNS!! Você ganhou! Escolheu {itens[usuario]} e eu escolhi {itens[computador]}.')
        elif computador == 3:
            if usuario == 2:
                print(f'Você perdeu! Eu joguei {itens[computador]} e você jogou {itens[usuario]}.')
            elif usuario == 1:
                print(f'PARABÉNS!! Você ganhou! Escolheu {itens[usuario]} e eu escolhi {itens[computador]}.')

        print('=*=' * 20)
        time.sleep(2)

    def piada(self):
        print('Certo, essa é boa!!')
        time.sleep(2)
        resposta = input('Por que ninguém gosta de bonecas russas? ').strip().lower()
        # Aceita a resposta sem acentos e com pequenas variações
        if 'cheias de si' in resposta:
            print('Isso! Muito boa né? kkkkk')
        else:
            print('Porque elas são muito cheias de si!')
            print('Muito boa né? kkkk')
        time.sleep(2)

    # Métodos auxiliares da calculadora
    def _soma(self, n):
        somas = cont2 = 0
        while True:
            nS = float(input("Digite outro número para somar: "))
            cont2 += 1
            print("=" * 10, end='>')
            print(" SOMANDO ", end='<')
            print("=" * 10)
            if cont2 <= 1:
                somas += nS + n
            else:
                somas += nS
            print(f"==> O resultado é {somas}")
            perg = input("Quer continuar? [S/N] ").strip()
            if perg and perg[0] in "Nn":
                break
            while perg and perg[0] not in "SsNn":
                perg = input("Por favor, apenas sim ou não: ").strip()
        print(f"A quantidade de números digitados foi {cont2+1} e a SOMA deles é {somas}")
        return somas

    def _sub(self, n):
        cont = 0
        subs = 0
        while True:
            nSB = float(input("Digite outro número para subtrair: "))
            cont += 1
            print("=" * 10, end='>')
            print(" SUBTRAINDO ", end='<')
            print("=" * 10)
            if cont <= 1:
                subs = n - nSB   # lógica corrigida: primeira subtração é n - nSB
            else:
                subs -= nSB
            print(f"==> O resultado é {subs}")
            perg = input("Quer continuar? [S/N] ").strip()
            if perg and perg[0] in "Nn":
                break
            while perg and perg[0] not in "SsNn":
                perg = input("Por favor, apenas sim ou não: ").strip()
        print(f"A quantidade de números digitados foi {cont} e a SUBTRAÇÃO deles é {subs}")
        return subs

    def _mult(self, n):
        cont = 0
        mults = 1
        while True:
            nM = float(input("Digite outro número para multiplicar: "))
            cont += 1
            print("=" * 10, end='>')
            print(" MULTIPLICANDO ", end='<')
            print("=" * 10)
            if cont <= 1:
                mults = n * nM   # primeira multiplicação
            else:
                mults *= nM
            print(f"==> O resultado é {mults}")
            perg = input("Quer continuar? [S/N] ").strip()
            if perg and perg[0] in "Nn":
                break
            while perg and perg[0] not in "SsNn":
                perg = input("Por favor, apenas sim ou não: ").strip()
        print(f"A quantidade de números digitados foi {cont} e a MULTIPLICAÇÃO deles é {mults}")
        return mults

    def _div(self, n):
        cont = 0
        divs = n   # o valor inicial é o próprio n (para a primeira divisão)
        while True:
            nDV = float(input("Digite outro número para dividir: "))
            cont += 1
            print("=" * 10, end='>')
            print(" DIVIDINDO ", end='<')
            print("=" * 10)
            if cont <= 1:
                divs = n / nDV
            else:
                divs /= nDV
            print(f"==> O resultado é {divs}")
            perg = input("Quer continuar? [S/N] ").strip()
            if perg and perg[0] in "Nn":
                break
            while perg and perg[0] not in "SsNn":
                perg = input("Por favor, apenas sim ou não: ").strip()
        print(f"A quantidade de números digitados foi {cont} e a DIVISÃO deles é {divs}")
        return divs

    def calc(self):
        print('-=-' * 10)
        print('Bem-vindo à super calculadora!')
        print('-=-' * 10)
        time.sleep(1)
        n = float(input("->> Digite um número: "))

        while True:
            print('=-' * 20)
            print('''Isso é o que eu posso fazer:
            [ 1 ] somar
            [ 2 ] subtrair
            [ 3 ] multiplicar
            [ 4 ] dividir
            [ 5 ] adicionar um número
            [ 6 ] calcular fatorial
            [ 7 ] calcular progressão aritmética
            [ 8 ] verificar TABUADA
            [ 9 ] sair da calculadora''')
            print('=-' * 20)
            try:
                op = int(input('>>> Que operação gostaria de fazer? '))
            except ValueError:
                continue

            if op == 1:
                self._soma(n)
            elif op == 2:
                self._sub(n)
            elif op == 3:
                self._mult(n)
            elif op == 4:
                self._div(n)
            elif op == 5:
                n = float(input("Digite um novo número: "))
            elif op == 6:
                print("+=" * 10)
                print("Calculador de fatoriais!!")
                print("+=" * 10)
                time.sleep(1)
                print('Analisando...')
                c = int(n)
                f = 1
                print(f'Calculando {n}! = ', end='')
                while c > 0:
                    print(f'{c}', end='')
                    print(' x ' if c > 1 else ' = ', end='')
                    f *= c
                    c -= 1
                print(f'{f}')
                time.sleep(2)
            elif op == 7:
                print("+=" * 20)
                print("Progressão Aritmética V3.0")
                print("+=" * 20)
                p = int(input("Digite o primeiro termo: "))
                r = int(input("Digite a razão: "))
                termo = p
                c = 1
                mais = 10
                total = 0
                print(f'{p} -> ', end='')
                while mais != 0:
                    total += mais
                    while c < total:
                        termo += r
                        c += 1
                        print(f'{termo} -> ', end='')
                    print('PAUSA')
                    mais = int(input('Quantos termos quer mostrar a mais? '))
                print(f'Progressão finalizada com {total} termos.')
            elif op == 8:
                while True:
                    num = int(input("Digite um número para ver a tabuada (negativo p/ sair): "))
                    if num < 0:
                        break
                    print('-' * 47)
                    for c in range(1, 11):
                        print(f"{num} X {c} = {num * c}")
                    print('-' * 47)
                print("Programa Tabuada ENCERRADO!")
            elif op == 9:
                print("Fim do programa Calculadora.")
                break

    def executar(self):
        self.apresentar()
        self.cumprimento_inicial()

        while True:
            opcao = self.mostrar_menu()
            if opcao == 1:
                self.analisador()
            elif opcao == 2:
                self.adivinha()
            elif opcao == 3:
                self.jokepo()
            elif opcao == 4:
                self.piada()
            elif opcao == 5:
                self.calc()
            elif opcao == 6:
                print('Tenha um bom dia!')
                rap = input('Se precisar, digite meu nome para reiniciar: ').strip().upper()
                if rap != 'DIGITO':
                    print('Dica: meu nome envolve o que você faz no computador.')
                print("Olá novamente!!")
                time.sleep(2)
                # volta ao menu principal automaticamente
            elif opcao == 7:
                print('Tenha um bom dia!')
                print('Até a próxima, espero ter ajudado.')
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    assistente = Digito()
    assistente.executar()
