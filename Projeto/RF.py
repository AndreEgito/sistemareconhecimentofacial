import cv2

# Carregar o classificador Haar Cascade para detecção de rostos
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # Certifique-se de que o arquivo XML do classificador está na pasta correta

# Carregar a imagem em que deseja detectar rostos
imagem = cv2.imread(r'C:\Users\autologon\Desktop\Sistemas Cognitivos [2023.2]\Projeto\rosto.jpg')  # Substitua 'andre01.jpg' pelo caminho da sua imagem

# Verificar se a imagem foi carregada com sucesso
if imagem is not None:
    # Converter a imagem em escala de cinza (detecção de rostos funciona melhor em imagens em escala de cinza)
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Detectar rostos na imagem
    faces = face_cascade.detectMultiScale(imagem_gray, scaleFactor=1.1, minNeighbors=5)

    # Desenhar retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Cor verde, largura da linha 3

    # Exibir a imagem com os rostos detectados
    cv2.imshow('Rostos Detectados', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Imagem não encontrada ou não pôde ser carregada.")
