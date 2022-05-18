import os
import random

nome = input('\nDigite seu nome: ')
print(f'Olá {nome.title()}, seja bem vindo ao jogo da forca!')
input('Pressione a tecla enter para começar o jogo: ')
os.system('cls')

lista_de_palavras = ['banana', 'laranja', 'abacaxi','limão', 'uva','morango']
palavra_selecionada = random.choice(lista_de_palavras).upper()
tamanho_palavra = len(palavra_selecionada)
palavra_codificada = ['_']*tamanho_palavra
quantidade_de_erros = 0

while '_' in palavra_codificada == True and quantidade_de_erros < 6:
    print(f'Sua palavra tem {tamanho_palavra} letras!')
    print(f'Erros: {quantidade_de_erros} de 6 tentativas')
    for letra in palavra_codificada:
        print(letra, end = ' ')
    print()
    
    letra_escolhida = input('Digite uma letra: ').upper()
    acertou = False    
    for i in range(tamanho_palavra):
        if letra_escolhida == palavra_selecionada[i]:
            palavra_codificada[i] = letra_escolhida
        acertou = True
    if acertou == True:
        print('parabéns, acertou!')
    else:
        print('A letra não existe na palavra!')
        quantidade_de_erros += 1
    
    if quantidade_de_erros == 6:
        print('Você perdeu, foi mal ai!')
    else:
        print('Parabens, você ganhou.')

print(f'A palavra era {palavra_selecionada}!')