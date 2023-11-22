import cv2
import os

def tirar_foto_tecla(tecla, pasta_destino="Foto_capturada"):
    # Obtém o caminho absoluto do diretório do script
    diretorio_script = os.path.dirname(os.path.abspath(__file__))

    # Cria o caminho absoluto para a pasta destino
    pasta_destino_abs = os.path.join(diretorio_script, pasta_destino)

    # Cria a pasta se não existir
    if not os.path.exists(pasta_destino_abs):
        os.makedirs(pasta_destino_abs)

    # Inicializa a câmera
    cap = cv2.VideoCapture(0)

    # Verifica se a câmera está aberta corretamente
    if not cap.isOpened():
        print("Erro ao abrir a câmera.")
        return

    print("Pressione a tecla '{}' para tirar a foto.".format(tecla))

    while True:
        # Captura um quadro da câmera
        ret, frame = cap.read()

        # Exibe o quadro em uma janela
        cv2.imshow("Pressione '{}' para tirar a foto".format(tecla), frame)

        # Aguarda pela tecla especificada
        key = cv2.waitKey(1)
        if key == ord(tecla):
            # Salva a foto na pasta destino
            nome_arquivo = os.path.join(pasta_destino_abs, "foto.jpg")
            cv2.imwrite(nome_arquivo, frame)
            print("Foto tirada com sucesso! Salva como {}".format(nome_arquivo))
            break

    # Libera os recursos da câmera e fecha a janela
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Chama a função para tirar a foto pressionando a tecla 'c'
    tirar_foto_tecla('c', pasta_destino="Foto_capturada")