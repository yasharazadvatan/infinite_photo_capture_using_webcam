import cv2
import os

path = ""

cap = cv2.VideoCapture(0)
print(f'width: {cap.get(3)}')
print(f'height: {cap.get(4)}')

global countFolder


def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(path + str(countFolder)):
        countFolder += 1
    os.makedirs(path + str(countFolder))


saveDataFunc()

count = 0
countSave = 0

while True:
    success, img = cap.read()

    if success:

        if count % 3 == 0:
            cv2.imwrite(path + str(countFolder) + "/" + "a" + str(countSave) + ".jpg", img)
            countSave += 1
            print(countSave)
        count += 1

        cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
