import os
import face_recognition

def load_face_encodings(folder_path):
    face_encodings = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(folder_path, filename)
            encoding = get_face_encoding(image_path)
            if encoding is not None:  # Verificar se encoding não é None
                face_encodings[filename] = encoding
    return face_encodings

def get_face_encoding(image_path):
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    return face_encodings[0] if face_encodings else None

def find_matching_faces(fotos_encodings, images_encodings):
    for foto_filename, foto_encoding in fotos_encodings.items():
        for image_filename, image_encoding in images_encodings.items():
            match = face_recognition.compare_faces([image_encoding], foto_encoding)
            if match[0]:
                print(f"Pessoa reconhecida. Acesso liberado!")
                return True
    return False

def main():
    # Pasta onde as fotos estão localizadas
    fotos_folder = "Foto_capturada"

    # Pasta onde as imagens de referência estão localizadas
    images_folder = "Imagens_cadastradas"

    # Carregar os encodings das faces nas fotos
    fotos_encodings = load_face_encodings(fotos_folder)

    # Carregar os encodings das imagens de referência
    images_encodings = load_face_encodings(images_folder)

    # Comparar os encodings e verificar se há correspondências
    if not find_matching_faces(fotos_encodings, images_encodings):
        print("Pessoa desconhecida. Acesso negado!")

if __name__ == "__main__":
    main()