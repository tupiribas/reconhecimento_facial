import mediapipe as mp  # Trata o  reconhecimento da imagem
import cv2  # Trata a imagem da camera

camera = cv2.VideoCapture(0)

# Um dos varios tipos de detectores da ferramenta
forma_de_detectar = mp.solutions.face_detection
reconhecedor = forma_de_detectar.FaceDetection()
formato = mp.solutions.drawing_utils

while True:
    informacao, imagem = camera.read()

    if not informacao:
        break

    rostos = reconhecedor.process(imagem)  # Lista de rostos que ele reconheceu

    print(rostos)
    if rostos.detections:
        for rosto in rostos.detections:
            # Local e objeto que deseja reconhecer o rosto
            formato.draw_detection(imagem, rosto)

    cv2.imshow('Rostos na webcan', imagem)

    if cv2.waitKey(5) == 27:
        break

camera.release()
cv2.destroyAllWindows()
