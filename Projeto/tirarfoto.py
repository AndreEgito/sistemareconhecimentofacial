import cv2

def tirar_foto(nome_arquivo="Foto_capturada.jpg"):
    # Inicializa a câmera
    cap = cv2.VideoCapture(0)

    # Verifica se a câmera está aberta corretamente
    if not cap.isOpened():
        print("Erro ao abrir a câmera.")
        return

    # Captura um quadro da câmera
    ret, frame = cap.read()

    # Salva a foto
    if ret:
        cv2.imwrite(nome_arquivo, frame)
        print(f"Foto tirada com sucesso! Salva como {nome_arquivo}")
    else:
        print("Erro ao capturar a foto.")

    # Libera os recursos da câmera
    cap.release()

if __name__ == "__main__":
    tirar_foto()