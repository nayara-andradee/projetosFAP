import random

# Listas de palavras por categoria
palavras_faceis = ['gato', 'cão', 'pato', 'sol']
palavras_medias = ['janela', 'caneta', 'bonito', 'camelo']
palavras_dificeis = ['hipopotamo', 'caracteristica', 'astronauta', 'paralelepipedo']

#fun para escolha de categoria
def escolher_palavra(categoria):
    if categoria == 'facil':
        return random.choice(palavras_faceis)
    elif categoria == 'medio':
        return random.choice(palavras_medias)
    elif categoria == 'dificil':
        return random.choice(palavras_dificeis)
    else:
        print("Categoria inválida!")
        return None

# fun para definir a quantidade de erros permitidos
def quant_erros(categoria):
    if categoria == 'facil':
        return 6
    elif categoria == 'medio':
        return 4
    elif categoria == 'dificil':
        return 3

def jogar():
    print("*** Bem vindo ao jogo da Forca! ***")
    
    # Solicitar categoria ao usuario
    categoria = input("Escolha a categoria (facil, medio, dificil): ").lower()
    
    palavra_secreta = escolher_palavra(categoria)
    
    if not palavra_secreta:
        print("Erro ao selecionar a palavra. Encerrando o jogo.")
        return
    
    # *len? para criar uma lista de __ para o numeros de letras da palavra secreta
    letras_acertadas = ["_"] * len(palavra_secreta)

    # variavel para difinir a quantidade de erros diacordo com a categoria
    dificuldade = quant_erros(categoria)

    enforcou = False
    acertou = False
    erros = 0
    primeira_tentativa = True

    while not enforcou and not acertou:
        print("\nJogando...")
        #.join? usado para concatenar uma string(palavra) com um separador especifico, nesse caso um espaço
        print("Palavra:", " ".join(letras_acertadas))

        chute = input("Já sabe qual a palavra? Senão, chute uma letra: ").lower()

        index = 0
        if len(chute) == 1: #se o usuario chutou apenas uma letra
            if chute in palavra_secreta:
            #enumerate? fun embutida no python que mostra tanto o valor quanto o index 
            #preferi usar o index por saber como usar
                for letra in palavra_secreta:
                    if letra == chute:
                        letras_acertadas[index] = letra
                    index += 1
            else:
                erros += 1
                print(f"Erros: {erros} de {dificuldade}")
        elif len(chute) > 1: #se o chute for uma palavra
            if chute == palavra_secreta:
                letras_acertadas = list(palavra_secreta)
                acertou = True
                #se errar a palavra enforcou
            else:
                enforcou = True
        
        primeira_tentativa = False #primeira tentativa ja foi 

        enforcou = enforcou or erros == dificuldade
        acertou = acertou or "_" not in letras_acertadas

    if acertou:
        print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
    else:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")
    print("Fim do jogo")

jogar()
