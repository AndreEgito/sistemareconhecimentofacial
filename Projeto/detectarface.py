# Importando as bibliotecas necessárias
import cv2
import numpy as np
import dlib

# Conectando a câmera do notebook
cap = cv2.VideoCapture(0)

# Detectando as coordenadas
detector = dlib.get_frontal_face_detector()

# Capturando quadros continuamente
while True:

    # Capturando quadro a quadro
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # RGB para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    # Iterador para contar rostos
    i = 0
    for face in faces:
        # Obtendo as coordenadas dos rostos
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        # Incrementando o iterador para cada face nas faces
        i = i + 1

        # Exibindo a caixa e os rostos
        cv2.putText(frame, 'face num' + str(i), (x - 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print(face, i)

        # Exibindo o quadro resultante
    cv2.imshow('frame', frame)

    # Pressionando a tecla “q” para fechar a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Capturando
cap.release()
cv2.destroyAllWindows()