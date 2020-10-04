import cv2
import os

a = []
image_main = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
f_features_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
save_directory = input()

info_f = open("savedphotos.txt", mode="r", encoding="utf8")
savedphoto = int(info_f.readlines()[0])
info_f.close()
info_f = open("savedphotos.txt", mode="w", encoding="utf8")


def draw_face_eyes_rectangles(faces):
    for (x, y, w, h) in faces:
        a = gray[y:y + h, x:x + w]
        b = a.copy()
        wb_mass.append(b)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        eyes_detected = f_features_cascade.detectMultiScale(a)
        for (ex, ey, ew, eh) in eyes_detected:
            cv2.rectangle(a, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 1)
        image_mass.append(a)


while True:
    ret, img = image_main.read()
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(5, 5))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_count = len(faces)
    image_mass = []
    wb_mass = []

    if face_count == 1:
        cv2.destroyWindow("Face features"+str(savedphoto)+"1")
        cv2.destroyWindow("Face features"+str(savedphoto)+"2")

    draw_face_eyes_rectangles(faces)

    cv2.imshow("Face recognition", img)
    for i in range(face_count):
        if len(image_mass[i]) != 0:
            cv2.imshow("Face features" + str(savedphoto) + str(i), image_mass[i])

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        info_f.write(str(savedphoto))
        break
    elif k == 32:
        os.chdir(save_directory)
        cv2.imwrite("all" + str(savedphoto) + ".jpg", img)
        info_f.write(str(int(savedphoto) + 1))
        for q in range(face_count):
            cv2.imwrite("photo" + str(q) + str(savedphoto) + ".jpg", wb_mass[q])
        break

info_f.close()
image_main.release()
cv2.destroyAllWindows()
