import cv2
import os

def tirar_e_salvar_fotos():
    # Abre a câmera padrão (0) ou outra câmera se especificado (por exemplo, 1, 2, etc.)
    cap = cv2.VideoCapture(0)

    # Verifica se a câmera foi aberta corretamente
    if not cap.isOpened():
        print("Erro ao abrir a câmera.")
        return

    # Cria a pasta "Images" se não existir
    if not os.path.exists('Imagens_cadastradas'):
        os.makedirs('Imagens_cadastradas')

    contador = 1

    while True:
        # Lê um frame da câmera
        ret, frame = cap.read()

        # Exibe o frame na janela
        cv2.imshow('Câmera', frame)

        # Tira a foto quando a tecla 'c' é pressionada
        if cv2.waitKey(1) & 0xFF == ord('c'):
            # Gera o caminho para a imagem
            image_path = os.path.join('Imagens_cadastradas', f'foto_{contador}.png')

            # Salva a foto no caminho especificado
            cv2.imwrite(image_path, frame)

            print(f"Foto {contador} salva em: {image_path}")
            contador += 1

        # Sai do loop quando a tecla 'q' é pressionada
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera os recursos
    cap.release()
    cv2.destroyAllWindows()

# Chama a função para tirar e salvar fotos
tirar_e_salvar_fotos()