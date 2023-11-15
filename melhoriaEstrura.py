import sys
import cv2
import numpy as np
import dlib

def load_face_models():
    sys.path.append('C:\\Reconhecimento facial\\Lib\\site-packages\\face_recognition_models-0.3.0-py3.12.0.egg')
    import face_recognition
    import face_recognition_models
    return face_recognition, face_recognition_models

def capture_frames():
    cap = cv2.VideoCapture(0)
    return cap

def detect_faces(frame, detector):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    return faces

def main():
    face_recognition, face_recognition_models = load_face_models()
    cap = capture_frames()
    detector = dlib.get_frontal_face_detector()

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        faces = detect_faces(frame, detector)

        i = 0
        for face in faces:
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
            cv2.putText(frame, 'face num' + str(i), (x - 10, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
#os módulos face_recognition e face_recognition_models vão importado quando a função load_face_models for chamada.
# Isso pode ajudar a melhorar a eficiência do  código.