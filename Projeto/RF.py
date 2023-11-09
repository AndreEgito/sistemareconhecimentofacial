import cv2
import os

# Verificar se a pasta 'faces' existe, caso contrário, criá-la
if not os.path.exists('faces'):
    os.makedirs('faces')

# Carregar o classificador Haar Cascade para detecção de rostos
face_cascade = cv2.CascadeClassifier('Projeto/haarcascade_frontalface_default.xml')  # Certifique-se de que o arquivo XML do classificador está na pasta correta

# Inicializar o objeto de captura de vídeo para a webcam (0 geralmente é a webcam padrão)
cap = cv2.VideoCapture(0)

# Inicializar um contador para atribuir IDs únicos a cada rosto
face_id_counter = 0

while True:
    # Capturar cada quadro do fluxo de vídeo
    ret, frame = cap.read()

    # Converter o quadro para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos no quadro
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Desenhar retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Cor verde, largura da linha 3
        cv2.putText(frame, f'Pressione ESPACO', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Exibir o quadro com os rostos detectados
    cv2.imshow('Detecção de Rostos', frame)

    # Esperar até que o usuário pressione a tecla ESPAÇO para capturar o rosto
    key = cv2.waitKey(1)
    if key == 32:  # Código da tecla ESPAÇO
        for (x, y, w, h) in faces:
            face_id_counter += 1
            face_image = frame[y:y + h, x:x + w]

            # Solicitar informações do usuário para cadastro
            nome_completo = input('Nome Completo: ')
            ano_nascimento = input('Data de nascimento: ')
            serie_cursada = input('Série: ')
            nome_responsavel = input('Nome do responsável: ')

            # Salvar as informações do rosto em um arquivo de texto
            info_filename = f'faces/face_{face_id_counter}_info.txt'
            with open(info_filename, 'w') as info_file:
                info_file.write(f'Nome Completo: {nome_completo}\nAno de Nascimento: {ano_nascimento}\nSérie Cursada: {serie_cursada}\nNome do Responsável: {nome_responsavel}')

            # Salvar a imagem do rosto na pasta 'faces'
            face_filename = f'faces/face_{face_id_counter}.jpg'
            cv2.imwrite(face_filename, face_image)

            print(f'Rosto capturado com sucesso! ID: {face_id_counter}')

    # Parar o loop ao pressionar 'q'
    elif key == ord('q'):
        break

# Liberar o objeto de captura e fechar as janelas
cap.release()
cv2.destroyAllWindows()
