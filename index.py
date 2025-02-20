import os
import cv2
import dlib
import sys
# import dotenv
import use

def faces(path, folder):
    detector = dlib.get_frontal_face_detector()
    frame = cv2.imread("test_data/" + path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    # detect the face
    for counter, face in enumerate(faces):
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (220, 255, 220), 1)
        img_to_save = frame[y1:y2, x1:x2]
        cv2.imwrite(f"faces{folder}/face{counter}.jpg", img_to_save)


def remove_dir(path):
    for i in os.listdir(path):
        os.remove(f"{path}/{i}")
    os.rmdir(path)


if __name__ == "__main__":
    # load_dotenv()
    idx = 1
    for i in os.listdir("test_data"):
        remove_dir(f"faces{idx}")
        os.mkdir(f"faces{idx}")
        faces(i, str(idx))
        idx += 1

    for i in os.listdir("faces3"):
        bytes = open(f"faces3/{i}", "rb").read()
        use.get_label(bytes)