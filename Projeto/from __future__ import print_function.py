from __future__ import print_function
import cv2 as cv
import argparse

# Função para detecção e exibição de rostos e olhos em um quadro
def detectAndDisplay(frame):
    # Converte o quadro para escala de cinza e equaliza o histograma
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    # Detecta rostos no quadro
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        frame = cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

        faceROI = frame_gray[y:y + h, x:x + w]

        # Em cada rosto, detecta olhos
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2, y2, w2, h2) in eyes:
            eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
            radius = int(round((w2 + h2) * 0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0), 4)

    # Exibe o quadro com as detecções
    cv.imshow('Captura - Detecção de Rosto', frame)

# Configuração dos argumentos da linha de comando
parser = argparse.ArgumentParser(description='Código para tutorial do Cascade Classifier.')
parser.add_argument('--face_cascade', help='Caminho para o cascade de rosto.', default='C:/Users/André do Egito/OneDrive/Área de Trabalho/André/TI/Sistemas Cognitivos/Projeto/haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Caminho para o cascade de olhos.', default='data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Número da câmera.', type=int, default=0)
args = parser.parse_args()

# Nomes dos arquivos XML dos classificadores em cascata
face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade

# Inicialização dos classificadores em cascata
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()

# Carrega os classificadores em cascata
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!) Erro ao carregar o cascade de rosto')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!) Erro ao carregar o cascade de olhos')
    exit(0)

# Número do dispositivo da câmera
camera_device = args.camera

# Inicializa a captura de vídeo
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!) Erro ao abrir a captura de vídeo')
    exit(0)

# Loop principal para a detecção
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) Nenhum quadro capturado -- Encerrando!')
        break

    # Chama a função para detecção de rostos e olhos no quadro
    detectAndDisplay(frame)

    # Encerra a execução ao pressionar a tecla "Esc" (código 27)
    if cv.waitKey(10) == 27:
        break
