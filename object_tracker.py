import cv2


cap=cv2.VideoCapture('car.mp4 ')

object_detector=cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame=cap.read()
    height,width,_=frame.shape
    print(height, width)

    roi=frame[600:,1500:]

    #object detection from mask
    mask=object_detector.apply(frame)
    contours,_=cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>300:
            cv2.drawContours(frame, [cnt], -1, (0,255,0), 2)



    cv2.imshow("Frame", frame)
    #cv2.imshow('Mask', mask)
    cv2.imshow('roi', roi)

    key=cv2.waitKey(30)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()
