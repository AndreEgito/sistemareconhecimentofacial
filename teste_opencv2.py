import cv2

# Carregue o classificador Haar Cascade para detecção de faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicialize a webcam (ou carregue uma imagem)
cap = cv2.VideoCapture(0)  # Use 0 para a webcam padrão, ou especifique um arquivo de vídeo

while True:
    # Capture um quadro da webcam
    ret, frame = cap.read()

    # Converta o quadro em escala de cinza para a detecção de faces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecte faces na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenhe retângulos ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostre o quadro com as faces detectadas
    cv2.imshow('Detecção de Faces', frame)

    # Encerre o loop ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere a webcam e feche a janela
cap.release()
cv2.destroyAllWindows()