import cv2, time

first_frame = None


video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    #get delta frame
    delta_frame = cv2.absdiff(first_frame,gray)

    #in future, use this to go "ok the brick is on screen, wait until
    #there is barely a difference in the background again before
    #sending another image over to brickognize. also make sure to get a clear
    #position of where the brick is so you can send as clear of a picture
    #as possible
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    #find all objects, might use this might not
    cnts , _ =cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Capturing",gray)
    cv2.imshow("Threshold",thresh_frame)
    cv2.imshow("Color Frame", frame)

    key=cv2.waitKey(1)
    #print(gray)
    #print(delta_frame)
    

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows
