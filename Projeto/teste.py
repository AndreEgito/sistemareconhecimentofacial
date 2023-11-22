# Importando as bibliotecas necessárias
import os
modelo_dlib_path = 'C:\\Reconhecimento facial\\Lib\\site-packages\\Dlib'
modelo_dlib_path_absoluto = os.path.abspath(modelo_dlib_path)
import glob
import sys
sys.path.append('C:\\Reconhecimento facial\\Lib\\site-packages\\face_recognition_models-0.3.0-py3.12.0.egg')

import face_recognition
import cv2
import numpy as np
import dlib
predictor_path = os.path.join(modelo_dlib_path, 'shape_predictor_68_face_landmarks.dat')
print(f"Verificando se o modelo Dlib existe: {os.path.exists(predictor_path)}")

# Conectando a câmera do notebook
cap = cv2.VideoCapture(0)

# Detectando as coordenadas
detector = dlib.get_frontal_face_detector()

# Lista para armazenar codificações faciais e nomes correspondentes
known_face_encodings = []
known_face_names = []

# Capturando e salvando foto
def capture_photo():
    print("Entrando na função capture_photo...")
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    print("Saindo da função capture_photo...")

    print(f"Número de faces detectadas: {len(faces)}")

    if len(faces) == 1:
        face = faces[0]
        x, y, x1, y1 = face.left(), face.top(), face.right(), face.bottom()
        face_image = frame[y:y1, x:x1]

        # Exibindo a foto capturada antes de salvar
        cv2.imshow('Foto capturada', face_image)
        cv2.waitKey(0)  # Wait for a key press before continuing

        # Salvando a foto capturada em um diretório separado
        capture_dir = 'captured_images'
        os.makedirs(capture_dir, exist_ok=True)
        filename = os.path.join(capture_dir, f'person_{len(known_face_encodings)}.jpeg')
        cv2.imwrite(filename, face_image)
        print(f"Foto capturada e salvada como {filename}")

    # Atualizar rostos conhecidos fora do bloco condicional
    update_known_faces()

# Atualizando rostos conhecidos
def update_known_faces():
    global known_face_encodings
    global known_face_names

    # Recarregando rostos conhecidos
    known_face_encodings = []
    known_face_names = []

    image_files = glob.glob("Imagens_cadastradas/*.png")

    for image_file in image_files:
        try:
            image = face_recognition.load_image_file(image_file)
        except Exception as e:
            print(f"Erro ao carregar a imagem {image_file}: {e}")
            continue  # Continuar a próxima iteração se ocorrer um erro

        encodings = face_recognition.face_encodings(image)
        if encodings:
            encoding = encodings[0]
            name = image_file.split('/')[-1].split('.')[0]
            known_face_encodings.append(encoding)
            known_face_names.append(name)
            print(f"Rosto conhecido atualizado: {name}")

# Comparando rostos das imagens armazenadas com rostos capturado pela câmera
def recognize_face(frame):
    print("Reconhecendo rosto...")
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = "Desconhecido"

        # Verificando se a correspondência do rosto capturado pela câmera foi encontrado
        if known_face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            print(f"Matches: {matches}")
            print(f"Nome reconhecido: {name}")

        # Desenhando o retângulo e a etiqueta na moldura
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

# Capturando quadros continuamente
while True:
    # Capturando quadros continuamente
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Verificando se alguma tecla está pressionada
    key = cv2.waitKey(1) & 0xFF

    # Imprimindo o código-chave para depuração
    print(f"Aperta a tecla c: {key}")

    if key == ord('c'):
        capture_photo()
        print(f"Codificações faciais conhecidas: {known_face_encodings}")
        print(f"Nomes de rostos conhecidos: {known_face_names}")

    # RGB para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    # Reconhecendo rostos e nomes de exibição
    recognize_face(frame)

    # Exibindo o quadro resultante
    cv2.imshow('frame', frame)

    # Pressionando a tecla “q” para fechar a janela
    if key == ord('q'):
        break

# Capturando
cap.release()
cv2.destroyAllWindows()