import cv2
import os
import numpy as np


def calcular_diferenca(imagem1, imagem2):
    # Redimensiona as imagens para terem o mesmo tamanho
    imagem1 = cv2.resize(imagem1, (imagem2.shape[1], imagem2.shape[0]))

    # Converte as imagens para escala de cinza
    cinza1 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)
    cinza2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)

    # Calcula a diferença absoluta entre as imagens
    diferenca = cv2.absdiff(cinza1, cinza2)

    # Calcula a similaridade entre as imagens
    similaridade = 1 - np.mean(diferenca) / 255.0

    return similaridade


def comparar_com_todas_as_imagens(imagem_a_comparar, pasta_imagens, limite_similaridade=0.8):
    imagens = []

    # Carrega a imagem para comparar
    imagem1 = cv2.imread(imagem_a_comparar)

    for arquivo in os.listdir(pasta_imagens):
        # Ignora arquivos que não são imagens
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            caminho_imagem = os.path.join(pasta_imagens, arquivo)
            imagem2 = cv2.imread(caminho_imagem)

            # Calcula a similaridade entre as imagens
            similaridade = calcular_diferenca(imagem1, imagem2)

            # Adiciona à lista se a similaridade for maior que o limite
            if similaridade > limite_similaridade:
                imagens.append((similaridade, caminho_imagem))

    # Ordena a lista com base na similaridade (quanto maior, melhor)
    imagens.sort(reverse=True)

    return imagens


def pessoa_reconhecida(resultados, limiar_reconhecimento=0.8):
    # Verifica se há pelo menos uma correspondência acima do limiar de reconhecimento
    if resultados and resultados[0][0] > limiar_reconhecimento:
        return True
    else:
        return False


if __name__ == "__main__":
    # Especifica a imagem para comparar
    imagem_a_comparar = "Foto_capturada/foto.jpg"

    # Especifica o diretório de imagens
    pasta_imagens = "Imagens_cadastradas"

    # Define um limite de similaridade (ajuste conforme necessário)
    limite_similaridade = 0.8

    # Compara a imagem com todas as imagens na pasta especificada
    resultados = comparar_com_todas_as_imagens(imagem_a_comparar, pasta_imagens, limite_similaridade)

    # Exibe os resultados
    print("Imagem de referência:", imagem_a_comparar)

    if pessoa_reconhecida(resultados):
        print("\nPessoa reconhecida!")
        print("Melhor correspondência:", resultados[0][1])
        print("Similaridade:", resultados[0][0])
    else:
        print("\nPessoa desconhecida.")