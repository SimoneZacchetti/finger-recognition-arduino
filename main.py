import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import serial

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(1)
arduino = serial.Serial(port='/dev/cu.usbmodem101', baudrate=9600, timeout=.1)


def fingerCount(finger):
    finger_count = 0
    for value in finger:
        if value == 1:
            finger_count += 1

    return finger_count


while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            count = fingerCount(fingerup)
            if count == 0:
                arduino.write(bytes('0', 'utf-8'))
                print("0")
            if count == 1:
                arduino.write(bytes('1', 'utf-8'))
                print("1")
            if count == 2:
                arduino.write(bytes('2', 'utf-8'))
                print("2")
            if count == 3:
                arduino.write(bytes('3', 'utf-8'))
                print("3")
            if count == 4:
                arduino.write(bytes('4', 'utf-8'))
                print("4")
            if count == 5:
                arduino.write(bytes('5', 'utf-8'))
                print("5")

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.1)

video.release()
cv2.destroyAllWindows()
