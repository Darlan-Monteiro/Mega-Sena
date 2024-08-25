# mega-sena
import random

def sortear_numero():
    return random.sample(range(1, 61), 6)

def pegar_numeros_do_usuario():
    while True:
        numeros_usuario = []
        while len(numeros_usuario) < 6:
            try:
                numero = int(input(f'Digite o {len(numeros_usuario) + 1}º número entre 1 e 60: '))
                if numero < 1 or numero > 60:
                    print('Número maior que 60 ou menor que 1. Tente novamente.')
                elif numero in numeros_usuario:
                    print('Número já inserido. Tente novamente.')
                else:
                    numeros_usuario.append(numero)
            except ValueError:
                print('Erro! Insira apenas um número inteiro.')

        return numeros_usuario


def main():
    numeros_sorteados = sortear_numero()
    numeros_usuario = pegar_numeros_do_usuario()
    acertos = set(numeros_sorteados).intersection(numeros_usuario) #intersection pra verificar os número iguais entre o jogo do usuário e os sprteados
    print(f'Os seus números jogados foram: {numeros_usuario}')
    print(f'Os números sorteados foram: {numeros_sorteados}')
    print(f'Você acertou {len(acertos)} número(s): {acertos}')

main()
