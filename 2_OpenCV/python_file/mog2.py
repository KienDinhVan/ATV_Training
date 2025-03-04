import cv2

cap = cv2.VideoCapture("car.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    fgmask = fgbg.apply(frame)

    cv2.imshow("Foreground Mask", fgmask)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()